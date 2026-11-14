# lecture_03/lecture_03_overfit_pytorch.pptx

Automatically inferred reading order and possible connections. **Connections are heuristic**, not verified semantic claims.

## Slide 1

Native text objects: 4; connectors: 9; embedded pictures: 0

- (0.6in, 1.5in) КУРС «НЕЙРОННЫЕ СЕТИ»
- (0.6in, 2.1in) Тема 2. Оптимизаторы и
- (0.6in, 6.0in) Лекция 3 · Модуль 1
- (12.0in, 7.0in) 1/25

### Possible connector endpoints (spatial inference)

- Тема 2. Оптимизаторы и -> 1/25 (unverified)
- Тема 2. Оптимизаторы и -> 1/25 (unverified)

## Slide 2

Native text objects: 22; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) ПЛАН ЛЕКЦИИ
- (0.6in, 0.7in) О чём сегодня говорим
- (0.6in, 1.9in) 1
- (1.4in, 1.9in) Правило цепочки и вычислительный граф
- (7.0in, 1.9in) 2
- (7.8in, 1.9in) Прямой и обратный проход
- (1.4in, 2.5in) математическая база backprop
- (7.8in, 2.5in) считаем вручную, сверяем с PyTorch
- (0.6in, 3.4in) 3
- (1.4in, 3.3in) От ручных циклов к nn.Module
- (7.0in, 3.4in) 4
- (7.8in, 3.3in) Многоклассовая классификация
- (1.4in, 3.9in) Linear, Sequential, ReLU
- (7.8in, 3.9in) softmax и cross-entropy
- (1.4in, 4.8in) torch.optim и мини-батчи
- (7.8in, 4.8in) MNIST: собираем и обучаем сеть
- (0.6in, 4.8in) 5
- (7.0in, 4.8in) 6
- (1.4in, 5.3in) DataLoader, эпохи, батчи
- (7.8in, 5.3in) полный цикл целиком
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 2/25

## Slide 3

Native text objects: 4; connectors: 0; embedded pictures: 2

- (0.6in, 0.3in) Минусы обычного SGD
- (0.6in, 0.7in) Издержки псевдоградиента
- (0.7in, 1.8in) Псевдаградиенту характерны “скачки” - численная нестабильность связанная с тем, что градиент высчитывается каждый раз заново
- (7.9in, 1.8in) В обычном спуске могут случаться застревания в локальной точке минимума (оптимума)

## Slide 4

Native text objects: 4; connectors: 0; embedded pictures: 5

- (0.6in, 0.3in) Как бороться
- (0.6in, 0.7in) Метод импульсов (momentum) и импульс Нестерова (NAG - Nesterov’s accelerated gradient)
- (0.6in, 2.1in) Усредняем градиент по шагам, и добавляем постепенное затухание предыдущих значений:
- (0.3in, 4.7in) В импульсе Нестерова сразу смещаемся :

## Slide 5

Native text objects: 3; connectors: 0; embedded pictures: 4

- (0.6in, 0.3in) Как бороться
- (0.6in, 0.7in) RMSProp и Adam
- (0.6in, 2.1in) Усредняем градиент по шагам, и добавляем постепенное затухание предыдущих значений:

## Slide 6

Native text objects: 8; connectors: 2; embedded pictures: 1

- (0.6in, 0.3in) Выборка
- (0.6in, 0.7in) Разделение
- (5.6in, 1.0in) format.json
- (9.0in, 1.0in) format.json
- (5.6in, 2.1in) { “class_1”: 1  “class_2”: 2 “class_3”: 3 “class_4”: 4 … }
- (9.1in, 2.1in) { “png_1”: [113, 131]  “png_2”: [123, 186] … }
- (5.6in, 4.9in) format.json соотносит изображение с меткой класса (классификация), либо с координатами местоположения искомого объекта (регрессия)
- (2.2in, 6.1in) format.json

### Possible connector endpoints (spatial inference)


## Slide 7

Native text objects: 3; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Выборка
- (0.6in, 0.7in) Баланс выборок и репрезентативность
- (0.5in, 2.1in) Если у одного из классов значительно превалирует количество образов, то модель может начать всегда выдавать метку этого класса и в среднем мало ошибаться  Образ

## Slide 8

Native text objects: 23; connectors: 27; embedded pictures: 0

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Структура нейронной сети
- (1.0in, 2.1in) x 1
- (4.0in, 1.9in) 1
- (7.6in, 2.0in) y 1
- (6.7in, 2.3in) 1
- (1.0in, 3.1in) x 2
- (4.0in, 2.9in) 2
- (7.6in, 3.0in) y 2
- (6.7in, 3.3in) 2
- (1.3in, 3.7in) …
- (4.0in, 3.5in) …
- (4.0in, 4.1in) 32
- (6.8in, 3.8in) …
- (7.6in, 4.0in) y 10
- (1.1in, 4.3in) x 784
- (6.7in, 4.3in) 10
- (3.9in, 5.1in) +1
- (1.2in, 5.5in) +1
- (6.9in, 5.5in) Дя доо нейрона мы находили ∂L/∂w формулой напряую. Для сети из многих слоёв формулу «в лоб» для каждого веса не выпишешь — нужен систематический способ. Это и е
- (10.7in, 6.4in) batch
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> 1 (unverified)
- x 1 -> 2 (unverified)
- x 1 -> 32 (unverified)
- x 1 -> … (unverified)
- x 2 -> … (unverified)
- … -> 32 (unverified)
- x 1 -> 32 (unverified)
- x 2 -> 32 (unverified)
- x 784 -> 32 (unverified)
- 1 -> 2 (unverified)
- 1 -> 10 (unverified)
- 1 -> 2 (unverified)
- 2 -> 10 (unverified)
- 1 -> 10 (unverified)
- … -> 10 (unverified)
- 32 -> 10 (unverified)
- 1 -> y 1 (unverified)
- 2 -> y 2 (unverified)
- 10 -> y 10 (unverified)
- x 1 -> +1 (unverified)
- x 2 -> +1 (unverified)
- x 784 -> +1 (unverified)
- 1 -> 10 (unverified)
- … -> 10 (unverified)
- 32 -> 10 (unverified)

## Slide 9

Native text objects: 30; connectors: 15; embedded pictures: 0

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Структура нейронной сети
- (1.6in, 1.7in) y 1
- (0.8in, 1.9in) 1
- (2.1in, 2.1in) -0.1521
- (4.9in, 2.1in) 0.0892
- (7.9in, 1.9in) loss_function = nn.CrossEntropyLoss()  loss = lss_function(predict, y_train)
- (0.8in, 2.7in) 1
- (1.6in, 2.5in) y 2
- (1.6in, 3.1in) y 3
- (2.1in, 2.8in) 0.7612
- (4.9in, 2.8in) 0.1182
- (0.8in, 3.4in) 1
- (2.8in, 3.4in) SoftMax
- (2.1in, 3.5in) 0.4214
- (4.9in, 3.5in) 0.1024
- (6.2in, 3.6in) = 1.0
- (1.6in, 4.0in) y 4
- (0.8in, 4.3in) 1
- (2.1in, 4.3in) -0.0592
- (4.9in, 4.3in) 0.0945
- (0.8in, 4.7in) …
- (2.2in, 4.6in) …
- (5.0in, 4.7in) …
- (1.6in, 4.9in) y 10
- (0.7in, 5.1in) 1
- (2.1in, 5.2in) -0.1306
- (4.9in, 5.2in) 0.0910
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- 1 -> -0.1521 (unverified)
- 1 -> y 3 (unverified)
- 1 -> -0.1306 (unverified)
- 1 -> y 3 (unverified)
- 1 -> -0.0592 (unverified)
- SoftMax -> 0.1182 (unverified)
- SoftMax -> 0.1024 (unverified)
- SoftMax -> 0.0945 (unverified)
- 0.7612 -> SoftMax (unverified)
- 0.4214 -> SoftMax (unverified)
- -0.0592 -> SoftMax (unverified)

## Slide 10

Native text objects: 7; connectors: 0; embedded pictures: 3

- (0.6in, 0.3in) Переобучение
- (0.6in, 0.7in) Слишком много нейронов
- (1.4in, 3.0in) Один нейрон
- (5.8in, 3.0in) Два нейрона
- (10.1in, 3.0in) Много нейронов
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 11

Native text objects: 8; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Переобучение
- (0.6in, 0.7in) Выборка валидации
- (7.4in, 1.4in) Критерии останова: Расхождение показателя качества для обучающей выборки и выборки валидации от итерации к итерации показатель качества Q практически не меняетс
- (0.6in, 1.9in) Обучающая выборка
- (3.7in, 1.9in) Выборка валидации
- (0.7in, 4.6in) Тестовая выборка
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 12

Native text objects: 6; connectors: 0; embedded pictures: 2

- (0.6in, 0.3in) Переобучение
- (0.6in, 0.7in) Регулизатор
- (6.9in, 1.7in) c L2-регуляризацией: optim.Adam(params=model.parameters(), lr=0.01, weight_decay=0.001)
- (0.7in, 2.0in) Без L2-регуляризации: optim.Adam(params=model.parameters(), lr=0.01)
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 13

Native text objects: 4; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Переобучение
- (0.6in, 0.7in) Dropout
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 14

Native text objects: 21; connectors: 27; embedded pictures: 0

- (0.6in, 0.3in) Переобучение
- (0.6in, 0.7in) Dropout
- (0.5in, 2.0in) x 1
- (3.4in, 1.8in) 1
- (7.0in, 1.9in) y 1
- (6.1in, 2.2in) 1
- (0.5in, 3.0in) x 2
- (3.4in, 2.8in) 2
- (7.0in, 2.9in) y 2
- (3.5in, 3.4in) …
- (6.1in, 3.2in) 2
- (0.8in, 3.6in) …
- (3.4in, 4.0in) 32
- (7.0in, 3.9in) y 10
- (0.5in, 4.2in) x 784
- (6.1in, 4.2in) 10
- (3.4in, 5.0in) +1
- (0.7in, 5.4in) +1
- (6.4in, 5.4in) Дя доо нейрона мы находили ∂L/∂ формулой напряую. Для сети из многих слоёв формулу «в лоб» для каждого веса не выпишешь — нужен систематический способ. Это и ес
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> 1 (unverified)
- x 1 -> 2 (unverified)
- x 1 -> 32 (unverified)
- x 1 -> … (unverified)
- x 2 -> … (unverified)
- … -> 32 (unverified)
- x 1 -> 32 (unverified)
- x 2 -> 32 (unverified)
- x 784 -> 32 (unverified)
- 1 -> 2 (unverified)
- 1 -> 10 (unverified)
- 1 -> 2 (unverified)
- 2 -> 10 (unverified)
- 1 -> 10 (unverified)
- … -> 10 (unverified)
- 32 -> 10 (unverified)
- 1 -> y 1 (unverified)
- 2 -> y 2 (unverified)
- 10 -> y 10 (unverified)
- x 1 -> +1 (unverified)
- x 2 -> +1 (unverified)
- x 784 -> +1 (unverified)
- 1 -> 10 (unverified)
- … -> 10 (unverified)
- 32 -> 10 (unverified)

## Slide 15

Native text objects: 8; connectors: 0; embedded pictures: 2

- (0.6in, 0.3in) Переобучение
- (0.6in, 0.7in) Batch Normalization
- (3.8in, 1.4in) Relu может резко обнулять значения, что приводит и резкому изменению распределения
- (1.8in, 1.9in) w = [0.5, 0.5, 1.0]
- (8.2in, 1.9in) w = [-0.5, 0.25, 1.0]
- (6.4in, 5.4in) Дя доо нейрона мы находили ∂L/∂ формулой напряую. Для сети из многих слоёв формулу «в лоб» для каждого веса не выпишешь — нужен систематический способ. Это и ес
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25
