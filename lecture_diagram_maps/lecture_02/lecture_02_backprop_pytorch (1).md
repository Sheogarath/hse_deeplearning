# lecture_02/lecture_02_backprop_pytorch (1).pptx

Automatically inferred reading order and possible connections. **Connections are heuristic**, not verified semantic claims.

## Slide 1

Native text objects: 7; connectors: 9; embedded pictures: 0

- (0.6in, 1.5in) КУРС «НЕЙРОННЫЕ СЕТИ»
- (0.6in, 2.1in) Тема 2. Backpropagation и автоматическое дифференцирование
- (0.6in, 4.2in) Как на самом деле обучаются нейронные сети — от правила цепочки до PyTorch и классификации MNIST
- (0.6in, 6.0in) Лекция 2 · Модуль 1
- (0.6in, 6.4in) [Имя преподавателя]
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 1/25

### Possible connector endpoints (spatial inference)

- Тема 2. Backpropagation и автоматическое дифференцирование -> 1/25 (unverified)
- Тема 2. Backpropagation и автоматическое дифференцирование -> 1/25 (unverified)
- Тема 2. Backpropagation и автоматическое дифференцирование -> 1/25 (unverified)
- Тема 2. Backpropagation и автоматическое дифференцирование -> 1/25 (unverified)

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

Native text objects: 6; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) МОСТИК ОТ ТЕМЫ 1 И СЕМИНАРА
- (0.6in, 0.7in) Что мы уже умеем
- (0.6in, 1.9in) Мы вручную реализовали один нейрон: z = w·x+b, ŷ = σ(z), и обучили его через loss.backward() + ручное обновление весов Мы своими глазами увидели, как точка скат
- (0.9in, 5.3in) Но мы ни разу не спросили: а как PyTorch вообще посчитал .grad для W1, если между W1 и loss стоит ещё три операции? Сегодня — ответ на этот вопрос, и это и есть
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 3/25

## Slide 4

Native text objects: 22; connectors: 12; embedded pictures: 0

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (1.9in, 1.8in) x 1
- (2.7in, 1.8in) ω 1 11
- (5.0in, 1.8in) Σ
- (6.5in, 1.8in) σ (z)
- (7.8in, 2.0in) ω 2 11
- (2.4in, 2.3in) ω 1 12
- (8.3in, 2.6in) Σ
- (9.7in, 2.6in) σ (z)
- (10.9in, 2.6in) y
- (1.8in, 3.0in) x 2
- (2.2in, 3.8in) ω  1 31
- (4.9in, 3.7in) Σ
- (6.5in, 3.7in) σ (z)
- (7.7in, 3.6in) ω 2 11
- (1.8in, 4.1in) x 3
- (2.9in, 4.4in) ω 1 32
- (6.9in, 5.5in) σ (z) =
- (7.8in, 5.7in) 1,   z >=  0,5  0,   z <=  0,5
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> Σ (unverified)
- x 2 -> Σ (unverified)
- x 1 -> Σ (unverified)
- x 1 -> Σ (unverified)
- ω  1 31 -> Σ (unverified)
- x 1 -> Σ (unverified)
- Σ -> σ (z) (unverified)
- Σ -> σ (z) (unverified)
- σ (z) -> Σ (unverified)
- σ (z) -> ω 2 11 (unverified)
- Σ -> σ (z) (unverified)

## Slide 5

Native text objects: 21; connectors: 17; embedded pictures: 0

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (8.2in, 0.7in) y 1 y 2
- (11.3in, 0.7in) x 1 x 2 x 3
- (9.0in, 1.0in) =
- (9.4in, 1.0in) σ 2
- (9.8in, 1.0in) W 2
- (10.2in, 0.9in) σ 1
- (10.8in, 1.0in) W 1
- (1.9in, 1.8in) x 1
- (8.3in, 2.1in) y 1
- (1.8in, 3.0in) x 2
- (8.3in, 3.5in) y 2
- (1.8in, 4.1in) x 3
- (6.9in, 4.6in) σ 2 (z)
- (4.9in, 5.2in) σ 1 (z)
- (6.9in, 5.5in) Для одного нейрона мы находили ∂L/∂w формулой напрямую. Для сети из многих слоёв формулу «в лоб» для каждого веса не выпишешь — нужен ситематический способ. Это
- (3.4in, 5.9in) W 1
- (6.2in, 5.9in) W 2
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- x 1 -> ПОСТАНОВКА ЗАДАЧИ (unverified)
- x 1 -> σ 1 (z) (unverified)
- x 3 -> σ 1 (z) (unverified)
- x 1 -> σ 1 (z) (unverified)
- σ 1 (z) -> σ 2 (z) (unverified)
- x 1 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- Сеть — это не один нейрон -> σ 2 (z) (unverified)
- Сеть — это не один нейрон -> y 2 (unverified)
- σ 1 (z) -> σ 2 (z) (unverified)
- Сеть — это не один нейрон -> σ 2 (z) (unverified)

## Slide 6

Native text objects: 28; connectors: 17; embedded pictures: 0

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (8.2in, 0.7in) y 1 y 2
- (11.3in, 0.7in) x 1 x 2 x 3
- (9.0in, 1.0in) =
- (9.4in, 1.0in) σ 2
- (9.8in, 1.0in) W 2
- (10.2in, 0.9in) σ 1
- (10.8in, 1.0in) W 1
- (1.9in, 1.8in) x 1
- (8.3in, 2.1in) y 1
- (9.7in, 2.3in) y = f(x; W 1 ,W 2 )
- (1.8in, 3.0in) x 2
- (9.8in, 3.0in) y = f(x; ω )
- (8.3in, 3.5in) y 2
- (1.8in, 4.1in) x 3
- (6.9in, 4.6in) σ 2 (z)
- (4.9in, 5.2in) σ 1 (z)
- (1.1in, 5.7in) ω 11 ω 12 ω 13   ω 21  ω 22 ω 23   ω 31  ω 32  ω 33
- (6.9in, 5.5in) Для одного нейрона мы находили ∂L/∂w формулой напрямую. Для сети из многих слоёв формулу «в лоб» для каждого веса не выпишешь — нужен систематический способ. Эт
- (3.4in, 5.9in) W 1
- (6.2in, 5.9in) W 2
- (6.6in, 6.0in) =
- (7.0in, 6.0in) ω 11 ω 12 ω 13   ω 21  ω 22 ω 23
- (0.3in, 6.1in) W 1
- (0.7in, 6.1in) =
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- x 1 -> ПОСТАНОВКА ЗАДАЧИ (unverified)
- x 1 -> σ 1 (z) (unverified)
- x 3 -> σ 1 (z) (unverified)
- x 1 -> σ 1 (z) (unverified)
- σ 1 (z) -> σ 2 (z) (unverified)
- x 1 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- Сеть — это не один нейрон -> σ 2 (z) (unverified)
- Сеть — это не один нейрон -> y 2 (unverified)
- σ 1 (z) -> σ 2 (z) (unverified)
- Сеть — это не один нейрон -> σ 2 (z) (unverified)

## Slide 7

Native text objects: 30; connectors: 17; embedded pictures: 0

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (8.2in, 0.7in) y 1 y 2
- (11.3in, 0.7in) x 1 x 2 x 3
- (9.0in, 1.0in) =
- (9.4in, 1.0in) σ 2
- (9.8in, 1.0in) W 2
- (10.2in, 0.9in) σ 1
- (10.8in, 1.0in) W 1
- (1.9in, 1.8in) x 1
- (8.3in, 2.1in) y 1
- (9.7in, 2.3in) y = f(x; W 1 ,W 2 )
- (1.8in, 3.0in) x 2
- (9.8in, 3.0in) y = f(x; ω )
- (8.3in, 3.5in) y 2
- (1.8in, 4.1in) x 3
- (6.9in, 4.6in) σ 2 (z)
- (4.9in, 5.2in) σ 1 (z)
- (5.8in, 5.5in) Для одного нейрона мы находили ∂L/∂w формулой напрямую. Для сети из многих слоёв формулу «в лоб» для каждого веса не выпишешь — нужен систематический способ. Эт
- (8.2in, 5.7in) x 11 x 12 …   x 1m  x 21  x 22 …   x 2m  …   …    …   … x l 1  x l 2 … x lm
- (8.6in, 5.5in) Для одного нейрона мы находили ∂L/∂w формулой напрямую. Для сети из многих слоёв формулу «в лоб» для каждого веса не выпишешь — нужен систематический способ. Эт
- (11.0in, 5.7in) y 11 y 12 …   y 1m  y 21  y 22 …   y 2m  …   …    …   … y l1  y l2 … y lm
- (3.4in, 5.9in) W 1
- (6.2in, 5.9in) W 2
- (7.4in, 6.0in) X l
- (7.7in, 6.0in) =
- (10.2in, 6.1in) Y l
- (10.6in, 6.1in) =
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- x 1 -> ПОСТАНОВКА ЗАДАЧИ (unverified)
- x 1 -> σ 1 (z) (unverified)
- x 3 -> σ 1 (z) (unverified)
- x 1 -> σ 1 (z) (unverified)
- σ 1 (z) -> σ 2 (z) (unverified)
- x 1 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- x 2 -> σ 1 (z) (unverified)
- Сеть — это не один нейрон -> σ 2 (z) (unverified)
- Сеть — это не один нейрон -> y 2 (unverified)
- σ 1 (z) -> σ 2 (z) (unverified)
- Сеть — это не один нейрон -> σ 2 (z) (unverified)

## Slide 8

Native text objects: 16; connectors: 17; embedded pictures: 2

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (9.1in, 0.9in) X l =[x 1 , x 2 , … x l ] T
- (1.9in, 1.8in) x 1
- (9.1in, 1.6in) Y l =[y 1 , y 2 , … y m ] T
- (8.3in, 2.1in) y 1
- (1.8in, 3.0in) x 2
- (9.2in, 2.8in) t i =f(x i , ω )
- (8.3in, 3.5in) y 2
- (9.3in, 3.5in) L i (t i ,y i ) - функция потерь
- (1.8in, 4.1in) x 3
- (6.9in, 4.6in) σ 2 (z)
- (1.7in, 5.3in) В задачах регрессии:
- (8.1in, 5.3in) В задачах бинарной классификации:
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> В задачах регрессии: (unverified)
- x 2 -> В задачах регрессии: (unverified)
- x 1 -> ПОСТАНОВКА ЗАДАЧИ (unverified)
- x 1 -> В задачах регрессии: (unverified)
- x 3 -> В задачах регрессии: (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 1 (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- x 2 -> В задачах регрессии: (unverified)
- x 2 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 2 (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)

## Slide 9

Native text objects: 15; connectors: 17; embedded pictures: 1

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (9.1in, 0.9in) X l = [x 1 , x 2 , … x l ] T
- (1.9in, 1.8in) x 1
- (9.3in, 1.6in) Y l = [y 1 , y 2 , … y m ] T
- (8.3in, 2.1in) y 1
- (1.8in, 3.0in) x 2
- (9.2in, 2.8in) t i = f(x i , ω)
- (8.3in, 3.5in) y 2
- (9.3in, 3.5in) L i (t i ,y i ) - функция потерь
- (1.8in, 4.1in) x 3
- (6.9in, 4.6in) σ 2 (z)
- (7.7in, 5.4in) Q(X l ; ω ) = 1/l ∑L i (t i , y i ; ω ) - показатель качества
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> σ 2 (z) (unverified)
- x 2 -> σ 2 (z) (unverified)
- x 1 -> ПОСТАНОВКА ЗАДАЧИ (unverified)
- x 1 -> σ 2 (z) (unverified)
- x 3 -> σ 2 (z) (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 1 (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- x 2 -> σ 2 (z) (unverified)
- x 2 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 2 (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)

## Slide 10

Native text objects: 15; connectors: 44; embedded pictures: 0

- (0.6in, 0.3in) БОЛЕЕ ШИРОКИЙ ВЗГЛЯД
- (0.6in, 0.7in) Функция потерь и градиентный спуск
- (0.6in, 1.6in) Правило Розенблатта — красивый частный случай. Общая идея, на которой держится всё обучение нейросетей: минимизация функции потерь L(w) — насколько сильно модел
- (8.0in, 2.2in) Градиент ∂L/∂w — направление наискорейшего РОСТА функции. Мы хотим loss уменьшить — значит, идём в обратную сторону:
- (0.5in, 2.8in) L(w)
- (7.7in, 3.7in) w ← w − η · ∂L/∂w
- (4.0in, 4.1in) шаги градиентного спуска →
- (8.4in, 4.5in) ∇L = ( ∂L/∂w 1 , ∂L/∂w 2 , ..., ∂L/∂w n )
- (5.6in, 4.9in) текущий вес
- (7.7in, 5.4in) Наклон положительный (как здесь) → двигаем w влево, к минимуму Чем ближе к минимуму, тем меньше наклон — шаги естественно замедляются Это и есть градиентный спу
- (3.5in, 6.3in) минимум
- (7.0in, 6.5in) w
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (1.0in, 6.8in) касательная = производная в точке (наклон)
- (12.0in, 7.0in) 14/19

### Possible connector endpoints (spatial inference)

- L(w) -> Тема 1 · Нейронные сети (unverified)
- Тема 1 · Нейронные сети -> w (unverified)
- L(w) -> Тема 1 · Нейронные сети (unverified)
- Тема 1 · Нейронные сети -> минимум (unverified)
- минимум -> текущий вес (unverified)
- Правило Розенблатта — красивый частный случай. Общая идея, на которой  -> текущий вес (unverified)
- шаги градиентного спуска → -> w (unverified)
- шаги градиентного спуска → -> текущий вес (unverified)

## Slide 11

Native text objects: 17; connectors: 17; embedded pictures: 1

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (9.1in, 0.9in) X l = [x 1 , x 2 , … x l ] T
- (1.9in, 1.8in) x 1
- (9.3in, 1.6in) Y l = [y 1 , y 2 , … y m ] T
- (8.3in, 2.1in) y 1
- (1.8in, 3.0in) x 2
- (9.2in, 2.8in) t i = f(x i , ω)
- (8.3in, 3.5in) y 2
- (9.3in, 3.5in) L i (t i ,y i ) - функция потерь
- (1.8in, 4.1in) x 3
- (6.9in, 4.6in) σ 2 (z)
- (8.1in, 4.8in) Q(X l ; ω ) = 1/l ∑L i (t i , y i ; ω ) - показатель качества
- (3.1in, 5.6in) 1,      z >= λ (например λ = 0)  0 ,      z < λ
- (1.8in, 5.9in) σ(z) =
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> 1,      z >= λ (например λ = 0)  0 ,      z < λ (unverified)
- x 2 -> 1,      z >= λ (например λ = 0)  0 ,      z < λ (unverified)
- x 1 -> ПОСТАНОВКА ЗАДАЧИ (unverified)
- x 1 -> 1,      z >= λ (например λ = 0)  0 ,      z < λ (unverified)
- x 3 -> 1,      z >= λ (например λ = 0)  0 ,      z < λ (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 1 (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- x 2 -> 1,      z >= λ (например λ = 0)  0 ,      z < λ (unverified)
- x 2 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 2 (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)

## Slide 12

Native text objects: 2; connectors: 0; embedded pictures: 2

- (0.6in, 0.3in) Функции активации
- (0.6in, 1.7in) import torch.nn.functional as F  F.sigmoid(x)

## Slide 13

Native text objects: 2; connectors: 0; embedded pictures: 2

- (0.6in, 0.3in) Функции активации
- (0.6in, 1.7in) import torch.nn.functional as F  F.tanh(x)

## Slide 14

Native text objects: 6; connectors: 0; embedded pictures: 3

- (0.6in, 0.3in) Функции активации
- (0.6in, 1.8in) import torch.nn.functional as F
- (2.4in, 3.1in) σ(z) = max(0, x)
- (0.6in, 3.1in) F.relu(x)
- (9.0in, 3.6in) leaky ReLu
- (0.6in, 5.6in) F.leaky_relu(x)

## Slide 15

Native text objects: 5; connectors: 0; embedded pictures: 3

- (0.6in, 0.3in) Функции активации
- (0.6in, 1.8in) import torch.nn.functional as F
- (2.4in, 3.1in) σ(x) = x
- (0.6in, 3.1in) F.linear(x)
- (0.6in, 5.6in) F.softmax(x)

## Slide 16

Native text objects: 1; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Функции потерь

## Slide 17

Native text objects: 15; connectors: 17; embedded pictures: 1

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (9.1in, 0.9in) X l = [x 1 , x 2 , … x l ] T
- (1.9in, 1.8in) x 1
- (9.3in, 1.6in) Y l = [y 1 , y 2 , … y m ] T
- (8.3in, 2.1in) y 1
- (1.8in, 3.0in) x 2
- (9.2in, 2.8in) t i = f(x i , ω)
- (8.3in, 3.5in) y 2
- (9.3in, 3.5in) L i (t i ,y i ) - функция потерь
- (1.8in, 4.1in) x 3
- (6.9in, 4.6in) σ 2 (z)
- (7.7in, 5.4in) Q(X l ; ω ) = 1/l ∑L i (t i , y i ; ω ) - показатель качества
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> σ 2 (z) (unverified)
- x 2 -> σ 2 (z) (unverified)
- x 1 -> ПОСТАНОВКА ЗАДАЧИ (unverified)
- x 1 -> σ 2 (z) (unverified)
- x 3 -> σ 2 (z) (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 1 (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- x 2 -> σ 2 (z) (unverified)
- x 2 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 2 (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)

## Slide 18

Native text objects: 15; connectors: 17; embedded pictures: 1

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (9.1in, 0.9in) X l = [x 1 , x 2 , … x l ] T
- (1.9in, 1.8in) x 1
- (9.3in, 1.6in) Y l = [y 1 , y 2 , … y m ] T
- (8.3in, 2.1in) y 1
- (1.8in, 3.0in) x 2
- (9.2in, 2.8in) t i = f(x i , ω)
- (8.3in, 3.5in) y 2
- (9.3in, 3.5in) L i (t i ,y i ) - функция потерь
- (1.8in, 4.1in) x 3
- (6.9in, 4.6in) σ 2 (z)
- (7.7in, 5.8in) O(N 2 )     O(K N)
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> σ 2 (z) (unverified)
- x 2 -> σ 2 (z) (unverified)
- x 1 -> ПОСТАНОВКА ЗАДАЧИ (unverified)
- x 1 -> σ 2 (z) (unverified)
- x 3 -> σ 2 (z) (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 1 (unverified)
- x 1 -> Сеть — это не один нейрон (unverified)
- x 2 -> σ 2 (z) (unverified)
- x 2 -> Сеть — это не один нейрон (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> y 2 (unverified)
- ПОСТАНОВКА ЗАДАЧИ -> σ 2 (z) (unverified)

## Slide 19

Native text objects: 22; connectors: 14; embedded pictures: 0

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Сеть — это не один нейрон
- (8.9in, 1.0in) Вход: обучающая выборка X l ; шаг обучения η Выход : вектров весовых коэффициентов ω инициализировать веса ω и по ним вычислить Q() Повторять: выбрать случайный
- (3.7in, 1.8in) ω 1 11
- (6.2in, 1.8in) ω 1 11
- (8.4in, 2.1in) y 1
- (1.7in, 2.4in) x 1
- (3.7in, 2.3in) ω 1 11
- (6.1in, 2.3in) ω 1 11
- (4.1in, 2.8in) ω 1 11
- (6.7in, 2.9in) ω 1 11
- (3.7in, 3.2in) ω 1 11
- (6.7in, 3.3in) ω 1 11
- (6.2in, 3.7in) ω 1 11
- (8.4in, 3.6in) y 2
- (1.8in, 4.0in) x 2
- (4.4in, 3.9in) ω 1 11
- (6.4in, 4.3in) ω 1 11
- (3.9in, 4.7in) ω 1 11
- (8.6in, 5.1in) Q(X l ; ω ) = 1/l ∑L i (x i , ω ) → min
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> ω 1 11 (unverified)
- x 2 -> ω 1 11 (unverified)
- x 1 -> ω 1 11 (unverified)
- x 1 -> ω 1 11 (unverified)
- x 1 -> ω 1 11 (unverified)
- x 1 -> ω 1 11 (unverified)

## Slide 20

Native text objects: 24; connectors: 14; embedded pictures: 0

- (0.6in, 0.3in) ПОСТАНОВКА ЗАДАЧИ
- (0.6in, 0.7in) Обратное распространение
- (3.7in, 1.8in) ω 1 11
- (6.2in, 1.8in) ω 2 11
- (1.7in, 2.4in) x 1
- (3.7in, 2.3in) ω 1 j 1
- (5.2in, 2.4in) …
- (5.6in, 2.4in) ω 2 1m
- (8.1in, 2.2in) y 1
- (4.1in, 2.8in) ω 1 1h
- (6.7in, 2.9in) ω 2 H1
- (7.1in, 3.0in) …
- (1.8in, 3.4in) …
- (3.7in, 3.2in) ω 1 jh
- (6.7in, 3.3in) ω 2 1m
- (6.2in, 3.7in) ω 1 hm
- (8.1in, 3.6in) y m
- (1.8in, 4.0in) x j
- (4.4in, 3.9in) ω 1 1H
- (5.2in, 3.8in) …
- (6.4in, 4.3in) ω 1 Hm
- (3.9in, 4.7in) ω 1 jH
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> ω 1 1H (unverified)
- x j -> ω 1 1H (unverified)
- x 1 -> ω 1 1h (unverified)
- x 1 -> ω 1 1H (unverified)
- ω 2 1m -> ω 2 11 (unverified)
- … -> ω 1 Hm (unverified)
- x 1 -> ω 1 1h (unverified)
- … -> ω 1 1H (unverified)
- ω 2 1m -> ω 1 hm (unverified)
- ω 2 1m -> ω 2 H1 (unverified)
- … -> ω 1 hm (unverified)
- ω 2 H1 -> y 1 (unverified)
- ω 2 1m -> ω 1 Hm (unverified)
- ω 2 1m -> y m (unverified)

## Slide 21

Native text objects: 9; connectors: 8; embedded pictures: 0

- (0.6in, 0.3in) Функции потерь
- (1.8in, 1.1in) f(x, y) = (x + y) 2 + 2xy
- (1.7in, 2.1in) x 1
- (4.1in, 2.0in) a = (x + y)
- (7.6in, 2.0in) a 2
- (9.5in, 2.9in) +
- (10.7in, 2.9in) f(x, y)
- (1.8in, 4.0in) x 2
- (4.0in, 3.8in) b = 2xy

### Possible connector endpoints (spatial inference)

- x 1 -> a = (x + y) (unverified)
- x 2 -> b = 2xy (unverified)
- x 1 -> b = 2xy (unverified)
- x 1 -> b = 2xy (unverified)
- a = (x + y) -> a 2 (unverified)
- a = (x + y) -> + (unverified)
- a 2 -> + (unverified)
- + -> f(x, y) (unverified)
