# Notebook contents

## homeworks/Homework_task_2.ipynb

### Cell 1: markdown

# Домашнее задание 2: смотрим на Землю из космоса

Спутники Sentinel-2 Европейского космического агентства фотографируют всю сушу Земли примерно раз в пять дней. Снимков столько, что людей на их просмотр никогда не хватит. Поэтому их разбирают нейросети: следят за вырубкой лесов, считают поля, замечают, как растут города и где разлились реки.

В этой домашке вы соберёте такую сеть сами. Датасет называется EuroSAT: 27 000 снимков 64 на 64 пикселя с территории Европы и 10 типов местности (лес, река, шоссе, жилой район, промзона и так далее). Один пиксель соответствует 10 метрам, так что каждая картинка показывает квадрат примерно 640 на 640 метров.

План такой:
1. собрать свёрточную сеть с нуля и дотянуть её до accuracy 0.85 на тесте;
2. написать residual-блок своими руками и собрать из таких блоков маленький ResNet. Потом дообучить настоящую ResNet-18, которую до нас обучили на миллионе фотографий из ImageNet;
3. разобраться, где сеть ошибается и почему;
4. заглянуть внутрь сети: что видят свёрточные слои и куда сеть смотрит, когда принимает решение. А в конце, если захочется, проверить её на спутниковом снимке своего района.

Оцениваются только части 1 и 2. В частях 3 и 4 весь код уже написан, их нужно просто запустить и прочитать. Там самое интересное: мы посмотрим на обученные вами модели изнутри.

Обучать свёрточные сети на процессоре можно, но долго. Удобнее запускать ноутбук в Google Colab с GPU (Среда выполнения > Сменить среду выполнения > T4 GPU). Код ниже сам переходит на видеокарту, если она есть.

Код пишете там, где стоит `# ваш код`. Остальные ячейки просто запускаете. На вопросы отвечайте в ячейках «Ответы» своими словами, хватит 2-3 предложений на вопрос.

### Оценивание

| Часть | Что смотрим | Баллы |
|---|---|---|
| 1. CNN с нуля | Dataset и аугментации, модель `SatNet`, функции `train_model` и `predict`, accuracy на тесте не ниже 0.85, ответы на вопросы | 4.5 |
| 2. ResNet | `ResidualBlock`, `MiniResNet` и её обучение , дообучение ResNet-18 в двух вариантах, сравнение моделей и ответы на вопросы | 5.5 |
| 3. Разбор ошибок | не оценивается, только запустить и прочитать | |
| 4. Внутри сети | не оценивается, только запустить и прочитать | |

Перед отправкой сделайте `Kernel > Restart & Run All` и проверьте, что весь ноутбук, включая части 3 и 4, выполняется без ошибок. Части 3 и 4 используют ваши модели, так что заодно это хорошая проверка частей 1 и 2. Если ячейка падает, задание из неё не засчитывается. Сдаёте `.ipynb` с выводами и графиками.

### Cell 2: code

import os
from PIL import Image
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import torchvision.transforms.v2 as tfs
from torchvision import datasets, models

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

### Cell 3: markdown

## Данные

Ячейка ниже скачивает EuroSAT (около 90 Мб), делит его на train, val и test и раскладывает в формате, который мы использовали на лекции: в каждой папке лежат картинки и `format.json`, где имени файла сопоставлен номер класса.

Если скачивание оборвалось, удалите папки `eurosat` и `eurosat_raw` и запустите ячейку ещё раз. Если torchvision ругается на адрес загрузки, обновите его: `pip install -U torchvision`.

### Cell 4: code

CLASSES = ["AnnualCrop", "Forest", "HerbaceousVegetation", "Highway", "Industrial",
           "Pasture", "PermanentCrop", "Residential", "River", "SeaLake"]
CLASSES_RU = ["пашня", "лес", "луг", "шоссе", "промзона",
              "пастбище", "сады", "жилой район", "река", "водоём"]


def make_dataset(path="eurosat", seed=42):
    if os.path.exists(path):
        print("Датасет уже готов")
        return

    raw = datasets.EuroSAT(root="eurosat_raw", download=True)
    assert raw.classes == CLASSES

    samples = list(raw.samples)
    random.Random(seed).shuffle(samples)
    n = len(samples)
    parts = {
        "train": samples[:int(0.7 * n)],
        "val": samples[int(0.7 * n):int(0.85 * n)],
        "test": samples[int(0.85 * n):],
    }

    for split, items in parts.items():
        folder = os.path.join(path, split)
        os.makedirs(folder)
        fmt = {}
        for src, target in tqdm(items, desc=split):
            name = os.path.basename(src)
            shutil.copy(src, os.path.join(folder, name))
            fmt[name] = target
        with open(os.path.join(folder, "format.json"), "w") as fp:
            json.dump(fmt, fp)

    shutil.rmtree("eurosat_raw")


make_dataset()

### Cell 5: code

with open("eurosat/train/format.json") as fp:
    fmt = json.load(fp)

fig, axes = plt.subplots(4, 10, figsize=(16, 7))
for j, name in enumerate(CLASSES_RU):
    files = [f for f, t in fmt.items() if t == j][:4]
    for i, f in enumerate(files):
        axes[i, j].imshow(Image.open(os.path.join("eurosat/train", f)))
        axes[i, j].axis("off")
    axes[0, j].set_title(name)
plt.show()

### Cell 6: markdown

---
## Часть 1. Свёрточная сеть с нуля (4.5 балла)

### 1.1 Dataset

Напишите `SatDataset` по образцу `SunDataset` с лекции. Разница две:
- вместо `train=True/False` будет параметр `split`, который принимает значения `"train"`, `"val"` или `"test"`. Это имя папки;
- в `SunDataset` решалась задача регрессии, поэтому метка была `float32`. У нас классификация, и `nn.CrossEntropyLoss` ждёт номер класса типа `torch.long`.

### Cell 7: code

class SatDataset(data.Dataset):
    def __init__(self, path, split="train", transform=None):
        pass  # ваш код

    def __getitem__(self, item):
        pass  # ваш код

    def __len__(self):
        pass  # ваш код

### Cell 8: markdown

### 1.2 Аугментации

У спутникового снимка нет верха и низа: лес, повёрнутый вверх ногами, остаётся лесом. Значит, во время обучения картинки можно случайно отражать, и сеть будет видеть больше разных примеров.

`transforms` ниже такой же, как на лекции. Напишите `train_transforms`: то же самое, но перед `ToDtype` добавьте случайное горизонтальное и вертикальное отражение (`tfs.RandomHorizontalFlip()` и `tfs.RandomVerticalFlip()`).

### Cell 9: code

transforms = tfs.Compose([tfs.ToImage(), tfs.ToDtype(torch.float32, scale=True)])

train_transforms = ...  # ваш код

### Cell 10: markdown

### 1.3 DataLoader

Создайте три датасета и три загрузчика с `batch_size=64`:
- `d_train` и `train_data` с аугментациями и перемешиванием;
- `d_val` и `val_data` без аугментаций и без перемешивания;
- `d_test` и `test_data` так же, как val.

### Cell 11: code

# ваш код

### Cell 12: code

# проверка
x, y = next(iter(train_data))
print(x.shape, x.dtype)  # torch.Size([64, 3, 64, 64]) torch.float32
print(y.shape, y.dtype)  # torch.Size([64]) torch.int64
print(len(d_train), len(d_val), len(d_test))

### Cell 13: markdown

Дальше несколько готовых функций для картинок и графиков, они понадобятся во всех частях. Просто запустите ячейку.

### Cell 14: code

def show_images(dataset, indices, titles=None, colors=None, ncols=8):
    "Показывает картинки dataset[i] для i из indices, с подписями и цветом подписей."
    nrows = (len(indices) + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(2 * ncols, 2.4 * nrows), squeeze=False)
    for ax in axes.flat:
        ax.axis("off")
    for k, idx in enumerate(indices):
        img, _ = dataset[int(idx)]
        ax = axes.flat[k]
        ax.imshow(img.permute(1, 2, 0).clamp(0, 1))
        if titles is not None:
            ax.set_title(titles[k], fontsize=9, color=colors[k] if colors else "black")
    plt.tight_layout()
    plt.show()


def plot_history(histories):
    "histories: словарь {название модели: (loss_lst, loss_lst_val, acc_lst_val)}"
    fig, axes = plt.subplots(1, 3, figsize=(17, 4))
    for name, (loss_lst, loss_lst_val, acc_lst_val) in histories.items():
        epochs_range = range(1, len(loss_lst) + 1)
        axes[0].plot(epochs_range, loss_lst, marker="o", label=name)
        axes[1].plot(epochs_range, loss_lst_val, marker="o", label=name)
        axes[2].plot(epochs_range, acc_lst_val, marker="o", label=name)
    for ax, title in zip(axes, ["loss на train", "loss на validation", "accuracy на validation"]):
        ax.set_title(title)
        ax.set_xlabel("эпоха")
        ax.grid(alpha=0.3)
        ax.legend()
    plt.show()


def plot_confusion(cm, class_names, hide_diagonal=False):
    "Рисует матрицу ошибок. hide_diagonal=True прячет диагональ, чтобы лучше были видны ошибки."
    cm = np.array(cm, dtype=float)
    if hide_diagonal:
        np.fill_diagonal(cm, 0)
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.imshow(cm, cmap="Blues")
    ax.set_xticks(range(len(class_names)), class_names, rotation=45, ha="right")
    ax.set_yticks(range(len(class_names)), class_names)
    ax.set_xlabel("ответ сети")
    ax.set_ylabel("правильный ответ")
    for i in range(len(class_names)):
        for j in range(len(class_names)):
            color = "white" if cm[i, j] > cm.max() / 2 else "black"
            ax.text(j, i, int(cm[i, j]), ha="center", va="center", color=color, fontsize=8)
    plt.tight_layout()
    plt.show()

### Cell 15: markdown

Посмотрим, как работают аугментации: одна и та же картинка, пропущенная через `train_transforms` восемь раз.

### Cell 16: code

show_images(d_train, [0] * 8)

### Cell 17: markdown

### 1.4 Модель

Соберите `SatNet` по схеме:

| Слой | Что делает | Размер на выходе |
|---|---|---|
| вход | | 3 × 64 × 64 |
| `conv1` | Conv2d(3, 32, kernel_size=3, padding=1), ReLU, MaxPool2d(2) | 32 × 32 × 32 |
| `conv2` | Conv2d(32, 64, kernel_size=3, padding=1), ReLU, MaxPool2d(2) | ? |
| `conv3` | Conv2d(64, 128, kernel_size=3, padding=1), ReLU, MaxPool2d(2) | ? |
| | flatten | ? |
| `fc1` | Linear(?, 128), ReLU | 128 |
| `fc2` | Linear(128, 10) | 10 |

Знаки вопроса заполните сами. Атрибуты назовите именно `conv1`, `conv2`, `conv3`, `fc1`, `fc2`: в части 4 мы будем доставать `conv1` и `conv2`, чтобы посмотреть, что они видят.

### Cell 18: code

class SatNet(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        # ваш код

    def forward(self, x):
        pass  # ваш код

### Cell 19: code

# проверка
model_cnn = SatNet()
print(model_cnn(x).shape)  # torch.Size([64, 10])
print("параметров:", sum(p.numel() for p in model_cnn.parameters()))

### Cell 20: markdown

### 1.5 Обучение

Напишите две функции.

`train_model` можно почти целиком взять из прошлой домашки. Она возвращает `loss_lst`, `loss_lst_val` и `acc_lst_val`. Новое здесь одно: батчи нужно переносить на `device` (`x.to(device)`, `y.to(device)`), иначе на GPU ничего не заработает. И метки теперь номера классов, а не one-hot, так что для accuracy `argmax` от `y` брать не нужно.

`predict` прогоняет модель по загрузчику и возвращает два тензора на CPU:
- `probs` размером (N, 10): вероятности классов (не забудьте softmax);
- `targets` размером (N,): правильные ответы.

Из `predict` accuracy считается в одну строку, а в части 3 нам понадобятся сами вероятности.

### Cell 21: code

def train_model(model, optimizer, train_data, val_data, epochs, verbose=True):
    loss_function = nn.CrossEntropyLoss()
    loss_lst = []
    loss_lst_val = []
    acc_lst_val = []

    # ваш код

    return loss_lst, loss_lst_val, acc_lst_val


def predict(model, loader):
    pass  # ваш код

### Cell 22: markdown

Обучите `SatNet` с Adam (`lr=0.001`) 10 эпох, нарисуйте кривые через `plot_history` и посчитайте accuracy на тесте. **Нужно получить не меньше 0.85.**

<details>
<summary>Если не получается дотянуть до 0.85</summary>

<br>

- проверьте, что `train_data` действительно с `shuffle=True`, а картинки нормированы в [0, 1];
- обучите подольше, например 15 эпох;
- добавьте `nn.BatchNorm2d` после каждой свёртки и Dropout перед `fc2`. Всё это у вас уже было в первой домашке.

</details>

### Cell 23: code

torch.manual_seed(42)

# ваш код

### Cell 24: markdown

**Вопросы**
1. Почему для спутниковых снимков можно отражать картинку вверх ногами, а, например, для фотографий котов или для рукописных цифр так делать не стоит?
2. Какие размеры у вас получились на месте знаков вопроса в таблице? В каком слое `SatNet` больше всего параметров и почему?

### Cell 25: markdown

**Ответы:**

1.

2.

### Cell 26: markdown

---
## Часть 2. ResNet (5.5 баллов)

Напомню идею с лекции. Обычный блок сети учит преобразование $F(x)$ и отдаёт его дальше. Residual-блок отдаёт $F(x) + x$: вход проходит в обход слоёв по короткому пути (skip connection) и прибавляется к результату. Слоям остаётся выучить только поправку к входу, а градиент по короткому пути без потерь доходит до первых слоёв. Благодаря этому получается обучать сети в десятки и сотни слоёв.

### 2.1 Residual-блок

Напишите `ResidualBlock(channels)`. Число каналов на входе и выходе одинаковое, размер картинки не меняется:

```
вход x
  conv1: Conv2d(channels, channels, 3, padding=1), затем bn1: BatchNorm2d, затем ReLU
  conv2: Conv2d(channels, channels, 3, padding=1), затем bn2: BatchNorm2d
  прибавить x
  ReLU
```

Обратите внимание: последний ReLU стоит после сложения.

### Cell 27: code

class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        # ваш код

    def forward(self, x):
        pass  # ваш код

### Cell 28: markdown

Хитрая проверка. Если обнулить веса `bn2`, то основная ветка блока всегда будет выдавать ноль, и от блока останется только короткий путь: $\mathrm{ReLU}(0 + x) = \mathrm{ReLU}(x)$. Если skip connection сделан правильно, проверка напечатает `True`.

### Cell 29: code

block = ResidualBlock(16)
x_test = torch.randn(4, 16, 32, 32)
print(block(x_test).shape)  # torch.Size([4, 16, 32, 32])

with torch.no_grad():
    block.bn2.weight.zero_()
print(torch.allclose(block(x_test), F.relu(x_test)))

### Cell 30: markdown

### 2.2 MiniResNet

Соберите маленький ResNet из трёх стадий. Каждая стадия устроена так: свёртка, которая меняет число каналов, потом BatchNorm и ReLU, потом residual-блок, потом MaxPool2d(2).

| Стадия | Что внутри | Размер на выходе |
|---|---|---|
| 1 | `conv1`: Conv2d(3, 32, 3, padding=1), `bn1`, ReLU, `block1`: ResidualBlock(32), MaxPool2d(2) | 32 × 32 × 32 |
| 2 | `conv2`: Conv2d(32, 64, 3, padding=1), `bn2`, ReLU, `block2`: ResidualBlock(64), MaxPool2d(2) | 64 × 16 × 16 |
| 3 | `conv3`: Conv2d(64, 128, 3, padding=1), `bn3`, ReLU, `block3`: ResidualBlock(128), MaxPool2d(2) | 128 × 8 × 8 |
| выход | `nn.AdaptiveAvgPool2d(1)`, flatten, `fc`: Linear(128, 10) | 10 |

В конце вместо большого полносвязного слоя стоит global average pooling: каждая из 128 карт признаков усредняется в одно число. Так сделано и в настоящих ResNet.

Обучите `MiniResNet` так же, как `SatNet`: Adam, `lr=0.001`, 10 эпох, `torch.manual_seed(42)` перед созданием модели. Нарисуйте кривые обеих моделей на одних графиках и выведите для обеих число параметров и accuracy на тесте.

### Cell 31: code

class MiniResNet(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        # ваш код

    def forward(self, x):
        pass  # ваш код

### Cell 32: code

torch.manual_seed(42)

model_res = MiniResNet().to(device)
# ваш код

### Cell 33: markdown

<details>
<summary><b>Пояснение: почему MiniResNet может обогнать SatNet совсем ненамного</b> (откройте после того, как посмотрите на результаты)</summary>

<br>

Skip connections придумали, чтобы решить проблему очень глубоких сетей. Когда слоёв 50 или 100, градиенту при обратном проходе нужно пройти через каждый из них, и по дороге он затухает или, наоборот, раздувается. В статье, где впервые предложили ResNet, есть показательный пример: обычная сеть из 56 слоёв обучалась хуже, чем сеть из 20 слоёв, причём даже на train. То есть дело было не в переобучении, а в том, что глубокую сеть просто не получалось нормально обучить. Короткий путь в обход слоёв это исправляет: градиент доходит по нему до первых слоёв почти без изменений.

В `SatNet` всего 3 свёрточных слоя, в `MiniResNet` их 9. На такой глубине градиент нормально проходит и без skip connections, поэтому большого выигрыша от них ждать не стоит. Если `MiniResNet` всё же заметно лучше, скорее всего, дело в двух других вещах: в BatchNorm, который стабилизирует обучение, и в global average pooling. Посмотрите на число параметров: в `SatNet` больше миллиона параметров, и почти все они в `fc1`, а в `MiniResNet` их в несколько раз меньше. Меньше параметров, меньше риск переобучиться.

Настоящая сила ResNet проявляется там, где слоёв много. Именно такую сеть мы сейчас и возьмём.

</details>

### Cell 34: markdown

### 2.3 Дообучение ResNet-18

ResNet-18 это 18 слоёв и около 11 миллионов параметров. Обучать такую сеть с нуля на 19 тысячах картинок долго и почти бессмысленно. Но в `torchvision` есть версия, которую уже обучили на ImageNet: это 1.2 миллиона фотографий, 1000 классов, от собак до грузовиков. Её мы и дообучим на спутниковых снимках.

Сначала данные. Предобученная сеть привыкла к картинкам, нормированным определённым образом, поэтому к трансформациям нужно добавить в конец
`tfs.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])`.
Это среднее и стандартное отклонение по каналам на ImageNet.

Создайте `transforms_in` и `train_transforms_in` (такие же, как раньше, плюс Normalize), три датасета и загрузчики `train_data_in`, `val_data_in`, `test_data_in`.

### Cell 35: code

# ваш код

### Cell 36: markdown

Теперь два варианта дообучения, по 3 эпохи каждый.

**Вариант А: заморозить всё, кроме последнего слоя.** Загрузите сеть через `models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)`, выключите градиенты у всех параметров (`p.requires_grad = False`), а затем замените последний слой `model.fc` на новый `nn.Linear(512, 10)`. У нового слоя градиенты включены по умолчанию. Оптимизатор: Adam по `model.fc.parameters()` с `lr=0.001`.

**Вариант Б: дообучить всю сеть.** Снова загрузите сеть, замените `fc`, но ничего не замораживайте. Оптимизатор: Adam по всем параметрам с маленьким `lr=0.0001`, чтобы не сломать то, чему сеть уже научилась.

Для каждого варианта выведите, сколько параметров обучается (`sum(p.numel() for p in model.parameters() if p.requires_grad)`), и сохраните историю обучения. Модели назовите `model_frozen` и `model_finetune`.

На CPU одна эпоха ResNet-18 может идти несколько минут, на GPU около полуминуты.

### Cell 37: code

torch.manual_seed(42)

# вариант А, ваш код

hist_frozen = train_model(model_frozen, optimizer, train_data_in, val_data_in, epochs=3)

### Cell 38: code

torch.manual_seed(42)

# вариант Б, ваш код

hist_finetune = train_model(model_finetune, optimizer, train_data_in, val_data_in, epochs=3)

### Cell 39: markdown

Сведем результаты всех четырёх моделей: кривые обучения через `plot_history` и accuracy на тесте для каждой.

### Cell 40: code

plot_history({
    "SatNet": hist_cnn,
    "MiniResNet": hist_res,
    "ResNet-18, только fc": hist_frozen,
    "ResNet-18, вся сеть": hist_finetune,
})

for name, m, loader in [("SatNet", model_cnn, test_data),
                        ("MiniResNet", model_res, test_data),
                        ("ResNet-18, только fc", model_frozen, test_data_in),
                        ("ResNet-18, вся сеть", model_finetune, test_data_in)]:
    probs, targets = predict(m, loader)
    acc = (probs.argmax(dim=1) == targets).float().mean().item()
    print(f"{name}: test accuracy {acc:.3f}")

### Cell 41: markdown

<details>
<summary><b>Пояснение: почему сеть, обученная на фотографиях собак и машин, так хорошо понимает спутниковые снимки</b> (откройте после того, как посмотрите на результаты)</summary>

<br>

Вспомните, что мы говорили про свёрточные сети на лекции: первые слои учатся находить простые вещи вроде границ, цветовых пятен и штриховки. Следующие слои собирают из них текстуры и узоры, и только последние слои отвечают за то, что это именно собака или грузовик.

Границы, текстуры и узоры есть на любых картинках. Ровные ряды деревьев в саду, сетка улиц жилого района, гладкая поверхность воды это всё тоже текстуры. Поэтому почти все слои сети, обученной на ImageNet, полезны и для спутниковых снимков. Новому приходится учить только последний слой. А ImageNet больше нашего датасета в 60 с лишним раз, так что фильтры у предобученной сети получились гораздо лучше тех, что мы можем обучить с нуля.

**Вариант А** использует предобученную сеть как готовый «извлекатель признаков». Каждая картинка превращается в 512 чисел, и сверху обучается обычный линейный классификатор. Это быстро и почти не переобучается: учится всего 5 тысяч параметров.

**Вариант Б** разрешает подстроить под спутниковые снимки все слои, поэтому обычно работает лучше. Learning rate берут маленьким, чтобы сеть аккуратно подправила веса, а не забыла всё, чему научилась на ImageNet.

И ещё одна деталь. ResNet-18 рассчитана на картинки 224 на 224, а наши в 3.5 раза меньше. После всех уменьшений от картинки к концу сети остаётся карта 2 на 2. Сеть всё равно справляется, но если увеличить снимки (например, добавить `tfs.Resize(128)`), accuracy обычно ещё подрастёт. Правда, и обучение станет заметно медленнее.

</details>

### Cell 42: markdown

**Вопросы**
1. Какая модель оказалась лучшей и на сколько она обогнала `SatNet`? Сравните модели по числу параметров и по времени обучения.
2. В варианте А обучается всего несколько тысяч параметров из 11 миллионов. Почему этого хватает для хорошего результата?

### Cell 43: markdown

**Ответы:**

1.

2.

### Cell 44: markdown

---
## Часть 3. Где и почему сеть ошибается

**Дальше ничего писать не нужно, эти части не оцениваются.** Запускайте ячейки по порядку и читайте. Код уже готов, но его стоит хотя бы пролистать: такие же приёмы пригодятся вам в любом проекте.

Accuracy 95% звучит отлично, но одно число мало что говорит о модели. Где именно она ошибается? Ошибки случайные или в них есть система? Может быть, иногда ошибается не сеть, а разметка? Чтобы ответить на такие вопросы, на ошибки нужно посмотреть глазами. Этим и займёмся.

Сначала выберем лучшую из четырёх моделей, которые вы обучили, и дальше будем работать с ней.

### Cell 45: code

candidates = [
    ("SatNet", model_cnn, test_data, transforms),
    ("MiniResNet", model_res, test_data, transforms),
    ("ResNet-18, только fc", model_frozen, test_data_in, transforms_in),
    ("ResNet-18, вся сеть", model_finetune, test_data_in, transforms_in),
]

best_acc = 0
for name, m, loader, tr in candidates:
    probs_m, targets_m = predict(m, loader)
    acc = (probs_m.argmax(dim=1) == targets_m).float().mean().item()
    print(f"{name}: test accuracy {acc:.3f}")
    if acc > best_acc:
        best_acc, best_name = acc, name
        best_model, best_test_data, best_transform = m, loader, tr
        probs, targets = probs_m, targets_m

best_test_ds = best_test_data.dataset
preds = probs.argmax(dim=1)
conf = probs.max(dim=1).values
print("\nДальше работаем с моделью:", best_name)

### Cell 46: markdown

### 3.1 Accuracy по каждому классу

Общая accuracy усредняет всё подряд. Модель может почти идеально узнавать воду и лес и при этом регулярно путать пастбища с лугами, а в среднем всё равно получится красивое число. Поэтому посмотрим на каждый класс отдельно: какая доля снимков этого класса распознана верно.

### Cell 47: code

class_acc = [(preds[targets == c] == c).float().mean().item() for c in range(10)]
order = np.argsort(class_acc)

plt.figure(figsize=(7, 4.5))
bars = plt.barh([CLASSES_RU[i] for i in order], [class_acc[i] for i in order], color="tab:blue")
for bar, i in zip(bars, order):
    plt.text(bar.get_width() + 0.002, bar.get_y() + bar.get_height() / 2,
             f"{class_acc[i]:.1%}", va="center", fontsize=9)
plt.xlim(min(class_acc) - 0.05, 1.03)
plt.title("Доля верных ответов по классам")
plt.grid(alpha=0.3, axis="x")
plt.show()

### Cell 48: markdown

Скорее всего, внизу списка у вас оказались луг, пастбище, сады или шоссе. Это классы, которые и человеку трудно различить на квадрате 640 на 640 метров: луг, пастбище и сады с высоты выглядят как зелёные пятна с похожей текстурой. А наверху почти наверняка лес и водоём: у них очень характерный цвет, и спутать их почти не с чем.

### 3.2 Матрица ошибок

Матрица ошибок (confusion matrix) это таблица 10 на 10. В строке «река» и столбце «шоссе» стоит число рек, которые сеть приняла за шоссе. На диагонали правильные ответы, всё остальное ошибки.

Нарисуем её два раза. На первой картинке диагональ настолько больше всего остального, что ошибок почти не видно. Поэтому на второй мы диагональ спрячем и оставим только ошибки.

### Cell 49: code

cm = torch.zeros(10, 10, dtype=torch.long)
for t, p in zip(targets, preds):
    cm[t, p] += 1

plot_confusion(cm, CLASSES_RU)
plot_confusion(cm, CLASSES_RU, hide_diagonal=True)

### Cell 50: markdown

Посмотрите на вторую картинку: ошибки не размазаны по всей таблице, а собраны в нескольких клетках. Значит, сеть путает не что попало, а конкретные пары похожих классов. Это хорошая новость. Систематические ошибки можно понять и исправить, например собрать больше примеров именно этих классов или показать сети снимки покрупнее.

### 3.3 Какие классы путаются чаще всего

Возьмём три самые «горячие» клетки вне диагонали и посмотрим на сами снимки.

### Cell 51: code

off_diag = cm.clone()
off_diag.fill_diagonal_(0)
top_pairs = torch.argsort(off_diag.flatten(), descending=True)[:3]

for k in top_pairs:
    t, p = divmod(k.item(), 10)
    print(f"Правильно «{CLASSES_RU[t]}», а сеть сказала «{CLASSES_RU[p]}»: {cm[t, p].item()} раз")
    idx = torch.where((targets == t) & (preds == p))[0][:8].tolist()
    titles = [f"сеть: {CLASSES_RU[p]} {conf[i].item():.0%}" for i in idx]
    show_images(d_test, idx, titles)

### Cell 52: markdown

Обычно эти ошибки легко объяснить, если посмотреть на снимки:
- **шоссе и река** выглядят почти одинаково: длинная полоса через весь кадр, по краям поля. Только у реки полоса тёмная, а у шоссе светлая. А в тени, в мутной воде или зимой эта разница пропадает;
- **луг, пастбище и сады** это зелёные и бурые пятна. Сады отличаются ровными рядами деревьев, но на разрешении 10 метров на пиксель ряды часто просто не видны;
- **пашня и сады** тоже похожи: и там и там прямоугольные участки с полосками.

Человек на таких снимках ошибался бы в тех же местах.

### 3.4 Самые уверенные ошибки

Отдельно интересны ошибки, в которых сеть была уверена на 90% и больше. Посмотрим на восемь самых уверенных.

### Cell 53: code

wrong = torch.where(preds != targets)[0]
worst = wrong[torch.argsort(conf[wrong], descending=True)[:8]].tolist()

titles = [f"разметка: {CLASSES_RU[targets[i].item()]}\nсеть: {CLASSES_RU[preds[i].item()]} {conf[i].item():.0%}"
          for i in worst]
show_images(d_test, worst, titles, colors=["red"] * len(worst))

### Cell 54: markdown

Присмотритесь к этим снимкам. Довольно часто оказывается, что сеть не так уж неправа:
- на снимке есть сразу два класса, например река и идущая вдоль неё дорога, или жилой район рядом с промзоной. А метка у снимка одна, и тот, кто размечал, выбрал одну из них;
- иногда разметка просто ошибочна. В любом большом датасете есть такие ошибки, и уверенные ошибки модели это самый быстрый способ их найти.

В реальных проектах так и делают: обучают модель, сортируют ошибки по уверенности и вручную проверяют верх списка. Часто так находится заметная доля ошибок разметки.

### 3.5 Карта: как сеть видит снимки

Перед последним линейным слоем каждая картинка превращается в вектор: у ResNet-18 это 512 чисел, у `SatNet` 128. Это и есть «описание» снимка, которое сеть составила сама. Последний слой просто проводит в этом пространстве границы между классами.

512 измерений увидеть нельзя, но есть алгоритм t-SNE. Он раскладывает точки на плоскости так, чтобы те, что были близки в исходном пространстве, остались рядом и на картинке. Возьмём векторы всех тестовых снимков и посмотрим на такую карту. Каждая точка это один снимок, цвет это правильный класс, чёрные крестики это ошибки сети.

Ячейка считается около минуты.

### Cell 55: code

from sklearn.manifold import TSNE

# вектор перед последним линейным слоем достаём через hook: функцию, которая
# вызывается при каждом проходе через слой и может подсмотреть его вход
last_linear = [m for m in best_model.modules() if isinstance(m, nn.Linear)][-1]
features = []
hook = last_linear.register_forward_hook(lambda module, inp, out: features.append(inp[0].detach().cpu()))
predict(best_model, best_test_data)
hook.remove()
features = torch.cat(features).numpy()
print("размер векторов:", features.shape)

emb = TSNE(n_components=2, init="pca", random_state=42).fit_transform(features)

plt.figure(figsize=(10, 8))
cmap = plt.get_cmap("tab10")
for c in range(10):
    mask = (targets == c).numpy()
    plt.scatter(emb[mask, 0], emb[mask, 1], s=6, color=cmap(c), label=CLASSES_RU[c])
mistakes = (preds != targets).numpy()
plt.scatter(emb[mistakes, 0], emb[mistakes, 1], s=25, color="black", marker="x", label="ошибки")
plt.legend(markerscale=3, loc="center left", bbox_to_anchor=(1, 0.5))
plt.axis("off")
plt.title("Тестовые снимки глазами сети (t-SNE)")
plt.show()

### Cell 56: markdown

Каждый класс собрался в своё облако, хотя сети никто не объяснял, как раскладывать снимки по пространству. Она сама научилась описывать их так, чтобы снимки одного класса оказывались рядом.

На карте видно и всё, о чём мы говорили выше:
- облака, которые соприкасаются, это как раз те классы, которые сеть путает. Найдите на карте луг, пастбище и сады;
- большинство крестиков лежит на границах облаков, там, где сеть сомневалась;
- крестики, которые лежат глубоко внутри чужого облака, это главные кандидаты на ошибки разметки. Сеть видит снимок как типичную реку, а метка у него «шоссе».

Одно предупреждение: расстояния между облаками на картинке t-SNE ничего не значат. Алгоритм сохраняет только соседство близких точек. Поэтому то, что лес на картинке далеко от реки, ещё не значит, что сеть считает их очень разными.

### Cell 57: markdown

---
## Часть 4. Заглядываем внутрь сети

Здесь тоже ничего писать не нужно. Мы посмотрим, что происходит внутри свёрточных слоёв и на какие части снимка сеть опирается, когда принимает решение.

### 4.1 Сеть за работой

Для начала просто 16 случайных снимков из теста. Зелёная подпись означает, что сеть ответила верно, красная, что ошиблась. Рядом с ответом уверенность сети.

### Cell 58: code

idx = random.Random(0).sample(range(len(d_test)), 16)
titles = [f"{CLASSES_RU[preds[i].item()]} {conf[i].item():.0%}" for i in idx]
colors = ["green" if preds[i] == targets[i] else "red" for i in idx]
show_images(d_test, idx, titles, colors)

### Cell 59: markdown

### 4.2 Чему научился первый слой ResNet-18

Свёрточный фильтр это маленький шаблон, который скользит по картинке и откликается там, где картинка на него похожа. В первом слое ResNet-18 64 фильтра размером 7 на 7 пикселей, по одному на каждый из трёх цветовых каналов. Их можно нарисовать как маленькие цветные картинки. Возьмём их из сети, предобученной на ImageNet.

### Cell 60: code

w = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1).conv1.weight.detach()  # (64, 3, 7, 7)

fig, axes = plt.subplots(4, 16, figsize=(16, 4.4))
for k, ax in enumerate(axes.flat):
    f = w[k]
    f = (f - f.min()) / (f.max() - f.min())  # растягиваем значения в [0, 1], чтобы нарисовать как картинку
    ax.imshow(f.permute(1, 2, 0), interpolation="nearest")
    ax.axis("off")
plt.suptitle("64 фильтра первого слоя ResNet-18")
plt.show()

### Cell 61: markdown

Почти все фильтры это либо перепады яркости под разными углами (детекторы границ и полосок), либо цветные пятна и переходы между цветами. Никто не закладывал их в сеть вручную: она сама пришла к ним, пока училась различать собак, машины и чашки.

Интересно, что живое зрение устроено похоже. В 1959-1962 годах Дэвид Хьюбел и Торстен Визел обнаружили в первичной зрительной коре кошек и обезьян нейроны, которые реагируют на полоски определённого наклона. За это открытие они получили Нобелевскую премию. Первый слой свёрточной сети, обученной на фотографиях, раз за разом приходит к очень похожим детекторам.

Это и объясняет результат части 2. Границы, полоски и цветовые пятна есть на любых картинках, поэтому первые слои сети, обученной на ImageNet, одинаково полезны и для собак, и для снимков из космоса.

### 4.3 Карты признаков

Если приложить один фильтр ко всем местам картинки, получится карта признаков: картинка, которая показывает, где на снимке нашёлся этот шаблон. Посмотрим на карты первых двух слоёв нашей `SatNet` для реки, шоссе и жилого района.

В каждом ряду слева исходный снимок, дальше 16 каналов. Яркие места означают, что фильтр сработал сильно.

### Cell 62: code

def show_feature_maps(img, n=16):
    model_cnn.eval()
    with torch.no_grad():
        x = img.unsqueeze(0).to(device)
        maps1 = F.relu(model_cnn.conv1(x))
        maps2 = F.relu(model_cnn.conv2(model_cnn.pool(maps1)))

    fig, axes = plt.subplots(2, n + 1, figsize=(n + 1.5, 2.6))
    for row, (maps, name) in enumerate([(maps1, "conv1"), (maps2, "conv2")]):
        axes[row, 0].imshow(img.permute(1, 2, 0))
        axes[row, 0].set_title(name)
        for k in range(n):
            axes[row, k + 1].imshow(maps[0, k].cpu(), cmap="viridis")
        for ax in axes[row]:
            ax.axis("off")
    plt.tight_layout()
    plt.show()


for cls in ["River", "Highway", "Residential"]:
    i = d_test.targets.index(CLASSES.index(cls))
    img, _ = d_test[i]
    print(CLASSES_RU[CLASSES.index(cls)])
    show_feature_maps(img)

### Cell 63: markdown

Карты `conv1` ещё очень похожи на исходный снимок. Каждая подсвечивает что-то простое: одна воду, другая светлые линии, третья зелень, четвёртая края объектов. Поищите на реке карту, где ярко горит только сама река.

Карты `conv2` вдвое меньше и заметно абстрактнее. Каждый нейрон второго слоя смотрит на участок побольше и реагирует уже не на отдельный перепад яркости, а на сочетания простых узоров. Чем глубже слой, тем меньше его карты похожи на снимок и тем больше они говорят о смысле: «здесь сетка улиц», «здесь вода с ровным берегом». А последний слой из этих признаков собирает ответ.

### 4.4 Куда смотрит сеть

Сеть уверенно говорит «река». Но на что она при этом смотрит, на саму реку или на поля вокруг неё? Проверить можно очень простым способом: будем по очереди закрывать разные участки снимка квадратом цвета фона и смотреть, насколько падает уверенность сети в правильном классе. Если закрыли что-то важное, уверенность сильно упадёт.

Так получается тепловая карта: чем ярче место, тем сильнее сеть на него опирается. Метод называется occlusion sensitivity.

### Cell 64: code

def occlusion_map(model, img, target, patch=16, stride=4):
    model.eval()
    positions = [(i, j) for i in range(0, 64 - patch + 1, stride)
                        for j in range(0, 64 - patch + 1, stride)]
    fill = img.mean(dim=(1, 2), keepdim=True)  # средний цвет снимка
    batch = img.unsqueeze(0).repeat(len(positions), 1, 1, 1)
    for k, (i, j) in enumerate(positions):
        batch[k, :, i:i + patch, j:j + patch] = fill

    with torch.no_grad():
        base = F.softmax(model(img.unsqueeze(0).to(device)), dim=1)[0, target].item()
        p = F.softmax(model(batch.to(device)), dim=1)[:, target].cpu()

    heat = torch.zeros(64, 64)
    count = torch.zeros(64, 64)
    for k, (i, j) in enumerate(positions):
        heat[i:i + patch, j:j + patch] += base - p[k]
        count[i:i + patch, j:j + patch] += 1
    return (heat / count).clamp(min=0)


show_classes = ["River", "Highway", "Residential", "Industrial", "SeaLake"]
fig, axes = plt.subplots(2, len(show_classes), figsize=(3 * len(show_classes), 6.4))
for j, cls in enumerate(show_classes):
    c = CLASSES.index(cls)
    # первый снимок этого класса, который сеть распознала правильно
    i = next(k for k in range(len(targets)) if targets[k] == c and preds[k] == c)
    heat = occlusion_map(best_model, best_test_ds[i][0], c)
    img = d_test[i][0].permute(1, 2, 0)

    axes[0, j].imshow(img)
    axes[0, j].set_title(CLASSES_RU[c])
    axes[1, j].imshow(img.mean(dim=2), cmap="gray")
    axes[1, j].imshow(heat, cmap="inferno", alpha=0.6)
    for ax in axes[:, j]:
        ax.axis("off")
axes[1, 0].set_title("куда смотрит сеть", loc="left")
plt.tight_layout()
plt.show()

### Cell 65: markdown

Хорошо, если у реки подсвечена сама река, а у шоссе сама дорога. Но иногда сеть смотрит в неожиданные места, например на поля вокруг дороги, а не на дорогу. Это повод насторожиться: возможно, модель выучила не сам объект, а его типичное окружение. Такое называют shortcut learning. Это одна из самых частых проблем нейросетей, и её регулярно находят даже у больших моделей. Известный пример есть в статье про метод объяснения моделей LIME: классификатор, который «отличал» волков от хаски, на самом деле смотрел на снег на фоне.

Попробуйте поменять в коде классы или номера снимков и посмотреть на другие примеры, особенно на ошибки из 3.4.

### 4.5 Бонус: ваш район из космоса

Совсем необязательно, но интересно. Откройте Яндекс Карты или Google Maps в режиме «Спутник» и найдите свой район, дачу или любое другое место. Подберите масштаб так, чтобы в кадр помещался квадрат примерно 600 на 600 метров (ориентируйтесь по линейке масштаба в углу). Сделайте скриншот, вырежьте из него квадрат и сохраните рядом с ноутбуком как `my_place.png`. Ячейка ниже покажет, что думает о нём лучшая модель.

### Cell 66: code

path = "my_place.png"

if os.path.exists(path):
    img = Image.open(path).convert("RGB").resize((64, 64))
    best_model.eval()
    with torch.no_grad():
        p = F.softmax(best_model(best_transform(img).unsqueeze(0).to(device)), dim=1)[0].cpu()
    top = torch.argsort(p, descending=True)[:3].tolist()

    plt.imshow(img)
    plt.axis("off")
    plt.title(", ".join(f"{CLASSES_RU[i]} {p[i].item():.0%}" for i in top))
    plt.show()
else:
    print("Положите рядом с ноутбуком файл my_place.png")

### Cell 67: markdown

Если сеть уверенно назвала ваш двор промзоной, не обижайтесь. Ваш снимок сильно отличается от тех, на которых она училась, и это называется сдвигом данных (domain shift):
- в EuroSAT снимки со спутника Sentinel-2 с разрешением 10 метров на пиксель. На картах обычно стоят гораздо более детальные снимки, часто аэрофотосъёмка, и после уменьшения до 64 на 64 они выглядят иначе;
- у разных спутников и камер разные цвета, а сеть к цветам очень чувствительна;
- в EuroSAT только Европа. Другая застройка, другие поля или снег сети незнакомы;
- у каждого снимка в датасете ровно один класс, а реальный квадрат 600 на 600 метров часто содержит всё сразу: дома, дорогу и кусок леса.

Для реальных проектов это обычная история. Модель, которая показывает 98% на тесте, в жизни может работать заметно хуже, если данные отличаются от обучающих. Поэтому модели всегда проверяют на данных, максимально похожих на те, с которыми им придётся работать.

## homeworks/Homework_tsk_1.ipynb

### Cell 1: markdown

# Домашнее задание: учим сеть угадывать рисунки

На семинаре мы учили сеть распознавать цифры. В домашке возьмём данные поживее: рисунки из игры [Quick, Draw!](https://quickdraw.withgoogle.com/) от Google. Там игроку дают слово, у него 20 секунд, чтобы это нарисовать, а сеть пытается угадать, что он рисует. Google выложил в открытый доступ больше 50 миллионов таких рисунков.

Мы возьмём 10 классов (яблоко, банан, кот, рыба, гитара, дом, луна, самолёт, велосипед, зонтик), по 2500 картинок на класс. Каждая картинка 28 на 28 пикселей, так что по размеру всё как с цифрами. Но рисуют люди очень по-разному и часто как попало, поэтому задача заметно интереснее.

Основа такая же, как на семинаре: свой Dataset, сеть из линейных слоёв, цикл обучения. Поверх этого добавятся три новые вещи:
1. посчитать градиент слоя руками и сверить с тем, что выдаёт PyTorch;
2. сравнить SGD, SGD с momentum и Adam;
3. переобучить сеть специально, а потом лечить её через Dropout и BatchNorm.

Код пишете там, где стоит `# ваш код`. Остальные ячейки просто запускаете. На вопросы отвечайте в ячейках «Ответы» своими словами, хватит 2-3 предложений на вопрос.

### Оценивание

| Часть | Что смотрим | Баллы |
|---|---|---|
| 1. Pipeline | Dataset и DataLoader, модель, функции `train_model` и `accuracy`, ответы на вопросы | 2.5 |
| 2. Градиент руками | формулы, `manual_grads` без `.backward()`, сверка с autograd, проверка на слое обученной сети | 2.5 |
| 3. Оптимизаторы | эксперимент с тремя оптимизаторами, графики сходимости, выводы | 2.5 |
| 4. Dropout и BatchNorm | модель `DrawNetReg`, четыре эксперимента с графиками, эксперимент с `model.train()`, анализ переобучения | 2.5 |

**Пересдачи нет.** Поэтому перед отправкой сделайте `Kernel > Restart & Run All` и проверьте, что всё выполняется сверху вниз без ошибок. Если ячейка падает, задание из неё не засчитывается. Сдаёте `.ipynb` с выводами и графиками.


### Cell 2: code

import os
import json
import urllib.request

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import torchvision.transforms.v2 as tfs

### Cell 3: markdown

## Данные

Ячейка ниже скачивает рисунки и раскладывает их по папкам в том же формате, что был на семинаре: `quickdraw/train/<класс>/*.png`, `quickdraw/test/<класс>/*.png` и `format.json` с номерами классов. Скачается около 20 Мб, займёт пару минут.

Если скачивание оборвалось на середине, удалите папку `quickdraw` и запустите ячейку ещё раз.

### Cell 4: code

CLASSES = ["apple", "banana", "cat", "fish", "guitar",
           "house", "moon", "airplane", "bicycle", "umbrella"]
N_TRAIN, N_TEST = 2000, 500
URL = "https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/{}.npy"


def download_drawings(name, n):
    # целиком файл весит около 100 Мб, поэтому читаем только первые n рисунков
    with urllib.request.urlopen(URL.format(name)) as r:
        version = np.lib.format.read_magic(r)
        if version == (1, 0):
            np.lib.format.read_array_header_1_0(r)
        else:
            np.lib.format.read_array_header_2_0(r)
        raw = r.read(n * 28 * 28)
    return np.frombuffer(raw, dtype=np.uint8).reshape(n, 28, 28)


def make_dataset(path="quickdraw"):
    if os.path.exists(path):
        print("Датасет уже скачан")
        return

    for part in ("train", "test"):
        os.makedirs(os.path.join(path, part))
        with open(os.path.join(path, part, "format.json"), "w") as fp:
            json.dump({name: i for i, name in enumerate(CLASSES)}, fp)

    for name in tqdm(CLASSES):
        drawings = download_drawings(name, N_TRAIN + N_TEST)
        for part, chunk in (("train", drawings[:N_TRAIN]), ("test", drawings[N_TRAIN:])):
            folder = os.path.join(path, part, name)
            os.makedirs(folder)
            for i, img in enumerate(chunk):
                Image.fromarray(img).save(os.path.join(folder, f"{i}.png"))


make_dataset()

### Cell 5: code

fig, axes = plt.subplots(3, 10, figsize=(14, 4.5))
for j, name in enumerate(CLASSES):
    for i in range(3):
        img = Image.open(f"quickdraw/train/{name}/{i}.png")
        axes[i, j].imshow(img, cmap="gray_r")
        axes[i, j].axis("off")
    axes[0, j].set_title(name)
plt.show()

### Cell 6: markdown

---
## Часть 1. Pipeline обучения
Здесь почти всё как на семинаре, только данные другие.

### 1.1 Dataset

Напишите класс `DrawDataset`. Он должен:
- в `__init__` прочитать `format.json` и собрать список всех файлов вместе с их классами;
- в `__getitem__` открыть картинку, превратить её в вектор длины 784 со значениями от 0 до 1 и вернуть вместе с one-hot меткой (как на семинаре, через `torch.eye(10)`);
- в `__len__` вернуть количество картинок.

### Cell 7: code

class DrawDataset(data.Dataset):
    def __init__(self, path, train=True, transform=None):
        pass  # ваш код

    def __getitem__(self, item):
        pass  # ваш код

    def __len__(self):
        pass  # ваш код

### Cell 8: markdown

### 1.2 DataLoader

Создайте обучающий датасет, разбейте его на train и validation в пропорции 0.8 / 0.2 (через `data.random_split` с генератором `torch.Generator().manual_seed(42)`) и сделайте три загрузчика:
- `train_data` с перемешиванием, `batch_size=32`;
- `train_data_val` без перемешивания, `batch_size=32`;
- `test_data` для тестовой выборки, `batch_size=500`.

### Cell 9: code

to_tensor = tfs.ToImage()

# ваш код

### Cell 10: code

# быстрая проверка
x, y = next(iter(train_data))
print(x.shape, y.shape)  # должно быть torch.Size([32, 784]) torch.Size([32, 10])
print(x.min().item(), x.max().item())  # от 0 до 1

### Cell 11: markdown

### 1.3 Модель

Сеть такая же, как `DigitNet` на семинаре: линейный слой, ReLU, второй линейный слой.

### Cell 12: code

class DrawNet(nn.Module):
    def __init__(self, input_dim, num_hidden, output_dim):
        super().__init__()
        # ваш код

    def forward(self, x):
        pass  # ваш код

### Cell 13: markdown

### 1.4 Цикл обучения как функция

 Дальше нам придётся обучать много разных моделей, поэтому оформите его в функцию `train_model`. Внутри можно почти дословно взять код с семинара.

Функция должна:
- на каждой эпохе обучать модель на `train_data` и считать средний loss (как `loss_mean` на семинаре);
- после каждой эпохи считать на `val_data` средний loss (как `Q_val`) и долю верных ответов;
- вернуть три списка: `loss_lst`, `loss_lst_val` и `acc_lst_val`.

Accuracy на валидации нам понадобится в частях 3 и 4: дальше будет видно, что loss и accuracy иногда рассказывают разные истории.

И ещё одна функция, `accuracy`, должна возвращать долю верных ответов модели на загрузчике (как мы считали `Q` на тесте).

### Cell 14: code

def train_model(model, optimizer, train_data, val_data, epochs, verbose=True):
    loss_function = nn.CrossEntropyLoss()
    loss_lst = []
    loss_lst_val = []
    acc_lst_val = []

    # ваш код

    return loss_lst, loss_lst_val, acc_lst_val


def accuracy(model, loader):
    pass  # ваш код

### Cell 15: markdown

Теперь обучите `DrawNet(28 * 28, 128, 10)` с Adam (`lr=0.001`) 10 эпох, нарисуйте график loss на train и validation и посчитайте accuracy на тесте. Ориентир по accuracy: около 0.8 и выше. Если получается сильно меньше, скорее всего где-то ошибка.

### Cell 16: code

torch.manual_seed(42)

# ваш код

### Cell 17: markdown

**Вопросы**
1. В `forward` мы не применяем softmax, хотя на выходе хотим вероятности классов. Почему так можно и даже нужно?
2. Посмотрите на картинки в начале ноутбука. Какие классы сеть, по-вашему, будет путать чаще всего и почему?
3. Сколько обучаемых параметров у `DrawNet(784, 128, 10)`? Посчитайте руками и проверьте кодом.

### Cell 18: code

# проверка числа параметров

### Cell 19: markdown

**Ответы:**

1.

2.

3.

### Cell 20: markdown

---
## Часть 2. Градиент руками

`loss.backward()` считает градиенты по цепному правилу. Давайте сделаем то же самое сами для одного слоя.

Берём линейный слой, после него ReLU, и функцию потерь MSE:

$$z = xW^T + b, \qquad h = \mathrm{ReLU}(z), \qquad L = \frac{1}{N \cdot d_{out}} \sum_{i,j} (h_{ij} - t_{ij})^2$$

Размеры: $x$ имеет размер $(N, d_{in})$, $W$ размер $(d_{out}, d_{in})$ (именно так веса хранит `nn.Linear`), $b$ размер $(d_{out})$, а $z$, $h$ и $t$ размер $(N, d_{out})$.

Нужно найти $\frac{\partial L}{\partial W}$, $\frac{\partial L}{\partial b}$ и $\frac{\partial L}{\partial x}$. Проще всего идти с конца: сначала $\frac{\partial L}{\partial h}$, потом $\frac{\partial L}{\partial z}$, а через него уже всё остальное.

### Cell 21: markdown

### 2.1 Считаем руками

Напишите функцию `manual_grads`, которая делает прямой проход (z, h, loss) и считает `dW`, `db`, `dx` по вашим формулам. Вызывать `.backward()` и пользоваться `torch.autograd` здесь нельзя, только операции с матрицами.

### Cell 22: code

def manual_grads(x, W, b, t):
    # ваш код
    return dW, db, dx


torch.manual_seed(0)
x = torch.randn(5, 4)
W = torch.randn(3, 4)
b = torch.randn(3)
t = torch.randn(5, 3)

dW, db, dx = manual_grads(x, W, b, t)
print(dW.shape, db.shape, dx.shape)  # должны совпадать с W.shape, b.shape, x.shape

### Cell 23: markdown

### 2.2 Сверяем с autograd

Теперь посчитайте те же градиенты через PyTorch: сделаем копии `x`, `W`, `b` с `requires_grad=True`, прогоним тот же прямой проход, вызовем `backward()` и сравним `.grad` с вашими `dW`, `db`, `dx`.

Сравнивать удобно через `torch.allclose(a, b, atol=1e-6)`. Все три сравнения должны дать `True`.

### Cell 24: code

x_ = x.clone().requires_grad_()
W_ = W.clone().requires_grad_()
b_ = b.clone().requires_grad_()

loss = ((F.relu(x_ @ W_.T + b_) - t) ** 2).mean()
loss.backward()

print("dW:", torch.allclose(dW, W_.grad, atol=1e-6))
print("db:", torch.allclose(db, b_.grad, atol=1e-6))
print("dx:", torch.allclose(dx, x_.grad, atol=1e-6))

### Cell 25: markdown

### 2.3 Проверка на настоящей сети

Возьмите первый слой модели, которую обучили в части 1 (`model.layer1`), и батч картинок из `train_data_val`. Целевые значения `t` возьмите случайные, размером (32, 128).

Посчитайте loss как `F.mse_loss(F.relu(model.layer1(x_batch)), t_batch)`, вызовите `backward()` и сравните `model.layer1.weight.grad` и `model.layer1.bias.grad` с тем, что выдаёт ваша `manual_grads`. Перед этим не забудьте `model.zero_grad()`, чтобы там не остались градиенты от обучения.

### Cell 26: code

torch.manual_seed(1)

x_batch, _ = next(iter(train_data_val))
t_batch = torch.randn(32, 128)

# ваш код

### Cell 27: markdown

**Вопросы**
1. ReLU не дифференцируема в нуле. Какую производную в этой точке берёт PyTorch? Проверьте маленьким экспериментом в ячейке ниже.
2. Зачем вообще считать $\frac{\partial L}{\partial x}$, если $x$ это данные и мы их не обучаем? Подумайте про сеть из нескольких слоёв.

### Cell 28: code

# эксперимент с производной ReLU в нуле

### Cell 29: markdown

**Ответы:**

1.

2.

### Cell 30: markdown

---
## Часть 3. Сравниваем оптимизаторы

Обучите одну и ту же `DrawNet(28 * 28, 128, 10)` тремя оптимизаторами по 15 эпох:

| Оптимизатор | Параметры |
|---|---|
| SGD | `lr=0.05` |
| SGD + momentum | `lr=0.05, momentum=0.9` |
| Adam | `lr=0.001` |

Чтобы сравнение было честным, перед созданием каждой модели вызывайте `torch.manual_seed(42)`. Тогда у всех трёх моделей будут одинаковые начальные веса и одинаковый порядок батчей.

Для каждой модели сохраните всё, что вернула `train_model`, и посчитайте accuracy на тесте. Функция `train_model` из части 1 уже умеет работать с любым оптимизатором, так что новый цикл писать не надо. Чтобы не засорять вывод, можно передать `verbose=False`.

### Cell 31: code

epochs = 15

configs = {
    "SGD": lambda params: # опитмизтор,
    "SGD + momentum": lambda params: # опитмизтор,
    "Adam": lambda params: # опитмизтор,
}

results = {}
for name, make_optimizer in configs.items():
  # ваш код

### Cell 32: markdown

Посмотрим три графика, на каждом все три оптимизатора:

### Cell 33: code

fig, axes = plt.subplots(1, 3, figsize=(17, 4))
x_epochs = range(1, epochs + 1)

for name, (loss_lst, loss_lst_val, acc_lst_val) in results.items():
    axes[0].plot(x_epochs, loss_lst, label=name)
    axes[1].plot(x_epochs, loss_lst_val, label=name)
    axes[2].plot(x_epochs, acc_lst_val, label=name)
    print(f"{name}: минимальный val loss {min(loss_lst_val):.3f} на эпохе {np.argmin(loss_lst_val) + 1}")

axes[0].set_yscale("log")
for ax, title in zip(axes, ["loss на train", "loss на validation", "accuracy на validation"]):
    ax.set_title(title)
    ax.set_xlabel("эпоха")
    ax.grid(alpha=0.3)
    ax.legend()
plt.show()

### Cell 34: markdown

<details>
<summary><b>Пояснение: почему у обычного SGD может оказаться самый низкий loss на валидации</b> (откройте после того, как посмотрите на графики)</summary>

<br>

Если у вас так получилось, это нормально, ошибки в коде нет.

**Adam и momentum не защищают от переобучения.** Это не регуляризация, а способ быстрее уменьшать loss на train. Чем быстрее оптимизатор учит сеть, тем раньше она начинает подстраиваться под конкретные картинки из обучающей выборки.

**Что происходит с Adam.** За несколько эпох он находит хорошее решение, а дальше сеть начинает переобучаться. Самое заметное последствие: она становится слишком уверенной в своих ответах. Раньше про картинку кота она говорила «кот с вероятностью 0.7», а теперь «кот с вероятностью 0.999».

Посмотрим, как на это реагирует кросс-энтропия. Loss на одном объекте равен $-\log p$, где $p$ это вероятность, которую сеть дала правильному классу:
- сеть правильно ответила с вероятностью 0.7: loss примерно 0.36;
- правильно с вероятностью 0.999: loss примерно 0.001. Выигрыш маленький;
- ошиблась, но неуверенно, правильному классу дала 0.3: loss примерно 1.2;
- ошиблась уверенно, правильному классу дала 0.001: loss примерно 6.9. Штраф огромный.

Так что пара уверенных ошибок поднимает средний loss на валидации, хотя доля правильных ответов почти не меняется. Поэтому у Adam val loss растёт, а val accuracy остаётся высокой.

**Что происходит с обычным SGD.** Он учит медленно. К 15-й эпохе он ещё не доучился и до переобучения не дошёл. Уверенных ошибок у него мало, поэтому val loss низкий. Но и правильных ответов меньше, отсюда худшая accuracy на тесте.

**Вывод.** Сравнивать модели по val loss в последней эпохе опасно, картина может получиться обманчивой. Смотрите на кривые целиком и на accuracy: на графике val accuracy видно, что SGD отстаёт. А эпоха, на которой val loss у Adam был минимальным, показывает, где обучение стоило остановить. Этот приём называется ранней остановкой (early stopping).

</details>

### Cell 35: markdown

**Вопросы**
1. Какой оптимизатор быстрее всех уменьшает loss на train? А какой даёт лучший результат на validation в конце?
2. Объясните своими словами, что делает momentum и почему он помогает обычному SGD. Видно ли это на ваших графиках?
3. Если бы вам дали новую задачу и одну попытку обучения, какой оптимизатор вы бы взяли первым и почему?

### Cell 36: markdown

**Ответы:**

1.

2.

3.

### Cell 37: markdown

---
## Часть 4. Dropout и BatchNorm

Чтобы было что лечить, сначала устроим переобучение. Оставим для обучения только 500 картинок и возьмём сеть побольше: два скрытых слоя по 512 нейронов. Такая сеть быстро выучит эти 500 картинок наизусть.

Потом добавим Dropout и BatchNorm и посмотрим, что из них на самом деле помогает от переобучения. Заранее не ждите, что помогут оба одинаково: про эти два слоя часто думают, что они делают одно и то же, но это не так.

### Cell 38: code

d_small = data.Subset(d_train, range(500))
train_small = data.DataLoader(d_small, shuffle=True, batch_size=32)
print(len(d_small))

### Cell 39: markdown

### 4.1 Модель

Напишите `DrawNetReg` с тремя линейными слоями: `input_dim > num_hidden > num_hidden > output_dim`. После каждого из двух скрытых слоёв идёт:
- BatchNorm (`nn.BatchNorm1d`), если `use_bn=True`;
- ReLU;
- Dropout с вероятностью `p_drop` (при `p_drop=0` он просто ничего не делает).

После последнего слоя ничего не добавляем.

### Cell 40: code

class DrawNetReg(nn.Module):
    def __init__(self, input_dim, num_hidden, output_dim, p_drop=0.0, use_bn=False):
        super().__init__()
        # ваш код

    def forward(self, x):
        pass  # ваш код

### Cell 41: markdown

### 4.2 Четыре эксперимента

Обучите четыре варианта `DrawNetReg(28 * 28, 512, 10, ...)` на `train_small` по 60 эпох, валидация по-прежнему на `train_data_val`. Оптимизатор Adam, `lr=0.001`, перед каждой моделью `torch.manual_seed(42)`.

| Вариант | p_drop | use_bn |
|---|---|---|
| baseline | 0 | False |
| dropout | 0.5 | False |
| batchnorm | 0 | True |
| dropout + bn | 0.5 | True |

Для каждого варианта нарисуйте график loss на train и validation и отдельно accuracy на validation (удобно сделать сетку 2 на 4: сверху loss, снизу accuracy) и посчитайте accuracy на тесте. Обученные модели сохраните, одна понадобится в 4.3.

### Cell 42: code

epochs = 60

variants = {
    "baseline": dict(#параметры модели),
    "dropout": dict(#параметры модели),
    "batchnorm": dict(#параметры модели),
    "dropout + bn": dict(#параметры модели),
}

reg_results = {}
reg_models = {}

# Ваш код

fig, axes = plt.subplots(2, 4, figsize=(18, 7), sharey="row")
for j, (name, (loss_lst, loss_lst_val, acc_lst_val)) in enumerate(reg_results.items()):
    axes[0, j].plot(loss_lst, label="train")
    axes[0, j].plot(loss_lst_val, label="val")
    axes[0, j].set_title(name)
    axes[0, j].legend()
    axes[1, j].plot(acc_lst_val, color="tab:green")
    axes[1, j].set_xlabel("эпоха")
    for ax in axes[:, j]:
        ax.grid(alpha=0.3)
axes[0, 0].set_ylabel("loss")
axes[1, 0].set_ylabel("accuracy на validation")
plt.show()

### Cell 43: markdown

<details>
<summary><b>Пояснение: почему BatchNorm может оказаться хуже baseline и как Dropout уживается с BatchNorm</b> (откройте после того, как посмотрите на графики)</summary>

<br>

**BatchNorm хуже baseline.** BatchNorm придумывали не для борьбы с переобучением. Его главная задача в том, чтобы ускорить и стабилизировать обучение. Он нормирует выходы слоя, и на вход следующему слою всегда приходят значения примерно одного масштаба. Из-за этого сеть учится быстрее и меньше зависит от неудачной инициализации или learning rate.

Небольшой регуляризующий эффект у BatchNorm тоже есть. Среднее и дисперсия считаются по случайному батчу, и это добавляет в обучение немного шума. Но эффект слабый и побочный.

У нас всего 500 картинок. Сеть с BatchNorm запоминает их ещё быстрее, чем baseline: train loss почти сразу уходит к нулю, а val loss начинает расти уже через несколько эпох. Сравните, как быстро падает train loss у baseline и у batchnorm. Это и есть ускорение, которое даёт BatchNorm. А по-настоящему от переобучения в этом эксперименте помогает Dropout.

**Dropout вместе с BatchNorm.** Использовать их вместе не запрещено, но есть известный эффект. Его подробно разобрали в статье [Li et al., 2019, «Understanding the Disharmony between Dropout and Batch Normalization by Variance Shift»](https://arxiv.org/abs/1801.05134).

Чтобы понять суть, вспомним, как работают оба слоя:
- BatchNorm во время обучения копит в `running_mean` и `running_var` среднее и дисперсию своих входов. В режиме `eval()` он нормирует данные именно по этим накопленным значениям;
- Dropout во время обучения обнуляет часть нейронов, а оставшиеся умножает на $\frac{1}{1-p}$, чтобы среднее не изменилось. Среднее действительно сохраняется, а вот разброс значений становится больше. В режиме `eval()` Dropout выключен, и разброс снова обычный.

Теперь представим, что Dropout стоит перед BatchNorm. Во время обучения BatchNorm видит данные с увеличенным разбросом и запоминает именно такую дисперсию. При предсказании Dropout выключается, разброс входов становится меньше, а BatchNorm продолжает нормировать по старой, завышенной дисперсии. Получается, что он подстроен под одни данные, а работает с другими. В нашей сети так устроен второй блок: Dropout после первого слоя стоит прямо перед BatchNorm второго слоя.

Сильнее всего это мешает глубоким свёрточным сетям, где таких мест много и ошибка накапливается от слоя к слою. В небольшой сети вроде нашей связка обычно работает нормально, что и видно в эксперименте. Если хочется подстраховаться, Dropout ставят только после последнего слоя с BatchNorm, ближе к выходу сети.

</details>

### Cell 44: markdown

### 4.3 Что будет, если забыть `model.eval()`

Возьмите модель `dropout` из прошлого пункта, переведите её в режим `model.train()` и посчитайте accuracy на тесте три раза подряд. Функция `accuracy` здесь не подойдёт, потому что она сама включает `eval()`, так что посчитайте вручную (не забудьте `torch.no_grad()`). Потом сравните с accuracy в режиме `eval()`.

### Cell 45: code

# ваш код

### Cell 46: markdown

**Вопросы**
1. Примерно с какой эпохи у baseline начинается переобучение? По каким признакам на графике вы это поняли?
2. Какой вариант сильнее всего уменьшил разрыв между train и validation? Какой дал лучшую accuracy на тесте? Это один и тот же вариант?
3. У модели с dropout loss на train может оказаться выше, чем на validation. Как такое может быть?

### Cell 47: markdown

**Ответы:**

1.

2.

3.

## lecture_01/seminar_1_zanatye.ipynb

### Cell 1: markdown

## Повтор формул с лекции

- Нейрон: $z = w \cdot x + b$
- Гладкая активация: $\hat{y} = \sigma(z) = \dfrac{1}{1+e^{-z}}$
- Функция потерь $L(w)$ — насколько сильно модель ошибается
- Градиент — вектор частных производных: $\nabla L = (\partial L/\partial w_1, ..., \partial L/\partial w_n)$
- Шаг градиентного спуска: $w \leftarrow w - \eta \nabla L$

Сегодня PyTorch возьмёт на себя вычисление $\nabla L$ (это и называется autograd), а сам цикл обновления весов мы напишем своими руками.

### Cell 2: code

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F

torch.manual_seed(0)
np.random.seed(0)
print("PyTorch версия:", torch.__version__)

### Cell 3: markdown

---

## Часть 1. PyTorch: тензоры и autograd

Тензор — это, по сути, тот же массив numpy, но с суперспособностью: если сказать `requires_grad=True`, PyTorch запоминает каждую операцию над тензором и потом может сам посчитать производную.

Проверим на игрушечном примере: $y = x^2$. Мы точно знаем аналитически, что $dy/dx = 2x$. Посмотрим, посчитает ли PyTorch то же самое сам.

### Cell 4: code

x = torch.tensor(3.0, requires_grad=True)
y = x ** 2

y.backward()  # здесь PyTorch вычисляет производную

print("x =", x.item())
print("y = x^2 =", y.item())
print("dy/dx, посчитанное PyTorch (x.grad):", x.grad.item())
print("dy/dx по формуле 2x:", 2 * x.item())

### Cell 5: markdown

Совпало. Это и есть autograd: `y.backward()` проходит по всем операциям в обратном порядке (отсюда и «обратное распространение», с которым мы подробно встретимся на следующей лекции) и раскладывает производную по всем тензорам с `requires_grad=True`.

> 🎓 **Попробуйте сами:** посчитайте градиент для $y = x^3 + 2x$ в точке $x=2$ и сверьте с формулой $dy/dx = 3x^2+2$.

### Cell 6: markdown

---

## Часть 2. Градиентный спуск вручную — на одной параболе

Возьмём ту самую функцию потерь с лекции: $L(w) = (w-3)^2 + 1$ — парабола с минимумом в точке $w=3$. Стартуем издалека, например с $w=-2$, и будем спускаться сами, шаг за шагом.

Ниже — каркас цикла с двумя пропущенными строчками. Заполните их по формуле $w \leftarrow w - \eta \cdot \partial L/\partial w$, где `w.grad` — это и есть $\partial L/\partial w$, уже посчитанный PyTorch.

### Cell 7: code

def loss_1d(w):
    return (w - 3.0) ** 2 + 1.0


w = torch.tensor([-2.0], requires_grad=True)
lr = 0.15
history_1d = [(w.item(), loss_1d(w).item())]

for step in range(14):
    loss = loss_1d(w)
    loss.backward()
    with torch.no_grad():
        # ЗАДАНИЕ: обновите w по формуле w <- w - lr * w.grad
        pass  # ВАШ КОД ЗДЕСЬ (1 строка)
    w.grad.zero_()  # обнуляем градиент - иначе PyTorch будет их суммировать
    history_1d.append((w.item(), loss_1d(w).item()))

print("Финальный w:", round(w.item(), 3), " (цель: 3.0)")

### Cell 8: markdown

### Решение (открыть после самостоятельной попытки)

### Cell 9: code

w = torch.tensor([-2.0], requires_grad=True)
lr = 0.03
history_1d = [(w.item(), loss_1d(w).item())]

for step in range(14):
    loss = loss_1d(w)
    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad          # w <- w - eta * dL/dw
    w.grad.zero_()
    history_1d.append((w.item(), loss_1d(w).item()))

print("Финальный w:", round(w.item(), 3), " (цель: 3.0)")
for i, (wv, lv) in enumerate(history_1d):
    if i % 3 == 0 or i == len(history_1d) - 1:
        print(f"  шаг {i:2d}: w={wv:6.3f}  L(w)={lv:.3f}")

### Cell 10: markdown

А теперь — та самая визуализация: нарисуем саму параболу и наложим на неё путь, который прошёл градиентный спуск. Каждая точка — это `w` в конце очередного шага; цвет от красного к зелёному показывает прогресс по времени.

### Cell 11: code

ws_plot = np.linspace(-3, 9, 200)
Ls_plot = [loss_1d(torch.tensor(wv)).item() for wv in ws_plot]

hw = [h[0] for h in history_1d]
hl = [h[1] for h in history_1d]

plt.figure(figsize=(7, 5))
plt.plot(ws_plot, Ls_plot, color="navy", linewidth=2, label="L(w) = (w-3)² + 1", zorder=1)
plt.plot(hw, hl, "-", color="gray", alpha=0.5, zorder=2)
sc = plt.scatter(hw, hl, c=range(len(hw)), cmap="autumn_r", s=70, zorder=3, edgecolor="k")
plt.scatter([hw[0]], [hl[0]], color="red", s=140, zorder=4, label="старт", edgecolor="k")
plt.scatter([hw[-1]], [hl[-1]], color="green", s=140, zorder=4, label="финиш", edgecolor="k")
plt.colorbar(sc, label="номер шага")
plt.xlabel("w")
plt.ylabel("L(w)")
plt.title("Градиентный спуск: точка постепенно скатывается к минимуму")
plt.legend()
plt.show()

plt.figure(figsize=(7, 3.5))
plt.plot(range(len(hl)), hl, marker="o", color="tab:blue")
plt.xlabel("Шаг")
plt.ylabel("L(w)")
plt.title("То же самое, но по оси времени")
plt.grid(alpha=0.3)
plt.show()

### Cell 12: markdown

> 🎓 **Попробуйте сами:** поставьте `lr = 1.05` и переобучите — что произойдёт с точкой на параболе? А если `lr = 0.01`? Это ровно то же самое «слишком быстро / слишком медленно» с лекции, только теперь видно буквально на графике, как шарик либо скачет, либо еле ползёт.

---

## Часть 3. Вектор признаков «кошка / собака» — быстрый повтор

Как и на лекции: превращаем животных в числа — два признака, размер и пушистость.

### Cell 13: code

def make_cats_dogs(n_per_class=40, noise=0.10):
    # 0 = кошка, 1 = собака
    cats = np.stack([
        np.random.normal(0.35, noise, n_per_class),  # размер
        np.random.normal(0.70, noise, n_per_class),  # пушистость
    ], axis=1)
    dogs = np.stack([
        np.random.normal(0.70, noise, n_per_class),
        np.random.normal(0.35, noise, n_per_class),
    ], axis=1)
    X = np.vstack([cats, dogs])
    y = np.array([0] * n_per_class + [1] * n_per_class)
    idx = np.random.permutation(len(y))
    return X[idx], y[idx]


X_np, y_np = make_cats_dogs()

# Переводим numpy -> torch. Это то, с чем вы будете работать весь курс.
X = torch.tensor(X_np, dtype=torch.float32)
y = torch.tensor(y_np, dtype=torch.float32)

print("X:", X.shape, X.dtype)
print("y:", y.shape, y.dtype)

plt.figure(figsize=(5.5, 4.5))
plt.scatter(X[y == 0, 0], X[y == 0, 1], label="кошки", edgecolor="k")
plt.scatter(X[y == 1, 0], X[y == 1, 1], label="собаки", edgecolor="k")
plt.xlabel("размер (норм.)")
plt.ylabel("пушистость (норм.)")
plt.legend()
plt.title("Вектор признаков x = (размер, пушистость)")
plt.show()

### Cell 14: markdown

---

## Часть 4. От перцептрона к гладкому нейрону

На лекции мы установили: ступенчатая активация перцептрона не дифференцируема — градиентный спуск с ней не работает. Поэтому сегодня наш нейрон устроен чуть иначе:

$$z = w \cdot x + b, \qquad \hat{y} = \sigma(z) = \frac{1}{1+e^{-z}}$$

Выход — не жёсткий 0 или 1, а число от 0 до 1: «вероятность, что это собака». А в качестве функции потерь возьмём стандартную для классификации — **binary cross-entropy** (бинарную кросс-энтропию): она сильно штрафует уверенные, но неправильные ответы. Формулу дифференцировать руками не нужно — за нас это сделает `loss.backward()`; в PyTorch она уже реализована как `F.binary_cross_entropy`.

### Cell 15: code

def neuron_forward(X, w, b):
    z = X @ w + b            # то самое w*x + b, только сразу для всех примеров матрицей
    return torch.sigmoid(z)  # гладкая активация вместо ступеньки


# быстрая проверка на необученных весах
w_demo = torch.zeros(2, requires_grad=True)
b_demo = torch.zeros(1, requires_grad=True)
pred_demo = neuron_forward(X, w_demo, b_demo)
loss_demo = F.binary_cross_entropy(pred_demo, y)
print("Предсказания необученного нейрона (первые 5):", pred_demo[:5].detach().numpy().round(3))
print("Loss необученного нейрона:", loss_demo.item())

### Cell 16: markdown

---

## Часть 5. Обучаем нейрон градиентным спуском — снова вручную

Структура цикла ровно та же, что и на параболе в части 2: посчитать loss → `backward()` → вручную обновить веса → обнулить градиенты. Разница только в том, что теперь у нас не один параметр, а вектор весов `w` (2 числа) и смещение `b`.

### Cell 17: code

w = torch.zeros(2, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
lr = 2.0
epochs = 300
loss_history = []

for epoch in range(epochs):
    pred = neuron_forward(X, w, b)
    loss = F.binary_cross_entropy(pred, y)

    loss.backward()
    with torch.no_grad():
        # ЗАДАНИЕ: обновите w и b по правилу w <- w - lr*w.grad, b <- b - lr*b.grad
        pass  # ВАШ КОД ЗДЕСЬ (2 строки)
    w.grad.zero_()
    b.grad.zero_()

    loss_history.append(loss.item())
    if epoch % 50 == 0 or epoch == epochs - 1:
        print(f"Эпоха {epoch+1:3d}: loss = {loss.item():.4f}")

### Cell 18: markdown

### Решение

### Cell 19: code

w = torch.zeros(2, requires_grad=True)
b = torch.zeros(1, requires_grad=True)
lr = 2.0
epochs = 300
loss_history = []

for epoch in range(epochs):
    pred = neuron_forward(X, w, b)
    loss = F.binary_cross_entropy(pred, y)

    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad
    w.grad.zero_()
    b.grad.zero_()

    loss_history.append(loss.item())
    if epoch % 50 == 0 or epoch == epochs - 1:
        print(f"Эпоха {epoch+1:3d}: loss = {loss.item():.4f}")

print("\nФинальные веса: w =", w.detach().numpy().round(3), " b =", round(b.item(), 3))

### Cell 20: markdown

---

## Часть 6. Визуализация: как падает loss и как выглядит граница

Сначала — как убывает loss (это и есть тот самый «шарик, скатывающийся вниз», только теперь в пространстве тысяч возможных весов сразу, а не на одной параболе). Потом — граница решения: обратите внимание, она уже не резкая линия «либо класс 0, либо класс 1», а плавный градиент вероятности — прямое следствие того, что активация гладкая.

### Cell 21: code

plt.figure(figsize=(7, 4))
plt.plot(range(1, len(loss_history) + 1), loss_history, color="tab:blue")
plt.xlabel("Эпоха")
plt.ylabel("Loss (BCE)")
plt.title("Loss убывает — тот же градиентный спуск, что и на параболе")
plt.grid(alpha=0.3)
plt.show()


def plot_boundary(forward_fn, X, y, title, label0="кошки", label1="собаки",
                   xlabel="размер (норм.)", ylabel="пушистость (норм.)", cbar_label="ŷ (вероятность класса 1)"):
    plt.figure(figsize=(6, 5))
    x_min, x_max = X[:, 0].min().item() - 0.15, X[:, 0].max().item() + 0.15
    y_min, y_max = X[:, 1].min().item() - 0.15, X[:, 1].max().item() + 0.15
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 150), np.linspace(y_min, y_max, 150))
    grid = torch.tensor(np.c_[xx.ravel(), yy.ravel()], dtype=torch.float32)
    with torch.no_grad():
        preds = forward_fn(grid).numpy().reshape(xx.shape)
    cs = plt.contourf(xx, yy, preds, levels=20, cmap="RdYlBu_r", alpha=0.55)
    plt.colorbar(cs, label=cbar_label)

    Xn, yn = X.numpy(), y.numpy()
    plt.scatter(Xn[yn == 0, 0], Xn[yn == 0, 1], label=label0, edgecolor="k", s=80)
    plt.scatter(Xn[yn == 1, 0], Xn[yn == 1, 1], label=label1, edgecolor="k", s=80)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


plot_boundary(lambda Xg: neuron_forward(Xg, w, b), X, y, "Обученный нейрон: вероятность, а не жёсткая граница")

### Cell 22: markdown

> 🎓 **Обсуждение:** сравните эту картинку с границей перцептрона из прошлого семинара. Перцептрон давал резкий обрыв между «точно 0» и «точно 1». Здесь — плавный переход: чем дальше от границы, тем увереннее модель. Это прямое следствие гладкости сигмоиды, о которой говорили на лекции.

---

## Часть 7. XOR: один нейрон — и снова не получается

Проверим кодом то, что доказали на лекции: ни жёсткий перцептрон, ни гладкий нейрон с одним слоем не решают XOR — дело не в жёсткости активации, а в самой линейности границы.

### Cell 23: code

X_xor = torch.tensor([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y_xor = torch.tensor([0., 1., 1., 0.])

w_x = torch.zeros(2, requires_grad=True)
b_x = torch.zeros(1, requires_grad=True)
lr = 1.0
epochs = 300
loss_hist_xor1 = []

for epoch in range(epochs):
    pred = neuron_forward(X_xor, w_x, b_x)
    loss = F.binary_cross_entropy(pred, y_xor)
    loss.backward()
    with torch.no_grad():
        w_x -= lr * w_x.grad
        b_x -= lr * b_x.grad
    w_x.grad.zero_()
    b_x.grad.zero_()
    loss_hist_xor1.append(loss.item())

print(f"Loss в начале: {loss_hist_xor1[0]:.4f}   Loss в конце: {loss_hist_xor1[-1]:.4f}   (ln 2 = {torch.log(torch.tensor(2.0)).item():.4f})")
print("Предсказания:", neuron_forward(X_xor, w_x, b_x).detach().numpy().round(3), " (нужно: [0,1,1,0])")

plt.figure(figsize=(6.5, 3.8))
plt.plot(loss_hist_xor1, color="tab:red")
plt.axhline(y=0.6931, color="gray", linestyle="--", linewidth=1, label="ln 2 ≈ 0.693")
plt.xlabel("Эпоха")
plt.ylabel("Loss")
plt.title("XOR, один нейрон: сходится ровно к ln 2 — и ни на йоту ниже")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

### Cell 24: markdown

Результат ещё более выразительный, чем «застряло где-то повыше нуля»: модель сходится **ровно** к $\ln 2 \approx 0{,}693$, а все предсказания — ровно к 0.5. Она не пытается угадать хотя бы 3 точки из 4 — она сдаётся полностью и одинаково неуверенно отвечает на все четыре примера.

Это не случайность и не неудачная инициализация — это математически доказуемый факт именно для XOR. У любой линейной модели логит $z=w_1x_1+w_2x_2+b$ устроен так, что сумма $z$ по точкам с меткой 1 всегда равна сумме $z$ по точкам с меткой 0 — какие бы $w$ и $b$ мы ни взяли (проверьте сами: $z(0,1)+z(1,0) = z(0,0)+z(1,1) = w_1+w_2+2b$). А раз так, для симметричной по логитам задачи и выпуклой функции потерь лучшая стратегия — не наклонять границу вообще: любой «наклон», который помогает одной паре точек, ровно настолько же вредит противоположной. Один линейный нейрон в буквальном смысле математически не может сделать на XOR ничего лучше, чем развести руками.

---

## Часть 8. XOR: скрытый слой из двух нейронов — получается

Добавим ровно то, о чём говорили на лекции: скрытый слой из двух нейронов. Каждый из них проведёт свою прямую (как `h₁` и `h₂` на слайде «Два перцептрона — две линии»), а выходной нейрон скомбинирует результаты.

### Cell 25: code

torch.manual_seed(0)

# входы(2) -> скрытый слой(2) -> выход(1), всё вручную матрицами
W1 = torch.randn(2, 2, requires_grad=True)
b1 = torch.zeros(2, requires_grad=True)
W2 = torch.randn(2, 1, requires_grad=True)
b2 = torch.zeros(1, requires_grad=True)
params = [W1, b1, W2, b2]


def mlp_forward(X):
    h = torch.sigmoid(X @ W1 + b1)   # скрытый слой: 2 нейрона, каждый - своя прямая
    out = torch.sigmoid(h @ W2 + b2)  # выходной нейрон комбинирует их
    return out.squeeze(-1)


lr = 1.0
epochs = 2000
loss_hist_xor2 = []

for epoch in range(epochs):
    pred = mlp_forward(X_xor)
    loss = F.binary_cross_entropy(pred, y_xor)
    loss.backward()
    with torch.no_grad():
        for p in params:
            p -= lr * p.grad
            p.grad.zero_()
    loss_hist_xor2.append(loss.item())
    if epoch % 400 == 0 or epoch == epochs - 1:
        print(f"Эпоха {epoch+1:4d}: loss = {loss.item():.4f}")

print("\nПредсказания:", mlp_forward(X_xor).detach().numpy().round(3), " (нужно: [0,1,1,0])")

### Cell 26: code

plt.figure(figsize=(6.5, 3.8))
plt.plot(loss_hist_xor1, color="tab:red", label=f"1 нейрон ({len(loss_hist_xor1)} эпох, застрял на ln2)")
plt.plot(loss_hist_xor2, color="tab:green", label=f"скрытый слой ({len(loss_hist_xor2)} эпох, дошёл до нуля)")
plt.xlabel("Эпоха")
plt.ylabel("Loss")
plt.title("С скрытым слоем loss реально доходит до нуля")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

plot_boundary(mlp_forward, X_xor, y_xor, "XOR решён: нелинейная граница из двух скрытых нейронов",
              label0="класс 0", label1="класс 1", xlabel="x\u2081", ylabel="x\u2082", cbar_label="ŷ")

### Cell 27: markdown

> 🎓 **Обсуждение:** если обучение не сошлось с первого раза — не страшно, это нормально для маленькой сети со случайной инициализацией (та самая чувствительность к начальным весам, о которой ещё пойдёт речь в курсе). Просто перезапустите ячейку с `torch.manual_seed(...)` с другим числом или увеличьте `epochs`.

---

## Итоги семинара

Сегодня мы:
- на игрушечном примере увидели, как PyTorch сам считает производные (`autograd`) — и сверили с формулой руками;
- написали цикл градиентного спуска полностью сами — `backward()` + ручное обновление весов — и увидели, как точка буквально скатывается по параболе к минимуму;
- обучили гладкий нейрон (сигмоида + BCE) на векторах признаков «кошка/собака» — тем же циклом, что и на параболе;
- воспроизвели центральный вывод лекции: один нейрон не решает XOR, а нейрон со скрытым слоем — решает, и увидели обе кривые loss рядом.

**Что дальше:** на лекции 2 — backpropagation разберём формально (что именно происходит внутри `.backward()`), и перейдём на «настоящий» PyTorch — `nn.Module`, `torch.optim`, `DataLoader` — вместо ручных циклов, которые мы писали сегодня.

### Задания на подумать (необязательно, для закрепления дома)
1. Замените `binary_cross_entropy` на `torch.mean((pred - y)**2)` (обычную MSE) — обучение всё ещё работает? Чем отличаются кривые loss?
2. Увеличьте скрытый слой до 4 нейронов вместо 2 — сходится ли обучение быстрее и стабильнее?
3. Постройте `loss.backward()` для функции $L(w_1, w_2) = (w_1-1)^2 + (w_2-2)^2$ и сравните `w1.grad, w2.grad` с аналитическими производными — это ровно та же идея, что на лекционном слайде «Градиент — это вектор».

## lecture_02/pytorch_homework.ipynb

### Cell 1: markdown

# Домашнее задание по PyTorch
Тема: Работа с тензорами и создание полносвязной нейронной сети.
Инструкция: Выполните все задания с пометкой TODO. Замените None на правильный код.

### Cell 2: code

import torch
import torch.nn as nn

### Cell 3: markdown

## Часть 1. Работа с тензорами
Тензоры являются основной структурой данных в PyTorch.

### Cell 4: code

# TODO 1. Создайте тензор a из списка [1, 2, 3]
a = None

# TODO 2. Создайте тензор b размером 2x2, заполненный нулями
b = None

# TODO 3. Создайте тензор c размером 3x3 со случайными числами (используйте torch.randn)
c = None

print("Тензор a:", a)
print("Тензор b:\n", b)
print("Тензор c:\n", c)

### Cell 5: markdown

### Операции с тензорами и изменение формы

### Cell 6: code

# TODO 4. Вычислите поэлементное произведение тензора c на скаляр 2.0
c_scaled = None

# TODO 5. Измените форму тензора c (3x3) на одномерный тензор (9,)
c_flat = None

# TODO 6. Создайте тензор d размером 1x3 и разверните его до 3x1 (используйте .view или .reshape)
d = torch.tensor([[4, 5, 6]])
d_reshaped = None

print("c_scaled:\n", c_scaled)
print("c_flat:", c_flat)
print("d_reshaped:\n", d_reshaped)

### Cell 7: markdown

## Часть 2. Полносвязная нейронная сеть
В этой части мы создадим простую нейронную сеть для классификации.

### Cell 8: code

# TODO 7. Создайте класс SimpleNN, наследуясь от nn.Module.
# Сеть должна иметь два линейных слоя:
# 1. input_size -> hidden_size
# 2. hidden_size -> output_size
# Между ними используйте функцию активации ReLU.

class SimpleNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        # Ваш код здесь
        pass

    def forward(self, x):
        # Ваш код здесь
        pass

### Cell 9: code

# TODO 8. Инициализируйте модель с параметрами: input_size=10, hidden_size=20, output_size=2
model = None

# TODO 9. Задайте функцию потерь CrossEntropyLoss
criterion = None

print(model)

### Cell 10: markdown

### Прямой проход и вычисление потерь
Сгенерируем синтетические данные и проведём прямой проход через сеть.

### Cell 11: code

# Синтетические данные
X = torch.randn(100, 10)  # 100 объектов, 10 признаков
y = torch.randint(0, 2, (100,))  # 100 меток классов (0 или 1)

# TODO 10. Проведите прямой проход через модель и вычислите потери.
# 1. Получите выходы модели, передав X
# 2. Вычислите потери между выходами и метками y

outputs = None
loss = None

print("Размер выходов:", outputs.shape)
print("Потери:", loss.item())

## lecture_02/seminar2.ipynb

### Cell 1: markdown

### Разминка - вспомним как алгоритм градиентного спуска
Напишите программу (без использования PyTorch) поиска точки минимума функции:

f(x) = 0.5 * x + 0.2 * x** 2 - 0.1 * x**3

c помощью градиентного алгоритма со следующими начальными значениям:
eta = 0.01
x0 = -4
N = 200 - число итерации градиентного алгоритма

### Cell 2: code

def func(x):
    return 0.5 * x + 0.2 * x ** 2 - 0.1 * x ** 3


def df(x):
    return # здесь выражение производной функции f(x)


# здесь продолжайте программу

### Cell 3: markdown

Дана функция f(x) = 0.1 * x**2 - sin(x) + 5
Необходимо выполнить ее аппросксимацию (восстановление) на интервале [-5; 5]
Моделью нейронной сети вида:
![ris_11_1.png]([embedded image])

### Cell 4: markdown

Математически ее работу можно записать следующим образом:
y = a(x) = w0 + w1 * x + w2 * x**2 + w3 * x**3
Вектор ппараметров [w0, w1, w2, w3] следует искать с помощью градиеньного алгоритма, где функционал качества Q представляет собой среднеквадратичную функцию: ![image.png]([embedded image])

Его частную производную по вектору параметров w можно записать в векторно-матричном виде следующим образом:
![image.png]([embedded image])
где s = [1, x, x**2, x**3] - вектор признако i-го образа обучающей выборки

Продолжите программу, в которой объявлена функция f(x) с именем func, заданы значения функции по оси абсцисс и ординат, а также начальные значения и параметры для алгоритма градиентного спуска.

Вычисленные параметры вектора w следует сохранить в виде тензора с именем w. Также нужно вычислить значение среднего эмпирического риска для обученной модели по формуле:
![image.png]([embedded image])

### Cell 5: code

import torch

# исходная функция, которую нужно аппроксимировать моделью a(x)
def func(x):
    return 0.1 * x**2 - torch.sin(x) + 5.


# здесь объявляйте необходимые функции


coord_x = torch.arange(-5.0, 5.0, 0.1) # значения по оси абсцисс [-5; 5] с шагом 0.1
coord_y = func(coord_x) # значения функции по оси ординат

sz = coord_x.size(0)	# количество значений функций (точек)
eta = torch.tensor([0.1, 0.01, 0.001, 0.0001]) # шаг обучения для каждого параметра w0, w1, w2, w3
w = torch.zeros(4, dtype=torch.float32) # начальные значения параметров модели
N = 200 # число итераций градиентного алгоритма

# здесь продолжайте программу

### Cell 6: markdown

**Закрепим материал по автоматическому дифференцированию:**

Расстояние, пройденное телом за время t описывается выражением:
![image.png]([embedded image])

Мгновенную скорость этого тела в момент времени t=d можно найти, как производную пути по времени:
![image.png]([embedded image])

В программе ниже выполняется чтение момента времени d, при котором необходимо вычислить скорость тела:

d = float(input())

Сформируйте тензор t со значением d и с помощью автоматического дифференцирования фреймворка PyTorch найдите мгновенную скорость тела в момент t=d. Результат вычисления производной ds(t)/dt следует хранить в тензоре t.

### Cell 7: code

import torch

tests = [4.5, -2.3, 0.1, 40.0]

for d in tests:
    t =

### Cell 8: code

Следующее задание:

### Cell 9: markdown

В программе дана следующая функция:

![image.png]([embedded image])

которую предполагается аппроксимировать (восстанавливать) с помощью следующей модели нейронной сети:

![image.png]([embedded image])

Математические ее работу можно описать следующим выражением:

![image.png]([embedded image])

Критерием качества будет выступать квадратичная функция потерь вида:

![image.png]([embedded image])

Найдите значения производных ∂L/∂w0, ∂L/∂w1, ∂L/∂w2, ∂L/∂w3 в точке:

xx = float(input())
x = torch.tensor(xx, dtype=torch.float32)

### Cell 10: code

import torch

tests = [
    (2.5,  (0.12, 0.5, -2.3, 0.1)),
    (-0.5, (5.12, -1.5, 1.3, -0.5)),
    (3.0,  (-4.3, 0.1, 0.2, -0.01)),
]

for xx, (x0, x1, x2, x3) in tests:
    x = torch.tensor(xx, dtype=torch.float32)

    w0 = torch.tensor(x0, dtype=torch.float32, requires_grad=True)
    w1 = torch.tensor(x1, dtype=torch.float32, requires_grad=True)
    w2 = torch.tensor(x2, dtype=torch.float32, requires_grad=True)
    w3 = torch.tensor(x3, dtype=torch.float32, requires_grad=True)

    # здесь решение

### Cell 11: markdown

**Обучение полносвязной нейронной сети на MNIST**

**Dataset и transforms**

### Cell 12: code

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

### Cell 13: markdown

`device` - где лежат тензоры и где считаются операции: видеокарта (`cuda`) или процессор (`cpu`). Строка выбирает видеокарту, если она доступна, иначе процессор. Дальше и модель, и данные нужно переносить на один и тот же `device` - иначе PyTorch выдаст ошибку несовпадения устройств.

## Данные

`datasets.MNIST` - готовый `Dataset` из `torchvision`: объект, у которого можно спросить длину (`len(dataset)`) и взять пример по индексу (`dataset[i]`), в ответ он отдает пару (картинка, метка). `transform=transforms.ToTensor()` переводит картинку из обычного изображения в тензор формы `(1, 28, 28)` со значениями от 0 до 1 - без этого преобразования датасет отдавал бы не тензор, а объект-картинку, с которым PyTorch не умеет работать напрямую.

### Cell 14: code

transform = transforms.ToTensor()

train_dataset = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root="./data", train=False, download=True, transform=transform)

print(len(train_dataset), len(test_dataset))

image, label = train_dataset[0]
print(image.shape, label)

### Cell 15: markdown

`train=True` / `train=False` - MNIST заранее разбит на две части: обучающую и тестовую. Модель обучается только на первой и ни разу не видит вторую до самой проверки.

`Dataset` отдает примеры по одному. Чтобы собирать их в пачки и перемешивать порядок каждую эпоху, используется `DataLoader`.

### Cell 16: code

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

images, labels = next(iter(train_loader))
print(images.shape, labels.shape)

### Cell 17: markdown

`batch_size` - сколько примеров в одной пачке. `shuffle=True` перемешивает порядок каждую эпоху - нужно для обучающей выборки, бессмысленно для тестовой, поэтому там `shuffle=False`. Форма пачки `(64, 1, 28, 28)` — спереди добавилось измерение пачки.

## Слои сети - по одному

Модель в PyTorch - класс, унаследованный от `nn.Module`, с двумя методами: `__init__`, где перечисляются слои, и `forward`, где описано, в каком порядке через них проходят данные. Когда пишут `model(x)`, PyTorch сам вызывает `model.forward(x)`.

Разберем по отдельности три слоя, из которых можно собрать простую сеть. Пример ниже - игрушечный, не для MNIST, просто чтобы увидеть синтаксис класса в действии.

### Cell 18: code

class ExampleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(10, 3)  # 10 входных чисел -> 3 выходных

    def forward(self, x):
        return self.layer(x)


example_net = ExampleNet()
dummy_input = torch.rand(4, 10)  # пачка из 4 примеров по 10 чисел
print(example_net(dummy_input).shape)

### Cell 19: markdown

`super().__init__()` - обязательная первая строка `__init__`: она настраивает внутренний учет параметров у `nn.Module`, без нее слои не зарегистрируются как обучаемые и оптимизатор их не увидит.

`nn.Linear(in_features, out_features)` - полносвязный слой: линейное преобразование `x @ W + b`, где `W` и `b` создаются автоматически при создании слоя и являются обучаемыми параметрами. На входе ждет тензор формы `(батч, in_features)`, на выходе отдает `(батч, out_features)` — в примере выше `(4, 10)` превратилось в `(4, 3)`.

MNIST-картинка после `ToTensor()` имеет форму `(1, 28, 28)` - это не плоский вектор, а `nn.Linear` умеет работать только с плоскими векторами. Превращает одно в другое `nn.Flatten()`.

### Cell 20: code

flatten = nn.Flatten()
dummy_images = torch.rand(4, 1, 28, 28)  # как будто пачка из 4 картинок MNIST
print(flatten(dummy_images).shape)

### Cell 21: markdown

`(4, 1, 28, 28)` превратилось в `(4, 784)` — все измерения, кроме первого (пачки), схлопнулись в одно. `28 * 28 = 784`.

Последний блок - нелинейность между слоями. Без нее несколько `nn.Linear` подряд математически эквивалентны одному линейному слою, сколько бы их ни было.

### Cell 22: code

relu = nn.ReLU()
print(relu(torch.tensor([-2.0, -0.5, 0.0, 1.5, 3.0])))

### Cell 23: markdown

`nn.ReLU()` - поэлементно `max(0, x)`: отрицательные значения обнуляются, остальные проходят без изменений.

Три этих блока - `nn.Flatten`, `nn.Linear`, `nn.ReLU` - и есть весь набор, нужный для того, чтобы собрать сеть под MNIST. Как именно их комбинировать (сколько слоев, какой ширины) - решать в задании ниже.

## Функция потерь и оптимизатор

`nn.CrossEntropyLoss()` - функция потерь для классификации на несколько классов. Ждет на входе сырые логиты (то, что отдает последний `nn.Linear`, без какой-либо активации после него) и целые числа-метки классов, а softmax считает сама, внутри себя. Если применить softmax к выходу модели самостоятельно и передать результат в `CrossEntropyLoss`, softmax применится дважды и обучение будет некорректным - поэтому последний слой сети всегда оставляют без активации.

### Cell 24: code

loss_fn = nn.CrossEntropyLoss()

dummy_logits = torch.randn(4, 3)         # как будто выход ExampleNet на 4 примерах, 3 класса
dummy_labels = torch.tensor([0, 2, 1, 0])  # правильные классы для них

print(loss_fn(dummy_logits, dummy_labels))

### Cell 25: markdown

## Что делает backward и как обновлять веса вручную

После `loss.backward()` у каждого параметра модели (все, что отдает `model.parameters()`) появляется заполненное поле `.grad` — градиент loss по этому параметру. Сам `backward()` веса не меняет, он только считает, в какую сторону и насколько сильно каждый вес влияет на ошибку. Дальше нужно сделать шаг градиентного спуска самим: каждый параметр сдвинуть против своего градиента на небольшую величину.

Покажем на `example_net`.

### Cell 26: code

output = example_net(dummy_input)
target = torch.tensor([0, 2, 1, 0])  # произвольные "правильные" классы, для примера

loss = loss_fn(output, target)
loss.backward()

print(example_net.layer.weight.grad.shape)

### Cell 27: markdown

`example_net.layer.weight.grad` - градиент loss по весам слоя `layer`, той же формы, что и сами веса. Теперь шаг обновления:

### Cell 28: code

lr = 0.01

with torch.no_grad():
    for param in example_net.parameters():
        param -= lr * param.grad
        param.grad.zero_()

### Cell 29: markdown

`torch.no_grad()` — сам шаг обновления не должен попадать в граф вычислений (иначе PyTorch попытается продифференцировать и это изменение весов, что не нужно). `param -= lr * param.grad` — сдвиг параметра против градиента, `lr` задает величину шага: слишком большой — модель будет "перепрыгивать" через нужные значения весов, слишком маленький — обучение будет идти очень медленно. `param.grad.zero_()` обнуляет градиент после того, как он использован — PyTorch по умолчанию не обнуляет градиенты сам, а прибавляет новые к уже накопленным, поэтому без обнуления на следующем шаге градиенты просто сложатся со старыми.

## Цикл обучения и проверки

Функции ниже не привязаны к конкретной архитектуре — они принимают модель как аргумент и одинаково работают с любой сетью, собранной из `nn.Module`. Их можно оставить как есть и переиспользовать для своей модели в задании.

### Cell 30: code

def train_one_epoch(model, loader, loss_fn, lr, device):
    model.train()
    running_loss = 0.0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        #  нужно найти функцию потерь (назовите ее loss) и подсчитать обратное распространение

        with torch.no_grad():
            for param in model.parameters():
                # написать шаг обучения

        running_loss += loss.item()
    return running_loss / len(loader)

### Cell 31: markdown

По шагам внутри цикла:

- `model.train()` - переключает модель в режим обучения.
- `images, labels = images.to(device), labels.to(device)` - переносит пачку на то же устройство, где лежит модель.
- `outputs = model(images)` - прямой проход через сеть.
- `loss = loss_fn(outputs, labels)` - насколько предсказания разошлись с правильными метками.
- `loss.backward()` - считает градиент loss по всем обучаемым параметрам модели.
- дальше - тот же самый ручной шаг обновления, что и в примере с `example_net` выше, только сразу для всех параметров модели циклом.

### Cell 32: code

def evaluate(model, loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            preds = outputs.argmax(dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    return correct / total

### Cell 33: markdown

`model.eval()` - режим использования модели, противоположность `model.train()`. `torch.no_grad()` отключает подсчет градиентов внутри блока — на проверке они не нужны. `outputs.argmax(dim=1)` берет индекс наибольшего логита по каждому примеру - это и есть предсказанный класс. `(preds == labels).sum().item()` считает число верных предсказаний в пачке.

---

## Задание

Используя три блока выше (`nn.Flatten`, `nn.Linear`, `nn.ReLU`) и функции `train_one_epoch`, `evaluate`, соберите свою сеть и обучите ее распознавать цифры MNIST.  Архитектуру, число слоев и их ширину нужно придумать и написать самим.

Работайте по группам. Правила, чтобы результаты были сравнимы:

- модель обучается с нуля, без предобученных весов;
- тестовая часть (`test_dataset`, `test_loader`) не используется во время обучения ни в каком виде, только для финальной проверки;
- итоговый результат - это `evaluate(model, test_loader, device)`, ровно той же функцией, что определена выше.

Что можно менять и пробовать: сколько слоев `nn.Linear` использовать и какой ширины, другую активацию вместо `nn.ReLU` (например `nn.LeakyReLU`), оптимизатор и `lr` (`torch.optim.SGD` вместо `Adam`, другие значения скорости обучения), число эпох, размер батча. Можно добавить `nn.Dropout(p)` между линейными слоями - во время обучения он случайно обнуляет долю `p` нейронов на каждом шаге, из-за чего сети сложнее подстроиться под конкретные примеры из обучающей выборки.

### Cell 34: code

class MyClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        # опишите свои слои здесь

    def forward(self, x):
        # опишите свой прямой проход здесь
        return x

### Cell 35: code

my_model = MyClassifier().to(device)
my_loss_fn = nn.CrossEntropyLoss()
my_lr =   # подберите сами

my_epochs =   # подберите сами

for epoch in range(my_epochs):
    train_loss = train_one_epoch(my_model, train_loader, my_loss_fn, my_lr, device)
    test_acc = evaluate(my_model, test_loader, device)
    print(f"Эпоха {epoch + 1}/{my_epochs}: loss = {train_loss:.4f}, точность на тесте = {test_acc:.4f}")

### Cell 36: code

# итоговый результат группы - его и сравниваем между группами
final_accuracy = evaluate(my_model, test_loader, device)
print(f"Итоговая точность на тесте: {final_accuracy:.4f}")

## lecture_05/seminar_tokens_embeddingsss.ipynb

### Cell 1: markdown

# Семинар: токенизация и эмбеддинги

Сегодня руками проверим всё, о чём говорили на лекции, и почти всё увидим на картинках.

| Часть | Что делаем | Время |
|---|---|---|
| 0 | Разминка: игра Contexto | 10 мин |
| 1 | BPE своими руками и настоящие токенизаторы | 25 мин |
| 2 | Векторы слов из подсчётов в «маленьком мире» | 15 мин |
| 3 | Настоящие векторы для русского (Navec) | 10 мин |
| 4 | Порядок слов: где ломается мешок слов | 20 мин |

**Как работать.** Запускайте ячейки сверху вниз. Ячейки с пометкой **[нужен интернет]** скачивают библиотеки или модели — в Colab они работают сразу. Всё остальное работает и без интернета.

Блоки **Задание** — для вас: меняйте код, запускайте снова, смотрите, что изменилось.

### Cell 2: code

# Служебные функции для рисунков. Читать не обязательно — просто запустите ячейку.
import re
import random
from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from sklearn.manifold import TSNE

INK, MUTED, PAPER, GRID, ACCENT = "#1B2430", "#646B78", "#F7F5F0", "#DDD6C8", "#B34A1C"
COLORS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#6250d6", "#e87ba4", "#008300", "#e34948"]
plt.rcParams.update({
    "figure.facecolor": PAPER, "axes.facecolor": PAPER, "savefig.facecolor": PAPER,
    "axes.edgecolor": GRID, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False,
    "axes.titlelocation": "left", "axes.titlesize": 14, "font.size": 12, "figure.dpi": 110,
})


def draw_tokens(rows, title=None, color_of=None, fontsize=14):
    """Рисует токены цветными плашками. rows — список пар (подпись, список токенов).
    Токен " " означает пробел между словами. color_of(token) может задать цвет токена."""
    fig, ax = plt.subplots(figsize=(13, 0.7 * len(rows) + 0.6))
    for attempt in range(4):                       # если строка не влезла, уменьшаем шрифт и рисуем заново
        ax.cla()
        ax.set_xlim(0, 100)
        ax.set_ylim(-3 * len(rows), 0)
        ax.axis("off")
        renderer, to_data = fig.canvas.get_renderer(), ax.transData.inverted()
        right = 0
        for r, (label, tokens) in enumerate(rows):
            y, x, k = -3 * r - 1.5, 21, 0
            ax.text(0, y, label, va="center", fontsize=11, color=MUTED)
            for t in tokens:
                if t == " ":
                    x += 1.5
                    continue
                text = ax.text(x + 0.4, y, t, va="center", fontsize=fontsize, family="monospace", zorder=3)
                box = text.get_window_extent(renderer)
                (x0, _), (x1, _) = to_data.transform([[box.x0, box.y0], [box.x1, box.y1]])
                w = x1 - x0 + 0.8
                color = color_of(t) if color_of else COLORS[k % 5]
                k += 1
                ax.add_patch(FancyBboxPatch((x, y - 1.1), w, 2.2, boxstyle="round,pad=0,rounding_size=0.4",
                                            zorder=2, facecolor=(color + "30") if color else "#E8E2D6",
                                            edgecolor=color or "#C9C0AE", linewidth=1.3))
                x += w + 0.25
            right = max(right, x)
        if right <= 100:
            break
        fontsize *= 0.95 * (100 - 21) / (right - 21)
    if title:
        ax.set_title(title)
    plt.show()


def heatmap(ax, M, rows, cols, title, fmt="{:.0f}"):
    ax.imshow(M, cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(cols)), cols, rotation=45, ha="right")
    ax.set_yticks(range(len(rows)), rows)
    for i in range(len(rows)):
        for j in range(len(cols)):
            ax.text(j, i, fmt.format(M[i, j]), ha="center", va="center", fontsize=9,
                    color="white" if M[i, j] > 0.6 * M.max() else INK)
    ax.set_title(title)
    ax.grid(False)


def cosine(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


def nearest(query, vectors, n=5, exclude=()):
    """Ближайшие слова по косинусу. query — слово или вектор, vectors — словарь {слово: вектор}."""
    if isinstance(query, str):
        exclude = set(exclude) | {query}
        query = vectors[query]
    sims = [(w, cosine(query, v)) for w, v in vectors.items() if w not in exclude]
    return sorted(sims, key=lambda p: -p[1])[:n]


def neighbors_table(words, vectors, n=5):
    rows = {w: ", ".join(f"{u} ({s:.2f})" for u, s in nearest(w, vectors, n)) for w in words if w in vectors}
    return pd.DataFrame.from_dict(rows, orient="index", columns=["ближайшие слова (косинус)"])


def analogy(a, b, c, vectors, exclude=True, n=3):
    """a − b + c: например, «москва − россия + франция»."""
    missing = [w for w in (a, b, c) if w not in vectors]
    if missing:
        return f"нет в словаре: {missing}"
    v = vectors[a] - vectors[b] + vectors[c]
    return nearest(v, vectors, n, exclude={a, b, c} if exclude else ())


def word_map(vectors, groups, title, highlight=()):
    """Карта слов на плоскости (t-SNE). groups — {название группы: [слова]}."""
    words = [w for ws in groups.values() for w in ws if w in vectors] + [w for w in highlight if w in vectors]
    X = np.array([vectors[w] for w in words])
    X = X / np.linalg.norm(X, axis=1, keepdims=True)
    xy = TSNE(n_components=2, perplexity=min(10, len(words) - 1), init="pca", metric="cosine",
              random_state=0).fit_transform(X)
    pos = dict(zip(words, xy))
    fig, ax = plt.subplots(figsize=(12, 7))
    for (name, ws), color in zip(groups.items(), COLORS):
        ws = [w for w in ws if w in pos]
        pts = np.array([pos[w] for w in ws])
        ax.scatter(pts[:, 0], pts[:, 1], s=80, color=color, edgecolor=PAPER, linewidth=1.5, label=name, zorder=3)
        for w in ws:
            ax.annotate(w, pos[w], xytext=(5, 4), textcoords="offset points", fontsize=11)
    for w in highlight:
        if w in pos:
            ax.scatter(*pos[w], s=220, facecolor="none", edgecolor=ACCENT, linewidth=2.5, zorder=4)
            ax.scatter(*pos[w], s=80, color=ACCENT, zorder=5)
            ax.annotate(w, pos[w], xytext=(8, -14), textcoords="offset points", fontsize=13,
                        color=ACCENT, fontweight="bold")
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)
    ax.set_title(title)
    ax.axis("off")
    plt.show()


print("Готово: можно идти дальше")

### Cell 3: markdown

## 1. Токенизация своими руками

### 1.1 BPE за 30 строк

Алгоритм с лекции: разбиваем слова на буквы, находим самую частую пару соседей, склеиваем её в новый токен, повторяем. Результат обучения — упорядоченный список слияний.

### Cell 4: code

def merge(word, pair):
    """Склеивает в слове (кортеже токенов) все вхождения пары."""
    out, i = [], 0
    while i < len(word):
        if word[i:i + 2] == pair:
            out.append(pair[0] + pair[1])
            i += 2
        else:
            out.append(word[i])
            i += 1
    return tuple(out)


def train_bpe(freqs, n_merges):
    """freqs — {слово: частота}. Возвращает список слияний и состояние корпуса после каждого шага."""
    vocab = {tuple(w): f for w, f in freqs.items()}
    merges, history = [], [("буквы", dict(vocab))]
    for _ in range(n_merges):
        pairs = Counter()
        for word, f in vocab.items():
            for p in zip(word, word[1:]):
                pairs[p] += f
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        merges.append(best)
        vocab = {merge(w, best): f for w, f in vocab.items()}
        history.append((f"{best[0]} + {best[1]} ({pairs[best]})", dict(vocab)))
    return merges, history


def encode(word, merges):
    """Режет новое слово выученными слияниями — строго в порядке обучения."""
    tokens = tuple(word)
    for pair in merges:
        tokens = merge(tokens, pair)
    return list(tokens)

### Cell 5: code

board = {"кт": 5, "коты": 3, "котик": 2, "рот": 4, "роты": 2}
merges, history = train_bpe(board, 4)

new_tokens = ["".join(p) for p in merges]
color_of = lambda t: COLORS[new_tokens.index(t)] if t in new_tokens else None   # буквы — серые

rows = []
for step, (label, vocab) in enumerate(history):
    tokens = []
    for word in vocab:
        tokens += list(word) + [" "]
    rows.append((f"шаг {step}: {label}", tokens))
rows.append(("новые слова", sum([encode(w, merges) + [" "] for w in ["котов", "ротик", "торт"]], [])))
draw_tokens(rows, "BPE на доске: корпус после каждого слияния", color_of=color_of)

### Cell 6: markdown

**Задание.** Добавьте в корпус `board` слово «торт» с частотой 3 и запустите ячейку снова. Как изменились слияния? Почему?

### Cell 7: markdown

### 1.2 BPE на настоящем тексте

Возьмём небольшую сказку про кота, который придумал токенизацию, и обучим на ней BPE.

### Cell 8: code

TEXT = """
Кот Тимофей жил в старом доме у реки. Каждое утро кот выходил во двор и долго смотрел на воду.
Соседские коты завидовали Тимофею: у него был тёплый подоконник, миска с молоком и хозяйка,
которая читала ему вслух. Хозяйка читала много: книги о далёких странах, книги о звёздах,
книги о котах и собаках. Кот слушал внимательно и иногда засыпал, не дослушав главу до конца.
Однажды хозяйка принесла домой новую книгу. Книга была толстая, с картинками и длинными словами.
«Токенизация», — прочитала хозяйка и рассмеялась. Кот не знал, что значит это слово, но слово ему
понравилось. Он попробовал разделить его на кусочки: «то», «кен», «изация». Кусочки получились
странные, но знакомые. Ведь кот уже слышал слова «организация» и «цивилизация», а значит, мог
догадаться, что новое слово тоже обозначает какой-то процесс.
С тех пор кот Тимофей стал разбирать на кусочки все незнакомые слова. Длинные слова он делил
на короткие части, короткие слова запоминал целиком. Частые кусочки он узнавал сразу, редкие
кусочки разглядывал подольше. Соседские коты смеялись над ним, но Тимофей не обижался.
Он понимал: чтобы читать быстро, не нужно знать все слова на свете. Достаточно знать хорошие
кусочки слов и уметь их складывать.
Вечером хозяйка снова читала вслух. Кот слушал, узнавал знакомые кусочки и радовался. Слова больше
не казались ему страшными. Даже самые длинные слова, вроде «достопримечательность» или
«электрификация», складывались из знакомых частей, как дом складывается из кирпичей. А если кусочек
попадался совсем незнакомый, кот просто запоминал его буквы и шёл дальше.
Так кот Тимофей, сам того не зная, придумал алгоритм, который сегодня работает внутри больших
языковых моделей. Модели тоже читают тексты кусочками, тоже узнают частые части слов и тоже
собирают из них новые слова. Только читают они не одну книгу, а миллионы книг, и кусочков у них
не сто, а десятки тысяч.
"""

words = re.findall(r"\w+", TEXT.lower())
freqs = Counter(words)
print(f"Слов в тексте: {len(words)}, разных слов: {len(freqs)}")
print("Самые частые:", freqs.most_common(8))

### Cell 9: code

merges, _ = train_bpe(freqs, 300)
print("Первые 30 выученных токенов:")
print(", ".join("".join(p) for p in merges[:30]))

### Cell 10: markdown

**Вопрос.** Какие токены появились первыми — корни, окончания или служебные слова? Почему именно они?

Теперь посмотрим, как длина токенов зависит от числа слияний. Метрика **fertility** — сколько токенов в среднем приходится на одно слово.

### Cell 11: code

steps = [0, 10, 25, 50, 100, 200, 300]
fertility = [np.mean([len(encode(w, merges[:n])) for w in words]) for n in steps]

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(steps, fertility, marker="o", color=COLORS[0], linewidth=2)
for n, f in zip(steps, fertility):
    ax.annotate(f"{f:.1f}", (n, f), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=10)
ax.set_xlabel("число слияний (размер словаря − алфавит)")
ax.set_ylabel("токенов на слово")
ax.set_title("Больше слияний — длиннее токены и короче последовательности")
ax.margins(y=0.15)
ax.grid(color=GRID)
plt.show()

### Cell 12: code

sentence = "Хозяйка читала коту книгу о токенизации"
rows = []
for n in [10, 50, 300]:
    tokens = []
    for w in sentence.lower().split():
        tokens += encode(w, merges[:n]) + [" "]
    rows.append((f"{n} слияний", tokens))
draw_tokens(rows, "Одно предложение при разном размере словаря")

### Cell 13: markdown

**Задание.** Придумайте предложение, в котором много слов, которых нет в сказке. Как оно режется? Какое слово распалось на больше всего кусков?

### Cell 14: markdown

### 1.3 Настоящие токенизаторы [нужен интернет]

Библиотека `tiktoken` содержит токенизаторы моделей OpenAI. Сравним старый (GPT-2) и новый (GPT-4o) на одной фразе по-русски и по-английски.

### Cell 15: code

!pip install -q tiktoken

### Cell 16: code

import tiktoken

phrases = {
    "EN": "The cat is sleeping on the warm windowsill",
    "RU": "Кошка спит на тёплом подоконнике",
}
encoders = {name: tiktoken.get_encoding(name) for name in ["gpt2", "cl100k_base", "o200k_base"]}

counts = pd.DataFrame({name: {lang: len(enc.encode(p)) for lang, p in phrases.items()}
                       for name, enc in encoders.items()}).T
counts["RU / EN"] = (counts["RU"] / counts["EN"]).round(1)
counts

### Cell 17: code

def pieces(enc, text):
    """Токены как строки. Кусок кириллической буквы (половина байтов) покажется как «�»."""
    return [enc.decode_single_token_bytes(t).decode("utf-8", errors="replace").replace(" ", "▁")
            for t in enc.encode(text)]

draw_tokens([(f"{name}: {lang}", pieces(enc, text))
             for name, enc in [("gpt2", encoders["gpt2"]), ("o200k", encoders["o200k_base"])]
             for lang, text in phrases.items()],
            "Одна фраза — разное число токенов", fontsize=12)

### Cell 18: markdown

**Задание.** Найдите фразу, у которой «налог на русский» (отношение RU / EN) максимальный. Попробуйте длинные слова, имена, числа, эмодзи. Почему у GPT-2 появляются кусочки «�»?

### Cell 19: markdown

## 2. Векторы слов из подсчётов: «маленький мир»

Сгенерируем корпус из простых предложений, в которых мы сами знаем все правила: животные спят и мяукают, еду режут и покупают, рыцари носят оружие. Слово «лук» специально живёт в двух мирах: его режут для супа и из него стреляют.

Предложения уже лемматизированы — как в корпусах, на которых обучены модели RusVectōrēs.

### Cell 20: code

random.seed(0)
CAPITALS = {"москва": "россия", "париж": "франция", "берлин": "германия", "рим": "италия"}
LANGS = {"россия": "русский", "франция": "французский", "германия": "немецкий", "италия": "итальянский"}
SLOTS = {
    "животное": ["кот", "кошка", "собака", "пёс", "хомяк", "попугай"],
    "кошачьи": ["кот", "кошка"], "собачьи": ["собака", "пёс"],
    "еда": ["суп", "хлеб", "сыр", "картошка", "морковь", "лук"], "овощ": ["картошка", "морковь", "лук"],
    "напиток": ["чай", "кофе", "молоко", "сок"],
    "температура": ["горячий", "холодный", "тёплый", "ледяной"],
    "оружие": ["меч", "копьё", "щит", "арбалет", "лук"], "стрелковое": ["лук", "арбалет"],
}
TEMPLATES = [
    "{животное} спать на диван", "погладить {животное}", "{животное} играть с мячик",
    "кормить {животное} утром", "{кошачьи} мяукать", "{собачьи} лаять", "попугай летать по комната",
    "хомяк грызть морковь", "купить {еда} в магазин", "резать {овощ} нож", "{еда} очень вкусный",
    "есть {еда} на обед", "суп с {овощ}", "пить {напиток}", "чашка {напиток}", "{температура} {напиток}",
    "налить {напиток} в кружка", "{температура} суп", "на улица очень {температура}", "{температура} вода",
    "рыцарь носить {оружие}", "воин взять {оружие}", "стрелять из {стрелковое}", "{оружие} висеть на стена",
    "GEO", "GEO",
]
GEO = ["{c} столица {k}", "жить в {c}", "поехать в {k}", "в {k} говорить на {l}",
       "в {c} говорить на {l}", "{c} большой город", "{k} красивый страна"]


def make_sentence():
    template = random.choice(TEMPLATES)
    if template == "GEO":
        c = random.choice(list(CAPITALS))
        return random.choice(GEO).format(c=c, k=CAPITALS[c], l=LANGS[CAPITALS[c]]).split()
    return [random.choice(SLOTS[t[1:-1]]) if t.startswith("{") else t for t in template.split()]


corpus = [make_sentence() for _ in range(6000)]
for s in corpus[:8]:
    print(" ".join(s))

### Cell 21: markdown

### 2.1 Матрица совстречаемости и PPMI

Считаем, сколько раз каждое слово встретилось в одном предложении с каждым другим. Строка матрицы — это и есть вектор слова.

### Cell 22: code

vocab = sorted({w for s in corpus for w in s})
idx = {w: i for i, w in enumerate(vocab)}
N = np.zeros((len(vocab), len(vocab)))
for s in corpus:
    for a in s:
        for b in s:
            if a != b:
                N[idx[a], idx[b]] += 1


def ppmi(N, alpha=0.75):
    p_w = N.sum(1, keepdims=True) / N.sum()
    p_c = N.sum(0) ** alpha
    p_c = p_c / p_c.sum()
    with np.errstate(divide="ignore"):
        return np.maximum(np.log(N / N.sum() / (p_w * p_c)), 0)


M = ppmi(N)
rows = ["кот", "собака", "чай", "кофе", "лук", "москва"]
cols = ["в", "на", "очень", "мяукать", "лаять", "пить", "резать", "стрелять", "столица"]
fig, axes = plt.subplots(1, 2, figsize=(14, 4.5))
heatmap(axes[0], N[np.ix_([idx[w] for w in rows], [idx[c] for c in cols])], rows, cols, "Сырые счётчики")
heatmap(axes[1], M[np.ix_([idx[w] for w in rows], [idx[c] for c in cols])], rows, cols, "PPMI", fmt="{:.1f}")
plt.tight_layout()
plt.show()

### Cell 23: markdown

**Вопрос.** Что случилось со столбцами «в» и «на» после PPMI? А со столбцом «мяукать»? Почему у «лука» два ярких столбца?

### Cell 24: markdown

### 2.2 SVD и карта смыслов

Сжимаем матрицу PPMI до 20 чисел на слово с помощью SVD и рисуем слова на плоскости.

### Cell 25: code

U, S, _ = np.linalg.svd(M)
k = 20
E = U[:, :k] * np.sqrt(S[:k])
vectors = {w: E[idx[w]] for w in vocab}

groups = {
    "животные": SLOTS["животное"], "еда": ["суп", "хлеб", "сыр", "картошка", "морковь"],
    "напитки": SLOTS["напиток"], "температура": SLOTS["температура"],
    "оружие": ["меч", "копьё", "щит", "арбалет"], "столицы": list(CAPITALS), "страны": list(LANGS),
}
word_map(vectors, groups, "Маленький мир: векторы из подсчётов (PPMI + SVD, k = 20)", highlight=["лук"])

### Cell 26: code

neighbors_table(["кот", "лук", "горячий", "чай", "меч", "москва"], vectors)

### Cell 27: markdown

**Вопросы.** Где оказался «лук» и кто его соседи? Почему «горячий» ближе всего к «холодному»? Вспомните разминку.

### 2.3 Аналогии

Проверим знаменитую арифметику: «москва − россия + франция ≈ ?». Сравним честный поиск (с исключением слов запроса) и поиск без исключения.

### Cell 28: code

print("с исключением слов запроса:", analogy("москва", "россия", "франция", vectors))
print("без исключения:            ", analogy("москва", "россия", "франция", vectors, exclude=False))

### Cell 29: markdown

**Задание.**

1. Поменяйте `k = 20` на `k = 5` и запустите ячейки 2.2–2.3 снова. Что стало с аналогией и с картой? Почему?
2. Сделайте ещё одно многозначное слово. Например, добавьте в `TEMPLATES` шаблоны `"открыть дверь {ключ}"` и `"пить вода из {ключ}"` и слот `"ключ": ["ключ"]` (или придумайте своё). Где окажется новое слово на карте?

### Cell 30: markdown

## 3. Настоящие векторы для русского [нужен интернет]

Navec — компактные (около 50 МБ) векторы для русского от проекта Natasha, обученные на художественной литературе. Используем те же функции, что и для «маленького мира».

### Cell 31: code

!pip install -q navec
!wget -q -nc https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar

### Cell 32: code

from navec import Navec

navec = Navec.load("navec_hudlit_v1_12B_500K_300d_100q.tar")

real_groups = {
    "животные": ["кот", "кошка", "собака", "пёс", "хомяк", "попугай", "лошадь", "корова"],
    "еда": ["суп", "хлеб", "сыр", "картошка", "морковь", "капуста", "чеснок"],
    "оружие": ["меч", "копьё", "щит", "арбалет", "стрела", "сабля"],
    "температура": ["горячий", "холодный", "тёплый", "ледяной", "раскалённый", "прохладный"],
    "люди": ["король", "королева", "мужчина", "женщина", "принц", "принцесса", "царь", "царица"],
    "города": ["москва", "париж", "берлин", "рим", "лондон", "мадрид"],
    "страны": ["россия", "франция", "германия", "италия", "англия", "испания"],
}
words = [w for ws in real_groups.values() for w in ws] + ["лук", "замок", "ключ", "коса"]
real = {w: navec[w] for w in words if w in navec}
print(f"Нашлось {len(real)} слов из {len(words)}")

### Cell 33: code

word_map(real, real_groups, "Navec: настоящие векторы для русского", highlight=["лук", "замок"])

### Cell 34: code

print("король − мужчина + женщина")
print("  с исключением: ", analogy("король", "мужчина", "женщина", real))
print("  без исключения:", analogy("король", "мужчина", "женщина", real, exclude=False))
print("москва − россия + франция")
print("  с исключением: ", analogy("москва", "россия", "франция", real))

### Cell 35: code

pairs = [("горячий", "раскалённый", "синонимы"), ("горячий", "холодный", "антонимы"),
         ("тёплый", "прохладный", "антонимы"), ("ледяной", "холодный", "синонимы"),
         ("король", "царь", "синонимы"), ("король", "королева", "пара")]
labels = [f"{a} — {b}" for a, b, _ in pairs]
sims = [cosine(real[a], real[b]) for a, b, _ in pairs]
kind_color = {"синонимы": COLORS[0], "антонимы": COLORS[1], "пара": COLORS[2]}
colors = [kind_color[kind] for _, _, kind in pairs]

fig, ax = plt.subplots(figsize=(9, 4))
ax.barh(labels[::-1], sims[::-1], color=colors[::-1], height=0.6)
for i, s in enumerate(sims[::-1]):
    ax.text(s + 0.01, i, f"{s:.2f}", va="center")
ax.set_xlabel("косинусная близость")
ax.set_title("Кто ближе: синонимы (синие), антонимы (оранжевые) или пара «король — королева» (зелёная)?")
plt.show()

### Cell 36: code

neighbors_table(["лук", "замок", "ключ", "коса"], real)

### Cell 37: markdown

**Задание.**

1. Что вернула аналогия «король − мужчина + женщина» без исключения слов запроса? Как это связано с лекцией?
2. Какие значения многозначных слов («замок», «коса», «ключ») видны среди соседей, а какие потерялись? Важно: соседи ищутся только среди слов нашего небольшого списка — добавьте в `real_groups` слова, которые помогут увидеть второе значение.
3. Добавьте в `pairs` свои пары синонимов и антонимов. Подтверждается ли картина?

### Cell 38: markdown

## 4. Порядок слов: где ломается мешок слов

Сгенерируем отзывы трёх видов:

- **простые**: «фильм отличный», «сериал очень скучный»;
- **локальное отрицание**: «фильм не плохой а отличный» — смысл зависит от соседних слов;
- **дальнее отрицание**: «не могу сказать что этот длинный мрачный фильм мне понравился» — «не» и глагол разделяют много слов.

Обучим логистическую регрессию на трёх наборах признаков: только отдельные слова (мешок слов), слова и пары соседей (окно 2), слова, пары и тройки (окно 3). Окно ширины k — это то же, что фильтр ширины k в TextCNN.

### Cell 39: code

random.seed(1)
POS = ["отличный", "прекрасный", "хороший", "замечательный"]
NEG = ["плохой", "ужасный", "скучный", "слабый"]
NOUNS = ["фильм", "сериал", "спектакль", "мультфильм"]
FILLERS = ["длинный", "затянутый", "мрачный", "медленный", "громкий", "новый", "странный", "дорогой"]


def review(kind):
    noun, label = random.choice(NOUNS), random.randint(0, 1)          # 1 — положительный
    good, bad = random.choice(POS), random.choice(NEG)
    if kind == "простые":
        return f"{noun} {random.choice(['', 'очень', 'просто'])} {good if label else bad}", label
    if kind == "локальное отрицание":
        return (f"{noun} не {bad} а {good}" if label else f"{noun} не {good} а {bad}"), label
    negated = random.randint(0, 1)                                      # «не могу сказать» переворачивает смысл
    liked = label ^ negated
    start = "не могу сказать" if negated else "могу честно сказать"
    end = "мне понравился" if liked else "меня разочаровал"
    middle = " ".join(random.sample(FILLERS, 4))
    return f"{start} что этот {middle} {noun} {end}", label


KINDS = ["простые", "локальное отрицание", "дальнее отрицание"]
train = [review(kind) for kind in KINDS for _ in range(600)]
test = {kind: [review(kind) for _ in range(300)] for kind in KINDS}
for kind in KINDS:
    text, label = test[kind][0]
    print(f"{kind:>20}: {text}  →  {'+' if label else '−'}")

### Cell 40: code

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

models = {"мешок слов": (1, 1), "окно 2": (1, 2), "окно 3": (1, 3)}
scores = {}
for name, ngrams in models.items():
    vectorizer = CountVectorizer(ngram_range=ngrams, token_pattern=r"(?u)\b\w+\b")
    X = vectorizer.fit_transform([t for t, _ in train])
    clf = LogisticRegression(max_iter=2000).fit(X, [y for _, y in train])
    scores[name] = {kind: clf.score(vectorizer.transform([t for t, _ in data]), [y for _, y in data])
                    for kind, data in test.items()}

scores = pd.DataFrame(scores)
fig, ax = plt.subplots(figsize=(11, 4.8))
width = 0.25
for i, name in enumerate(scores.columns):
    xs = np.arange(len(KINDS)) + (i - 1) * width
    ax.bar(xs, scores[name] * 100, width=width - 0.03, color=COLORS[i], label=name)
    for x, v in zip(xs, scores[name] * 100):
        ax.text(x, v + 1.5, f"{v:.0f}", ha="center", fontsize=10)
ax.axhline(50, color=MUTED, linestyle="--", linewidth=1)
ax.text(-0.45, 52, "угадывание", color=MUTED, fontsize=10)
ax.set_xticks(range(len(KINDS)), KINDS)
ax.set_ylabel("точность на тесте, %")
ax.set_ylim(0, 112)
ax.set_title("Мешок слов не видит порядок, окно видит только соседей")
ax.legend(frameon=False, loc="upper right")
plt.show()
scores.round(2)

### Cell 41: markdown

**Вопросы.**

1. Почему мешок слов не справляется с локальным отрицанием, хотя видел такие примеры при обучении?
2. Почему окно 2 справляется с локальным отрицанием, но не с дальним?
3. Поможет ли окно 5? А окно 10? Проверьте, поменяв `models`. Что придётся делать, если отрицание может стоять сколь угодно далеко?

**Задание.** Придумайте свой вид отзывов, который сломает окно 3, и добавьте его в `review`.

### Cell 42: markdown

## Итоги

- BPE строит словарь из частых кусочков: частые слова становятся одним токеном, редкие собираются из частей, а незнакомых токенов не бывает.
- Один и тот же текст стоит разное число токенов на разных языках и в разных токенизаторах.
- Векторы слов можно получить без нейросети: совстречаемость → PPMI → SVD. Похожие слова оказываются рядом, но рядом оказываются и антонимы, а у многозначного слова один вектор на все значения.
- Мешок слов теряет порядок. Окно (n-граммы, свёртки) видит только соседей. Чтобы связать далёкие слова, нужна модель, которая читает текст по порядку и помнит прочитанное. Это рекуррентные сети — тема следующего занятия.
