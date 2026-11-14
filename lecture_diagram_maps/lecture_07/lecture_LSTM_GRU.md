# lecture_07/lecture_LSTM_GRU.pptx

Automatically inferred reading order and possible connections. **Connections are heuristic**, not verified semantic claims.

## Slide 1

Native text objects: 3; connectors: 7; embedded pictures: 0

- (0.6in, 1.6in) КУРС «НЕЙРОННЫЕ СЕТИ»
- (0.6in, 2.1in) Тема 7. RNN, LSTM, GRU
- (0.6in, 6.5in) Лекция 7 · Модуль 1

### Possible connector endpoints (spatial inference)


## Slide 2

Native text objects: 11; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Сети прямого распространения
- (1.2in, 2.3in) x
- (3.7in, 2.3in) u
- (6.1in, 2.3in) o
- (8.6in, 2.3in) y
- (1.3in, 2.8in) Входной слой
- (3.7in, 2.9in) Скрытые слои
- (6.0in, 2.8in) Выходной слой
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

## Slide 3

Native text objects: 11; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Сети прямого распространения
- (1.2in, 2.3in) x
- (3.7in, 2.3in) u
- (6.1in, 2.3in) o
- (8.6in, 2.3in) y
- (1.3in, 2.8in) Входной слой
- (3.7in, 2.9in) Скрытые слои
- (6.0in, 2.8in) Выходной слой
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

## Slide 4

Native text objects: 9; connectors: 0; embedded pictures: 3

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Сети прямого распространения
- (10.4in, 1.1in) y 2
- (12.0in, 1.1in) y 3
- (8.7in, 1.2in) y 1
- (0.6in, 1.8in) x 1  Император x 2  Петр x 3 Великий
- (4.0in, 2.0in) Модель прямого распространения
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

## Slide 5

Native text objects: 17; connectors: 0; embedded pictures: 6

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Сети прямого распространения
- (10.4in, 1.1in) y 2
- (12.0in, 1.1in) y 3
- (8.7in, 1.2in) y 1
- (0.6in, 1.8in) x 1  Император x 2  Петр x 3 Великий
- (4.0in, 2.0in) Модель прямого распространения
- (8.7in, 3.7in) y 1
- (10.1in, 3.7in) y 2 | y 1
- (11.8in, 3.7in) y 3 | y 2 , y 1
- (0.6in, 4.5in) x 1  Император x 2  Петр x 3 Великий
- (3.8in, 4.7in) Модель
- (8.1in, 6.3in) Император
- (9.7in, 6.3in) Император Петр
- (11.5in, 6.3in) Император Петр Великий
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

## Slide 6

Native text objects: 7; connectors: 5; embedded pictures: 1

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Сети прямого распространения
- (1.3in, 2.1in) Император x 1   Петр x 2   Великий  x 3  …  0 x n  +1
- (11.8in, 2.2in) y
- (6.5in, 3.2in) Модель
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ -> Модель (unverified)
- Император x 1   Петр x 2   Великий  x 3  …  0 x n  +1 -> Модель (unverified)
- Император x 1   Петр x 2   Великий  x 3  …  0 x n  +1 -> Модель (unverified)
- Император x 1   Петр x 2   Великий  x 3  …  0 x n  +1 -> Модель (unverified)
- Император x 1   Петр x 2   Великий  x 3  …  0 x n  +1 -> Модель (unverified)

## Slide 7

Native text objects: 8; connectors: 2; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Способ обработки последовательностей
- (1.3in, 2.1in) x n  ,..., x 3, x 2, x 1   +1
- (6.5in, 3.2in) Модель
- (11.4in, 3.3in) y
- (1.4in, 4.7in) h k = f(x k , h k-1 )
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- x n  ,..., x 3, x 2, x 1   +1 -> Модель (unverified)
- x n  ,..., x 3, x 2, x 1   +1 -> Модель (unverified)

## Slide 8

Native text objects: 10; connectors: 2; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Способ обработки последовательностей
- (1.3in, 2.1in) x n  ,..., x 3, x 2, x 1   +1
- (6.5in, 3.2in) Модель
- (11.4in, 3.3in) y
- (1.4in, 4.7in) h k = f(x k , h k-1 )
- (6.8in, 5.0in) h k = (((x 1 + 0) α + x 2 ) α + x 3 )α = = α 3 x 1 + α 2 x 2 + αx 3
- (1.4in, 5.7in) h k = f(x k , h k-1 ) = α (x k , h k-1 )
- (0.6in, 7.0in) Тема 1 · Нейронные сети
- (12.0in, 7.0in) 19/23

### Possible connector endpoints (spatial inference)

- x n  ,..., x 3, x 2, x 1   +1 -> Модель (unverified)
- x n  ,..., x 3, x 2, x 1   +1 -> Модель (unverified)

## Slide 9

Native text objects: 39; connectors: 62; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Рекуррентная нейронная сеть
- (2.6in, 1.1in) h t-1
- (6.6in, 1.0in) h k = f(x k , h k-1 )
- (4.5in, 1.4in) z -1
- (1.7in, 1.8in) W
- (6.3in, 1.8in) V
- (0.3in, 2.1in) x 1
- (2.8in, 2.1in) ∑
- (4.2in, 2.2in) +
- (4.6in, 2.2in) σ(z)
- (8.7in, 2.3in) y 1
- (0.3in, 2.7in) x 2
- (6.6in, 2.6in) ∑
- (7.8in, 2.6in) s (z)
- (2.8in, 3.0in) ∑
- (4.0in, 3.0in) +
- (4.6in, 3.0in) σ(z)
- (0.3in, 3.3in) x 3
- (6.6in, 3.4in) ∑
- (8.7in, 3.2in) y 2
- (7.8in, 3.5in) s (z)
- (0.9in, 4.0in) …
- (2.8in, 3.9in) ∑
- (3.7in, 3.9in) +
- (4.6in, 3.9in) σ(z)
- (6.7in, 4.0in) …
- (0.3in, 4.2in) x n
- (8.7in, 4.2in) y m
- (2.9in, 4.5in) …
- (6.6in, 4.4in) ∑
- (7.8in, 4.5in) s (z)
- (0.3in, 5.0in) +1
- (2.8in, 5.0in) ∑
- (3.4in, 5.0in) +
- (4.6in, 5.1in) σ(z)
- (5.6in, 5.4in) +1
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> … (unverified)
- x 3 -> … (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- … -> ∑ (unverified)
- +1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- ∑ -> + (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- + -> σ(z) (unverified)
- + -> z -1 (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- σ(z) -> +1 (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> +1 (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> … (unverified)
- ∑ -> … (unverified)
- σ(z) -> ∑ (unverified)
- ∑ -> s (z) (unverified)
- ∑ -> s (z) (unverified)
- ∑ -> s (z) (unverified)
- z -1 -> + (unverified)
- z -1 -> + (unverified)
- h t-1 -> + (unverified)
- h t-1 -> + (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- s (z) -> y 1 (unverified)
- s (z) -> y 2 (unverified)
- s (z) -> y m (unverified)

## Slide 10

Native text objects: 41; connectors: 62; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Рекуррентная нейронная сеть
- (2.6in, 1.1in) h t-1
- (6.6in, 1.0in) h k = f(x k , h k-1 )
- (4.5in, 1.4in) z -1
- (1.7in, 1.8in) W
- (6.3in, 1.8in) V
- (0.3in, 2.1in) x 1
- (2.8in, 2.1in) ∑
- (4.2in, 2.2in) +
- (4.6in, 2.2in) σ(z)
- (8.7in, 2.3in) y 1
- (0.3in, 2.7in) x 2
- (6.6in, 2.6in) ∑
- (7.8in, 2.6in) s(z)
- (2.8in, 3.0in) ∑
- (4.0in, 3.0in) +
- (4.6in, 3.0in) σ(z)
- (0.3in, 3.3in) x 3
- (6.6in, 3.4in) ∑
- (8.7in, 3.2in) y 2
- (7.8in, 3.5in) s(z)
- (0.9in, 4.0in) …
- (2.8in, 3.9in) ∑
- (3.7in, 3.9in) +
- (4.6in, 3.9in) σ(z)
- (6.7in, 4.0in) …
- (0.3in, 4.2in) x n
- (8.7in, 4.2in) y m
- (2.9in, 4.5in) …
- (6.6in, 4.4in) ∑
- (7.8in, 4.5in) s(z)
- (0.3in, 5.0in) +1
- (2.8in, 5.0in) ∑
- (3.4in, 5.0in) +
- (4.6in, 5.1in) σ(z)
- (5.6in, 5.4in) +1
- (0.8in, 5.9in) a t = W x t + h t-1 + b
- (5.3in, 6.0in) h t = σ(a t )
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> … (unverified)
- x 3 -> … (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- … -> ∑ (unverified)
- +1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- ∑ -> + (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- + -> σ(z) (unverified)
- + -> z -1 (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- σ(z) -> +1 (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> +1 (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> … (unverified)
- ∑ -> … (unverified)
- σ(z) -> ∑ (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- z -1 -> + (unverified)
- z -1 -> + (unverified)
- h t-1 -> + (unverified)
- h t-1 -> + (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- s(z) -> y 1 (unverified)
- s(z) -> y 2 (unverified)
- s(z) -> y m (unverified)

## Slide 11

Native text objects: 42; connectors: 62; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Рекуррентная нейронная сеть
- (2.6in, 1.1in) h t-1
- (6.6in, 1.0in) h k = f(x k , h k-1 )
- (4.5in, 1.4in) z -1
- (1.7in, 1.8in) W
- (6.3in, 1.8in) V
- (0.3in, 2.1in) x 1
- (2.8in, 2.1in) ∑
- (4.2in, 2.2in) +
- (4.6in, 2.2in) σ(z)
- (8.7in, 2.3in) y 1
- (0.3in, 2.7in) x 2
- (6.6in, 2.6in) ∑
- (7.8in, 2.6in) s(z)
- (2.8in, 3.0in) ∑
- (4.0in, 3.0in) +
- (4.6in, 3.0in) σ(z)
- (0.3in, 3.3in) x 3
- (6.6in, 3.4in) ∑
- (8.7in, 3.2in) y 2
- (7.8in, 3.5in) s(z)
- (0.9in, 4.0in) …
- (2.8in, 3.9in) ∑
- (3.7in, 3.9in) +
- (4.6in, 3.9in) σ(z)
- (6.7in, 4.0in) …
- (0.3in, 4.2in) x n
- (8.7in, 4.2in) y m
- (2.9in, 4.5in) …
- (6.6in, 4.4in) ∑
- (7.8in, 4.5in) s(z)
- (0.3in, 5.0in) +1
- (2.8in, 5.0in) ∑
- (3.4in, 5.0in) +
- (4.6in, 5.1in) σ(z)
- (5.6in, 5.4in) +1
- (0.8in, 5.9in) a t = W x t + h t-1 + b
- (5.3in, 6.0in) h t = σ(a t )
- (8.0in, 6.0in) o t = V h t + c y t = s(o t )
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> … (unverified)
- x 3 -> … (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- … -> ∑ (unverified)
- +1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- ∑ -> + (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- + -> σ(z) (unverified)
- + -> z -1 (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- σ(z) -> +1 (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> +1 (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> … (unverified)
- ∑ -> … (unverified)
- σ(z) -> ∑ (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- z -1 -> + (unverified)
- z -1 -> + (unverified)
- h t-1 -> + (unverified)
- h t-1 -> + (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- s(z) -> y 1 (unverified)
- s(z) -> y 2 (unverified)
- s(z) -> y m (unverified)

## Slide 12

Native text objects: 43; connectors: 62; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Рекуррентная нейронная сеть
- (2.6in, 1.1in) h t-1
- (6.6in, 1.0in) h k = f(x k , h k-1 )
- (4.5in, 1.4in) z -1
- (1.7in, 1.8in) W
- (6.3in, 1.8in) V
- (0.3in, 2.1in) x 1
- (2.8in, 2.1in) ∑
- (4.2in, 2.2in) +
- (4.6in, 2.2in) σ(z)
- (8.7in, 2.3in) y 1
- (0.3in, 2.7in) x 2
- (6.6in, 2.6in) ∑
- (7.8in, 2.6in) s(z)
- (2.8in, 3.0in) ∑
- (4.0in, 3.0in) +
- (4.6in, 3.0in) σ(z)
- (0.3in, 3.3in) x 3
- (6.6in, 3.4in) ∑
- (8.7in, 3.2in) y 2
- (7.8in, 3.5in) s(z)
- (0.9in, 4.0in) …
- (2.8in, 3.9in) ∑
- (3.7in, 3.9in) +
- (4.6in, 3.9in) σ(z)
- (6.7in, 4.0in) …
- (0.3in, 4.2in) x n
- (8.7in, 4.2in) y m
- (2.9in, 4.5in) …
- (6.6in, 4.4in) ∑
- (7.8in, 4.5in) s(z)
- (0.3in, 5.0in) +1
- (2.8in, 5.0in) ∑
- (3.4in, 5.0in) +
- (4.6in, 5.1in) σ(z)
- (5.6in, 5.4in) +1
- (0.8in, 5.9in) a t = W x t + h t-1 + b
- (5.3in, 6.0in) h t = σ(a t )
- (8.0in, 6.0in) o t = V h t + c y t = s(o t )
- (3.8in, 6.7in) h 0 = [0, 0, 0, …, 0 n ]
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> … (unverified)
- x 3 -> … (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- … -> ∑ (unverified)
- +1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- ∑ -> + (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- + -> σ(z) (unverified)
- + -> z -1 (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- σ(z) -> +1 (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> +1 (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> … (unverified)
- ∑ -> … (unverified)
- σ(z) -> ∑ (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- z -1 -> + (unverified)
- z -1 -> + (unverified)
- h t-1 -> + (unverified)
- h t-1 -> + (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- s(z) -> y 1 (unverified)
- s(z) -> y 2 (unverified)
- s(z) -> y m (unverified)

## Slide 13

Native text objects: 51; connectors: 63; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Рекуррентная нейронная сеть
- (2.6in, 1.1in) h t-1
- (6.6in, 1.0in) h k = f(x k , h k-1 )
- (10.0in, 0.8in) h t-1
- (4.5in, 1.4in) z -1
- (10.5in, 1.4in) z -1
- (1.7in, 1.8in) W
- (6.3in, 1.8in) V
- (9.2in, 1.7in) x
- (11.4in, 1.6in) h t
- (12.7in, 1.6in) y t
- (0.3in, 2.1in) x 1
- (10.5in, 2.0in) RNN
- (11.9in, 2.0in) ∑
- (2.8in, 2.1in) ∑
- (4.2in, 2.2in) +
- (4.6in, 2.2in) σ(z)
- (8.3in, 2.3in) y 1
- (9.8in, 2.2in) +
- (0.3in, 2.7in) x 2
- (6.6in, 2.6in) ∑
- (7.4in, 2.6in) s(z)
- (2.8in, 3.0in) ∑
- (4.0in, 3.0in) +
- (4.6in, 3.0in) σ(z)
- (0.3in, 3.3in) x 3
- (6.6in, 3.4in) ∑
- (8.3in, 3.2in) y 2
- (7.4in, 3.5in) s(z)
- (0.9in, 4.0in) …
- (2.8in, 3.9in) ∑
- (3.7in, 3.9in) +
- (4.6in, 3.9in) σ(z)
- (6.7in, 4.0in) …
- (0.3in, 4.2in) x n
- (8.3in, 4.2in) y m
- (2.9in, 4.5in) …
- (6.6in, 4.4in) ∑
- (7.4in, 4.5in) s(z)
- (0.3in, 5.0in) +1
- (2.8in, 5.0in) ∑
- (3.4in, 5.0in) +
- (4.6in, 5.1in) σ(z)
- (5.6in, 5.4in) +1
- (0.8in, 5.9in) a t = W x t + h t-1 + b
- (5.3in, 6.0in) h t = σ(a t )
- (8.0in, 6.0in) o t = V h t + c y t = s(o t )
- (3.8in, 6.7in) h 0 = [0, 0, 0, …, 0 n ]
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> … (unverified)
- x 3 -> … (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- … -> ∑ (unverified)
- +1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- ∑ -> + (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- + -> σ(z) (unverified)
- + -> z -1 (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- σ(z) -> +1 (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> +1 (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> … (unverified)
- ∑ -> … (unverified)
- σ(z) -> ∑ (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- z -1 -> + (unverified)
- z -1 -> + (unverified)
- h t-1 -> + (unverified)
- h t-1 -> + (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- s(z) -> y 1 (unverified)
- s(z) -> y 2 (unverified)
- s(z) -> y m (unverified)
- z -1 -> h t (unverified)

## Slide 14

Native text objects: 56; connectors: 66; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Рекуррентная нейронная сеть
- (2.6in, 1.1in) h t-1
- (6.6in, 1.0in) h k = f(x k , h k-1 )
- (10.0in, 0.8in) h t-1
- (4.5in, 1.4in) z -1
- (10.5in, 1.4in) z -1
- (1.7in, 1.8in) W
- (6.3in, 1.8in) V
- (9.2in, 1.7in) x
- (11.4in, 1.6in) h t
- (12.7in, 1.6in) y t
- (0.3in, 2.1in) x 1
- (10.5in, 2.0in) RNN
- (11.9in, 2.0in) ∑
- (2.8in, 2.1in) ∑
- (4.2in, 2.2in) +
- (4.6in, 2.2in) σ(z)
- (8.3in, 2.3in) y 1
- (9.8in, 2.2in) +
- (0.3in, 2.7in) x 2
- (6.6in, 2.6in) ∑
- (7.4in, 2.6in) s(z)
- (2.8in, 3.0in) ∑
- (4.0in, 3.0in) +
- (4.6in, 3.0in) σ(z)
- (0.3in, 3.3in) x 3
- (6.6in, 3.4in) ∑
- (8.3in, 3.2in) y 2
- (7.4in, 3.5in) s(z)
- (0.9in, 4.0in) …
- (2.8in, 3.9in) ∑
- (3.7in, 3.9in) +
- (4.6in, 3.9in) σ(z)
- (6.7in, 4.0in) …
- (0.3in, 4.2in) x n
- (8.3in, 4.2in) y m
- (10.8in, 4.3in) h t
- (12.1in, 4.3in) y t
- (2.9in, 4.5in) …
- (6.6in, 4.4in) ∑
- (7.4in, 4.5in) s(z)
- (9.4in, 4.4in) x
- (9.9in, 4.7in) RNN
- (11.3in, 4.7in) ∑
- (0.3in, 5.0in) +1
- (2.8in, 5.0in) ∑
- (3.4in, 5.0in) +
- (4.6in, 5.1in) σ(z)
- (5.6in, 5.4in) +1
- (0.8in, 5.9in) a t = W x t + h t-1 + b
- (5.3in, 6.0in) h t = σ(a t )
- (8.0in, 6.0in) o t = V h t + c y t = s(o t )
- (3.8in, 6.7in) h 0 = [0, 0, 0, …, 0 n ]
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x 1 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> … (unverified)
- x 3 -> … (unverified)
- … -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- x 3 -> ∑ (unverified)
- … -> ∑ (unverified)
- +1 -> ∑ (unverified)
- … -> ∑ (unverified)
- x 2 -> ∑ (unverified)
- x 1 -> ∑ (unverified)
- ∑ -> + (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- + -> σ(z) (unverified)
- + -> z -1 (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- ∑ -> σ(z) (unverified)
- σ(z) -> +1 (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> σ(z) (unverified)
- z -1 -> +1 (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> ∑ (unverified)
- σ(z) -> … (unverified)
- ∑ -> … (unverified)
- σ(z) -> ∑ (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- ∑ -> s(z) (unverified)
- z -1 -> + (unverified)
- z -1 -> + (unverified)
- h t-1 -> + (unverified)
- h t-1 -> + (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- ∑ -> +1 (unverified)
- s(z) -> y 1 (unverified)
- s(z) -> y 2 (unverified)
- s(z) -> y m (unverified)
- z -1 -> h t (unverified)
- RNN -> ∑ (unverified)
- ∑ -> y t (unverified)

## Slide 15

Native text objects: 25; connectors: 19; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Развертка рекуррентной сети во времени
- (1.4in, 2.4in) y
- (4.6in, 2.5in) y 1
- (6.4in, 2.5in) y 2
- (9.6in, 2.5in) y t-1
- (11.4in, 2.5in) y t
- (1.2in, 3.3in) RNN
- (3.8in, 3.5in) h 0
- (4.6in, 3.5in) σ
- (5.5in, 3.5in) h 1
- (6.3in, 3.5in) σ
- (7.3in, 3.5in) h 2
- (8.0in, 3.5in) …
- (8.7in, 3.5in) h t-1
- (9.5in, 3.5in) σ
- (10.5in, 3.5in) h t
- (11.3in, 3.5in) σ
- (1.4in, 4.4in) x
- (4.6in, 4.4in) x 1
- (6.4in, 4.4in) x 2
- (9.6in, 4.4in) x t-1
- (11.4in, 4.4in) x t
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- RNN -> x (unverified)
- y -> RNN (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t-1 -> σ (unverified)
- σ -> x t-1 (unverified)
- y t-1 -> σ (unverified)
- σ -> h t (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t-1 (unverified)

## Slide 16

Native text objects: 40; connectors: 33; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектуры Many-to-One и One-to-Many
- (2.5in, 1.6in) y
- (11.1in, 1.7in) y
- (2.3in, 2.3in) RNN
- (4.6in, 2.6in) h 0
- (5.3in, 2.5in) σ
- (6.1in, 2.6in) h 1
- (6.8in, 2.5in) σ
- (7.6in, 2.5in) h 2
- (8.2in, 2.6in) …
- (8.8in, 2.6in) h t-1
- (9.5in, 2.5in) σ
- (10.4in, 2.6in) h t
- (11.1in, 2.5in) σ
- (2.5in, 3.3in) x
- (5.3in, 3.3in) x 1
- (6.8in, 3.3in) x 2
- (9.6in, 3.3in) x t-1
- (11.1in, 3.3in) x t
- (2.5in, 4.3in) y
- (5.3in, 4.3in) y 1
- (6.8in, 4.3in) y 2
- (9.5in, 4.3in) y t-1
- (11.1in, 4.3in) y t
- (2.3in, 5.0in) RNN
- (4.5in, 5.2in) h 0
- (5.2in, 5.2in) σ
- (6.0in, 5.2in) h 1
- (6.7in, 5.2in) σ
- (7.5in, 5.2in) h 2
- (8.1in, 5.2in) …
- (8.7in, 5.2in) h t-1
- (9.4in, 5.2in) σ
- (10.3in, 5.2in) h t
- (11.0in, 5.2in) σ
- (2.5in, 6.0in) x
- (5.3in, 6.0in) x 1
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- RNN -> x (unverified)
- y -> RNN (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- σ -> h 2 (unverified)
- h t-1 -> σ (unverified)
- σ -> x t-1 (unverified)
- σ -> h t (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t-1 (unverified)
- RNN -> x (unverified)
- y -> RNN (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t-1 -> σ (unverified)
- y t-1 -> σ (unverified)
- σ -> h t (unverified)
- h t -> σ (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t-1 (unverified)
- y -> x t (unverified)

## Slide 17

Native text objects: 5; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектуры рекуррентных сетей
- (1.1in, 2.0in) Many-to-Many - перевод текста  Many-to-One - анализ эмоциональной окраски текста (на входе текст, на выходе категория - положительный, нейтральный, отрицательны
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 18

Native text objects: 26; connectors: 19; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Развертка рекуррентной сети во времени
- (1.4in, 2.4in) y
- (4.6in, 2.5in) y 1
- (6.4in, 2.5in) y 2
- (9.6in, 2.5in) y t-1
- (11.4in, 2.5in) y t
- (1.2in, 3.3in) RNN
- (3.8in, 3.5in) h 0
- (4.6in, 3.5in) σ
- (5.5in, 3.5in) h 1
- (6.3in, 3.5in) σ
- (7.3in, 3.5in) h 2
- (8.0in, 3.5in) …
- (8.7in, 3.5in) h t-1
- (9.5in, 3.5in) σ
- (10.5in, 3.5in) h t
- (11.3in, 3.5in) σ
- (1.4in, 4.4in) x
- (4.6in, 4.4in) x 1
- (6.4in, 4.4in) x 2
- (9.6in, 4.4in) x t-1
- (11.4in, 4.4in) x t
- (2.8in, 6.1in) д
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- RNN -> x (unverified)
- y -> RNN (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t-1 -> σ (unverified)
- σ -> x t-1 (unverified)
- y t-1 -> σ (unverified)
- σ -> h t (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t-1 (unverified)

## Slide 19

Native text objects: 7; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Реализация рекуррентного слоя в PyTorch
- (0.6in, 2.6in) р, е, к, у, р, р, е, н
- (4.1in, 2.5in) RNN
- (6.3in, 2.6in) т
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 20

Native text objects: 17; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Реализация рекуррентного слоя в PyTorch
- (0.6in, 2.6in) р, е, к, у, р, р, е, н
- (4.1in, 2.5in) RNN
- (6.3in, 2.6in) т
- (3.5in, 3.4in) torch.nn. RNN
- (4.9in, 4.1in) h t-1
- (5.8in, 4.6in) z -1
- (4.1in, 4.9in) V
- (3.1in, 5.2in) W
- (7.1in, 5.3in) h t
- (2.3in, 5.6in) x t
- (5.6in, 5.6in) tanh
- (8.6in, 5.7in) y t
- (4.4in, 5.8in) +
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 21

Native text objects: 18; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Реализация рекуррентного слоя в PyTorch
- (0.6in, 2.6in) р, е, к, у, р, р, е, н
- (4.1in, 2.5in) RNN
- (6.3in, 2.6in) т
- (3.5in, 3.4in) torch.nn. RNN
- (9.5in, 3.6in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = h t
- (4.9in, 4.1in) h t-1
- (5.8in, 4.6in) z -1
- (4.1in, 4.9in) V
- (3.1in, 5.2in) W
- (7.1in, 5.3in) h t
- (2.3in, 5.6in) x t
- (5.6in, 5.6in) tanh
- (8.6in, 5.7in) y t
- (4.4in, 5.8in) +
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 22

Native text objects: 19; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Реализация рекуррентного слоя в PyTorch
- (7.1in, 1.8in) torch.nn .RNN( input_size , hidden_size , num_layers=1 ,  nonlinearity=’tanh’ , bias=True,  batch_first=False )
- (0.6in, 2.6in) р, е, к, у, р, р, е, н
- (4.1in, 2.5in) RNN
- (6.3in, 2.6in) т
- (3.5in, 3.4in) torch.nn. RNN
- (4.9in, 4.1in) h t-1
- (9.5in, 4.3in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = h t
- (5.8in, 4.6in) z -1
- (4.1in, 4.9in) V
- (3.1in, 5.2in) W
- (7.1in, 5.3in) h t
- (2.3in, 5.6in) x t
- (5.6in, 5.6in) tanh
- (8.6in, 5.7in) y t
- (4.4in, 5.8in) +
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 23

Native text objects: 16; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Реализация рекуррентного слоя в PyTorch
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (7.8in, 2.3in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = h t
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (0.6in, 5.0in) x t (seq_length, batch_size, d_sieze)  seq_length - длина подаваемой последовательности (число элементов) batch_size - размер батча d_size  - размер каждого под
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 24

Native text objects: 29; connectors: 14; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Исчезающие и взрывающиеся градиенты
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (8.3in, 2.3in) y 1
- (9.8in, 2.3in) y 2
- (12.6in, 2.3in) y t
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (7.5in, 3.2in) h 0
- (8.2in, 3.2in) σ
- (9.0in, 3.2in) h 1
- (9.7in, 3.2in) σ
- (10.6in, 3.2in) h 2
- (11.2in, 3.2in) …
- (11.9in, 3.2in) h t
- (12.6in, 3.2in) σ
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (8.3in, 4.0in) x 1
- (9.8in, 4.0in) x 2
- (12.6in, 3.9in) x t
- (1.6in, 4.9in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = h t
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t (unverified)

## Slide 25

Native text objects: 33; connectors: 14; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Исчезающие и взрывающиеся градиенты
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (8.3in, 2.3in) y 1
- (9.8in, 2.3in) y 2
- (12.6in, 2.3in) y t
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (7.5in, 3.2in) h 0
- (8.2in, 3.2in) σ
- (9.0in, 3.2in) h 1
- (9.7in, 3.2in) σ
- (10.6in, 3.2in) h 2
- (11.2in, 3.2in) …
- (11.9in, 3.2in) h t
- (12.6in, 3.2in) σ
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (8.3in, 4.0in) x 1
- (9.8in, 4.0in) x 2
- (12.6in, 3.9in) x t
- (1.6in, 4.9in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = h t
- (7.3in, 5.0in) LSTM, GRU
- (10.4in, 5.2in) δ j , | δ j | < λ
- (9.1in, 5.6in) δ j =
- (10.4in, 6.0in) λ , |δ j | ≥ λ
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t (unverified)

## Slide 26

Native text objects: 5; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (1.8in, 1.4in) Предыдущие символы
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 27

Native text objects: 5; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (1.8in, 1.4in) Предыдущие символы
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 28

Native text objects: 5; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (1.8in, 1.4in) Предыдущие символы
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 29

Native text objects: 5; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (2.7in, 1.4in) Предыдущие символы
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 30

Native text objects: 6; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (4.0in, 1.4in) Предыдущие символы
- (2.1in, 5.9in) Many-to-One
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

## Slide 31

Native text objects: 10; connectors: 2; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (4.0in, 1.4in) Предыдущие символы
- (7.7in, 3.8in) a: 0 б: 1 в: 2 … я: 32 ‘’: 33
- (9.3in, 4.3in) x t
- (10.8in, 4.3in) h t
- (9.9in, 4.4in) RNN
- (2.1in, 5.9in) Many-to-One
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- RNN -> h t (unverified)
- x t -> RNN (unverified)

## Slide 32

Native text objects: 16; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (4.0in, 1.4in) Предыдущие символы
- (8.9in, 3.0in) x t
- (11.3in, 3.0in) y t
- (6.3in, 3.5in) a: [1, 0, 0, …, 0]
- (6.3in, 3.9in) б : [0, 1, 0, …, 0]
- (6.3in, 4.5in) в : [0, 0, 1, …, 0]
- (9.9in, 4.4in) RNN
- (6.3in, 4.9in) …
- (8.9in, 5.3in) …
- (11.3in, 5.3in) …
- (2.1in, 5.9in) Many-to-One
- (6.5in, 6.4in) One Hot Encoding
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- x t -> RNN (unverified)
- x t -> RNN (unverified)
- … -> RNN (unverified)
- … -> RNN (unverified)
- y t -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- a: [1, 0, 0, …, 0] -> x t (unverified)
- б : [0, 1, 0, …, 0] -> x t (unverified)

## Slide 33

Native text objects: 15; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (3.3in, 1.5in) x t
- (5.7in, 1.5in) y t
- (0.7in, 1.9in) a: [1, 0, 0, …, 0]
- (0.6in, 2.4in) б: [0, 1, 0, …, 0]
- (0.6in, 2.9in) в: [0, 0, 1, …, 0]
- (4.3in, 2.9in) RNN
- (0.7in, 3.4in) …
- (9.8in, 3.7in) d _size
- (3.3in, 3.8in) …
- (5.6in, 3.8in) …
- (7.1in, 4.0in) batch_size
- (0.7in, 5.6in) x i (batch_size, seq_length, d_size)
- (5.6in, 5.7in) seq_length

### Possible connector endpoints (spatial inference)

- x t -> RNN (unverified)
- x t -> RNN (unverified)
- … -> RNN (unverified)
- … -> RNN (unverified)
- y t -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- a: [1, 0, 0, …, 0] -> x t (unverified)
- б: [0, 1, 0, …, 0] -> x t (unverified)

## Slide 34

Native text objects: 17; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Класс torch.nn.RNN
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (6.7in, 2.3in) rnn = nn.RNN(d_size, hidden_size, batch_first=True)
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (6.8in, 2.9in) x = torch.randn(8, 3, 33) y, h = rnn(x)
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (1.2in, 5.2in) x i (batch_size, seq_length, d_size)
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 35

Native text objects: 31; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Класс torch.nn.RNN
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (6.7in, 2.3in) rnn = nn.RNN(d_size, hidden_size, batch_first=True)
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (6.8in, 2.9in) x = torch.randn(8, 3, 33) y, h = rnn(x)
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (8.1in, 4.2in) y 1
- (9.7in, 4.2in) y 2
- (11.2in, 4.1in) y t
- (7.4in, 5.1in) h 0
- (8.1in, 5.0in) σ
- (8.9in, 5.1in) h 1
- (9.6in, 5.0in) σ
- (10.4in, 5.0in) h 2
- (11.1in, 5.0in) σ
- (11.9in, 5.0in) h 3
- (1.2in, 5.2in) x i (batch_size, seq_length, d_size)
- (6.8in, 5.5in) y t
- (8.1in, 5.8in) x 1
- (9.7in, 5.8in) x 2
- (11.2in, 5.8in) x t
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> σ (unverified)
- σ -> h 3 (unverified)

## Slide 36

Native text objects: 16; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Модель рекурентной нейронной сети
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (7.0in, 3.4in) U  Linear
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (2.7in, 3.8in) +
- (9.7in, 3.8in) y t
- (1.6in, 4.9in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = U h t + b y
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 37

Native text objects: 15; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Модель рекурентной нейронной сети
- (2.7in, 2.4in) h t-1
- (3.4in, 2.9in) z -1
- (1.2in, 3.4in) W
- (2.0in, 3.1in) V
- (4.5in, 3.4in) h t
- (5.8in, 3.5in) U  Linear
- (0.6in, 3.8in) x t
- (2.3in, 3.9in) +
- (3.3in, 3.8in) tanh
- (8.0in, 3.9in) y t
- (1.6in, 4.9in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = U h t + b y
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 38

Native text objects: 15; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (3.3in, 1.5in) x t
- (5.7in, 1.5in) y t
- (0.7in, 1.9in) a: [1, 0, 0, …, 0]
- (6.3in, 1.9in) class CharsDataset(data.Dataset): def __init__(self, prev_chars=3): self prev_chars = prev_chars  with open(path, ‘r’, encoding=’utf-8’) as f: self.text = f.rea
- (0.6in, 2.4in) б: [0, 1, 0, …, 0]
- (0.6in, 2.9in) в: [0, 0, 1, …, 0]
- (4.3in, 2.9in) RNN
- (0.7in, 3.4in) …
- (3.3in, 3.8in) …
- (4.4in, 4.1in) d_size
- (5.6in, 3.8in) …
- (1.7in, 4.5in) batch_size
- (0.2in, 6.1in) seq_length

### Possible connector endpoints (spatial inference)

- x t -> RNN (unverified)
- x t -> RNN (unverified)
- … -> RNN (unverified)
- … -> RNN (unverified)
- y t -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- RNN -> d_size (unverified)
- a: [1, 0, 0, …, 0] -> x t (unverified)
- б: [0, 1, 0, …, 0] -> x t (unverified)

## Slide 39

Native text objects: 19; connectors: 11; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Модель для прогноза слов
- (11.6in, 1.1in) y t
- (0.6in, 1.7in) машина : [1, 0, 0, …, 0]
- (7.2in, 1.9in) h t-1
- (0.6in, 2.1in) желтый : [0, 1, 0, …, 0]
- (7.9in, 2.3in) z -1
- (0.4in, 2.6in) дирижабль : [0, 0, 1, …, 0]
- (3.5in, 2.6in) Embedding
- (6.5in, 2.6in) V
- (5.8in, 2.8in) W
- (8.9in, 2.9in) h t
- (10.2in, 2.9in) U  Linear
- (6.8in, 3.3in) +
- (7.7in, 3.2in) tanh
- (3.5in, 3.5in) …
- (11.7in, 3.4in) …
- (1.0in, 3.9in) лес : [0, 0, 0, …, 1]
- (9.5in, 4.8in) e t = Emb* x t a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = U h t + b y

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- … -> Embedding (unverified)
- … -> Embedding (unverified)
- y t -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)

## Slide 40

Native text objects: 21; connectors: 11; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Модель для прогноза слов
- (11.6in, 1.2in) y t
- (0.6in, 1.7in) машина: [1, 0, 0, …, 0]
- (7.2in, 1.9in) h t-1
- (0.6in, 2.1in) желтый: [0, 1, 0, …, 0]
- (7.9in, 2.3in) z -1
- (0.4in, 2.6in) дирижабль: [0, 0, 1, …, 0]
- (3.5in, 2.6in) Embedding
- (6.5in, 2.6in) V
- (5.8in, 2.8in) W
- (8.9in, 2.9in) h t
- (10.2in, 2.9in) U  Linear
- (6.8in, 3.3in) +
- (7.7in, 3.2in) tanh
- (3.5in, 3.5in) …
- (11.7in, 3.4in) …
- (1.0in, 3.9in) лес: [0, 0, 0, …, 1]
- (0.7in, 4.9in) torch.nn .Embedding ( num_embeddings, embedding_dim, …)
- (9.5in, 4.8in) e t = Emb* x t a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = U h t + b y
- (0.7in, 5.6in) num_embedding - размер словаря  embedding_dim - размер вектора эмбедингов

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- … -> Embedding (unverified)
- … -> Embedding (unverified)
- y t -> … (unverified)
- y t -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)

## Slide 41

Native text objects: 18; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Модель для прогноза слов
- (11.6in, 1.2in) y t
- (0.6in, 1.7in) машина: [1, 0, 0, …, 0]
- (7.2in, 1.9in) h t-1
- (0.6in, 2.1in) желтый: [0, 1, 0, …, 0]
- (7.9in, 2.3in) z -1
- (0.4in, 2.6in) дирижабль: [0, 0, 1, …, 0]
- (3.5in, 2.6in) Embedding
- (6.5in, 2.6in) V
- (5.8in, 2.8in) W
- (8.9in, 2.9in) h t
- (10.2in, 2.9in) U  Linear
- (6.8in, 3.3in) +
- (7.7in, 3.2in) tanh
- (3.5in, 3.5in) …
- (11.7in, 3.4in) …
- (1.0in, 3.9in) лес: [0, 0, 0, …, 1]

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- … -> Embedding (unverified)
- … -> Embedding (unverified)
- y t -> … (unverified)
- y t -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)
- + -> tanh (unverified)

## Slide 42

Native text objects: 20; connectors: 11; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Модель для прогноза слов
- (11.6in, 1.2in) y t
- (0.6in, 1.7in) машина: [1, 0, 0, …, 0]
- (7.2in, 1.9in) h t-1
- (0.6in, 2.1in) желтый: [0, 1, 0, …, 0]
- (7.9in, 2.3in) z -1
- (0.4in, 2.6in) дирижабль: [0, 0, 1, …, 0]
- (3.5in, 2.6in) Embedding
- (6.5in, 2.6in) V
- (5.8in, 2.8in) W
- (8.9in, 2.9in) h t
- (10.2in, 2.9in) U  Linear
- (6.8in, 3.3in) +
- (7.7in, 3.2in) tanh
- (3.5in, 3.5in) …
- (11.7in, 3.4in) …
- (1.0in, 3.9in) лес: [0, 0, 0, …, 1]
- (2.6in, 4.3in) 300
- (0.0in, 5.6in) vocab_size

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- … -> Embedding (unverified)
- … -> Embedding (unverified)
- y t -> … (unverified)
- y t -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)
- U  Linear -> … (unverified)

## Slide 43

Native text objects: 15; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) Прогноз символов
- (0.6in, 0.7in) Формирование обучающей выборки
- (3.3in, 1.5in) x t
- (5.7in, 1.5in) y t
- (0.7in, 1.9in) a: [1, 0, 0, …, 0]
- (6.3in, 1.9in) class CharsDataset(data.Dataset): def __init__(self, prev_chars=3): self prev_chars = prev_chars  with open(path, ‘r’, encoding=’utf-8’) as f: self.text = f.rea
- (0.6in, 2.4in) б: [0, 1, 0, …, 0]
- (0.6in, 2.9in) в: [0, 0, 1, …, 0]
- (4.3in, 2.9in) RNN
- (0.7in, 3.4in) …
- (3.3in, 3.8in) …
- (4.4in, 4.1in) d_size
- (5.6in, 3.8in) …
- (1.7in, 4.5in) batch_size
- (0.2in, 6.1in) seq_length

### Possible connector endpoints (spatial inference)

- x t -> RNN (unverified)
- x t -> RNN (unverified)
- … -> RNN (unverified)
- … -> RNN (unverified)
- y t -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- RNN -> … (unverified)
- RNN -> d_size (unverified)
- a: [1, 0, 0, …, 0] -> x t (unverified)
- б: [0, 1, 0, …, 0] -> x t (unverified)

## Slide 44

Native text objects: 14; connectors: 1; embedded pictures: 1

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Исчезающие и взрывающиеся градиенты
- (3.2in, 2.1in) h t-1
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (1.6in, 4.9in) h t = tanh( W x t + V h t-1 + b x + b n  )  y = h t
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 45

Native text objects: 27; connectors: 14; embedded pictures: 1

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Исчезающие и взрывающиеся градиенты
- (3.2in, 2.1in) h t-1
- (8.3in, 2.3in) y 1
- (9.8in, 2.3in) y 2
- (12.6in, 2.3in) y t
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (7.5in, 3.2in) h 0
- (8.2in, 3.2in) σ
- (9.0in, 3.2in) h 1
- (9.7in, 3.2in) σ
- (10.6in, 3.2in) h 2
- (11.2in, 3.2in) …
- (11.9in, 3.2in) h t
- (12.6in, 3.2in) σ
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (8.3in, 4.0in) x 1
- (9.8in, 4.0in) x 2
- (12.6in, 3.9in) x t
- (1.6in, 4.9in) h t = tanh( W x t + V h t-1 + b x + b n  )  y = h t
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t (unverified)

## Slide 46

Native text objects: 28; connectors: 14; embedded pictures: 1

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Исчезающие и взрывающиеся градиенты
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (8.3in, 2.3in) y 1
- (9.8in, 2.3in) y 2
- (12.6in, 2.3in) y t
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (7.5in, 3.2in) h 0
- (8.2in, 3.2in) σ
- (9.0in, 3.2in) h 1
- (9.7in, 3.2in) σ
- (10.6in, 3.2in) h 2
- (11.2in, 3.2in) …
- (11.9in, 3.2in) h t
- (12.6in, 3.2in) σ
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (8.3in, 4.0in) x 1
- (9.8in, 4.0in) x 2
- (12.6in, 3.9in) x t
- (1.6in, 4.9in) h t = ReLU( W x t + V h t-1 + b x + b n  )  y = h t
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t (unverified)

## Slide 47

Native text objects: 28; connectors: 14; embedded pictures: 1

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Исчезающие и взрывающиеся градиенты
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (8.3in, 2.3in) y 1
- (9.8in, 2.3in) y 2
- (12.6in, 2.3in) y t
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (7.5in, 3.2in) h 0
- (8.2in, 3.2in) σ
- (9.0in, 3.2in) h 1
- (9.7in, 3.2in) σ
- (10.6in, 3.2in) h 2
- (11.2in, 3.2in) …
- (11.9in, 3.2in) h t
- (12.6in, 3.2in) σ
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (8.3in, 4.0in) x 1
- (9.8in, 4.0in) x 2
- (12.6in, 3.9in) x t
- (1.4in, 5.2in) h t = tanh( W x t + V h t-1 + b x + b n  )  y = h t
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t (unverified)

## Slide 48

Native text objects: 28; connectors: 14; embedded pictures: 1

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Исчезающие и взрывающиеся градиенты
- (0.6in, 1.5in) torch.nn .RNN( input_size , hidden_size , num_layers=1 , nonlinearity=’tanh’ , bias=True, batch_first=False )
- (3.2in, 2.1in) h t-1
- (8.3in, 2.3in) y 1
- (9.8in, 2.3in) y 2
- (12.6in, 2.3in) y t
- (4.1in, 2.6in) z -1
- (2.3in, 2.9in) V
- (1.4in, 3.2in) W
- (5.4in, 3.3in) h t
- (7.5in, 3.2in) h 0
- (8.2in, 3.2in) σ
- (9.0in, 3.2in) h 1
- (9.7in, 3.2in) σ
- (10.6in, 3.2in) h 2
- (11.2in, 3.2in) …
- (11.9in, 3.2in) h t
- (12.6in, 3.2in) σ
- (0.6in, 3.6in) x t
- (3.9in, 3.6in) tanh
- (6.9in, 3.7in) y t
- (2.7in, 3.8in) +
- (8.3in, 4.0in) x 1
- (9.8in, 4.0in) x 2
- (12.6in, 3.9in) x t
- (1.4in, 5.2in) h t = sigma( W x t + V h t-1 + b x + b n  )  y = h t
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)
- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- y 1 -> σ (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> x 2 (unverified)
- y 2 -> σ (unverified)
- σ -> h 2 (unverified)
- h t -> σ (unverified)
- σ -> x t (unverified)
- y t -> σ (unverified)
- h 2 -> … (unverified)
- … -> h t (unverified)

## Slide 49

Native text objects: 6; connectors: 1; embedded pictures: 5

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Задачи с известной последовательностью
- (0.6in, 1.5in) Продолжайте учиться. Трудности в конце концов создают сильных людей.  Пацаны ваще ребята, внатуре четко… Умеете, могете!
- (0.6in, 4.6in) Мне публично выступить? Что вы?! Это точно не мое!
- (0.6in, 5.4in) Чего тебе надо у меня дома?
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- Чего тебе надо у меня дома? -> 4/25 (unverified)

## Slide 50

Native text objects: 63; connectors: 42; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Двунаправленные (bidirectional) RNN
- (2.1in, 1.3in) y 1
- (4.3in, 1.3in) y 2
- (6.3in, 1.4in) …
- (8.0in, 1.3in) y t-1
- (10.0in, 1.3in) y t
- (2.0in, 2.1in) σ
- (4.2in, 2.1in) σ
- (8.0in, 2.1in) σ
- (10.0in, 2.1in) σ
- (2.7in, 2.4in) U
- (4.8in, 2.4in) U
- (8.6in, 2.4in) U
- (10.5in, 2.5in) U
- (1.6in, 2.8in) concat
- (3.8in, 2.8in) concat
- (6.3in, 2.9in) …
- (7.6in, 2.9in) concat
- (9.6in, 2.8in) concat
- (6.3in, 3.6in) V l
- (8.8in, 3.7in) V l
- (10.9in, 3.7in) V l
- (2.0in, 4.1in) σ
- (2.8in, 3.8in) V l
- (3.2in, 4.0in) g 2
- (4.2in, 4.1in) σ
- (4.8in, 3.8in) V l
- (5.3in, 4.0in) g 3
- (6.7in, 3.9in) g t-1
- (8.3in, 3.9in) σ
- (9.2in, 3.9in) g t
- (10.3in, 4.0in) σ
- (11.3in, 3.8in) g 0
- (6.1in, 4.1in) …
- (1.0in, 4.7in) V r
- (2.3in, 4.7in) W l
- (4.6in, 4.7in) W l
- (8.5in, 4.5in) W l
- (9.3in, 4.7in) V r
- (10.5in, 4.7in) W l
- (0.6in, 5.0in) h 0
- (1.6in, 5.0in) σ
- (2.8in, 5.0in) h 1
- (3.3in, 4.8in) V r
- (3.7in, 5.0in) σ
- (4.8in, 5.1in) h 2
- (5.2in, 4.8in) V r
- (6.0in, 5.0in) …
- (6.8in, 5.0in) h t-2
- (7.3in, 4.8in) V r
- (7.7in, 5.0in) σ
- (8.6in, 5.1in) h t-1
- (9.7in, 5.0in) σ
- (7.4in, 5.4in) W r
- (0.9in, 5.4in) W r
- (3.1in, 5.4in) W r
- (9.2in, 5.5in) W r
- (1.3in, 5.8in) x 1
- (3.6in, 5.8in) x 2
- (7.8in, 5.8in) x t-1
- (9.6in, 5.8in) x t
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> h 2 (unverified)
- h t-2 -> σ (unverified)
- … -> h t-2 (unverified)
- σ -> x 1 (unverified)
- σ -> concat (unverified)
- y 1 -> σ (unverified)
- concat -> σ (unverified)
- σ -> concat (unverified)
- y 2 -> σ (unverified)
- concat -> σ (unverified)
- h 2 -> V r (unverified)
- σ -> x 2 (unverified)
- σ -> x 2 (unverified)
- g 2 -> σ (unverified)
- σ -> g 2 (unverified)
- σ -> g 3 (unverified)
- h t-1 -> σ (unverified)
- concat -> σ (unverified)
- σ -> x t (unverified)
- σ -> x t (unverified)
- g t -> σ (unverified)
- σ -> g t (unverified)
- σ -> g 0 (unverified)
- σ -> x t-1 (unverified)
- σ -> x t-1 (unverified)
- g t-1 -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- y t-1 -> σ (unverified)
- σ -> concat (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- y t -> σ (unverified)
- σ -> concat (unverified)
- concat -> σ (unverified)
- σ -> h t-1 (unverified)
- g 3 -> … (unverified)
- … -> g t-1 (unverified)

## Slide 51

Native text objects: 63; connectors: 42; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (8.6in, 0.2in) h t = sigma( W r x t + V r h t-1 + b x + b n  )  g t = sigma(W l x l + V l g t-1 + b x l + b x l  )  o t = [h t , g t ] y t = sigma(U * o t + b y )
- (0.6in, 0.7in) Двунаправленные (bidirectional) RNN
- (1.6in, 2.3in) y 1
- (3.8in, 2.3in) y 2
- (5.8in, 2.4in) …
- (7.6in, 2.3in) y t-1
- (9.6in, 2.3in) y t
- (1.6in, 3.1in) σ
- (3.8in, 3.1in) σ
- (7.5in, 3.1in) σ
- (9.6in, 3.1in) σ
- (2.2in, 3.4in) U
- (4.4in, 3.4in) U
- (8.1in, 3.4in) U
- (10.1in, 3.4in) U
- (1.2in, 3.8in) concat
- (3.4in, 3.8in) concat
- (5.8in, 3.9in) …
- (7.1in, 3.8in) concat
- (9.1in, 3.8in) concat
- (5.8in, 4.6in) V l
- (8.3in, 4.7in) V l
- (10.4in, 4.7in) V l
- (1.6in, 5.1in) σ
- (2.3in, 4.8in) V l
- (2.7in, 5.0in) g 2
- (3.8in, 5.1in) σ
- (4.4in, 4.8in) V l
- (4.8in, 5.0in) g 3
- (6.3in, 4.9in) g t-1
- (7.8in, 4.9in) σ
- (8.8in, 4.8in) g t
- (9.8in, 4.9in) σ
- (10.9in, 4.8in) g 0
- (5.7in, 5.1in) …
- (0.5in, 5.7in) V r
- (1.8in, 5.6in) W l
- (4.1in, 5.7in) W l
- (8.1in, 5.5in) W l
- (8.9in, 5.7in) V r
- (10.1in, 5.7in) W l
- (0.1in, 6.0in) h 0
- (1.1in, 6.0in) σ
- (2.3in, 6.0in) h 1
- (2.8in, 5.8in) V r
- (3.2in, 6.0in) σ
- (4.3in, 6.0in) h 2
- (4.7in, 5.8in) V r
- (5.6in, 6.0in) …
- (6.3in, 6.0in) h t-2
- (6.9in, 5.8in) V r
- (7.3in, 6.0in) σ
- (8.2in, 6.0in) h t-1
- (9.3in, 6.0in) σ
- (6.9in, 6.4in) W r
- (0.4in, 6.4in) W r
- (2.7in, 6.4in) W r
- (8.7in, 6.4in) W r
- (0.8in, 6.8in) x 1
- (3.1in, 6.8in) x 2
- (7.3in, 6.8in) x t-1
- (9.1in, 6.8in) x t

### Possible connector endpoints (spatial inference)

- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> h 2 (unverified)
- h t-2 -> σ (unverified)
- … -> h t-2 (unverified)
- σ -> x 1 (unverified)
- σ -> concat (unverified)
- y 1 -> σ (unverified)
- concat -> σ (unverified)
- σ -> concat (unverified)
- y 2 -> σ (unverified)
- concat -> σ (unverified)
- h 2 -> V r (unverified)
- σ -> x 2 (unverified)
- σ -> x 2 (unverified)
- g 2 -> σ (unverified)
- σ -> g 2 (unverified)
- σ -> g 3 (unverified)
- h t-1 -> σ (unverified)
- concat -> σ (unverified)
- σ -> x t (unverified)
- σ -> x t (unverified)
- g t -> σ (unverified)
- σ -> g t (unverified)
- σ -> g 0 (unverified)
- σ -> x t-1 (unverified)
- σ -> x t-1 (unverified)
- g t-1 -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- y t-1 -> σ (unverified)
- σ -> concat (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- y t -> σ (unverified)
- σ -> concat (unverified)
- concat -> σ (unverified)
- σ -> h t-1 (unverified)
- g 3 -> … (unverified)
- … -> g t-1 (unverified)

## Slide 52

Native text objects: 50; connectors: 34; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Двунаправленные (bidirectional) RNN
- (1.1in, 1.3in) torch.nn . RNN (input_size, hidden_size, batch_first=True, bidirectional=True , …)  rnn = nn.RNN(input_size, hidden_size, batch_first=True, bidirectional=True) 
- (1.2in, 3.8in) concat
- (3.4in, 3.8in) concat
- (5.8in, 3.9in) …
- (7.1in, 3.8in) concat
- (9.1in, 3.8in) concat
- (5.8in, 4.6in) V l
- (8.3in, 4.7in) V l
- (10.4in, 4.7in) V l
- (1.6in, 5.1in) σ
- (2.3in, 4.8in) V l
- (2.7in, 5.0in) g 2
- (3.8in, 5.1in) σ
- (4.4in, 4.8in) V l
- (4.8in, 5.0in) g 3
- (6.3in, 4.9in) g t-1
- (7.8in, 4.9in) σ
- (8.8in, 4.8in) g t
- (9.8in, 4.9in) σ
- (10.9in, 4.8in) g 0
- (5.7in, 5.1in) …
- (0.5in, 5.7in) V r
- (1.8in, 5.6in) W l
- (4.1in, 5.7in) W l
- (8.1in, 5.5in) W l
- (8.9in, 5.7in) V r
- (10.1in, 5.7in) W l
- (0.1in, 6.0in) h 0
- (1.1in, 6.0in) σ
- (2.3in, 6.0in) h 1
- (2.8in, 5.8in) V r
- (3.2in, 6.0in) σ
- (4.3in, 6.0in) h 2
- (4.7in, 5.8in) V r
- (5.6in, 6.0in) …
- (6.3in, 6.0in) h t-2
- (6.9in, 5.8in) V r
- (7.3in, 6.0in) σ
- (8.2in, 6.0in) h t-1
- (9.3in, 6.0in) σ
- (6.9in, 6.4in) W r
- (0.4in, 6.4in) W r
- (2.7in, 6.4in) W r
- (8.7in, 6.4in) W r
- (0.8in, 6.8in) x 1
- (3.1in, 6.8in) x 2
- (7.3in, 6.8in) x t-1
- (9.1in, 6.8in) x t

### Possible connector endpoints (spatial inference)

- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> h 2 (unverified)
- h t-2 -> σ (unverified)
- … -> h t-2 (unverified)
- σ -> x 1 (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- h 2 -> V r (unverified)
- σ -> x 2 (unverified)
- σ -> x 2 (unverified)
- g 2 -> σ (unverified)
- σ -> g 2 (unverified)
- σ -> g 3 (unverified)
- h t-1 -> σ (unverified)
- concat -> σ (unverified)
- σ -> x t (unverified)
- σ -> x t (unverified)
- g t -> σ (unverified)
- σ -> g t (unverified)
- σ -> g 0 (unverified)
- σ -> x t-1 (unverified)
- σ -> x t-1 (unverified)
- g t-1 -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- σ -> h t-1 (unverified)
- g 3 -> … (unverified)
- … -> g t-1 (unverified)

## Slide 53

Native text objects: 54; connectors: 38; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Модель RNN-сети для сентимент-анализа
- (7.8in, 1.3in) y
- (6.9in, 1.9in) Linear
- (6.9in, 2.4in) concat
- (6.8in, 2.8in) g l
- (8.3in, 2.8in) h t
- (2.0in, 3.3in) concat
- (4.2in, 3.4in) concat
- (6.6in, 3.4in) …
- (7.9in, 3.4in) concat
- (10.0in, 3.4in) concat
- (3.1in, 4.3in) V l
- (5.2in, 4.3in) V l
- (6.6in, 4.1in) V l
- (7.1in, 4.4in) g t-1
- (9.1in, 4.2in) V l
- (9.6in, 4.4in) g t
- (11.2in, 4.2in) V l
- (11.7in, 4.3in) g 0
- (2.4in, 4.6in) σ
- (3.5in, 4.5in) g 2
- (4.6in, 4.6in) σ
- (5.6in, 4.5in) g 3
- (6.5in, 4.6in) …
- (8.6in, 4.5in) σ
- (10.6in, 4.5in) σ
- (8.9in, 5.0in) W l
- (1.3in, 5.2in) V r
- (2.6in, 5.2in) W lя
- (3.6in, 5.3in) V r
- (4.9in, 5.2in) W l
- (5.5in, 5.3in) V r
- (7.7in, 5.3in) V r
- (9.7in, 5.2in) V r
- (10.9in, 5.3in) W l
- (0.9in, 5.6in) h 0
- (1.9in, 5.5in) σ
- (3.1in, 5.6in) h 1
- (4.0in, 5.5in) σ
- (5.1in, 5.6in) h 2
- (6.4in, 5.6in) …
- (7.1in, 5.6in) h t-2
- (8.1in, 5.5in) σ
- (9.0in, 5.6in) h t-1
- (10.1in, 5.6in) σ
- (1.2in, 5.9in) W r
- (3.5in, 5.9in) W r
- (7.7in, 5.9in) W r
- (9.5in, 6.0in) W r
- (1.6in, 6.3in) x 1
- (3.9in, 6.3in) x 2
- (8.1in, 6.3in) x t-1
- (10.0in, 6.3in) x t

### Possible connector endpoints (spatial inference)

- h 0 -> σ (unverified)
- σ -> x 1 (unverified)
- σ -> h 1 (unverified)
- h 1 -> σ (unverified)
- σ -> h 2 (unverified)
- h t-2 -> σ (unverified)
- … -> h t-2 (unverified)
- σ -> x 1 (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- h 2 -> V r (unverified)
- σ -> x 2 (unverified)
- σ -> x 2 (unverified)
- g 2 -> σ (unverified)
- σ -> g 2 (unverified)
- σ -> g 3 (unverified)
- h t-1 -> σ (unverified)
- concat -> σ (unverified)
- σ -> x t (unverified)
- σ -> x t (unverified)
- g t -> σ (unverified)
- σ -> g t (unverified)
- σ -> g 0 (unverified)
- σ -> x t-1 (unverified)
- σ -> x t-1 (unverified)
- g t-1 -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- concat -> σ (unverified)
- σ -> h t-1 (unverified)
- g 3 -> … (unverified)
- … -> g t-1 (unverified)
- Linear -> concat (unverified)
- y -> Linear (unverified)

## Slide 54

Native text objects: 5; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Формат обучающей выборки
- (5.7in, 1.5in) seq_lenght
- (-0.3in, 3.1in) batch_Size
- (1.3in, 6.9in) ,,,

## Slide 55

Native text objects: 15; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Простой RNN-слой
- (3.2in, 1.5in) h t-1
- (7.2in, 1.7in) Я очень люблю программировать , …, поэтому в будущем хочу стать программистом.
- (4.1in, 2.0in) z -1
- (2.3in, 2.4in) V
- (1.4in, 2.7in) W
- (5.4in, 2.7in) h t
- (0.6in, 3.1in) x t
- (3.9in, 3.1in) tanh
- (2.7in, 3.3in) +
- (6.9in, 3.1in) y t
- (1.5in, 4.7in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = h t
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 56

Native text objects: 16; connectors: 1; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Простой RNN-слой
- (3.2in, 1.5in) h t-1
- (7.1in, 1.7in) Я очень люблю программировать , …, поэтому в будущем хочу стать программистом.
- (4.1in, 2.0in) z -1
- (2.3in, 2.4in) V
- (1.4in, 2.7in) W
- (5.4in, 2.7in) h t
- (0.6in, 3.1in) x t
- (3.9in, 3.1in) tanh
- (2.7in, 3.3in) +
- (6.9in, 3.1in) y t
- (1.5in, 4.7in) a = W x t + V h t-1 + b x + b n  h t = tanh(a t )  y = h t
- (6.3in, 5.2in) LSTM (Long Short-Term Memory) - долга краткосрочная память
- (0.6in, 7.0in) Тема 2 · Backprop и PyTorch
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- z -1 -> h t (unverified)

## Slide 57

Native text objects: 17; connectors: 9; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  LSTM
- (7.0in, 1.9in) h t
- (1.2in, 2.9in) C t-1
- (3.1in, 3.1in) x
- (4.9in, 3.0in) +
- (7.9in, 2.9in) C t
- (6.7in, 3.4in) tanh
- (4.9in, 3.8in) x
- (6.8in, 3.9in) x
- (3.0in, 4.2in) σ
- (4.0in, 4.2in) σ
- (4.9in, 4.2in) tanh
- (5.7in, 4.2in) σ
- (1.6in, 4.6in) h t-1
- (8.2in, 4.5in) h t
- (3.3in, 5.8in) x t

### Possible connector endpoints (spatial inference)

- C t-1 -> C t (unverified)
- + -> tanh (unverified)
- x -> σ (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t -> x (unverified)

## Slide 58

Native text objects: 17; connectors: 11; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  LSTM
- (2.5in, 1.7in) забывание ненужного
- (4.6in, 1.6in) запоминание нового
- (7.0in, 1.9in) h t
- (1.2in, 2.9in) C t-1
- (3.1in, 3.1in) x
- (4.9in, 3.0in) +
- (7.9in, 2.9in) C t
- (6.7in, 3.4in) tanh
- (4.9in, 3.8in) x
- (6.8in, 3.9in) x
- (3.0in, 4.2in) σ
- (4.0in, 4.2in) σ
- (4.9in, 4.2in) tanh
- (5.7in, 4.2in) σ
- (3.3in, 5.8in) x t

### Possible connector endpoints (spatial inference)

- + -> tanh (unverified)
- x -> σ (unverified)
- σ -> x t (unverified)
- h t -> x (unverified)
- C t-1 -> C t (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)

## Slide 59

Native text objects: 21; connectors: 12; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  LSTM
- (2.5in, 1.7in) забывание ненужного
- (4.6in, 1.6in) запоминание нового
- (7.0in, 1.9in) h t
- (1.2in, 2.9in) C t-1
- (3.1in, 3.1in) x
- (4.9in, 3.0in) +
- (7.9in, 2.9in) C t
- (6.7in, 3.4in) tanh
- (2.9in, 3.7in) f t
- (4.9in, 3.8in) x
- (6.8in, 3.9in) x
- (3.0in, 4.2in) σ
- (4.0in, 4.2in) σ
- (4.9in, 4.2in) tanh
- (5.7in, 4.2in) σ
- (1.6in, 4.6in) h t-1
- (3.3in, 5.8in) x t
- (5.2in, 6.7in) f t = [0, 2; 0, 3; 0, 9; 0, 1; 0, 5,...] T
- (1.8in, 6.8in) f t = σ ( W f  [ h t-1 , x t ] + b f )

### Possible connector endpoints (spatial inference)

- + -> tanh (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t -> x (unverified)
- C t-1 -> C t (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)
- x -> σ (unverified)
- h t-1 -> σ (unverified)

## Slide 60

Native text objects: 41; connectors: 29; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  LSTM
- (1.3in, 2.0in) забывание ненужного
- (3.1in, 1.9in) запоминание нового
- (7.9in, 2.0in) забывание ненужного
- (9.7in, 2.0in) запоминание нового
- (5.1in, 2.2in) h t
- (11.7in, 2.2in) h t
- (0.2in, 3.0in) C t-1
- (5.8in, 3.0in) C t
- (6.9in, 3.0in) C t-1
- (12.5in, 3.0in) C t
- (1.8in, 3.1in) x
- (3.4in, 3.1in) +
- (4.8in, 3.4in) tanh
- (8.5in, 3.2in) x
- (10.0in, 3.2in) +
- (1.7in, 3.7in) f t
- (3.4in, 3.7in) x
- (9.2in, 3.6in) f t
- (10.4in, 3.7in) С t
- (11.5in, 3.4in) tanh
- (4.9in, 3.9in) x
- (10.0in, 3.8in) x
- (11.6in, 3.9in) x
- (1.7in, 4.1in) σ
- (2.6in, 4.1in) σ
- (3.3in, 4.1in) tanh
- (4.0in, 4.1in) σ
- (8.4in, 4.2in) σ
- (9.2in, 4.2in) σ
- (10.0in, 4.2in) tanh
- (10.7in, 4.2in) σ
- (0.5in, 4.5in) h t-1
- (7.2in, 4.5in) h t-1
- (2.0in, 5.4in) x t
- (8.6in, 5.5in) x t
- (0.7in, 6.3in) f t = σ ( W f  [ h t-1 , x t ] + b f )
- (3.3in, 6.3in) f t = [0, 2; 0, 3; 0, 9; 0, 1; 0, 5,...] T
- (6.9in, 6.3in) i t = σ ( W p  [ h t-1 , x t ] + b fi )
- (9.7in, 6.4in) C t = tanh ( W C  [ h t-1 , x t ] + b C )

### Possible connector endpoints (spatial inference)

- + -> tanh (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t -> x (unverified)
- C t-1 -> C t (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)
- x -> σ (unverified)
- h t-1 -> σ (unverified)
- Архитектура  LSTM -> f t = [0, 2; 0, 3; 0, 9; 0, 1; 0, 5,...] T (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t -> x (unverified)
- x -> σ (unverified)
- h t-1 -> σ (unverified)
- C t-1 -> C t (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)
- + -> tanh (unverified)
- h t-1 -> σ (unverified)
- h t-1 -> tanh (unverified)
- h t-1 -> x t (unverified)
- h t-1 -> x t (unverified)

## Slide 61

Native text objects: 43; connectors: 29; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  LSTM
- (1.3in, 2.0in) забывание ненужного
- (3.1in, 1.9in) запоминание нового
- (7.9in, 2.0in) забывание ненужного
- (9.7in, 2.0in) запоминание нового
- (5.1in, 2.2in) h t
- (11.7in, 2.2in) h t
- (0.2in, 3.0in) C t-1
- (5.8in, 3.0in) C t
- (6.9in, 3.0in) C t-1
- (12.5in, 3.0in) C t
- (1.8in, 3.1in) x
- (3.4in, 3.1in) +
- (4.8in, 3.4in) tanh
- (8.5in, 3.2in) x
- (10.0in, 3.2in) +
- (1.7in, 3.7in) f t
- (3.4in, 3.7in) x
- (9.2in, 3.6in) i t
- (10.4in, 3.7in) С t
- (11.5in, 3.4in) tanh
- (4.9in, 3.9in) x
- (10.0in, 3.8in) x
- (11.6in, 3.9in) x
- (1.7in, 4.1in) σ
- (2.6in, 4.1in) σ
- (3.3in, 4.1in) tanh
- (4.0in, 4.1in) σ
- (8.4in, 4.2in) σ
- (9.2in, 4.2in) σ
- (10.0in, 4.2in) tanh
- (10.7in, 4.2in) σ
- (0.5in, 4.5in) h t-1
- (7.2in, 4.5in) h t-1
- (2.0in, 5.4in) x t
- (8.6in, 5.5in) x t
- (0.7in, 6.3in) f t = σ ( W f  [ h t-1 , x t ] + b f )
- (3.3in, 6.3in) f t = [0, 2; 0, 3; 0, 9; 0, 1; 0, 5,...] T
- (6.9in, 6.3in) i t = σ ( W p  [ h t-1 , x t ] + b fi )
- (9.9in, 6.4in) C t = tanh ( W C  [ h t-1 , x t ] + b C )
- (6.9in, 7.0in) a t = i t  ⊗ C t
- (8.7in, 6.9in) C t = f t  ⊗ C t-1 + a t

### Possible connector endpoints (spatial inference)

- + -> tanh (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t -> x (unverified)
- C t-1 -> C t (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)
- x -> σ (unverified)
- h t-1 -> σ (unverified)
- Архитектура  LSTM -> a t = i t  ⊗ C t (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t -> x (unverified)
- x -> σ (unverified)
- h t-1 -> σ (unverified)
- C t-1 -> C t (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)
- + -> tanh (unverified)
- h t-1 -> σ (unverified)
- h t-1 -> tanh (unverified)
- h t-1 -> x t (unverified)
- h t-1 -> x t (unverified)

## Slide 62

Native text objects: 24; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  LSTM
- (2.5in, 1.7in) забывание ненужного
- (4.6in, 1.6in) запоминание нового
- (7.0in, 1.9in) h t
- (1.2in, 2.9in) C t-1
- (3.1in, 3.1in) x
- (4.9in, 3.0in) +
- (7.9in, 2.9in) C t
- (9.1in, 2.9in) i t = σ ( W o  [ h t-1 , x t ] + b o )
- (6.7in, 3.4in) tanh
- (5.8in, 3.7in) o t
- (9.2in, 3.5in) a t = o t  ⊗ tanh( C t )
- (4.9in, 3.8in) x
- (6.8in, 3.9in) x
- (3.0in, 4.2in) σ
- (4.0in, 4.2in) σ
- (4.9in, 4.2in) tanh
- (5.7in, 4.2in) σ
- (1.6in, 4.6in) h t-1
- (8.3in, 4.7in) h t
- (3.3in, 5.8in) x t
- (1.8in, 6.8in) f t = σ ( W f  [ h t-1 , x t ] + b f )
- (4.9in, 6.8in) f t = [0, 2; 0, 3; 0, 9; 0, 1; 0, 5,...] T

### Possible connector endpoints (spatial inference)

- + -> tanh (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t-1 -> σ (unverified)
- x -> σ (unverified)
- C t-1 -> C t (unverified)
- h t -> x (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)

## Slide 63

Native text objects: 27; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  LSTM
- (9.1in, 0.5in) f t = σ ( W f  [ h t-1 , x t ] + b f )
- (9.1in, 1.3in) i t = σ ( W p  [ h t-1 , x t ] + b t )
- (2.5in, 1.7in) забывание ненужного
- (4.6in, 1.6in) запоминание нового
- (7.0in, 1.9in) h t
- (9.1in, 2.0in) C t = tanh ( W C  [ h t-1 , x t ] + b C )
- (9.2in, 2.6in) a t = i t  ⊗ C t
- (1.2in, 2.9in) C t-1
- (3.1in, 3.1in) x
- (4.9in, 3.0in) +
- (7.9in, 2.9in) C t
- (6.7in, 3.4in) tanh
- (9.2in, 3.2in) C t = f t  ⊗ C t-1 + a t
- (5.8in, 3.7in) o t
- (4.9in, 3.8in) x
- (6.8in, 3.9in) x
- (9.1in, 3.8in) o t = σ ( W o  [ h t-1 , x t ] + b o )
- (3.0in, 4.2in) σ
- (4.0in, 4.2in) σ
- (4.9in, 4.2in) tanh
- (5.7in, 4.2in) σ
- (9.2in, 4.4in) h t = o t  ⊗ tanh( C t )
- (1.6in, 4.6in) h t-1
- (8.3in, 4.7in) h t
- (3.3in, 5.8in) x t

### Possible connector endpoints (spatial inference)

- + -> tanh (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t-1 -> σ (unverified)
- x -> σ (unverified)
- C t-1 -> C t (unverified)
- h t -> x (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)

## Slide 64

Native text objects: 18; connectors: 16; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  GRU
- (7.4in, 1.8in) h t
- (9.3in, 1.6in) Gated Recurrent Units (GRU)
- (1.2in, 3.0in) h t-1
- (5.8in, 3.0in) x
- (6.8in, 3.0in) +
- (8.3in, 2.9in) y t
- (3.5in, 3.7in) x
- (4.8in, 3.7in) r t
- (5.8in, 3.6in) l-
- (5.4in, 3.8in) z t
- (6.8in, 3.8in) x
- (7.3in, 3.8in) h t
- (4.5in, 4.2in) σ
- (5.7in, 4.2in) σ
- (6.8in, 4.2in) tanh
- (2.9in, 5.8in) x t

### Possible connector endpoints (spatial inference)

- h t-1 -> y t (unverified)
- + -> tanh (unverified)
- h t-1 -> x t (unverified)
- x -> x t (unverified)
- x -> x t (unverified)
- x -> σ (unverified)
- r t -> x t (unverified)
- h t-1 -> x (unverified)
- l- -> σ (unverified)
- x -> σ (unverified)
- x -> r t (unverified)
- x -> l- (unverified)
- l- -> σ (unverified)
- l- -> x (unverified)
- h t -> + (unverified)

## Slide 65

Native text objects: 20; connectors: 18; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  GRU
- (3.3in, 1.3in) забывание ненужного
- (5.4in, 1.3in) запоминание нового
- (7.4in, 1.8in) h t
- (9.3in, 1.6in) Gated Recurrent Units (GRU)
- (1.2in, 3.0in) h t-1
- (5.8in, 3.0in) x
- (6.8in, 3.0in) +
- (8.3in, 2.9in) y t
- (3.5in, 3.7in) x
- (4.8in, 3.7in) r t
- (5.8in, 3.6in) l-
- (5.4in, 3.8in) z t
- (6.8in, 3.8in) x
- (7.3in, 3.8in) h t
- (4.5in, 4.2in) σ
- (5.7in, 4.2in) σ
- (6.8in, 4.2in) tanh
- (2.9in, 5.8in) x t

### Possible connector endpoints (spatial inference)

- + -> tanh (unverified)
- h t-1 -> x t (unverified)
- x -> x t (unverified)
- x -> x t (unverified)
- x -> σ (unverified)
- r t -> x t (unverified)
- h t-1 -> x (unverified)
- l- -> σ (unverified)
- x -> σ (unverified)
- x -> r t (unverified)
- x -> l- (unverified)
- l- -> σ (unverified)
- l- -> x (unverified)
- h t -> + (unverified)
- h t-1 -> y t (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)

## Slide 66

Native text objects: 21; connectors: 18; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  GRU
- (3.3in, 1.3in) забывание ненужного
- (5.4in, 1.3in) запоминание нового
- (7.4in, 1.8in) h t
- (9.3in, 2.3in) z t = σ ( W z  [ h t-1 , x t ] + b z )
- (1.2in, 3.0in) h t-1
- (5.8in, 3.0in) x
- (6.8in, 3.0in) +
- (8.3in, 2.9in) y t
- (9.4in, 3.0in) f t = h t=1  ⊗ (1 -z t )
- (3.5in, 3.7in) x
- (4.8in, 3.7in) r t
- (5.8in, 3.6in) 1 -
- (5.4in, 3.8in) z t
- (6.8in, 3.8in) x
- (7.3in, 3.8in) h t
- (4.5in, 4.2in) σ
- (5.7in, 4.2in) σ
- (6.8in, 4.2in) tanh
- (2.9in, 5.8in) x t

### Possible connector endpoints (spatial inference)

- + -> tanh (unverified)
- x -> x t (unverified)
- x -> σ (unverified)
- r t -> x t (unverified)
- h t-1 -> x (unverified)
- x -> σ (unverified)
- x -> r t (unverified)
- 1 - -> σ (unverified)
- 1 - -> x (unverified)
- h t -> + (unverified)
- h t-1 -> y t (unverified)
- забывание ненужного -> x (unverified)
- запоминание нового -> + (unverified)
- h t-1 -> x t (unverified)
- x -> x t (unverified)
- 1 - -> σ (unverified)
- x -> 1 - (unverified)

## Slide 67

Native text objects: 23; connectors: 16; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  GRU
- (7.4in, 1.8in) h t
- (9.3in, 1.6in) Gated Recurrent Units (GRU)
- (9.3in, 2.3in) z t = σ ( W z  [ h t-1 , x t ] + b z )
- (1.2in, 3.0in) h t-1
- (5.8in, 3.0in) x
- (6.8in, 3.0in) +
- (8.3in, 2.9in) y t
- (9.4in, 3.0in) f t = h t=1  ⊗ (1 -z t )
- (3.5in, 3.7in) x
- (4.8in, 3.7in) r t
- (5.8in, 3.6in) l-
- (9.3in, 3.6in) r t = σ ( W p  [ h t-1 , x t ] + b r )
- (5.4in, 3.8in) z t
- (6.8in, 3.8in) x
- (7.3in, 3.8in) h t
- (4.5in, 4.2in) σ
- (5.7in, 4.2in) σ
- (6.8in, 4.2in) tanh
- (8.9in, 4.3in) h t = tanh ( W xh  x t + W hh (r t ⊗h t-1 )  + b h )
- (8.9in, 5.1in) h t = h t=1  ⊗ (1 -z t ) + h t  ⊗ z t
- (2.9in, 5.8in) x t

### Possible connector endpoints (spatial inference)

- h t-1 -> y t (unverified)
- + -> tanh (unverified)
- h t-1 -> x t (unverified)
- x -> x t (unverified)
- x -> x t (unverified)
- x -> σ (unverified)
- r t -> x t (unverified)
- h t-1 -> x (unverified)
- l- -> σ (unverified)
- x -> σ (unverified)
- x -> r t (unverified)
- x -> l- (unverified)
- l- -> σ (unverified)
- l- -> x (unverified)
- h t -> + (unverified)

## Slide 68

Native text objects: 24; connectors: 16; embedded pictures: 0

- (0.6in, 0.3in) РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
- (0.6in, 0.7in) Архитектура  GRU
- (7.4in, 1.8in) h t
- (9.3in, 1.6in) Gated Recurrent Units (GRU)
- (9.3in, 2.3in) z t = σ ( W z  [ h t-1 , x t ] + b z )
- (1.2in, 3.0in) h t-1
- (5.8in, 3.0in) x
- (6.8in, 3.0in) +
- (8.3in, 2.9in) y t
- (9.4in, 3.0in) f t = h t=1  ⊗ (1 -z t )
- (3.5in, 3.7in) x
- (4.8in, 3.7in) r t
- (5.8in, 3.6in) l-
- (9.3in, 3.6in) r t = σ ( W p  [ h t-1 , x t ] + b r )
- (5.4in, 3.8in) z t
- (6.8in, 3.8in) x
- (7.3in, 3.8in) h t
- (4.5in, 4.2in) σ
- (5.7in, 4.2in) σ
- (6.8in, 4.2in) tanh
- (8.9in, 4.3in) h t = tanh ( W xh  x t + W hh (r t ⊗h t-1 ) + b h )
- (8.9in, 5.1in) h t = h t=1  ⊗ (1 -z t ) + h t  ⊗ z t
- (2.9in, 5.8in) x t
- (3.9in, 6.5in) torch.nn .GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, …)

### Possible connector endpoints (spatial inference)

- h t-1 -> y t (unverified)
- + -> tanh (unverified)
- h t-1 -> x t (unverified)
- x -> x t (unverified)
- x -> x t (unverified)
- x -> σ (unverified)
- r t -> x t (unverified)
- h t-1 -> x (unverified)
- l- -> σ (unverified)
- x -> σ (unverified)
- x -> r t (unverified)
- x -> l- (unverified)
- l- -> σ (unverified)
- l- -> x (unverified)
- h t -> + (unverified)
