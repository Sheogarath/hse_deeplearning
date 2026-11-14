# Other text files

## LECTURE_REVIEW.md

# Конспект визуального изучения лекций

Проверено 2026-11-14. Источники: `lecture_text/`, `lecture_visuals/`, `lecture_image_data/`, `lecture_diagrams/`. Просмотрены все контактные листы с 371 слайдами (включая две идентичные версии лекции 6). Это конспект для повторного обращения, а не дословная транскрипция. При спорных формулах открывать исходный слайд.

## Лекция 1 — 22 слайда
От классического ML к нейросетям; перевод объектов в векторы признаков; линейная и логистическая регрессия; биологический нейрон и искусственный; история Маккаллок—Питтс, Розенблатт, Минский—Пейперт; скалярное произведение; геометрия линейной границы в 2D/3D; правило обновления весов; loss и градиентный спуск; XOR и невозможность разделения одной прямой; скрытый слой и комбинация двух границ; универсальная аппроксимация. Визуальные ключи: карта знака w·x+b, четыре XOR-точки, две линии решения XOR.

## Лекция 2 — 21 слайд
Сеть из нескольких слоёв, матричная запись и размеры весов; функции потерь и обучение; сигмоида, tanh, ReLU/leaky ReLU, линейная и softmax; обзор MSE, L1, BCE, BCEWithLogits, CrossEntropy, NLL; прямой и обратный проход; вычислительный граф и производные. Визуально многократно раскрывается одна и та же сеть: входы -> скрытый слой -> выход, затем добавляются веса, функция потерь и backprop.

## Лекция 3 — 15 слайдов
Недостатки стохастического градиента, momentum/Nesterov, RMSProp/Adam; структура train/test, баланс классов; overfitting как чрезмерная сложность разделяющей границы; validation и early stopping; L2-регуляризация; dropout и batch normalization. Визуально: колеблющаяся траектория SGD, локальные минимумы, изменение границы при росте числа нейронов, кривые train/validation и dropout-маски.

## Лекция 4 — 41 слайд
Зрительная кора как мотивация CNN; скользящее ядро 3×3, stride, padding, выходные карты и несколько каналов; max/min/average pooling; PyTorch Conv2d/MaxPool2d; свёрточный экстрактор и классификатор; vanishing gradients; skip/residual connection H(x)=F(x)+x; basic block, bottleneck, ResNet-18/34/50/101, изменение числа каналов и spatial dimensions. Визуально особенно важны слайды 3–9 (сдвиг окна), 22–27 (residual и bottleneck), 28–40 (поэтапная сборка ResNet), 41 (граф связей).

## Лекция 5 — 36 слайдов
TF, TF-IDF, one-hot, переход к плотным embedding; word2vec и контекст; нормализация и токенизация; BPE с пошаговым подсчётом частот пар, WordPiece, Unigram, byte-level BPE; языковые различия в числе токенов; PMI/PPMI и связь SGNS с матричной факторизацией; fastText и n-граммы; nn.Embedding как lookup по строкам матрицы; обучение с нуля, заморозка, дообучение; оценка сходства и аналогий, ограничения косинуса и стереотипы; embedding предложений, TextCNN и потеря порядка при усреднении.

## Лекция 6 — 21 слайд (две одинаковые версии)
Encoder -> узкое латентное представление -> decoder; простой линейный автоэнкодер и реконструкция; manifold и понижение размерности; VAE как параметризация распределения latent (mu, log variance), выборка через шум, reconstruction + KL loss; GAN как генератор, дискриминатор, реальные и синтетические образцы; примеры генерации цифр, изображений, лиц и предметов. Слайды 13–15 особенно наглядно показывают sampling и decoder.

## Лекция 7 — 68 слайдов
Feedforward против последовательного обновления состояния; h_t=f(x_t,h_{t-1}), развёртка во времени, many-to-one/one-to-many/many-to-many; nn.RNN, размеры (batch, seq, features); предсказание символов и слов, one-hot, embedding, подготовка окон последовательностей; затухающие/взрывающиеся градиенты и gradient clipping; двунаправленные RNN, sentiment classification; поэтапная схема LSTM: forget, input, candidate cell, output gates и память C_t; GRU: update/reset gates, смешивание прошлого и кандидата; nn.GRU.

## Лекция 8 — 126 слайдов
Seq2seq encoder-decoder, деградация BLEU на длинных последовательностях; alignment/attention и контекстные векторы; self-attention кодера, decoder self-attention, cross-attention; последовательное построение вычислений Q=XWq, K=XWk, V=XWv, A=softmax(QK^T/sqrt(dk)), output=AV; multi-head attention, конкатенация голов и выходная проекция; residual Add & LayerNorm, pre-norm/post-norm, FFN; позиционное кодирование (включая синусоидальные компоненты и упоминание RoPE); decoder с masked self-attention, encoder-decoder attention, causal mask, linear/softmax. Ключевые визуальные блоки: слайды 61–90 QKV и multi-head, 91–101 residual/FFN, 102–114 positions, 115–126 decoder и causal masking.

## Замечания при дальнейшем использовании
- Не путать учебную схему и строгую формулировку: отдельные слайды упрощают архитектуры и формулы.
- В нескольких лекциях есть повторяющиеся анимационные этапы (каждый этап отдельным слайдом).
- Контактные листы позволяют видеть композицию и связи; для проверки мелких индексов формул использовать текстовый слой или оригинальную презентацию.
- Семинарские ноутбуки и другие файлы репозитория **не входят** в этот завершённый визуальный просмотр.


## lecture_03/dataset_class_gen.py

import os
import json
import torch
import torchvision
import torchvision.transforms.v2 as tfs

transform = tfs.ToPILImage()

mnist_train = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=True)
mnist_test = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=False)

dir_out = 'dataset'
file_format = 'format.json'
train_data = {'dir': "train", 'data': mnist_train}
test_data = {'dir': "test", 'data': mnist_test}

if not os.path.exists(dir_out):
    os.mkdir(dir_out)

    for info in (train_data, test_data):
        os.mkdir(os.path.join(dir_out, info['dir']))

        for i in range(10):
            os.mkdir(os.path.join(dir_out, info['dir'], f"class_{i}"))


for info in (train_data, test_data):
    for i in range(10):
        path = os.path.join(dir_out, info['dir'], f"class_{i}")
        cls = info['data'].data[info['data'].targets == i]

        for n, x in enumerate(cls):
            x = transform(x)
            x.save(os.path.join(path, f"img_{n}.png"), "png")

targets = dict()
for i in range(10):
    targets[f'class_{i}'] = i

fp = open(os.path.join(dir_out, file_format), "w")
json.dump(targets, fp)
fp.close()

## lecture_03/practise/Dataset_example.py

import os
import json

from PIL import Image

import torch
import torch.nn as nn
import torch.utils.data as data
import torchvision
import torchvision.transforms.v2 as tfs


class DigitDataset(data.Dataset):
    def __init__(self, path, train=True, transform=None):
        self.path = os.path.join(path, "train" if train else "test")
        self.transform = transform

        with open(os.path.join(self.path, "format.json"), "r") as fp:
            self.format = json.load(fp)

        self.length = 0
        self.files = []
        self.targets = torch.eye(10)

        for _dir, _target in self.format.items():
            path = os.path.join(self.path, _dir)
            list_files = os.listdir(path)
            self.length += len(list_files)
            self.files.extend(map(lambda _x: (os.path.join(path, _x), _target), list_files))

    def __getitem__(self, item):
        path_file, target = self.files[item]
        t = self.targets[target]
        img = Image.open(path_file)

        if self.transform:
            img = self.transform(img).ravel().float() / 255.0

        return img, t

    def __len__(self):
        return self.length


to_tensor = tfs.ToImage()  # PILToTensor
d_train = DigitDataset("dataset", transform=to_tensor)
train_data = data.DataLoader(d_train, batch_size=32, shuffle=True)

it = iter(train_data)
x, y = next(it)
print(len(d_train))

## lecture_03/practise/DigitNet.py

import os
import json
from PIL import Image

import torch
import torch.utils.data as data
import torchvision.transforms.v2 as tfs
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm


class DigitDataset(data.Dataset):
    def __init__(self, path, train=True, transform=None):
        self.path = os.path.join(self.path, "train" if train else "test")
        self.transform = transform

        with open(os.path.join(path, "format.json"), "r") as fp:
            self.format = json.load(fp)

        self.length = 0
        self.files = []
        self.targets = torch.eye(10)

        for _dir, _target in self.format.items():
            path = os.path.join(self.path, _dir)
            list_files = os.listdir(path)
            self.length += len(list_files)
            self.files.extend(map(lambda _x: (os.path.join(path, _x), _target), list_files))

    def __getitem__(self, item):
        path_file, target = self.files[item]
        t = self.targets[target]
        img = Image.open(path_file)

        if self.transform:
            img = self.transform(img).ravel().float() / 255.0

        return img, t

    def __len__(self):
        return self.length


class DigitNN(nn.Module):
    def __init__(self, input_dim, num_hidden, output_dim):
        super().__init__()
        self.layer1 = nn.Linear(input_dim, num_hidden)
        self.layer2 = nn.Linear(num_hidden, output_dim)

    def forward(self, x):
        x = self.layer1(x)
        x = nn.functional.relu(x)
        x = self.layer2(x)
        return x


model = DigitNN(28 * 28, 32, 10)

to_tensor = tfs.ToImage()  # PILToTensor
d_train = DigitDataset("dataset", transform=to_tensor)
train_data = data.DataLoader(d_train, batch_size=32, shuffle=True)

optimizer = optim.Adam(params=model.parameters(), lr=0.01)
loss_function = nn.CrossEntropyLoss()
epochs = 2
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict = model(x_train)
        loss = loss_function(predict, y_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

d_test = DigitDataset("dataset", train=False, transform=to_tensor)
test_data = data.DataLoader(d_test, batch_size=500, shuffle=False)

Q = 0

# тестирование обученной НС
model.eval()

for x_test, y_test in test_data:
    with torch.no_grad():
        p = model(x_test)
        p = torch.argmax(p, dim=1)
        y = torch.argmax(y_test, dim=1)
        Q += torch.sum(p == y).item()

Q /= len(d_test)
print(Q)

## lecture_03/prepare_fashion_mnist.py

import os
import json
import torchvision
import torchvision.transforms.v2 as tfs

# Fashion-MNIST: картинки одежды и обуви, 28x28, оттенки серого, 10 классов.
# Индексы классов:
#   0 - T-shirt/top (футболка)    5 - Sandal (сандалия)
#   1 - Trouser (брюки)           6 - Shirt (рубашка)
#   2 - Pullover (свитер)         7 - Sneaker (кроссовок)
#   3 - Dress (платье)            8 - Bag (сумка)
#   4 - Coat (пальто)             9 - Ankle boot (ботинок)

# сюда torchvision скачает исходные файлы датасета
root = r'C:\datasets\fashion_mnist'

transform = tfs.ToPILImage()

fashion_train = torchvision.datasets.FashionMNIST(root, download=True, train=True)
fashion_test = torchvision.datasets.FashionMNIST(root, download=True, train=False)

# отдельная папка, чтобы не перемешаться с датасетом MNIST, если он лежит рядом
dir_out = 'dataset_fashion'
file_format = 'format.json'
train_data = {'dir': "train", 'data': fashion_train}
test_data = {'dir': "test", 'data': fashion_test}

for info in (train_data, test_data):
    for i in range(10):
        os.makedirs(os.path.join(dir_out, info['dir'], f"class_{i}"), exist_ok=True)

for info in (train_data, test_data):
    for i in range(10):
        path = os.path.join(dir_out, info['dir'], f"class_{i}")
        cls = info['data'].data[info['data'].targets == i]

        for n, x in enumerate(cls):
            x = transform(x)
            x.save(os.path.join(path, f"img_{n}.png"), "png")

        print(f"{info['dir']}/class_{i}: {len(cls)} изображений")

targets = dict()
for i in range(10):
    targets[f'class_{i}'] = i

with open(os.path.join(dir_out, file_format), "w") as fp:
    json.dump(targets, fp)


## lecture_03/requirements.txt

torch
torchvision
tqdm
matplotlib

## lecture_04/dataset.py

import torch.utils.data as data
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms.v2 as tfs
import torch
import os
import json
from PIL import Image
import torch.optim as optim
from tqdm import tqdm
import matplotlib.pyplot as plt
import torchvision.transforms.v2 as v2

class SunDataset(data.Dataset):
    def __init__(self, path, train=True, transform=None):
        self.path = os.path.join(path, "train" if train else "test")
        self.transform = transform

        with open(os.path.join(self.path, "format.json"), "r") as fp:
            self.format = json.load(fp)

        self.length = len(self.format)
        self.files = tuple(self.format.keys())
        self.targets = tuple(self.format.values())


    def __getitem__(self, item):
        file_path = os.path.join(self.path, self.files[item])
        img = Image.open(file_path).convert('RGB')

        if self.transform:
            img = self.transform(img)

        return img, torch.tensor(self.targets[item], dtype=torch.float32)

    def __len__(self):
        return self.length

transforms = tfs.Compose([tfs.ToImage(), tfs.ToDtype(torch.float32, scale=True)])
d_train = SunDataset('dataset_reg', transform=transforms)
train_data = data.DataLoader(d_train, batch_size=32, shuffle=True)


## lecture_04/dataset_reg_gen.py

import os
from random import randint
import json
import pygame

train_data = {'total': 10000, 'dir': "train"}
test_data = {'total': 1000, 'dir': "test"}
total_bk = 10
total_cls = 4
dir_out = 'dataset_reg'
file_format = 'format.json'
cls = [(255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0)]

if not os.path.exists(dir_out):
    os.mkdir(dir_out)
    if not os.path.exists(os.path.join(dir_out, "train")):
        os.mkdir(os.path.join(dir_out, "train"))
    if not os.path.exists(os.path.join(dir_out, "test")):
        os.mkdir(os.path.join(dir_out, "test"))

sun = pygame.image.load("images/sun64.png")
backs = [pygame.image.load(f"images/back_{n}.png") for n in range(1, total_bk+1)]

for info in (train_data, test_data):
    sun_coords = dict()

    for i in range(1, info['total']+1):
        file_out = f"sun_reg_{i}.png"
        im = backs[randint(0, total_bk-1)].copy()

        for _ in range(randint(20, 100)):
            x0 = randint(0, 256)
            y0 = randint(0, 256)
            pygame.draw.circle(im, cls[randint(0, total_cls-1)], (x0, y0), 1)

        x = randint(32, 256 - 32)
        y = randint(32, 256 - 32)
        sun_coords[file_out] = (x, y)
        im.blit(sun, (x-32, y-32))

        pygame.image.save(im, os.path.join(dir_out, info['dir'], file_out))

    fp = open(os.path.join(dir_out, info['dir'], file_format), "w")
    json.dump(sun_coords, fp)
    fp.close()


## lecture_04/evaluate_submission.py

"""
У вас папка с двумя файлами:

    submission/
        model.py       содержит функцию build_model() -> torch.nn.Module
        weights.pt     state_dict, сохранённый через torch.save(model.state_dict(), "weights.pt")

Контракт модели:
  - вход: float32-тензор [B, 3, 32, 32] со значениями в [0, 1] (без нормализации);
    нормализация (если нужна) выполняется внутри модели;
  - выход: логиты [B, 10].

"""
import argparse
import importlib.util
import json
import os
import re
import sys
import time

import numpy as np
import torch
from PIL import Image

NUM_CLASSES = 10


def parse_args():
    p = argparse.ArgumentParser(description="Оценка работы в турнире «бюджет параметров»")
    p.add_argument("--submission", required=True, help="папка с model.py и weights.pt")
    p.add_argument("--data", required=True, help="папка теста с подпапками class_0 ... class_9")
    p.add_argument("--max-params", type=int, default=150_000, help="бюджет параметров (по умолчанию 150000)")
    p.add_argument("--batch", type=int, default=500)
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    return p.parse_args()


def natural_key(name):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", name)]


def load_images(root):
    """Читает root/class_i/*.png -> (тензор [N,3,32,32] float32 в [0,1], метки [N])."""
    xs, ys = [], []
    for c in range(NUM_CLASSES):
        d = os.path.join(root, f"class_{c}")
        if not os.path.isdir(d):
            raise FileNotFoundError(f"Нет папки {d}")
        for name in sorted((f for f in os.listdir(d) if f.lower().endswith(".png")), key=natural_key):
            img = np.asarray(Image.open(os.path.join(d, name)).convert("RGB"), dtype=np.uint8)
            if img.shape != (32, 32, 3):
                raise ValueError(f"{name}: ожидается 32x32 RGB, получено {img.shape}")
            xs.append(img)
            ys.append(c)
    x = torch.from_numpy(np.stack(xs)).permute(0, 3, 1, 2).float() / 255.0
    return x, torch.tensor(ys, dtype=torch.long)


def load_model(submission_dir):
    model_path = os.path.join(submission_dir, "model.py")
    weights_path = os.path.join(submission_dir, "weights.pt")
    for path in (model_path, weights_path):
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Не найден файл {path}")

    spec = importlib.util.spec_from_file_location("student_model", model_path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.abspath(submission_dir))  # чтобы работали импорты рядом с model.py
    spec.loader.exec_module(module)
    if not hasattr(module, "build_model"):
        raise AttributeError("В model.py нет функции build_model()")

    model = module.build_model()
    state = torch.load(weights_path, map_location="cpu", weights_only=True)
    model.load_state_dict(state)
    return model


@torch.no_grad()
def accuracy(model, x, y, batch, device):
    model.eval().to(device)
    correct = 0
    for i in range(0, len(x), batch):
        logits = model(x[i:i + batch].to(device))
        if logits.shape[-1] != NUM_CLASSES:
            raise ValueError(f"Ожидается {NUM_CLASSES} логитов, получено {tuple(logits.shape)}")
        correct += (logits.argmax(1).cpu() == y[i:i + batch]).sum().item()
    return correct / len(x)


def main():
    args = parse_args()
    model = load_model(args.submission)
    params = sum(p.numel() for p in model.parameters())

    x, y = load_images(args.data)
    t0 = time.time()
    acc = accuracy(model, x, y, args.batch, args.device)
    elapsed = time.time() - t0

    result = {
        "submission": os.path.basename(os.path.abspath(args.submission)),
        "params": params,
        "max_params": args.max_params,
        "within_budget": params <= args.max_params,
        "images": len(x),
        "accuracy": round(acc, 4),
        "eval_seconds": round(elapsed, 2),
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()


## lecture_04/prectise/CNN_net.py

import os
import json
from PIL import Image

import torch
import torch.utils.data as data
import torchvision.transforms.v2 as tfs
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm


class SunDataset(data.Dataset):
    def __init__(self, path, train=True, transform=None):
        self.path = os.path.join(path, "train" if train else "test")
        self.transform = transform

        with open(os.path.join(self.path, "format.json"), "r") as fp:
            self.format = json.load(fp)

        self.length = len(self.format)
        self.files = tuple(self.format.keys())
        self.targets = tuple(self.format.values())

    def __getitem__(self, item):
        path_file = os.path.join(self.path, self.files[item])
        img = Image.open(path_file).convert('RGB')

        if self.transform:
            img = self.transform(img)

        return img, torch.tensor(self.targets[item], dtype=torch.float32)

    def __len__(self):
        return self.length


model = nn.Sequential(
    nn.Conv2d(3, 32, 3, padding='same'),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(32, 8, 3, padding='same'),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(8, 4, 3, padding='same'),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(4096, 128),
    nn.ReLU(),
    nn.Linear(128, 2)
)

transforms = tfs.Compose([tfs.ToImage(), tfs.ToDtype(torch.float32, scale=True)])
d_train = SunDataset("dataset_reg", transform=transforms)
train_data = data.DataLoader(d_train, batch_size=32, shuffle=True)

optimizer = optim.Adam(params=model.parameters(), lr=0.001, weight_decay=0.001)
loss_function = nn.MSELoss()
epochs = 5
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict = model(x_train)
        loss = loss_function(predict, y_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

st = model.state_dict()
torch.save(st, 'model_sun_2.tar')

d_test = SunDataset("dataset_reg", train=False, transform=transforms)
test_data = data.DataLoader(d_test, batch_size=50, shuffle=False)

# тестирование обученной НС
Q = 0
count = 0
model.eval()

test_tqdm = tqdm(test_data, leave=True)
for x_test, y_test in test_tqdm:
    with torch.no_grad():
        p = model(x_test)
        Q += loss_function(p, y_test).item()
        count += 1

Q /= count
print(Q)

## lecture_04/prepare_cifar10.py

"""
Датасет для задания 2

10 классов (самолёт, машина, птица, кот, олень, собака, лягушка, лошадь, корабль, грузовик),
цветные картинки 3x32x32, 50 000 в train и 10 000 в test.

Формат такой же, как у датасета с семинара:

    dataset_cifar/
        train/class_0/img_0.png ...
        test/class_0/...
        format.json          {"class_0": 0, ..., "class_9": 9}
        class_names.json     {"0": "airplane", ...}

Картинки цветные: открывайте их через Image.open(path).convert("RGB"), в сети in_channels=3.

Скрытый тест для турнира «бюджет параметров» (часть D задания 2)
----------------------------------------------------------------
Ключ --hidden-out DIR делит тест пополам внутри каждого класса:
  - чётные картинки остаются в <out>/test (публичный тест, 5000 картинок) — его раздаёте студентам;
  - нечётные уходят в <hidden-out>/test (скрытый тест, 5000 картинок) — его храните у себя
    и прогоняете через evaluate_submission.py.
Без этого ключа весь тест (10 000) остаётся в <out>/test.

Запуск:
    python prepare_cifar10.py
    python prepare_cifar10.py --hidden-out dataset_cifar_hidden
    python prepare_cifar10.py --per-class-train 1000 --force      # урезанный train для отладки
"""
import argparse
import json
import os
import shutil

import torchvision

NUM_CLASSES = 10
CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck",
]


def parse_args():
    p = argparse.ArgumentParser(description="Экспорт CIFAR-10 в папки с PNG")
    p.add_argument("--raw", default="raw_data",
                   help="куда torchvision скачает исходные файлы (по умолчанию raw_data)")
    p.add_argument("--out", default="dataset_cifar",
                   help="папка для готового датасета (по умолчанию dataset_cifar)")
    p.add_argument("--hidden-out", default=None,
                   help="папка для скрытой половины теста (для турнира); без ключа тест не делится")
    p.add_argument("--per-class-train", type=int, default=None,
                   help="оставить в train не более N картинок на класс (для быстрых экспериментов)")
    p.add_argument("--force", action="store_true",
                   help="удалить существующие папки --out и --hidden-out и создать заново")
    return p.parse_args()


def make_class_dirs(split_dir):
    for i in range(NUM_CLASSES):
        os.makedirs(os.path.join(split_dir, f"class_{i}"), exist_ok=True)


def save(img, split_dir, label, n):
    img.save(os.path.join(split_dir, f"class_{label}", f"img_{n}.png"), "png")


def export_split(ds, split_dir, limit=None, hidden_dir=None):
    """Сохраняет картинки в split_dir/class_i/img_n.png.

    Если задан hidden_dir, нечётные по порядку картинки каждого класса уходят туда.
    Возвращает (число картинок по классам в split_dir, то же для hidden_dir).
    """
    make_class_dirs(split_dir)
    if hidden_dir:
        make_class_dirs(hidden_dir)

    seen = [0] * NUM_CLASSES        # сколько картинок класса прочитано
    kept = [0] * NUM_CLASSES        # сколько записано в split_dir
    hidden = [0] * NUM_CLASSES      # сколько записано в hidden_dir

    for img, label in ds:  # img - PIL.Image (RGB), label - int
        k = seen[label]
        seen[label] += 1
        if hidden_dir and k % 2 == 1:
            save(img, hidden_dir, label, hidden[label])
            hidden[label] += 1
            continue
        if limit is not None and kept[label] >= limit:
            continue
        save(img, split_dir, label, kept[label])
        kept[label] += 1
    return kept, hidden


def write_meta(root):
    with open(os.path.join(root, "format.json"), "w", encoding="utf-8") as fp:
        json.dump({f"class_{i}": i for i in range(NUM_CLASSES)}, fp)
    with open(os.path.join(root, "class_names.json"), "w", encoding="utf-8") as fp:
        json.dump({str(i): name for i, name in enumerate(CLASS_NAMES)}, fp, ensure_ascii=False, indent=2)


def main():
    args = parse_args()

    targets = [args.out] + ([args.hidden_out] if args.hidden_out else [])
    existing = [t for t in targets if os.path.exists(t)]
    if existing:
        if not args.force:
            print(f"Уже существует: {', '.join(existing)}. Запустите с --force, чтобы пересоздать.")
            return
        for t in existing:
            shutil.rmtree(t)
    for t in targets:
        os.makedirs(t)

    train = torchvision.datasets.CIFAR10(args.raw, train=True, download=True)
    test = torchvision.datasets.CIFAR10(args.raw, train=False, download=True)

    train_counts, _ = export_split(train, os.path.join(args.out, "train"), args.per_class_train)
    hidden_test = os.path.join(args.hidden_out, "test") if args.hidden_out else None
    test_counts, hidden_counts = export_split(test, os.path.join(args.out, "test"), hidden_dir=hidden_test)

    for t in targets:
        write_meta(t)

    print(f"Готово: {args.out}")
    print(f"  train: {sum(train_counts)} картинок, по классам: {train_counts}")
    print(f"  test:  {sum(test_counts)} картинок, по классам: {test_counts}")
    if args.hidden_out:
        print(f"Скрытый тест: {args.hidden_out}/test, {sum(hidden_counts)} картинок "
              f"(храните у себя, студентам не раздавайте)")


if __name__ == "__main__":
    main()


## lecture_04/prepare_colored_mnist.py

"""
Датасет для задания. Цветной MNIST с ложной корреляцией.

Каждая цифра окрашена в один из 10 цветов. В обучающих данных цвет почти всегда
определяется классом (по умолчанию в 97% случаев цифра своего цвета):
сеть может научиться угадывать ответ по цвету вместо формы.
Проверка на данных, где цвет не связан с цифрой, показывает, чему она научилась на самом деле.

Выходная структура:

    dataset_colored/
        train/class_0/img_0_c0.png ...      обучающая выборка (смещённая)
        val/class_0/...                     валидация: то же распределение, что и train
        test_biased/class_0/...             тест с тем же смещением цвета
        test_unbiased/class_0/...           те же тестовые картинки, цвет не зависит от класса
        format.json                         {"class_0": 0, ..., "class_9": 9}
        meta.json                           палитра, параметры генерации, доля «своего» цвета в каждой выборке

В имени файла `img_{n}_c{k}.png` число k — номер цвета из палитры (meta.json),
n — номер картинки внутри класса. Картинки с одинаковыми n в test_biased и test_unbiased
(в одной папке класса) — одна и та же цифра в разных цветах.

Источник цифр — один из двух вариантов:
  1) папка в формате семинара (dataset/train/class_i/*.png, dataset/test/class_i/*.png):
         python prepare_colored_mnist.py --src dataset
  2) MNIST через torchvision (скачается автоматически):
         python prepare_colored_mnist.py

Дополнительно:
    --bias 0.97          доля цифр «своего» цвета в train/val/test_biased
    --max-per-class N    взять не более N картинок на класс (быстрая отладка)
    --seed 0             воспроизводимость
    --force              пересоздать существующую папку
"""
import argparse
import json
import os
import re
import shutil

import numpy as np
from PIL import Image

NUM_CLASSES = 10

PALETTE = [
    ("red", (255, 0, 0)),
    ("green", (0, 200, 0)),
    ("blue", (60, 60, 255)),
    ("yellow", (255, 255, 0)),
    ("magenta", (255, 0, 255)),
    ("cyan", (0, 255, 255)),
    ("orange", (255, 128, 0)),
    ("purple", (150, 60, 255)),
    ("white", (255, 255, 255)),
    ("brown", (180, 100, 40)),
]


def parse_args():
    p = argparse.ArgumentParser(description="Цветной MNIST с ложной корреляцией цвета и класса")
    p.add_argument("--src", default=None,
                   help="папка с цифрами в формате семинара (train/, test/ с подпапками class_i); "
                        "без этого ключа MNIST скачивается через torchvision")
    p.add_argument("--raw", default="raw_data", help="папка для скачанного MNIST (если нет --src)")
    p.add_argument("--out", default="dataset_colored", help="папка для результата")
    p.add_argument("--bias", type=float, default=0.97,
                   help="доля цифр «своего» цвета в смещённых выборках (по умолчанию 0.97)")
    p.add_argument("--val-frac", type=float, default=0.1,
                   help="доля исходного train, уходящая в val (по умолчанию 0.1)")
    p.add_argument("--max-per-class", type=int, default=None,
                   help="не более N картинок на класс в каждой исходной выборке")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--force", action="store_true", help="удалить существующую папку --out")
    return p.parse_args()


def _natural_key(name):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", name)]


def load_from_folder(root, max_per_class=None):
    """Читает root/class_i/*.png -> (список массивов uint8 28x28 по классам)."""
    per_class = []
    for i in range(NUM_CLASSES):
        cls_dir = os.path.join(root, f"class_{i}")
        if not os.path.isdir(cls_dir):
            raise FileNotFoundError(f"Нет папки {cls_dir}")
        names = sorted((f for f in os.listdir(cls_dir) if f.lower().endswith(".png")), key=_natural_key)
        if max_per_class is not None:
            names = names[:max_per_class]
        imgs = []
        for name in names:
            img = Image.open(os.path.join(cls_dir, name)).convert("L")
            if img.size != (28, 28):
                raise ValueError(f"{name}: ожидается 28x28, получено {img.size}")
            imgs.append(np.asarray(img, dtype=np.uint8))
        per_class.append(imgs)
    return per_class


def load_from_torchvision(raw, train, max_per_class=None):
    import torchvision  # импорт здесь, чтобы режим --src работал без torchvision

    ds = torchvision.datasets.MNIST(raw, train=train, download=True)
    data = ds.data.numpy()
    targets = ds.targets.numpy()
    per_class = []
    for i in range(NUM_CLASSES):
        imgs = [np.asarray(x, dtype=np.uint8) for x in data[targets == i]]
        if max_per_class is not None:
            imgs = imgs[:max_per_class]
        per_class.append(imgs)
    return per_class


def colorize(gray, color_idx):
    """gray: uint8 HxW -> uint8 HxWx3, чёрный фон, штрих цвета PALETTE[color_idx]."""
    rgb = (gray[..., None].astype(np.float32) / 255.0) * np.array(PALETTE[color_idx][1], np.float32)
    return np.clip(np.rint(rgb), 0, 255).astype(np.uint8)


def sample_biased_color(label, rng, bias):
    if rng.random() < bias:
        return label
    others = [c for c in range(NUM_CLASSES) if c != label]
    return int(rng.choice(others))


def sample_uniform_color(rng):
    return int(rng.integers(NUM_CLASSES))


def write_split(split_dir, per_class, color_fn):
    """Сохраняет картинки, возвращает (число картинок по классам, число «своих» цветов)."""
    counts, own = [], 0
    for label, imgs in enumerate(per_class):
        out = os.path.join(split_dir, f"class_{label}")
        os.makedirs(out, exist_ok=True)
        for n, gray in enumerate(imgs):
            c = color_fn(label, n)
            Image.fromarray(colorize(gray, c)).save(os.path.join(out, f"img_{n}_c{c}.png"), "png")
            own += int(c == label)
        counts.append(len(imgs))
    return counts, own


def main():
    args = parse_args()
    if not 0.0 <= args.bias <= 1.0:
        raise SystemExit("--bias должен быть в диапазоне [0, 1]")

    if os.path.exists(args.out):
        if not args.force:
            print(f"Папка '{args.out}' уже существует. Запустите с --force, чтобы пересоздать.")
            return
        shutil.rmtree(args.out)

    if args.src:
        train_src = load_from_folder(os.path.join(args.src, "train"), args.max_per_class)
        test_src = load_from_folder(os.path.join(args.src, "test"), args.max_per_class)
    else:
        train_src = load_from_torchvision(args.raw, True, args.max_per_class)
        test_src = load_from_torchvision(args.raw, False, args.max_per_class)

    rng = np.random.default_rng(args.seed)

    # train / val: часть картинок каждого класса откладывается в val
    train_cls, val_cls = [], []
    for imgs in train_src:
        order = rng.permutation(len(imgs))
        n_val = int(round(len(imgs) * args.val_frac))
        val_cls.append([imgs[j] for j in order[:n_val]])
        train_cls.append([imgs[j] for j in order[n_val:]])

    # test_biased и test_unbiased строятся из одних и тех же картинок в одном порядке
    def biased(label, n):
        return sample_biased_color(label, rng, args.bias)

    def uniform(label, n):
        return sample_uniform_color(rng)

    os.makedirs(args.out)
    summary = {}
    for name, per_class, color_fn in (
        ("train", train_cls, biased),
        ("val", val_cls, biased),
        ("test_biased", test_src, biased),
        ("test_unbiased", test_src, uniform),
    ):
        counts, own = write_split(os.path.join(args.out, name), per_class, color_fn)
        total = sum(counts)
        summary[name] = {
            "images": total,
            "per_class": counts,
            "own_color_fraction": round(own / total, 4) if total else None,
        }

    with open(os.path.join(args.out, "format.json"), "w", encoding="utf-8") as fp:
        json.dump({f"class_{i}": i for i in range(NUM_CLASSES)}, fp)

    meta = {
        "palette": [{"index": i, "name": n, "rgb": list(rgb)} for i, (n, rgb) in enumerate(PALETTE)],
        "bias": args.bias,
        "seed": args.seed,
        "filename_pattern": "img_{n}_c{color_index}.png",
        "own_color_rule": "у класса i «свой» цвет имеет индекс i",
        "splits": summary,
    }
    with open(os.path.join(args.out, "meta.json"), "w", encoding="utf-8") as fp:
        json.dump(meta, fp, ensure_ascii=False, indent=2)

    print(f"Готово: {args.out}")
    for name, s in summary.items():
        print(f"  {name:14s} {s['images']:6d} картинок, доля «своего» цвета: {s['own_color_fraction']}")


if __name__ == "__main__":
    main()


## lecture_04/teacher_notes.md

# Заметки преподавателя (не раздавать студентам)

## Что в комплекте

| Файл | Для чего |
| --- | --- |
| `prepare_colored_mnist.py` | датасет задания 1: цветной MNIST с ложной корреляцией |
| `prepare_cifar10.py` | датасет задания 2: CIFAR-10, при желании с делением теста на публичный и скрытый |
| `evaluate_submission.py` | проверка работ турнира (часть D задания 2) на скрытом тесте |
| `zadaniya_v2.md` | тексты заданий для студентов |
| `teacher_notes.md` | этот файл |

Подготовка:

```
python prepare_colored_mnist.py --src dataset
python prepare_cifar10.py --hidden-out dataset_cifar_hidden
```

Студентам раздаются `dataset_colored/` и `dataset_cifar/`. Папку `dataset_cifar_hidden/` храните у себя.

Прогон турнира:

```
python evaluate_submission.py --submission submission_ivanov --data dataset_cifar_hidden/test
```

На каждую работу печатается одна строка JSON: число параметров, уложился ли студент в бюджет, точность на скрытом тесте. **`model.py` студента исполняется как обычный код**, поэтому запускайте проверку в изолированной среде (Colab, контейнер).

## Замысел

**Задание 1** учит смотреть на сеть как на подозреваемого. Студенты сначала получают красивые цифры на валидации, потом видят провал на `test_unbiased` и доказывают причину тремя независимыми способами. Попутно отрабатываются свертки, число параметров, рецептивное поле, карты чувствительности и роль размера ядра (сеть из свёрток 1×1 «видит» только цвет).

**Задание 2** учит ResNet через эксперименты, а не через пересказ статьи: деградация plain-сетей, удаление блоков (идея Veit, Wilber, Belongie, 2016, «Residual Networks Behave Like Ensembles of Relatively Shallow Networks») и турнир, в котором ширину и глубину приходится выбирать самостоятельно.

## Что я проверил и что нет

Проверено:

- Все три скрипта проходят `py_compile`.
- `prepare_colored_mnist.py` прогнан целиком с источником в формате семинара. Источником служили цифры 8×8 из `sklearn`, увеличенные до 28×28, потому что настоящего MNIST в моём окружении не было. Доля «своего» цвета получилась 0,97 в `train` и около 0,10 в `test_unbiased`, как задумано.
- Логика деления теста на публичный и скрытый в `prepare_cifar10.py` проверена на заглушке: по 5 + 5 картинок на класс на 10 исходных.

Не проверено:

- Скачивание MNIST и CIFAR-10 через `torchvision`: в моём окружении нет сети и нет `torch`.
- `evaluate_submission.py` не запускался (нет `torch`), проверен только синтаксис.
- Ни одной модели на настоящих MNIST и CIFAR-10 я не обучал. Все числа ниже — ожидания, которые нужно подтвердить референсным решением до выдачи.

## Ожидаемые результаты

### Задание 1

На упрощённой проверке (MLP из `sklearn` на цифрах 8×8, увеличенных до 28×28 и раскрашенных скриптом, три запуска, среднее) получилось:

| Вход | val | test_biased | test_unbiased |
| --- | --- | --- | --- |
| RGB | 0,98 | 0,997 | 0,57 |
| оттенки серого по яркости | 0,98 | 0,99 | 0,96 |
| серый, нормированный по максимуму картинки | 0,99 | 0,99 | 0,985 |
| только средний цвет | — | 0,99 | 0,10 |

Это не CNN и не MNIST, но качественная картина должна повториться:

- Валидация выглядит прекрасно, потому что она из того же смещённого распределения. Это главный урок части C.
- Модель «только цвет» (сеть из свёрток 1×1) даёт почти идеальную точность на смещённом тесте и около 10% на несмещённом.
- **Оттенки серого лечат не до конца**: яркость штриха зависит от цвета, а значит, и от класса. Студенты, которые проверят это (подсказка есть в части D), обычно удивляются. Нормировка по максимуму картинки убирает остаток.
- Настоящая CNN на реальном MNIST, скорее всего, использует форму частично и покажет на `test_unbiased` что-то промежуточное. Если разрыв окажется слишком мал (например, меньше 5 п.п.), поднимите смещение (`--bias 0.99`) или усложните цвет. Если провал полный, смягчите до `--bias 0.95`.

Порог «разрыв не больше 2 п.п.» в части D взят по аналогии с проверкой выше. После пробного прогона скорректируйте его.

### Задание 2

- Деградация plain-сетей зависит от рецепта обучения. С `BatchNorm` и аугментацией разрыв между plain-38 и ResNet-38 может быть умеренным, а plain-8 против plain-38 покажет деградацию не всегда. Если у студентов эффект не воспроизводится, это тоже результат, но стоит снизить число эпох или увеличить глубину (`n = 9`, 56 слоёв).
- Удаление блоков: по статье Veit и соавторов, у глубокой ResNet удаление одного блока почти не меняет точность, а у plain-сети (в их случае VGG-подобной) обычно приводит к сильному падению. Для маленьких сетей эффект выражен слабее. Для ResNet-38 ожидаются небольшие падения точности; для plain-38 заметно большие. Конкретные числа нужно получить референсным прогоном.
- `MiniResNet(n=3)` (около 0,27 млн параметров) в бюджет 150k не укладывается. Студентам придётся сузить каналы. Ориентир по точности на турнире — высокие 80% при хорошей аугментации и 30–40 эпохах; это моя оценка, а не измерение.
- Для CIFAR-10 нужен GPU: шесть моделей части B на CPU не реалистичны. Для отладки кода можно взять `--per-class-train 1000`.

## Типичные ошибки студентов

- В задании 1: выбор модели по `test_unbiased`, смешивание `val` с проверкой на несмещённом тесте, `model.eval()` забыт, размер входа в `Linear` зашит числом.
- В задании 1, часть D: после перевода в серый обучают на «сером» train, а проверяют на цветном тесте (или наоборот): преобразование должно быть одинаковым везде.
- В задании 2, часть B: у plain-сети убирают вместе со skip ещё и `BatchNorm`; или у ResNet сложение происходит после ReLU вместо до него.
- В задании 2, часть C: измерения в режиме `train()` (BatchNorm пересчитывает статистику по батчу и портит измерение), попытка удалить блоки со сменой размерности, случайные выборки без фиксированного seed.
- В турнире: нормализация осталась снаружи модели, `weights.pt` сохранён целой моделью, а не `state_dict`, число параметров считается с учётом отключённых слоёв.

## Критерии оценки

Баллы по частям приведены в конце `zadaniya_v2.md`. Что смотреть в первую очередь:

| Задание | Часть | На что смотреть |
| --- | --- | --- |
| 1 | A | форма и параметры совпадают с кодом, прогноз записан до запуска |
| 1 | B | три-четыре числа в таблице, выбор по `val`, графики |
| 1 | C | не менее трёх инструментов, пункт 1 обязателен, вывод опирается на цифры |
| 1 | D | не менее двух способов, проверка утечки через яркость, объяснение |
| 2 | A | вывод градиента, подсчёт параметров, число путей `2^n` |
| 2 | B | блок с `use_skip`, шесть моделей, сравнение кривых |
| 2 | C | `eval()`, корректный список удаляемых блоков, два графика, объяснение |
| 2 | D | бюджет соблюдён, `submission/` запускается, абляции |


## lecture_06/AE.py

import os
import numpy as np
import matplotlib.pyplot as plt
from mpmath.identification import transforms

from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim

class AutoEncoderMNIST(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim):
        super().__init__()


    def forward(self, x):

transforms = tfs_v2.Compose([tfs_v2.ToImage(), tfs_v2.ToDtype(dtype=torch.float32, scale=True),
                             tfs_v2.Lambda(lambda _img: _img.ravel())])

d_train = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=True, transform=transforms)
train_data = data.DataLoader(d_train, batch_size=32, shuffle=True)

# Вызовев функции потерь

epochs = 5
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict, _ = model(x_train)
        loss = loss_func(predict, x_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss_mean + (1 - 1/lm_count) * loss_mean

st = model.state_dict()
torch.save(st, 'model_autoencoder.tar')

# st= torch.load('model_autoencoder.tar', weights_only=True)
# model.load_state_dict(st)

n = 10
model.eval()

# plt.figure(figsize=(2*n, 2*2))
# for i in range(n):
#     img, _ = d_train[i]
#     predict, _ = model(img.unsqueeze(0))
#
#     predict = predict.squeeze(0).view(28, 28)
#     img = img.view(28, 28)
#
#     dec_img = predict.detach().numpy()
#
#     ax = plt.subplot(2, n, i+1)
#     plt.imshow(img, cmap='gray')
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#
#     ax2 = plt.subplot(2, n, i+n+1)
#     plt.imshow(dec_img, cmap='gray')
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
# plt.show()



# plt.figure(figsize=(2*n, 2*2))
# frm, to = d_train.data[d_train.targets == 5][10:12]
# frm = transforms(frm)
# to = transforms(to)
#
# for i, t in enumerate(np.linspace(0., 1., n)):
#     img = frm * (1-t) + to * t
#     predict, _ = model(img.unsqueeze(0))
#     predict = predict.squeeze(0).view(28, 28)
#     dec_img = predict.detach().numpy()
#     img = img.view(28, 28).numpy()
#
#     ax = plt.subplot(2, n, i+1)
#     plt.imshow(img, cmap='gray')
# plt.show()

## lecture_06/VAE.py

import os
import numpy as np
import matplotlib.pyplot as plt
from mpmath.identification import transforms

from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class AutoEncoderMNIST(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ELU(inplace=True),
            nn.Linear(128, 64),
            nn.ELU(inplace=True),
            nn.Linear(64, self.hidden_dim)
        )

        self.decoder = nn.Sequential(
            nn.Linear(self.hidden_dim, 64),
            nn.ELU(inplace=True),
            nn.Linear(64, 128),
            nn.ELU(inplace=True),
            nn.Linear(128, output_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        h = self.encoder(x)
        x = self.decoder(h)

        return x, h

model = AutoEncoderMNIST(28 * 28, 28 * 28, 2)
transforms = tfs_v2.Compose([tfs_v2.ToImage(), tfs_v2.ToDtype(dtype=torch.float32, scale=True),
                             tfs_v2.Lambda(lambda _img: _img.ravel())])

d_train = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=True, transform=transforms)
train_data = data.DataLoader(d_train, batch_size=32, shuffle=True)

# Объявим функцию потерь и оптимизатор
optimizer = optim.Adam(params=model.parameters(), lr=0.001)
loss_func = nn.MSELoss()

epochs = 0
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict, _ = model(x_train)
        loss = loss_func(predict, x_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss_mean + (1 - 1/lm_count) * loss_mean

st = model.state_dict()
torch.save(st, 'model_autoencoder.tar')

# st= torch.load('model_autoencoder.tar', weights_only=True)
# model.load_state_dict(st)


### Вариационные автоэнкодеры
# Отображение в двумерном пространстве
# d_test = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=False, transform=transforms)
# x_data = transforms(d_test.data).view(len(d_test), -1)
#
# h = model.encoder(x_data)
# h =  h.detach().numpy()
#
# plt.scatter(h[:, 0], h[:, 1])
# plt.grid()
# plt.show()

# Восстановление
# h = torch.tensor([], dtype=torch.float32)
# predict = model.decoder(h.unsqueeze(0))
# predict = predict.detach().squeeze(0).view(28, 28)
# dec_img = predict.numpy()
# plt.imshow(dec_img, cmap='gray')
# plt.show()


# Берем рандомные цифры
# n = 5
# total = 2*n + 1
#
# plt.figure(figsize=(total, total))
#
# num = 1
# for i in range(-n, n+1):
#     for j in range(-n, n+1):
#         ax = plt.subplot(total, total, num)
#         num += 1
#         h = torch.tensor([3*i/n, 3*j/n], dtype=torch.float32)
#         predict = model.decoder(h.unsqueeze(0))
#         predict = predict.detach().squeeze(0).view(28, 28)
#         dec_img = predict.numpy()
#
#         plt.imshow(dec_img, cmap='gray')
#         ax.get_xaxis().set_visible(False)
#         ax.get_xaxis().set_visible(False)
# plt.show()

## lecture_06/dataset_class_gen.py

import os
import json
import torch
import torchvision
import torchvision.transforms.v2 as tfs

transform = tfs.ToPILImage()

mnist_train = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=True)
mnist_test = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=False)

dir_out = 'dataset'
file_format = 'format.json'
train_data = {'dir': "train", 'data': mnist_train}
test_data = {'dir': "test", 'data': mnist_test}

if not os.path.exists(dir_out):
    os.mkdir(dir_out)

    for info in (train_data, test_data):
        os.mkdir(os.path.join(dir_out, info['dir']))

        for i in range(10):
            os.mkdir(os.path.join(dir_out, info['dir'], f"class_{i}"))


for info in (train_data, test_data):
    for i in range(10):
        path = os.path.join(dir_out, info['dir'], f"class_{i}")
        cls = info['data'].data[info['data'].targets == i]

        for n, x in enumerate(cls):
            x = transform(x)
            x.save(os.path.join(path, f"img_{n}.png"), "png")

targets = dict()
for i in range(10):
    targets[f'class_{i}'] = i

fp = open(os.path.join(dir_out, file_format), "w")
json.dump(targets, fp)
fp.close()

## lecture_06/practise/AE.py

import os
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class AutoEncoderMNIST(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ELU(inplace=True),
            nn.Linear(128, 64),
            nn.ELU(inplace=True),
            nn.Linear(64, self.hidden_dim)
        )

        self.decoder = nn.Sequential(
            nn.Linear(self.hidden_dim, 64),
            nn.ELU(inplace=True),
            nn.Linear(64, 128),
            nn.ELU(inplace=True),
            nn.Linear(128, output_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        h = self.encoder(x)
        x = self.decoder(h)

        return x, h


model = AutoEncoderMNIST(784, 784, 2)
transforms = tfs_v2.Compose([tfs_v2.ToImage(), tfs_v2.ToDtype(dtype=torch.float32, scale=True),
                             tfs_v2.Lambda(lambda _img: _img.ravel())])

d_train = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=True, transform=transforms)
train_data = data.DataLoader(d_train, batch_size=100, shuffle=True)

optimizer = optim.Adam(params=model.parameters(), lr=0.001)
loss_func = nn.MSELoss()

epochs = 0
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict, _ = model(x_train)
        loss = loss_func(predict, x_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

# st = model.state_dict()
# torch.save(st, 'model_vae.tar')

st = torch.load('model_vae.tar', weights_only=True)
model.load_state_dict(st)

model.eval()

# d_test = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=False, transform=transforms)
# x_data = transforms(d_test.data).view(len(d_test), -1)
#
# h = model.encoder(x_data)
# h = h.detach().numpy()
#
# plt.scatter(h[:, 0], h[:, 1])
# plt.grid()

h = torch.tensor([-40, -20], dtype=torch.float32)
predict = model.decoder(h.unsqueeze(0))
predict = predict.detach().squeeze(0).view(28, 28)
dec_img = predict.numpy()
plt.imshow(dec_img, cmap='gray')

plt.show()

## lecture_06/practise/GAn.py

import os
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class DigitDataset(data.Dataset):
    def __init__(self, path, train=True, target=5, transform=None):
        _dataset = torchvision.datasets.MNIST(path, download=True, train=train)
        self.dataset = _dataset.data[_dataset.targets == target]
        self.length = self.dataset.size(0)
        self.target = torch.tensor([target], dtype=torch.float32)

        if transform:
            self.dataset = transform(self.dataset).view(-1, 1, 28, 28)

    def __getitem__(self, item):
        return self.dataset[item], self.target

    def __len__(self):
        return self.length


model_gen = nn.Sequential(
    nn.Linear(2, 512*7*7, bias=False),
    nn.ELU(inplace=True),
    nn.BatchNorm1d(512*7*7),
    nn.Unflatten(1, (512, 7, 7)),
    nn.Conv2d(512, 256, 5, 1, padding='same', bias=False),
    nn.ELU(inplace=True),
    nn.BatchNorm2d(256),
    nn.Conv2d(256, 128, 5, 1, padding='same', bias=False),
    nn.ELU(inplace=True),
    nn.BatchNorm2d(128),
    nn.ConvTranspose2d(128, 64, 4, 2, padding=1, bias=False),
    nn.ELU(inplace=True),
    nn.BatchNorm2d(64),
    nn.ConvTranspose2d(64, 32, 4, 2, padding=1, bias=False),
    nn.ELU(inplace=True),
    nn.BatchNorm2d(32),
    nn.Conv2d(32, 1, 1, 1),
    nn.Sigmoid()
)

model_dis = nn.Sequential(
    nn.Conv2d(1, 64, 5, 2, padding=2, bias=False),
    nn.ELU(inplace=True),
    nn.BatchNorm2d(64),
    nn.Conv2d(64, 128, 5, 2, padding=2, bias=False),
    nn.ELU(inplace=True),
    nn.BatchNorm2d(128),
    nn.Flatten(),
    nn.Linear(128*7*7, 1),
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

model_gen.to(device)
model_dis.to(device)

epochs = 20
hidden_dim = 2
batch_size = 16

transforms = tfs_v2.Compose([tfs_v2.ToImage(), tfs_v2.ToDtype(dtype=torch.float32, scale=True)])
d_train = DigitDataset(r'C:\datasets\mnist', train=True, transform=transforms)
train_data = data.DataLoader(d_train, batch_size=batch_size, shuffle=True, drop_last=True)

optimizer_gen = optim.Adam(params=model_gen.parameters(), lr=0.001)
optimizer_dis = optim.Adam(params=model_dis.parameters(), lr=0.001)
loss_func = nn.BCEWithLogitsLoss()

targets_0 = torch.zeros(batch_size, 1).to(device)
targets_1 = torch.ones(batch_size, 1).to(device)

loss_gen_lst = []
loss_dis_lst = []

model_gen.train()
model_dis.train()

for _e in range(epochs):
    loss_mean_gen = 0
    loss_mean_dis = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        x_train = x_train.to(device)

        h = torch.normal(mean=torch.zeros((batch_size, hidden_dim)), std=torch.ones((batch_size, hidden_dim)))
        h = h.to(device)

        img_gen = model_gen(h)
        fake_out = model_dis(img_gen)

        loss_gen = loss_func(fake_out, targets_1)

        optimizer_gen.zero_grad()
        loss_gen.backward()
        optimizer_gen.step()

        # discriminator learning
        img_gen = model_gen(h)
        fake_out = model_dis(img_gen)
        real_out = model_dis(x_train)

        outputs = torch.cat([real_out, fake_out], dim=0).to(device)
        targets = torch.cat([targets_1, targets_0], dim=0).to(device)

        loss_dis = loss_func(outputs, targets)

        optimizer_dis.zero_grad()
        loss_dis.backward()
        optimizer_dis.step()

        lm_count += 1
        loss_mean_gen = 1/lm_count * loss_gen.item() + (1 - 1/lm_count) * loss_mean_gen
        loss_mean_dis = 1/lm_count * loss_dis.item() + (1 - 1/lm_count) * loss_mean_dis

        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean_gen={loss_mean_gen:.3f}, loss_mean_dis={loss_mean_dis:.3f}")

    loss_gen_lst.append(loss_mean_gen)
    loss_dis_lst.append(loss_mean_dis)

st = model_gen.state_dict()
torch.save(st, 'model_gen.tar')

st = model_dis.state_dict()
torch.save(st, 'model_dis.tar')

st = {'loss_gen': loss_gen_lst, 'loss_dis': loss_dis_lst}
torch.save(st, 'model_gan_losses.tar')

# st = torch.load('model_gen.tar', weights_only=True)
# model_gen.load_state_dict(st)

# îòîáðàæåíèå ðåçóëüòàòîâ ãåíåðàöèè
model_gen.eval()
n = 2
total = 2*n+1

plt.figure(figsize=(total, total))

num = 1
for i in range(-n, n+1):
  for j in range(-n, n+1):
    ax = plt.subplot(total, total, num)
    num += 1
    h = torch.tensor([[1 * i / n, 1 * j / n]], dtype=torch.float32)
    predict = model_gen(h.to(device))
    predict = predict.detach().squeeze()
    dec_img = predict.cpu().numpy()

    plt.imshow(dec_img, cmap='gray')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.show()

## lecture_06/practise/VAE.py

import os
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class AutoEncoderMNIST(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ELU(inplace=True),
            nn.BatchNorm1d(128),
            nn.Linear(128, 64),
            nn.ELU(inplace=True),
            nn.BatchNorm1d(64)
        )

        self.h_mean = nn.Linear(64, self.hidden_dim)
        self.h_log_var = nn.Linear(64, self.hidden_dim)

        self.decoder = nn.Sequential(
            nn.Linear(self.hidden_dim, 64),
            nn.ELU(inplace=True),
            nn.BatchNorm1d(64),
            nn.Linear(64, 128),
            nn.ELU(inplace=True),
            nn.BatchNorm1d(128),
            nn.Linear(128, output_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        enc = self.encoder(x)

        h_mean = self.h_mean(enc)
        h_log_var = self.h_log_var(enc)

        noise = torch.normal(mean=torch.zeros_like(h_mean), std=torch.ones_like(h_log_var))
        h = noise * torch.exp(h_log_var / 2) + h_mean
        x = self.decoder(h)

        return x, h, h_mean, h_log_var


class VAELoss(nn.Module):
    def forward(self, x, y, h_mean, h_log_var):
        img_loss = torch.sum(torch.square(x - y), dim=-1)
        kl_loss = -0.5 * torch.sum(1 + h_log_var - torch.square(h_mean) - torch.exp(h_log_var), dim=-1)
        return torch.mean(img_loss + kl_loss)


model = AutoEncoderMNIST(784, 784, 2)
transforms = tfs_v2.Compose([tfs_v2.ToImage(), tfs_v2.ToDtype(dtype=torch.float32, scale=True),
                             tfs_v2.Lambda(lambda _img: _img.ravel())])

d_train = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=True, transform=transforms)
train_data = data.DataLoader(d_train, batch_size=100, shuffle=True)

optimizer = optim.Adam(params=model.parameters(), lr=0.001)
loss_func = VAELoss()

epochs = 5
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict, _, h_mean, h_log_var = model(x_train)
        loss = loss_func(predict, x_train, h_mean, h_log_var)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

st = model.state_dict()
torch.save(st, 'model_vae_3.tar')

# st = torch.load('model_vae.tar', weights_only=True)
# model.load_state_dict(st)

model.eval()

d_test = torchvision.datasets.MNIST(r'C:\datasets\mnist', download=True, train=False, transform=transforms)
x_data = transforms(d_test.data).view(len(d_test), -1)

_, h, _, _ = model(x_data)
h = h.detach().numpy()

plt.scatter(h[:, 0], h[:, 1])
plt.grid()


n = 5
total = 2*n+1

plt.figure(figsize=(total, total))

num = 1
for i in range(-n, n+1):
    for j in range(-n, n+1):
        ax = plt.subplot(total, total, num)
        num += 1
        h = torch.tensor([3*i/n, 3*j/n], dtype=torch.float32)
        predict = model.decoder(h.unsqueeze(0))
        predict = predict.detach().squeeze(0).view(28, 28)
        dec_img = predict.numpy()

        plt.imshow(dec_img, cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

plt.show()

## lecture_07/gru.py

import os
import numpy as np
import re

from navec import Navec
from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
from torchvision import models
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class WordsDataset(data.Dataset):
    def __init__(self, path, navec_emb, prev_words=3):
        self.prev_words = prev_words
        self.navec_emb = navec_emb

        with open(path, 'r', encoding='utf-8') as f:
            self.text = f.read()
            self.text = self.text.replace('\ufeff', '')  # убираем первый невидимый символ
            self.text = self.text.replace('\n', ' ')
            self.text = re.sub(r'[^А-яA-z- ]', '', self.text)  # удаляем все неразрешенные символы

        self.words = self.text.lower().split()
        self.words = [word for word in self.words if word in self.navec_emb] # оставляем слова, которые есть в словаре
        vocab = set(self.words)

        self.int_to_word = dict(enumerate(vocab))
        self.word_to_int = {b: a for a, b in self.int_to_word.items()}
        self.vocab_size = len(vocab)

    def __getitem__(self, item):
        _data = torch.vstack([torch.tensor(self.navec_emb[self.words[x]]) for x in range(item, item+self.prev_words)])
        word = self.words[item+self.prev_words]
        t = self.word_to_int[word]
        return _data, t

    def __len__(self):
        return len(self.words) - 1 - self.prev_words


class WordsRNN(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.hidden_size = 64
        self.in_features = in_features
        self.out_features = out_features

        self.rnn = nn.(in_features, self.hidden_size, batch_first=True)
        self.out = nn.Linear(self.hidden_size, out_features)

    def forward(self, x):
        x, h = self.rnn(x)
        y = self.out(h)
        return y


path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)

d_train = WordsDataset("text_2", navec, prev_words=3)
train_data = data.DataLoader(d_train, batch_size=8, shuffle=False)

model = WordsRNN(300, d_train.vocab_size)

optimizer = optim.Adam(params=model.parameters(), lr=0.001, weight_decay=0.0001)
loss_func = nn.CrossEntropyLoss()

epochs = 20
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict = model(x_train).squeeze(0)
        loss = loss_func(predict, y_train.long())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

st = model.state_dict()
torch.save(st, 'model_rnn_words.tar')

model.eval()
predict = "подумал встал и снова лег".lower().split()
total = 10

for _ in range(total):
    _data = torch.vstack([torch.tensor(d_train.navec_emb[predict[-x]]) for x in range(d_train.prev_words, 0, -1)])
    p = model(_data.unsqueeze(0)).squeeze(0)
    indx = torch.argmax(p, dim=1)
    predict.append(d_train.int_to_word[indx.item()])

print(" ".join(predict))

## lecture_07/lstm_bidirect.py

import os
import numpy as np
import re

from navec import Navec
from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
from torchvision import models
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class PhraseDataset(data.Dataset):
    def __init__(self, path_true, path_false, navec_emb, batch_size=8):
        self.navec_emb = navec_emb
        self.batch_size = batch_size

        with open(path_true, 'r', encoding='utf-8') as f:
            phrase_true = f.readlines()
            self._clear_phrase(phrase_true)

        with open(path_false, 'r', encoding='utf-8') as f:
            phrase_false = f.readlines()
            self._clear_phrase(phrase_false)

        self.phrase_lst = [(_x, 0) for _x in phrase_true] + [(_x, 1) for _x in phrase_false]
        self.phrase_lst.sort(key=lambda _x: len(_x[0]))
        self.dataset_len = len(self.phrase_lst)

    def _clear_phrase(self, p_lst):
        for _i, _p in enumerate(p_lst):
            _p = _p.lower().replace('\ufeff', '').strip()
            _p = re.sub(r'[^А-яA-z- ]', '', _p)
            _words = _p.split()
            _words = [w for w in _words if w in self.navec_emb]
            p_lst[_i] = _words

    def __getitem__(self, item):
        item *= self.batch_size
        item_last = item + self.batch_size
        if item_last > self.dataset_len:
            item_last = self.dataset_len

        _data = []
        _target = []
        max_length = len(self.phrase_lst[item_last-1][0])

        for i in range(item, item_last):
            words_emb = []
            phrase = self.phrase_lst[i]
            length = len(phrase[0])

            for k in range(max_length):
                t = torch.tensor(self.navec_emb[phrase[0][k]], dtype=torch.float32) if k < length else torch.zeros(300)
                words_emb.append(t)

            _data.append(torch.vstack(words_emb))
            _target.append(torch.tensor(phrase[1], dtype=torch.float32))

        _data_batch = torch.stack(_data)
        _target = torch.vstack(_target)
        return _data_batch, _target

    def __len__(self):
        last = 0 if self.dataset_len % self.batch_size == 0 else 1
        return self.dataset_len // self.batch_size + last


class WordsRNN(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.hidden_size = 16
        self.in_features = in_features
        self.out_features = out_features

        self.rnn = nn.(in_features, self.hidden_size, batch_first=True, bidirectional=True)
        self.out = nn.Linear(self.hidden_size * 2, out_features)

    def forward(self, x):
        x, (h, c) = self.rnn(x)
        hh = torch.cat((h[-2, :, :], h[-1, :, :]), dim=1)
        y = self.out(hh)
        return y


path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)

d_train = PhraseDataset("train_data_true.txt", "train_data_false.txt", navec)
train_data = data.DataLoader(d_train, batch_size=1, shuffle=True)

model = WordsRNN(300, 1)

optimizer = optim.Adam(params=model.parameters(), lr=0.001, weight_decay=0.001)
loss_func = nn.BCEWithLogitsLoss()

epochs = 20
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict = model(x_train.squeeze(0)).squeeze(0)
        loss = loss_func(predict, y_train.squeeze(0))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

st = model.state_dict()
torch.save(st, 'model_rnn_bidir.tar')

model.eval()

phrase = "Сегодня пасмурная погода"
phrase_lst = phrase.lower().split()
phrase_lst = [torch.tensor(navec[w]) for w in phrase_lst if w in navec]
_data_batch = torch.stack(phrase_lst)
predict = model(_data_batch.unsqueeze(0)).squeeze(0)
p = torch.nn.functional.sigmoid(predict).item()
print(p)
print(phrase, ":", "положительное" if p < 0.5 else "отрицательное")

## lecture_07/rnn_biderect.py

import os
import numpy as np
import re

from navec import Navec
from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
from torchvision import models
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class PhraseDataset(data.Dataset):
    def __init__(self, path_true, path_false, navec_emb, batch_size=8):
        self.navec_emb = navec_emb
        self.batch_size = batch_size

        with open(path_true, 'r', encoding='utf-8') as f:
            phrase_true = f.readlines()
            self._clear_phrase(phrase_true)

        with open(path_false, 'r', encoding='utf-8') as f:
            phrase_false = f.readlines()
            self._clear_phrase(phrase_false)

        self.phrase_lst = [(_x, 0) for _x in phrase_true] + [(_x, 1) for _x in phrase_false]
        self.phrase_lst.sort(key=lambda _x: len(_x[0]))
        self.dataset_len = len(self.phrase_lst)

    def _clear_phrase(self, p_lst):
        for _i, _p in enumerate(p_lst):
            _p = _p.lower().replace('\ufeff', '').strip()
            _p = re.sub(r'[^А-яA-z- ]', '', _p)
            _words = _p.split()
            _words = [w for w in _words if w in self.navec_emb]
            p_lst[_i] = _words

    def __getitem__(self, item):
        item *= self.batch_size
        item_last = item + self.batch_size
        if item_last > self.dataset_len:
            item_last = self.dataset_len

        _data = []
        _target = []
        max_length = len(self.phrase_lst[item_last-1][0])

        for i in range(item, item_last):
            words_emb = []
            phrase = self.phrase_lst[i]
            length = len(phrase[0])

            for k in range(max_length):
                t = torch.tensor(self.navec_emb[phrase[0][k]], dtype=torch.float32) if k < length else torch.zeros(300)
                words_emb.append(t)

            _data.append(torch.vstack(words_emb))
            _target.append(torch.tensor(phrase[1], dtype=torch.float32))

        _data_batch = torch.stack(_data)
        _target = torch.vstack(_target)
        return _data_batch, _target

    def __len__(self):
        last = 0 if self.dataset_len % self.batch_size == 0 else 1
        return self.dataset_len // self.batch_size + last


class WordsRNN(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.hidden_size = 16
        self.in_features = in_features
        self.out_features = out_features

        self.rnn = nn.RNN(in_features, self.hidden_size, batch_first=True, bidirectional=True)
        self.out = nn.Linear(self.hidden_size * 2, out_features)

    def forward(self, x):
        x, h = self.rnn(x)
        hh = torch.cat((h[-2, :, :], h[-1, :, :]), dim=1)
        y = self.out(hh)
        return y


path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)

d_train = PhraseDataset("train_data_true.txt", "train_data_false.txt", navec)
train_data = data.DataLoader(d_train, batch_size=1, shuffle=True)

model = WordsRNN(300, 1)

optimizer = optim.Adam(params=model.parameters(), lr=0.001, weight_decay=0.001)
loss_func = nn.BCEWithLogitsLoss()

epochs = 100
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict = model(x_train.squeeze(0)).squeeze(0)
        loss = loss_func(predict, y_train.squeeze(0))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

st = model.state_dict()
torch.save(st, 'model_rnn_bidir.tar')

model.eval()

phrase = "Сегодня погода яснеая"
phrase_lst = phrase.lower().split()
phrase_lst = [torch.tensor(navec[w]) for w in phrase_lst if w in navec]
_data_batch = torch.stack(phrase_lst)
predict = model(_data_batch.unsqueeze(0)).squeeze(0)
p = torch.nn.functional.sigmoid(predict).item()
print(p)
print(phrase, ":", "положительное" if p < 0.5 else "отрицательное")

## lecture_07/rnn_chars.py

import os
import numpy as np
import re

from PIL import Image
import matplotlib.pyplot as plt

from tqdm import tqdm
import torch
from torch.utils.data import BatchSampler, SequentialSampler
import torch.utils.data as data
import torchvision
from torchvision import models
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class CharsDataset(data.Dataset):
    def __init__(self, path, prev_chars=3):
        self.prev_chars = prev_chars

        with open(path, 'r', encoding='utf-8') as f:
            self.text = f.read()
            self.text = self.text.replace('\ufeff', '')  # убираем первый невидимый символ
            self.text = re.sub(r'[^А-яA-z0-9.,?;: ]', '', self.text)  # заменяем все неразрешенные символы на пустые символы

        self.text = self.text.lower()
        self.alphabet = set(self.text)
        self.int_to_alpha = dict(enumerate(sorted(self.alphabet)))
        self.alpha_to_int = {b: a for a, b in self.int_to_alpha.items()}
        # self.alphabet = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ё': 6, 'ж': 7, 'з': 8, 'и': 9,
        #                  'й': 10, 'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18,
        #                  'т': 19, 'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27,
        #                  'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32, ' ': 33, '.': 34, '!': 35, '?': 36}
        self.num_characters = len(self.alphabet)
        self.onehots = torch.eye(self.num_characters)

    def __getitem__(self, item):
        _data = torch.vstack([self.onehots[self.alpha_to_int[self.text[x]]] for x in range(item, item+self.prev_chars)])
        ch = self.text[item+self.prev_chars]
        t = self.alpha_to_int[ch]
        return _data, t

    def __len__(self):
        return len(self.text) - 1 - self.prev_chars


class TextRNN(nn.Module):
    def __init__(self):
        pass


    def forward(self, x):
        pass


d_train = CharsDataset("train_data_true.txt", prev_chars=10)
train_data = data.DataLoader(d_train, batch_size=8, shuffle=False)

model = TextRNN(d_train.num_characters, d_train.num_characters)

optimizer = optim.Adam(params=model.parameters(), lr=0.001)
loss_func = nn.CrossEntropyLoss()

epochs = 100
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict = model(x_train).squeeze(0)
        loss = loss_func(predict, y_train.long())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

st = model.state_dict()
torch.save(st, 'model_rnn_1.tar')

# st = torch.load('model_rnn_1.tar', weights_only=False)
# model.load_state_dict(st)

model.eval()
predict = "Мой дядя самых".lower()
total = 40

for _ in range(total):
    _data = torch.vstack([d_train.onehots[d_train.alpha_to_int[predict[-x]]] for x in range(d_train.prev_chars, 0, -1)])
    p = model(_data.unsqueeze(0)).squeeze(0)
    indx = torch.argmax(p, dim=1)
    predict += d_train.int_to_alpha[indx.item()]

print(predict)

## lecture_07/rnn_words.py

import os
import numpy as np
import re

from navec import Navec
from tqdm import tqdm
import torch
import torch.utils.data as data
import torchvision
from torchvision import models
import torchvision.transforms.v2 as tfs_v2
import torch.nn as nn
import torch.optim as optim


class WordsDataset(data.Dataset):
    def __init__(self, path, navec_emb, prev_words=3):
        self.prev_words = prev_words
        self.navec_emb = navec_emb

        with open(path, 'r', encoding='utf-8') as f:
            self.text = f.read()
            self.text = self.text.replace('\ufeff', '')  # убираем первый невидимый символ
            self.text = self.text.replace('\n', ' ')
            self.text = re.sub(r'[^А-яA-z- ]', '', self.text)  # удаляем все неразрешенные символы

        self.words = self.text.lower().split()
        self.words = [word for word in self.words if word in self.navec_emb] # оставляем слова, которые есть в словаре
        vocab = set(self.words)

        self.int_to_word = dict(enumerate(vocab))
        self.word_to_int = {b: a for a, b in self.int_to_word.items()}
        self.vocab_size = len(vocab)

    def __getitem__(self, item):
        _data = torch.vstack([torch.tensor(self.navec_emb[self.words[x]]) for x in range(item, item+self.prev_words)])
        word = self.words[item+self.prev_words]
        t = self.word_to_int[word]
        return _data, t

    def __len__(self):
        return len(self.words) - 1 - self.prev_words


class WordsRNN(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.hidden_size = 256
        self.in_features = in_features
        self.out_features = out_features

        self.rnn = nn.RNN(in_features, self.hidden_size, batch_first=True)
        self.out = nn.Linear(self.hidden_size, out_features)

    def forward(self, x):
        x, h = self.rnn(x)
        y = self.out(h)
        return y


path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
navec = Navec.load(path)

d_train = WordsDataset("text_2", navec, prev_words=3)
train_data = data.DataLoader(d_train, batch_size=8, shuffle=False)

model = WordsRNN(300, d_train.vocab_size)

optimizer = optim.Adam(params=model.parameters(), lr=0.001, weight_decay=0.0001)
loss_func = nn.CrossEntropyLoss()

epochs = 20
model.train()

for _e in range(epochs):
    loss_mean = 0
    lm_count = 0

    train_tqdm = tqdm(train_data, leave=True)
    for x_train, y_train in train_tqdm:
        predict = model(x_train).squeeze(0)
        loss = loss_func(predict, y_train.long())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        lm_count += 1
        loss_mean = 1/lm_count * loss.item() + (1 - 1/lm_count) * loss_mean
        train_tqdm.set_description(f"Epoch [{_e+1}/{epochs}], loss_mean={loss_mean:.3f}")

st = model.state_dict()
torch.save(st, 'model_rnn_words.tar')

model.eval()
predict = "подумал встал и снова лег".lower().split()
total = 10

for _ in range(total):
    _data = torch.vstack([torch.tensor(d_train.navec_emb[predict[-x]]) for x in range(d_train.prev_words, 0, -1)])
    p = model(_data.unsqueeze(0)).squeeze(0)
    indx = torch.argmax(p, dim=1)
    predict.append(d_train.int_to_word[indx.item()])

print(" ".join(predict))

## lecture_07/train_data_false.txt

Я притягиваю только плохое
Кому я нужен с такой внешностью
Не доверяй никому, тебя обязательно обманут
Если рискнешь высунуться, то добром это не кончиться
Говорила я тебе, не верь никому
Все новое и неизвестное – это опасно
Чтобы я не сделал, мне все равно не повезет
Я не могу с этим ничего поделать
Как бы я не старался, от судьбы не уйдешь
Мне не повезло родиться в бедной семье, значит, и умру я нищим
У меня точно не получиться, никогда
Я всегда все путаю, поэтому такой бестолковый
Мне все равно не выиграть, можно даже не пытаться
Кому я такая страшная нужна
Мне всегда не везет
Меня никто не любит
У меня плохая память
Я неудачник
Мне публично выступить? Что вы?! Это точно не мое!
У меня такая плохая карма
Чтобы я не делал, ни в чем нет успеха
Мой возраст не позволяет сделать этого.
Я никогда не сяду за руль, это же смертельно опасно!
Я никому не доверяю, это опасно. Только понадеешься, тут же подведут
Этих жизненных препятствий никогда не преодолеть, уж лучше и не начинать.
Мне никогда не выздороветь
Никакие лекарства не помогут мне
Эту болячку я сама накликала на себя
Лишний вес никогда не уйдет, даже не стоит и пробовать
Что толку от этих медитаций, только потерянное время
С возрастом болячки только усиливаются и увеличиваются
К врачам только попади, сразу найдут кучу болезней
Ни один врач не сможет вылечить мою болезнь
От хронических болезней еще никто не избавлялся – это приговор на всю жизнь
Внутреннюю энергию ни чем не вернешь
Меня любят только тогда, когда я болею
Мои дети звонят только тогда, когда я плохо себя чувствую
Только когда я болею, я могу себе позволить есть фрукты
Здоровое питание сильно дорого для меня
Много пить воды вредно, вчера по телевизору показывали.
Все мужчины рано или поздно изменяют
Муж должен держать жену в строгости
Всем парням только одно надо, и чем раньше, тем лучше
Порядочных девушек сейчас не осталось, все доступные – только свистни, в койку так и прыгают
Любовь бывает только в фильмах и в книжках, а в жизни все более прагматично
Стоит только пожениться, тут же начинаются ссора и обиды
Сама выросла без отца и дедушки, и ребенка выращу без мужика
Я первым никогда не подойду, не мужской поступок, пусть сама на коленях приползет
Если женщина в браке следит за собой, то значит кто-то есть
Все женщины — стервы
Женщинам только и подавай: деньги и шопинг
Блондинки все пустоголовые
Мужики все бесчувственные
Меня никогда не полюбят
По карьерной лестнице не пробиться, двигают только своих
Хоть сто пядей во лбу, начальник никогда тебя не похвалит
На работе инициатива наказуема, лучше не бери на себя лишнего, не подводи коллег
Нельзя быть в коллективе самым умным, этого никто не любит
Работа не волк, в лес не убежит, поэтому делай все в последний момент
Хороших начальников не бывает
Никогда не признавайся в своих ошибках, а то накажут
Сиди и помалкивай, пока тебя лично, поименно и прямо не спросили
Никому никогда не помогай, это к добру не приведет, все равно, виноватым будешь
Любое сказанное слово против тебя обернется
Мой опыт никому не нужен
Вокруг полно более молодых и успешных
С такой внешностью не работать в этой профессии
Во столько лет на хорошую работу не устроиться
Хоть 3 копейки» но зато свои, и два раза в месяц
Огромные деньги наживают только воровством
Честные деньги не бывают большими
Если денег много, значит, добыты обманным путем
Чтобы заработать свою получку, надо попотеть
То, что получено быстро, мигом и теряется
Не зря говорят, что бесплатный сыр в мышеловке
Особняки и вертолеты только у воров
За помощь надо платить монетой
Бескорыстно никто никому ничего не делает
Благотворительность только для богатых, у них денег куры не клюют, пусть и помогают
Почему такой умный, и такой бедный? Как только появляются деньги, так начинаешь их транжирить
Богатство – это зло, а бедность — не порок
Чем больше денег, тем больше зависти. Чем больше зависти, тем больше болезней
Богатство до добра не доведет
Большие деньги честными не бывают
Много денег портят человека
У того, кто имеет очень много денег, черствеет душа
Для того чтобы заработать миллион – жизни не хватит
За все хорошее надо платить

## lecture_07/train_data_true.txt

Мне нравится работа
Это шедевр изобразительного искусства
Думайте позитивно и верьте в свою способность достигать отличных результатов.
Вы — лучший ответ на проблемы, которые возникли в понедельник.
Если вы смогли в понедельник подняться с постели, значит вы супер герой.
Твои утренние мысли в понедельник задают тон всей твоей неделе.
Живи так чтобы увидеть, как ты становишься сильнее и живешь счастливой, полноценной жизнью.
Не позволяйте утренним проблемам помешать вам быть успешным.
Тяжелые времена часто приводят к величайшим моментам вашей жизни.
Продолжайте двигаться. Трудности в конце концов создают сильных людей.
Независимо через что вы проходите, в конце туннеля есть свет. Может показаться, что добраться до него сложно, но вы сможете сделать это.
Чем больше вы настроены позитивно и говорите: я хочу иметь хорошую жизнь, тем больше вы строите для себя эту реальность
Принятие позитивного отношения ко всему происходящему может творить чудеса.
Хорошее настроение добавляет годы к вашей жизни, весну к вашему шагу, искорку в ваших глазах.
Природные способности важны, но вы можете многого достичь и без них, если у вас есть целеустремленность
Окружите себя позитивными людьми, которые верят в ваши мечты, поддерживают ваши идеи
Оставайся позитивным. Прости других. Инвестируй в себя. Доверяй своим инстинктам.
Не позволяй другим испортить твой день. Делай вещи, которые приносят тебе радость. Люби себя.
Иногда лучшее, что ты можешь сделать — это не думать, не удивляться, не воображать, не зацикливаться.
Просто дыши и верь, что все получится к лучшему.
Не просто учись, а приобретай опыт; не читай, а впитывай. Не просто меняйся, а трансформируйся; не просто связывай, а защищай; не обещай, а докажи.
Не критикуй, а поощряй; не просто возьми, а дай; не просто увидь, а почувствуй.
Не просто мечтай, а делай; не достаточно услышать, а слушай; не просто расскажи, а покажи.
Преданность, вера и позитивное отношение — все это важно, если вы собираетесь добиться успеха
Выбор позитивного настроя и благодарного отношения определит, как вы собираетесь прожить свою жизнь.
Для меня жизнь заключается в том, чтобы быть позитивным и обнадеживающим, выбирая радость
Вы можете сделать позитивный выбор на всю оставшуюся жизнь
Не тратьте свое время на гнев, сожаления, беспокойства и обиды.
Жизнь слишком коротка, чтобы быть несчастной.
Я люблю
Я хочу любви
Всегда верьте в себя и выходите за пределы своих возможностей.
Ваша жизнь стоит намного больше, чем думаете, потому что вы способны достичь большего, чем знаете.
У вас больше потенциала, чем вам кажется. Но вряд ли вы узнаете весь свой потенциал, если не будете бросать себе вызов
Живи каждый день так, словно твоя жизнь только началась.
Если вы просто посмотрите на жизнь позитивно, произойдут позитивные вещи.
Жизнь становится легче и прекраснее, когда мы видим добро в других людях.
Я беру все негативы в своей жизни и превращаю их в позитив.
Держись за свои мечты о лучшей жизни и оставайся приверженным стремлению реализовать это.
Вы не можете жить позитивной жизнью с негативным умом.
Чтобы иметь положительный результат нужно только больше позитива, а от всего остального просто отшутиться.
Мы все можем привнести позитивную энергию в нашу повседневную жизнь.
Если будем больше улыбаться, разговаривать с незнакомцами, заменять рукопожатия объятиями и звонить друзьям, просто чтобы сказать им, что мы их любим.
Чем меньше вы реагируете на негативных людей, тем более позитивной станет ваша жизнь.
Когда вы контролируете свое отношение, вы контролируете свою жизнь.
Сфокусируйтесь на своих сильных сторонах, а не на слабостях.
Сосредоточьтесь на своей личности, а не на своей репутации, на своих благословениях, а не на несчастьях.
Будьте позитивны с каждой идеей, питающей ваши мечты.
Подумайте о возможности того, что вы планируете делать, и подойдите к этому с оптимизмом.
Оставайтесь на позитиве.
Вы уникальны! У вас разные таланты и способности. Вам не нужно всегда идти по стопам других.
Всегда напоминайте себе, что вам не нужно делать то, что делают все остальные.
Вы должны развивать таланты, которые были вам даны.
Старайтесь сделать хорошие дни великими и взять что-то положительное из тех дней, когда не чувствуете себя хорошо.
Будьте позитивным человеком и продолжайте двигаться вперед.
Когда вы просыпаетесь, у вас есть два варианта: быть положительным или отрицательным, оптимистом или пессимистом.
Практически нет ничего невозможного в этом мире, если вы просто сосредоточитесь на цели и сохраните позитивный настрой.
На мгновение отвлекись от проблем и сосредоточься на положительных возможностях.
Подумай, как много ты можешь сделать.
Победители в преддверии мероприятия имеют привычку выдвигать свои собственные позитивные ожидания.
Работай усердно ради того, чего хочешь, потому что оно не придет к тебе без боя.
Ты должен быть сильным и смелым, зная, что можешь делать все, что задумал.
Если кто-то тебя критикует, просто продолжай верить в себя и превращай это во что-то позитивное.
Самая большая стена, на которую вам нужно подняться — это та, которую вы строите в своем уме.
Никогда не позволяйте своему разуму отговорить вас от мечты и обманом заставить вас сдаться.
Не позволяйте ему стать величайшим препятствием на вашем пути к успеху.
Ничто не делает человека счастливее, чем счастливое сердце.
Скажите и сделайте нечто позитивное, желая помочь ситуации. Чтобы жаловаться, мозги не нужны.
Изменения не всегда приносят рост, но без изменений нет роста.
Никогда не фокусируйтесь на негативе, а всегда смотрите на позитив.
Всегда превращай счастье, боль, печаль и слезы в позитивную энергию.
Либо ты бежишь день, либо день бежит за тобой.
Будь позитивным и смейся над всем.
Каждый день живи с позитивным настроем и пытайся улучшиться.
Позитивное всё — лучше, чем негативное ничего.
Никто не идеален — вот почему у карандашей есть ластики.
Позитивность всегда побеждает мудрость.
Самое главное — смотреть в будущее. Прошлое — это твой якорь.
В глубине своего сердца верьте, что вам суждено совершать великие дела.
Чудеса рождаются из убеждений.
Одна вещь за один раз. Сначала самое главное. Начинай сейчас.
Мы ограничены, но мы можем раздвинуть границы наших ограничений.
Пусть позитив будет вашим вторым именем. Ваша позитивность станет щитом вокруг вас, который защитит вас от стрелы негатива.
Если вы настроены позитивно, то увидите возможности, а не препятствия.
Позитивное мышление и визуализация моего успеха были моими ключами к успеху.
Только хорошее действие в сочетании с позитивным мышлением приводит к успеху.
Чтобы создать радугу, нужны солнечный свет и дождь, а без них не было бы радуги.
Худшие времена могут стать лучшими, если вы думаете о них с хорошим настроем.

## lecture_08/multihead.py

import torch

batch_size = 3
emb_size = 16
enc_output_length = 7
dec_input_length = 11

x_enc = torch.normal(0, 1, (batch_size, enc_output_length, emb_size))
x_dec = torch.normal(0, 1, (batch_size, dec_input_length, emb_size))

cross_attn = torch.nn.MultiheadAttention(emb_size, num_head=2, batch_first=True)
c, weights = cross_attn(x_dec, x_enc, x_enc)

# masked_attn = torch.nn.MultiheadAttention(emb_size, num_head=2, batch_first=True)
# mask = torch.triu(torch.ones(dec_input_length, dec_input_length) * float('-inf'), diagonal=1)
# c, weights = masked_attn(x_dec, x_enc, x_enc)
#
# self_attn = torch.nn.MultiheadAttention(emb_size, num_head=2, batch_first=True)
# c, weights = self_attn(x_dec, x_enc, x_enc)

## tools/encode_lecture_images.py

#!/usr/bin/env python3
"""Encode existing lecture contact sheets as text for GitHub text-only readers."""
from pathlib import Path
import base64
root=Path(__file__).resolve().parents[1]
source=root/"lecture_visuals"
out=root/"lecture_image_data"
index=["# Encoded lecture slide contact sheets","","Base64 JPEG files mirror the contact sheets for text-only GitHub API clients.",""]
for f in sorted(source.rglob("contact_*.jpg")):
    rel=f.relative_to(source)
    dest=out/rel.with_suffix(".b64")
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(base64.b64encode(f.read_bytes()).decode("ascii"),encoding="ascii")
    index.append(f"- [{rel}]({rel.with_suffix('.b64').as_posix()})")
out.mkdir(exist_ok=True)
(out/"INDEX.md").write_text("\n".join(index)+"\n",encoding="utf-8")


## tools/extract_diagrams.py

#!/usr/bin/env python3
"""Describe native PowerPoint drawing geometry and relationships as searchable text.

This complements rendered contact sheets and OCR. It does not claim to interpret
raster pictures or guarantee semantic understanding of diagrams.
"""
from pathlib import Path
import re, zipfile, xml.etree.ElementTree as ET
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"lecture_diagrams"
NS={"p":"http://schemas.openxmlformats.org/presentationml/2006/main",
    "a":"http://schemas.openxmlformats.org/drawingml/2006/main"}
SLIDE=re.compile(r"ppt/slides/slide(\d+)\.xml$")
def attr(node, path, name, default=""):
    child=node.find(path,NS)
    return child.get(name,default) if child is not None else default
def desc(shape):
    text=" ".join((x.text or "") for x in shape.findall(".//a:t",NS)).strip()
    xfrm=shape.find(".//a:xfrm",NS)
    x=y=w=h=""
    if xfrm is not None:
        off=xfrm.find("a:off",NS);ext=xfrm.find("a:ext",NS)
        if off is not None:x,y=off.get("x",""),off.get("y","")
        if ext is not None:w,h=ext.get("cx",""),ext.get("cy","")
    tag=shape.tag.rsplit("}",1)[-1]
    kind=attr(shape,".//a:prstGeom","prst")
    name=attr(shape,".//p:cNvPr","name")
    rot=xfrm.get("rot","") if xfrm is not None else ""
    return f"- {tag} {name!r} type={kind or 'custom'} pos=({x},{y}) size=({w},{h}) rotation={rot} text={text[:350]!r}"
def main():
    OUT.mkdir(exist_ok=True)
    index=["# Native PowerPoint diagram structure","","Coordinates are EMUs. Shapes and connectors are recorded in drawing order. This is structural evidence, not a substitute for inspecting the rendered slide.",""]
    for src in sorted(ROOT.rglob("*.pptx")):
        if ".git" in src.parts:continue
        rel=src.relative_to(ROOT); dest=OUT/rel.with_suffix(".md")
        dest.parent.mkdir(parents=True,exist_ok=True)
        lines=[f"# {rel.as_posix()}","","Native shapes, connectors and images in the original slide XML.",""]
        try:
            with zipfile.ZipFile(src) as z:
                slides=sorted((int(m.group(1)),n) for n in z.namelist() if (m:=SLIDE.fullmatch(n)))
                for number,name in slides:
                    root=ET.fromstring(z.read(name))
                    shapes=root.find(".//p:spTree",NS)
                    lines.extend([f"## Slide {number}",""])
                    if shapes is None:continue
                    for el in shapes:
                        kind=el.tag.rsplit("}",1)[-1]
                        if kind in ("sp","cxnSp","pic","graphicFrame","grpSp"):
                            lines.append(desc(el))
                    lines.append("")
            dest.write_text("\n".join(lines),encoding="utf-8")
            index.append(f"- [{rel.as_posix()}]({rel.with_suffix('.md').as_posix()})")
        except Exception as exc:index.append(f"- {rel}: ERROR {exc}")
    (OUT/"INDEX.md").write_text("\n".join(index)+"\n",encoding="utf-8")
if __name__=="__main__":main()


## tools/extract_lectures.py

#!/usr/bin/env python3
"""Extract slide text and speaker notes from PowerPoint files using Python stdlib."""
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "lecture_text"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
SLIDE = re.compile(r"ppt/slides/slide(\d+)\.xml$")
NOTES = re.compile(r"ppt/notesSlides/notesSlide(\d+)\.xml$")


def extract(xml):
    root = ET.fromstring(xml)
    paragraphs = []
    for p in root.findall(".//a:p", NS):
        parts = [t.text or "" for t in p.findall(".//a:t", NS)]
        line = "".join(parts).strip()
        if line:
            paragraphs.append(line)
    return paragraphs


def process(src):
    relative = src.relative_to(ROOT)
    dest = OUT / relative.with_suffix(".md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = "https://github.com/Sheogarath/hse_deeplearning/blob/main/" + quote(relative.as_posix(), safe="/")
    lines = [f"# {relative.name}", "", f"Source: {url}", ""]
    with zipfile.ZipFile(src) as archive:
        names = archive.namelist()
        slides = sorted(((int(m.group(1)), name) for name in names if (m := SLIDE.fullmatch(name))))
        notes = {int(m.group(1)): name for name in names if (m := NOTES.fullmatch(name))}
        for num, name in slides:
            lines.extend([f"## Slide {num}", ""])
            lines.extend(extract(archive.read(name)) or ["[No extractable text]"])
            lines.append("")
            if num in notes:
                note_text = extract(archive.read(notes[num]))
                if note_text:
                    lines.extend(["### Speaker notes", "", *note_text, ""])
    dest.write_text("\n".join(lines), encoding="utf-8")
    return relative.as_posix(), dest.relative_to(ROOT).as_posix(), len(slides)


def main():
    OUT.mkdir(exist_ok=True)
    presentations = sorted(p for p in ROOT.rglob("*.pptx") if ".git" not in p.parts and "lecture_text" not in p.parts)
    index = ["# Lecture presentations", "", "Automatically extracted slide text. Images, equations stored as images, and charts may require viewing the original PPTX.", ""]
    for src in presentations:
        try:
            original, output, count = process(src)
            index.append(f"- [{original}]({output.removeprefix('lecture_text/')}) — {count} slides")
        except Exception as exc:
            index.append(f"- {src.relative_to(ROOT)} — extraction error: {exc}")
    (OUT / "INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()


## tools/index_remaining_course.py

#!/usr/bin/env python3
"""Inventory and summarize all course files, with notebook cell contents."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
out=root/"COURSE_CODE_REVIEW"
out.mkdir(exist_ok=True)
skip={".git","lecture_text","lecture_visuals","lecture_image_data","lecture_diagrams","lecture_diagram_maps","COURSE_CODE_REVIEW"}
files=sorted(p for p in root.rglob("*") if p.is_file() and not any(part in skip for part in p.relative_to(root).parts))
lines=["# Repository inventory","",f"Files: {len(files)}",""]
for p in files:
    rel=p.relative_to(root)
    lines.append(f"- `{rel}` ({p.stat().st_size} bytes)")
(out/"INVENTORY.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
notebooks=["# Notebook contents",""]
texts=["# Other text files",""]
for p in files:
    rel=p.relative_to(root)
    if p.suffix==".ipynb":
        try:
            data=json.loads(p.read_text(encoding="utf-8"))
            notebooks.extend([f"## {rel}",""])
            for i,c in enumerate(data.get("cells",[]),1):
                source="".join(c.get("source",[]))
                # Remove embedded image base64 data URIs and notebook output blobs
                import re
                source=re.sub(r"data:image/[^;]+;base64,[A-Za-z0-9+/=]+","[embedded image]",source)
                notebooks.extend([f"### Cell {i}: {c.get('cell_type')}","",source[:20000],""])
        except Exception as e:notebooks.append(f"ERROR {rel}: {e}")
    elif p.suffix.lower() in {".py",".md",".txt",".yml",".yaml",".toml",".json",".csv",".sh"} and not rel.as_posix().startswith(".github/"):
        try:
            s=p.read_text(encoding="utf-8")
            if len(s)>300000:s=s[:300000]+"\n[TRUNCATED]"
            texts.extend([f"## {rel}","",s,""])
        except Exception:pass
(out/"NOTEBOOKS.md").write_text("\n".join(notebooks),encoding="utf-8")
(out/"TEXT_FILES.md").write_text("\n".join(texts),encoding="utf-8")


## tools/render_lecture_visuals.py

#!/usr/bin/env python3
"""Render PPTX slides and extract text visible in images with OCR.

Creates per-slide OCR transcripts and compact visual contact sheets.
Original PowerPoint files remain unchanged.
"""
from pathlib import Path
import subprocess
import tempfile
import re
import xml.etree.ElementTree as ET
import zipfile
import shutil
from urllib.parse import quote
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "lecture_visuals"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}

def run(args):
    return subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

def extract(pptx):
    rel = pptx.relative_to(ROOT)
    target = OUT / rel.with_suffix("")
    target.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)
        run(["libreoffice", "-env:UserInstallation=file:///tmp/lo_lecture_visual", "--headless", "--convert-to", "pdf", "--outdir", str(temp), str(pptx)])
        pdf = temp / (pptx.stem + ".pdf")
        if not pdf.exists():
            raise RuntimeError("LibreOffice did not produce PDF")
        run(["pdftoppm", "-f", "1", "-l", "1000", "-r", "95", "-png", str(pdf), str(temp / "slide")])
        pngs = sorted(temp.glob("slide-*.png"))
        transcript = [f"# Visual review: {rel.as_posix()}", "", "OCR of fully rendered slides; also includes image-only labels. OCR may contain mistakes.", ""]
        thumbs = []
        for n, png in enumerate(pngs, 1):
            txt = run(["tesseract", str(png), "stdout", "-l", "rus+eng"]).stdout.strip()
            transcript += [f"## Slide {n}", "", txt or "[No text detected in rendered slide]", ""]
            with Image.open(png) as original:
                im = original.convert("RGB")
                im.thumbnail((650, 400))
                tile = Image.new("RGB", (680, 430), "white")
                tile.paste(im, ((680-im.width)//2, 8))
                ImageDraw.Draw(tile).text((12, 407), f"Slide {n}", fill="black")
                thumbs.append(tile)
        for offset in range(0, len(thumbs), 12):
            batch = thumbs[offset:offset+12]
            sheet = Image.new("RGB", (680*3, 430*4), "#dddddd")
            for j, im in enumerate(batch):
                sheet.paste(im, ((j%3)*680, (j//3)*430))
            sheet.save(target / f"contact_{offset//12+1:02d}.jpg", quality=70, optimize=True)
        (target / "OCR.md").write_text("\n".join(transcript), encoding="utf-8")
        return len(pngs), len(thumbs)

def main():
    OUT.mkdir(exist_ok=True)
    index = ["# Visual lecture index", "", "Rendered slide contact sheets and OCR of text embedded in diagrams, screenshots and pictures.", ""]
    for pptx in sorted(ROOT.rglob("*.pptx")):
        if ".git" in pptx.parts:
            continue
        try:
            count, _ = extract(pptx)
            rel = pptx.relative_to(ROOT)
            folder = rel.with_suffix("").as_posix()
            index.append(f"- [{rel.as_posix()}]({folder}/OCR.md): {count} rendered slides; contact sheets in adjacent folder")
        except Exception as exc:
            index.append(f"- {pptx.relative_to(ROOT)}: ERROR {exc}")
    (OUT / "INDEX.md").write_text("\n".join(index)+"\n", encoding="utf-8")

if __name__ == "__main__":
    main()


## tools/summarize_diagrams.py

#!/usr/bin/env python3
"""Build compact per-slide diagram maps from PowerPoint native shapes.

Outputs spatial reading order, labelled objects, and connector endpoint candidates.
Endpoint associations are heuristic; they are explicitly marked as such.
"""
from pathlib import Path
import zipfile, re, math, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"lecture_diagram_maps"
NS={"p":"http://schemas.openxmlformats.org/presentationml/2006/main","a":"http://schemas.openxmlformats.org/drawingml/2006/main"}
SLIDE=re.compile(r"ppt/slides/slide(\d+)\.xml$")
def pos(e):
    t=e.find(".//a:xfrm",NS)
    if t is None:return None
    o=t.find("a:off",NS);s=t.find("a:ext",NS)
    if o is None or s is None:return None
    return tuple(int(x) for x in (o.get("x","0"),o.get("y","0"),s.get("cx","0"),s.get("cy","0")))
def label(e):
    return " ".join((x.text or "").strip() for x in e.findall(".//a:t",NS)).strip()
def midpoint(p):return (p[0]+p[2]/2,p[1]+p[3]/2)
def process(pptx):
    rel=pptx.relative_to(ROOT);out=OUT/rel.with_suffix(".md")
    out.parent.mkdir(parents=True,exist_ok=True)
    lines=[f"# {rel.as_posix()}","","Automatically inferred reading order and possible connections. **Connections are heuristic**, not verified semantic claims.",""]
    with zipfile.ZipFile(pptx) as z:
        slides=sorted((int(m.group(1)),name) for name in z.namelist() if (m:=SLIDE.fullmatch(name)))
        for number,name in slides:
            root=ET.fromstring(z.read(name));tree=root.find(".//p:spTree",NS)
            lines.extend([f"## Slide {number}",""])
            if tree is None:continue
            shapes=[];links=[];pictures=0
            for e in tree.iter():
                tag=e.tag.rsplit("}",1)[-1]
                if tag=="pic":pictures+=1
                if tag not in ("sp","cxnSp"):continue
                p=pos(e)
                if not p:continue
                if tag=="cxnSp":links.append(p)
                elif label(e):shapes.append((p,label(e).replace("\n"," ")[:160]))
            shapes.sort(key=lambda x:(round(x[0][1]/300000),x[0][0]))
            lines.append(f"Native text objects: {len(shapes)}; connectors: {len(links)}; embedded pictures: {pictures}")
            lines.append("")
            for p,s in shapes[:100]:
                lines.append(f"- ({round(p[0]/914400,1)}in, {round(p[1]/914400,1)}in) {s}")
            if len(shapes)>100:lines.append(f"- ... {len(shapes)-100} more labelled objects")
            if links and shapes:
                lines.extend(["","### Possible connector endpoints (spatial inference)",""])
                for p in links[:80]:
                    a=(p[0],p[1]);b=(p[0]+p[2],p[1]+p[3])
                    near=lambda point:min(shapes,key=lambda s:math.dist(point,midpoint(s[0])))[1]
                    start,end=near(a),near(b)
                    if start!=end:lines.append(f"- {start[:70]} -> {end[:70]} (unverified)")
            lines.append("")
    out.write_text("\n".join(lines),encoding="utf-8")
    return rel,out.relative_to(ROOT),len(slides)
def main():
    OUT.mkdir(exist_ok=True)
    index=["# Spatial diagram maps","","Heuristic maps generated from editable PowerPoint shapes. Raster graphics still require direct visual inspection.",""]
    for p in sorted(ROOT.rglob("*.pptx")):
        if ".git" in p.parts:continue
        try:
            rel,out,n=process(p)
            index.append(f"- [{rel}]({out.relative_to(OUT) if out.is_absolute() else out.relative_to(Path('lecture_diagram_maps'))}): {n} slides")
        except Exception as e:index.append(f"- {p.relative_to(ROOT)}: ERROR {e}")
    (OUT/"INDEX.md").write_text("\n".join(index)+"\n",encoding="utf-8")
if __name__=="__main__":main()

