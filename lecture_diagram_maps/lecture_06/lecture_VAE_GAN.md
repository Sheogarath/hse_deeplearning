# lecture_06/lecture_VAE_GAN.pptx

Automatically inferred reading order and possible connections. **Connections are heuristic**, not verified semantic claims.

## Slide 1

Native text objects: 5; connectors: 7; embedded pictures: 0

- (0.6in, 1.6in) КУРС «НЕЙРОННЫЕ СЕТИ»
- (0.6in, 2.1in) Тема 6. Автоэнкодеры и генеративно состязательные сети
- (0.6in, 4.2in) Математическая основа нейросетей и связь с классическим машинным обучением
- (0.6in, 6.5in) Лекция 6 · Модуль 1
- (12.0in, 7.0in) 2/23

### Possible connector endpoints (spatial inference)


## Slide 2

Native text objects: 9; connectors: 125; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Решение: скрытый слой
- (0.2in, 3.4in) входной слой
- (10.0in, 3.4in) выходной слой
- (5.2in, 4.8in) вектор скрытого состояния
- (3.4in, 6.4in) кодер
- (6.8in, 6.5in) декодер
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- входной слой -> ВЫХОД ЕСТЬ (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- входной слой -> кодер (unverified)
- Тема 1 · Нейронные сети -> кодер (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- кодер -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- кодер -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- ВЫХОД ЕСТЬ -> вектор скрытого состояния (unverified)
- Решение: скрытый слой -> вектор скрытого состояния (unverified)
- Решение: скрытый слой -> вектор скрытого состояния (unverified)
- Решение: скрытый слой -> вектор скрытого состояния (unverified)
- Решение: скрытый слой -> вектор скрытого состояния (unverified)
- Решение: скрытый слой -> вектор скрытого состояния (unverified)
- Решение: скрытый слой -> вектор скрытого состояния (unverified)
- Решение: скрытый слой -> декодер (unverified)
- вектор скрытого состояния -> декодер (unverified)

## Slide 3

Native text objects: 13; connectors: 6; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Автоэнкодеры
- (3.8in, 2.4in) w 21
- (5.4in, 2.3in) y 1
- (1.7in, 2.5in) x 1
- (2.8in, 2.5in) w 11
- (5.4in, 3.3in) y 2
- (1.6in, 3.6in) x 2
- (2.8in, 3.6in) w 12
- (3.5in, 3.5in) h 1
- (4.0in, 3.8in) w 22
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- w 11 -> h 1 (unverified)
- w 11 -> w 12 (unverified)
- h 1 -> w 22 (unverified)

## Slide 4

Native text objects: 16; connectors: 6; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Автоэнкодеры
- (3.8in, 2.4in) w 21
- (5.4in, 2.3in) y 1
- (1.7in, 2.5in) x 1
- (2.8in, 2.5in) w 11
- (5.4in, 3.3in) y 2
- (1.6in, 3.6in) x 2
- (2.8in, 3.6in) w 12
- (3.5in, 3.5in) h 1
- (4.0in, 3.8in) w 22
- (2.1in, 4.5in) h 1 =  w 11 *x 1 + w 12 *x 2
- (2.1in, 5.5in) y 1 =  w 21 * h 1
- (2.1in, 6.2in) y 2 =  w 22 * h 2
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- w 11 -> h 1 (unverified)
- w 11 -> w 12 (unverified)
- h 1 -> w 22 (unverified)

## Slide 5

Native text objects: 21; connectors: 6; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Автоэнкодеры
- (7.5in, 1.8in) h 1 =  x 1 + x 2
- (9.6in, 1.8in) w 11 =  w 12 = 1
- (3.8in, 2.4in) w 21
- (5.4in, 2.3in) y 1
- (1.7in, 2.5in) x 1
- (2.8in, 2.5in) w 11
- (7.5in, 2.9in) y 1 =  0.5 * h 1
- (9.7in, 2.9in) w 21 =  w 22 = 0,5
- (5.4in, 3.3in) y 2
- (1.6in, 3.6in) x 2
- (2.8in, 3.6in) w 12
- (3.5in, 3.5in) h 1
- (7.5in, 3.5in) y 2 =  0.5 * h 2
- (4.0in, 3.8in) w 22
- (2.1in, 4.5in) h 1 =  w 11 *x 1 + w 12 *x 2
- (2.1in, 5.5in) y 1 =  w 21 * h 1
- (2.1in, 6.2in) y 2 =  w 22 * h 2
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- w 11 -> h 1 (unverified)
- w 11 -> w 12 (unverified)
- h 1 -> w 22 (unverified)

## Slide 6

Native text objects: 26; connectors: 15; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Автоэнкодеры
- (7.5in, 1.8in) h 1 =  x 1 + x 2
- (9.6in, 1.8in) w 11 =  w 12 = 1
- (3.8in, 2.4in) w 21
- (5.4in, 2.3in) y 1
- (1.7in, 2.5in) x 1
- (2.8in, 2.5in) w 11
- (7.5in, 2.9in) y 1 =  0.5 * h 1
- (9.7in, 2.9in) w 2 1 =  w 2 2 = 0,5
- (5.4in, 3.3in) y 2
- (1.6in, 3.6in) x 2
- (2.8in, 3.6in) w 12
- (3.5in, 3.5in) h 1
- (7.5in, 3.5in) y 2 =  0.5 * h 2
- (4.0in, 3.8in) w 22
- (2.1in, 4.5in) h 1 =  w 11 *x 1 + w 12 *x 2
- (7.2in, 5.2in) 2
- (2.1in, 5.5in) y 1 =  w 21 * h 1
- (7.2in, 5.7in) 1
- (9.0in, 5.5in) h 1  =  x 1 + x 2
- (2.1in, 6.2in) y 2 =  w 22 * h 2
- (7.9in, 6.3in) 1
- (8.3in, 6.3in) 2
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- w 11 -> h 1 (unverified)
- w 11 -> w 12 (unverified)
- h 1 -> w 22 (unverified)
- 2 -> 1 (unverified)
- 1 -> h 1  =  x 1 + x 2 (unverified)
- 1 -> 2 (unverified)

## Slide 7

Native text objects: 25; connectors: 15; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Автоэнкодеры
- (7.5in, 1.8in) h 1 =  x 1 + x 2
- (9.6in, 1.8in) w 11 =  w 12 = 1
- (3.8in, 2.4in) w 21
- (5.4in, 2.3in) y 1
- (1.7in, 2.5in) x 1
- (2.8in, 2.5in) w 11
- (7.5in, 2.9in) y 1 =  0.5 * h 1
- (5.4in, 3.3in) y 2
- (1.6in, 3.6in) x 2
- (2.8in, 3.6in) w 12
- (3.5in, 3.5in) h 1
- (7.5in, 3.5in) y 2 =  0.5 * h 2
- (4.0in, 3.8in) w 22
- (2.1in, 4.5in) h 1 =  w 11 *x 1 + w 12 *x 2
- (7.3in, 5.0in) 3
- (7.2in, 5.3in) 2
- (2.1in, 5.5in) y 1 =  w 21 * h 1
- (7.3in, 5.7in) 1
- (2.1in, 6.2in) y 2 =  w 22 * h 2
- (7.8in, 6.2in) 1
- (8.2in, 6.2in) 2
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- w 11 -> h 1 (unverified)
- w 11 -> w 12 (unverified)
- h 1 -> w 22 (unverified)
- 3 -> 1 (unverified)
- 1 -> 2 (unverified)
- 3 -> 2 (unverified)
- 3 -> 1 (unverified)

## Slide 8

Native text objects: 26; connectors: 84; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Решение: скрытый слой
- (1.9in, 1.3in) 784
- (7.6in, 1.5in) 128
- (8.7in, 1.3in) 784
- (3.2in, 1.6in) 128
- (4.4in, 1.9in) 64
- (6.5in, 1.8in) 64
- (5.4in, 2.2in) 28
- (0.2in, 3.4in) входной слой
- (5.5in, 3.3in) …
- (10.0in, 3.4in) выходной слой
- (6.6in, 3.7in) …
- (4.6in, 3.9in) …
- (3.4in, 4.2in) …
- (7.7in, 4.2in) …
- (2.0in, 4.7in) …
- (8.8in, 4.7in) …
- (5.2in, 4.8in) вектор скрытого состояния
- (11.2in, 5.2in) x,             x ≧ 0
- (9.8in, 5.6in) ELU(x)=
- (11.2in, 5.8in) α * (e x -1), x < 0
- (3.4in, 6.4in) кодер
- (6.8in, 6.5in) декодер
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- 784 -> 128 (unverified)
- 784 -> 128 (unverified)
- 784 -> 128 (unverified)
- 784 -> … (unverified)
- 784 -> … (unverified)
- 784 -> 128 (unverified)
- 784 -> … (unverified)
- 784 -> … (unverified)
- 784 -> … (unverified)
- входной слой -> … (unverified)
- входной слой -> … (unverified)
- 784 -> … (unverified)
- 784 -> … (unverified)
- 784 -> … (unverified)
- 784 -> … (unverified)
- 784 -> … (unverified)
- 784 -> … (unverified)
- 128 -> 64 (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> 64 (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 64 -> … (unverified)
- 64 -> … (unverified)
- 28 -> … (unverified)
- … -> вектор скрытого состояния (unverified)
- … -> вектор скрытого состояния (unverified)
- 28 -> … (unverified)
- 64 -> 128 (unverified)
- 64 -> … (unverified)
- 64 -> … (unverified)
- 64 -> … (unverified)
- 64 -> … (unverified)
- 64 -> … (unverified)
- 64 -> … (unverified)
- 128 -> 784 (unverified)
- 128 -> 784 (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> 784 (unverified)
- 128 -> 784 (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)
- 128 -> … (unverified)

## Slide 9

Native text objects: 19; connectors: 23; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Представление данных
- (2.0in, 1.5in) x 1
- (8.5in, 1.5in) x 1
- (2.5in, 2.1in) Изображения цифр
- (0.8in, 2.8in) x 784
- (7.2in, 2.7in) x 784
- (0.3in, 3.5in) x 783
- (6.8in, 3.5in) x 783
- (10.9in, 4.4in) x 2
- (4.5in, 4.4in) x 2
- (0.6in, 4.8in) …
- (7.1in, 4.8in) …
- (4.1in, 5.2in) модель изображений
- (10.6in, 5.2in) модель изображений
- (1.1in, 5.6in) x 3
- (7.5in, 5.6in) x 3
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- x 1 -> x 3 (unverified)
- … -> x 2 (unverified)
- x 784 -> x 2 (unverified)
- x 783 -> x 2 (unverified)
- x 783 -> x 3 (unverified)
- Изображения цифр -> x 2 (unverified)
- x 784 -> Изображения цифр (unverified)
- x 783 -> … (unverified)
- x 1 -> Изображения цифр (unverified)
- x 2 -> модель изображений (unverified)
- x 1 -> x 3 (unverified)
- … -> x 2 (unverified)
- x 784 -> x 2 (unverified)
- x 783 -> x 2 (unverified)
- x 783 -> x 3 (unverified)
- x 1 -> x 2 (unverified)
- x 784 -> x 2 (unverified)
- x 783 -> … (unverified)
- x 2 -> модель изображений (unverified)

## Slide 10

Native text objects: 20; connectors: 24; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Представление данных
- (2.0in, 1.5in) x 1
- (8.5in, 1.5in) x 1
- (2.5in, 2.1in) Изображения цифр
- (8.9in, 2.4in) прямая гомотопии
- (0.8in, 2.8in) x 784
- (7.2in, 2.7in) x 784
- (0.3in, 3.5in) x 783
- (6.8in, 3.5in) x 783
- (10.9in, 4.4in) x 2
- (4.5in, 4.4in) x 2
- (0.6in, 4.8in) …
- (7.1in, 4.8in) …
- (4.1in, 5.2in) модель изображений
- (10.6in, 5.2in) модель изображений
- (1.1in, 5.6in) x 3
- (7.5in, 5.6in) x 3
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- x 1 -> x 3 (unverified)
- … -> x 2 (unverified)
- x 784 -> x 2 (unverified)
- x 783 -> x 2 (unverified)
- x 783 -> x 3 (unverified)
- Изображения цифр -> x 2 (unverified)
- x 784 -> Изображения цифр (unverified)
- x 783 -> … (unverified)
- x 1 -> Изображения цифр (unverified)
- x 2 -> модель изображений (unverified)
- x 1 -> x 3 (unverified)
- … -> x 2 (unverified)
- x 784 -> x 2 (unverified)
- x 783 -> x 2 (unverified)
- x 783 -> x 3 (unverified)
- прямая гомотопии -> x 2 (unverified)
- x 784 -> прямая гомотопии (unverified)
- x 783 -> … (unverified)
- прямая гомотопии -> модель изображений (unverified)
- x 1 -> прямая гомотопии (unverified)

## Slide 11

Native text objects: 8; connectors: 4; embedded pictures: 1

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Вариационные автоэнкодеры (VAE)
- (9.2in, 1.7in) h 2
- (8.2in, 2.8in) μ 2
- (11.9in, 4.6in) h 1
- (10.8in, 4.8in) μ 1
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- h 2 -> μ 1 (unverified)
- μ 2 -> h 1 (unverified)
- h 2 -> μ 1 (unverified)
- μ 2 -> h 2 (unverified)

## Slide 12

Native text objects: 10; connectors: 4; embedded pictures: 1

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Вариационные автоэнкодеры (VAE)
- (9.2in, 1.7in) h 2
- (8.2in, 2.8in) μ 2
- (11.9in, 4.6in) h 1
- (10.8in, 4.8in) μ 1
- (1.6in, 5.9in) ω G (h 1 , h 2 , …)
- (8.2in, 5.9in) ω N (h 1 , h 2 , …)
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- h 2 -> ω N (h 1 , h 2 , …) (unverified)
- μ 2 -> h 1 (unverified)
- h 2 -> μ 1 (unverified)
- μ 2 -> h 2 (unverified)

## Slide 13

Native text objects: 19; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Вариационные автоэнкодеры (VAE)
- (6.0in, 2.4in) μ
- (11.7in, 2.7in) выходное изображение
- (0.1in, 3.3in) входное изображение
- (2.5in, 3.7in) Нейронная сеть
- (5.9in, 3.8in) σ h 2
- (8.5in, 3.9in) Нейронная сеть
- (8.6in, 3.9in) h
- (6.6in, 4.2in) x
- (7.7in, 4.2in) +
- (1.8in, 5.2in) …
- (10.7in, 5.2in) …
- (5.9in, 5.5in) Генератор нормальных СВ
- (8.6in, 6.4in) h = σ h  ⛒ N + μ
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (3.4in, 6.8in) кодер
- (6.8in, 6.9in) декодер
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- входное изображение -> Нейронная сеть (unverified)
- входное изображение -> Нейронная сеть (unverified)
- входное изображение -> Нейронная сеть (unverified)
- … -> Нейронная сеть (unverified)
- … -> Нейронная сеть (unverified)
- … -> кодер (unverified)
- σ h 2 -> x (unverified)
- x -> + (unverified)
- + -> Нейронная сеть (unverified)
- x -> Генератор нормальных СВ (unverified)
- μ -> + (unverified)

## Slide 14

Native text objects: 6; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Функция потерь
- (0.6in, 2.1in) class VAELoss(nn.Module): def forward(self, x, y, h_mean, h_log_var): img_loss = torch.sum(torch.square(x - y), dim=-1) kl_loss = -0.5 * torch.sum(1 + h_log_var
- (0.7in, 4.5in) x - тензор входных данных y - тензор выходных данных h_mean - мини-батч средних значений h_log_var - мини-батч логарифмов дисперсий
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

## Slide 15

Native text objects: 19; connectors: 13; embedded pictures: 1

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Вариационные автоэнкодеры (VAE)
- (6.0in, 1.7in) μ
- (11.7in, 2.1in) выходное изображение
- (0.1in, 2.6in) входное изображение
- (2.5in, 3.0in) Нейронная сеть
- (5.9in, 3.2in) σ h 2
- (8.5in, 3.3in) Нейронная сеть
- (8.6in, 3.2in) h
- (6.6in, 3.6in) x
- (7.7in, 3.6in) +
- (1.8in, 4.6in) …
- (10.7in, 4.6in) …
- (5.9in, 4.8in) Генератор нормальных СВ
- (8.6in, 5.8in) MSE = 1/N
- (3.4in, 6.3in) кодер
- (6.7in, 6.4in) декодер
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- входное изображение -> Нейронная сеть (unverified)
- входное изображение -> Нейронная сеть (unverified)
- входное изображение -> Нейронная сеть (unverified)
- … -> Нейронная сеть (unverified)
- … -> Нейронная сеть (unverified)
- … -> кодер (unverified)
- σ h 2 -> x (unverified)
- x -> + (unverified)
- + -> Нейронная сеть (unverified)
- x -> Генератор нормальных СВ (unverified)
- μ -> + (unverified)

## Slide 16

Native text objects: 4; connectors: 5; embedded pictures: 7

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Генеративно-состязательные сети (GAN)
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- ВЫХОД ЕСТЬ -> Тема 1 · Нейронные сети (unverified)
- ВЫХОД ЕСТЬ -> Тема 1 · Нейронные сети (unverified)
- ВЫХОД ЕСТЬ -> Генеративно-состязательные сети (GAN) (unverified)
- ВЫХОД ЕСТЬ -> Генеративно-состязательные сети (GAN) (unverified)

## Slide 17

Native text objects: 9; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Генеративно-состязательные сети (GAN)
- (6.2in, 2.3in) Сгенерированное изображение
- (2.2in, 2.8in) Генератор
- (9.9in, 2.6in) Дискриминатор
- (12.8in, 2.7in) y
- (0.2in, 2.8in) входной сигнал
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)


## Slide 18

Native text objects: 14; connectors: 1; embedded pictures: 6

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Генеративно-состязательные сети (GAN)
- (6.2in, 3.9in) Сгенерированное изображение
- (0.2in, 4.4in) входной сигнал
- (2.2in, 4.4in) Генератор
- (9.9in, 4.2in) Дискриминатор
- (12.8in, 4.3in) y
- (1.8in, 5.5in) real_out = y
- (10.3in, 5.6in) y = sigmoid(y)
- (1.8in, 6.3in) fake _out = y
- (10.3in, 6.1in) y > 0,5 -> real
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (10.3in, 6.8in) y ≤ 0,5 -> fake
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)


## Slide 19

Native text objects: 3; connectors: 0; embedded pictures: 2

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Генеративно-состязательные сети (GAN)
- (12.0in, 7.0in) 19/23

## Slide 20

Native text objects: 6; connectors: 0; embedded pictures: 4

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Генеративно-состязательные сети (GAN)
- (2.4in, 4.2in) -
- (4.6in, 4.2in) +
- (7.0in, 4.2in) =
- (12.0in, 7.0in) 19/23

## Slide 21

Native text objects: 13; connectors: 1; embedded pictures: 7

- (0.6in, 0.3in) ВЫХОД ЕСТЬ
- (0.6in, 0.7in) Генеративно-состязательные сети (GAN)
- (6.2in, 3.9in) Сгенерированное изображение
- (2.2in, 4.4in) Генератор
- (9.9in, 4.2in) Дискриминатор
- (12.8in, 4.3in) y
- (1.8in, 5.5in) real_out = y
- (10.3in, 5.6in) y = sigmoid(y)
- (1.8in, 6.3in) fake_out = y
- (10.3in, 6.1in) y > 0,5 -> real
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (10.3in, 6.8in) y ≤ 0,5 -> fake
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

