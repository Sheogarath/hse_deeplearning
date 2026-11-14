# transformery.pptx

Source: https://github.com/Sheogarath/hse_deeplearning/blob/main/lecture_08/transformery.pptx

## Slide 1

КУРС «НЕЙРОННЫЕ СЕТИ»
Механизм внимания и трансформеры
Лекция 4 · Модуль 1
2/19

### Speaker notes

Вступление, знакомство. Обозначить формат курса: лекция + семинар 2 раза в неделю.
‹#›

## Slide 2

Механизм внимания - attention
Архитектура Seq2Seq
h0
h1
h2
h3
hl
…
x1
x2
x3
x1
…
<bos>
Я
снимаю
<eos>
Embedding
Encoder
Decoder
h0
h1
h2
h3
hl
…
x1
x2
x3
x1
…
<bos>
Я
снимаю
<eos>
Embedding
fc
fc
fc
fc
SM
SM
SM
SM
SoftMax
argmax

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 3

Механизм внимания - attention
Архитектура Seq2Seq
h0
h1
h2
h3
hl
…
x1
x2
x3
x1
…
<bos>
Я
снимаю
<eos>
Embedding
Encoder
Decoder
h0
h1
h2
h3
hl
…
x1
x2
x3
x1
…
<bos>
Я
снимаю
<eos>
Embedding
fc
fc
fc
fc
SM
SM
SM
SM
SoftMax
argmax
σ
xt
Ct-1
ht-1
ht
ht
Ct
σ
tanh
x
+
σ
x
tanh
x

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 4

Механизм внимания - attention
Качество перевода сетью типа Seq2Seq

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 5

Механизм внимания - attention
Механизм внимания (attention)
А почему он поедет в Египет, а я когда поеду туда вместо него
Why is he going to Egypt, and when will I go there instead of him?

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 6

Механизм внимания - attention
Архитектура Seq2Seq с attention
4/25
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0
y
<bos>
bos - begin of sentence
eos - end of sentence

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 7

Механизм внимания - attention
Архитектура Seq2Seq с attention
4/25
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0
y
<bos>
bos - begin of sentence
eos - end of sentence
s(ht, h0)
w1

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 8

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0
y
<bos>
bos - begin of sentence
eos - end of sentence
s(ht, h0)
w1
a = [a1, a2, ..., an]T
b = [b1, b2, ..., bn]T
w = aT * b = ∑ a * b = |a| * |b| * cos α
α
w
b
a
wi = s(hie ,h0d) = (hie)T * h0d,      i = 1,2, …, 5

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 9

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
wi = s(hie, h0d)
i = 1, 2, …, 5

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 10

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
wi = s(hie, h0d)
i = 1, 2, …, 5
s(h1e, h0d)
s(h2e, h0d)
w3
w4

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 11

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
wi = s(hie, h0d)
i = 1, 2, …, 5
s(h1e, h0d)
s(h2e, h0d)
w3
w4
SoftMax
α1
α2
α3
α4

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 12

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
wi = s(hie, h0d)
i = 1, 2, …, 5
s(h1e, h0d)
s(h2e, h0d)
w3
w4
SoftMax
α1
α2
α3
α4
c0 = ∑ αi * hie

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 13

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
wi = s(hie, h0d)
i = 1, 2, …, 5
s(h1e, h0d)
s(h2e, h0d)
w3
w4
SoftMax
α1
α2
α3
α4
c0 = ∑ αi * hie
c0
h1d = RNN([v1, c0], h0d)

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 14

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
wi = s(hie, h0d)
i = 1, 2, …, 5
s(h1e, h0d)
s(h2e, h0d)
w3
w4
SoftMax
α1
α2
α3
α4
c0 = ∑ αi * hie
c0
h1d = RNN([v1, c0], h0d)
fc
SM
SoftMax
argmax

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 15

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
s(h1e, h0d)
s(h2e, h0d)
w3
w4
SoftMax
α1
α2
α3
α4
c0 = ∑ αi * hie
c0
h1d = RNN([v1, c0], h0d)
fc
SM
SoftMax
argmax
Attention (внимание)

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 16

Механизм внимания - attention
Структура сети определяет ее функциональность
∑
x1
x2
y
1
1

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 17

Механизм внимания - attention
Структура сети определяет ее функциональность
∑
x1
x2
y
1
1
Фрагмент нейронной сети
Фрагмент нейронной сети
Фрагмент нейронной сети
…
…

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 18

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
s(h1e, h0d)
s(h2e, h0d)
w3
w4
SoftMax
α1
α2
α3
α4
c0 = ∑ αi * hie
c0
h1d = RNN([v1, c0], h0d)
fc
SM
SoftMax
argmax
Attention (внимание)

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 19

Механизм внимания - attention
Механизм внимания (attention)

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 20

Механизм внимания - attention
Архитектура Seq2Seq с attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
s(h1e, h0d)
s(h2e, h0d)
w3
w4
SoftMax
α1
α2
α3
α4
c0 = ∑ αi * hie
c0
h2d = RNN([v2, c1], h1d)
fc
SM
SoftMax
argmax
Attention (внимание)
h2d
y2
I

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 21

Механизм внимания - attention
Качество работы механизма вниамния
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
s(h1e, h0d)
w1
s(h2e, h0d)
w2
s(h1e, h0d)
s(h2e, h0d)
w3
w4
SoftMax
α1
α2
α3
α4
c0 = ∑ αi * hie
fc
SM
Attention (внимание)
h2d
y2
I
fc
SM
h3d
y3
filming
fc
SM

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 22

Механизм внимания - attention
Архитектура Seq2Seq с attention

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 23

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 24

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
А почему он поедет в Египет, а я когда поеду туда вместо него

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 25

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 26

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 27

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 28

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 29

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3
c1 = α1 h2e + α2 h3e +α3 h4e

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 30

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3
c1 = α1 h2e + α2 h3e +α3 h4e
h1
c1

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 31

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3
c1 = α1 h2e + α2 h3e +α3 h4e
h1e
c1
W
H1e

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 32

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3
c1 = α1 h2e + α2 h3e +α3 h4e
h1e
c1
W
H1e
Self-attention

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 33

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3
c2 = α1 h2e + α2 h3e +α3 h4
H1e
Self-attention
Updated:

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 34

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3
c2 = α1 h2e + α2 h3e +α3 h4e
H1e
Self-attention
Updated:
H2e

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 35

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3
c1 = α1 h2e + α2 h3e +α3 h4e
H1e
Self-attention
Updated:
H2e

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 36

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
s
w1
s
w2
s
w3
SoftMax
α1
α2
α3
c1 = α1 h2e + α2 h3e +α3 h4e
H1e
Self-attention
Updated:
H2e
H3e

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 37

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
H1e
Self-attention
Updated:
H2e
H3e
H4e

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 38

Механизм внимания - attention
Механизм внимания (attention)
Why is he going to Egypt, and when will I go there instead of him?

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 39

Механизм внимания - attention
self-attention в декодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
copy

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 40

Механизм внимания - attention
self-attention в декодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
fc
SM
SoftMax
argmax
h1d= RNN(y1,h0d)

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 41

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
fc
SM
SoftMax
argmax
h2d
y
I
I

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 42

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
h2d
y
I
s
SM
c1= α1 * h1d
α1 = 1

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 43

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
fc
SM
SoftMax
argmax
h2d
y
I
I

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 44

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
fc
SM
SoftMax
argmax
h2d
y2
I
fc
SM
I
filming
h2d
y3
filming

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 45

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
h2d
y2
I
h3d
y3
filming
s
s
w1
w2

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 46

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
h2d
y2
I
h3d
y3
filming
s
s
w1
w2
SoftMax
α1
α2
c3= α1 * h1d + α2 * h2d

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 47

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
h2d
y2
I
h3d
y3
filming
s
s
w1
w2
SoftMax
α1
α2
c3= α1 * h1d + α2 * h2d
h3d
c3
H3d

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 48

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
h2d
y2
I
h3d
y3
filming
s
s
w1
w2
SoftMax
α1
α2
c3= α1 * h1d + α2 * h2d
h3d
c3
H3d
fc
SM
cinema

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 49

Механизм внимания - attention
self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
h2d
y2
I
h3d
y3
filming
h4d
y4
cinema
s
s
s
w1
w2
w3
SoftMax
α1
α2
c3= α1 * h1d + α2 * h2d+ α3 * h3d
α3
h4d
c4
H4d
fc
SM
<eos>
h4d
c4
fc
SM
h4d
c4

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 50

Механизм внимания - attention
Attention c Self-attentiona  декодера
А почему он поедет в Египет, а я когда поеду туда вместо него
Why is he going to Egypt, and when will I go there instead of him?
Self-attention decoder
Cross-Attention

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 51

Механизм внимания - attention
Attention с Self-attention декодера
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y
<bos>
SoftMax
c0 = ∑ αi * hie
c0
h1d = RNN([y1, a0], h0d)
s
s
s
s
Attention
fc
SM
I

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 52

Механизм внимания - attention
Attention с Self-attention декодера
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
SoftMax
c0 = ∑ αi * hie
s
s
s
s
Attention
fc
SM
I
h2d
fc
SM
filming
y2
I

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 53

Механизм внимания - attention
Attention с Self-attention декодера
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
SoftMax
c0 = ∑ αi * hie
s
s
s
s
Attention
fc
SM
I
h2d
fc
SM
filming
y2
I
h3d
y3
filming
h3d = RNN([y3, a2], h2d)
a2

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 54

Механизм внимания - attention
Attention с Self-attention декодера
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
SoftMax
c0 = ∑ αi * hie
s
s
s
s
Attention
h2d
y2
I
h3d
y3
filming
a2
s
s
SoftMax
c3 = ∑ αi * hie
Self-attention
cinema
fc
SM
h3d
c3

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 55

Механизм внимания - attention
Attention с Self-attention декодера
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
h0d
h1d
y1
<bos>
SoftMax
c0 = ∑ αi * hie
s
s
s
s
Attention
h2d
y2
I
h3d
y3
filming
a2
s
s
SoftMax
c3 = ∑ αi * hie
Self-attention
h3d
y3
cinema
<eos>
fc
SM
h4d
c4
s

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 56

Механизм внимания - attention
Механизм внимания (attention)
А почему он поедет в Египет, а я когда поеду туда вместо него
Why is he going to Egypt, and when will I go there instead of him?
Self-attention decoder
Cross-Attention
Self-attention decoder

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 57

Механизм внимания - attention
self-attention в кодере
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
H1e
Updated:
H2e
H3e
H4e

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 58

Механизм внимания - attention
Attention  с Self-attention
h0
h1
h2
h3
h4
x1
x2
x3
x1
<bos>
Я
снимаю
<eos>
Embedding
H1e
Self-attention
Updated:
H2e
H3e
H4e
SoftMax
c0 = ∑ αi * hie
s
s
s
s
Attention
h0d
h1d
y1
<bos>
h2d
y2
I
h3d
y3
filming
a2
s
s
SoftMax
c3 = ∑ αi * hie
Self-attention
cinema
fc
SM
h4d
c4
copy

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 59

Механизм внимания - attention
Архитектура Seq2Seq
h0
h1
h2
h3
hl
…
x1
x2
x3
x1
…
<bos>
Я
снимаю
<eos>
Embedding
Encoder
Decoder
h0
h1
h2
h3
hl
…
x1
x2
x3
x1
…
<bos>
Я
снимаю
<eos>
Embedding
fc
fc
fc
fc
SM
SM
SM
SM
SoftMax
argmax
цепочки данных обрабатываются последовательно и эти вычисления не распараллеливаются
при обучении возникает известная проблема взрывающихся или затухающих градиентов

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 60

Механизм внимания - attention
Трансформер. Архитектура
могут обрабатывать последовательности данных в параллельном режиме

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 61

Механизм внимания - attention
Трансформер. Архитектура
могут обрабатывать последовательности данных в параллельном режиме
ChatGPT (OpenAI)
Gemini (Google DeepMind)
Claude (Anthropic)
Llama (Meta)
DeepSeek
YandexGPT

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 62

Механизм внимания - attention
Трансформер. Архитектура

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 63

Механизм внимания - attention
Трансформер.  QKV Self-Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 64

Механизм внимания - attention
Трансформер.  QKV Self-Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
s
s
s
s
s
Embedding

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 65

Механизм внимания - attention
Трансформер.  QKV Self-Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
query
q = Wq * xi
Wq * x1
Wq * x2
Wq * x3
Wq * x4
Wq * x5
Embedding
s
s
s
s
s
w = s(a,b) = aT * b = ∑ ai * bi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 66

Механизм внимания - attention
Трансформер.  QKV Self-Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
query
q = Wq * xi
Embedding
s
s
s
s
s
w = s(a,b) = aT * b = ∑ ai * bi
Linear, Wk
k1
k2
k3
k4
k5
w11
w12
w13
w14
w15
ki= Wk * xi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 67

Механизм внимания - attention
Трансформер.  QKV Self-Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
query
q = Wq * xi
Embedding
s
s
s
s
s
w = s(a,b) = aT * b = ∑ ai * bi
Linear, Wk
k1
k2
k3
k4
k5
w11
w12
w13
w14
w15
ki= Wk * xi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 68

Механизм внимания - attention
Трансформер.  QKV Self-Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
query
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
ki= Wk * xi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 69

Механизм внимания - attention
Трансформер.  QKV Self-Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
query
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * ?
ki= Wk * xi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 70

Механизм внимания - attention
Трансформер.  QKV Self-Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 71

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
emb_size
X
N

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 72

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
emb_size
X
N
d_attn
Wq
emb_size
d_attn
Q = X * Wq
N
=
X
X
N
Wq
emb_size
K = X * Wk
N
=
X
X
N
Wq
emb_size
V = X * Wv
N
=
X

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 73

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
N
d_attn
Q
N
K
N
V

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 74

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
N
d_attn
Q
N
K
N
V
N
d_attn
N
W = Q * KT
N
=
X
KT

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 75

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
N
d_attn
Q
N
V
N
d_attn
N
W = Q * KT
N
=
X
KT
A =SoftMax(QKT/√dattn)
N
A
N
=

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 76

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
N
d_attn
Q
N
V
N
d_attn
N
W = Q * KT
N
=
X
KT
A =SoftMax(QKT/√dattn)
N
A
N
=
A
N
X
=
N
С

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 77

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
N
d_attn
Q
N
d_attn
N
W = Q * KT
N
=
X
KT
A =SoftMax(QKT/√dattn) * V
N

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 78

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
N
d_attn
Q
N
V
N
d_attn
N
W = Q * KT
N
=
X
KT
A =SoftMax(QKT/√dattn) * V
N
GPT-4: 32768 токенов
LLaMA 3.1 : 128000 токенов

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 79

Механизм внимания - attention
Трансформер. Multi-head Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
N
d_attn
Q
N
d_attn
N
W = Q * KT
N
=
X
KT
A =SoftMax(QKT/√dattn) * V
N
влияние токена А на токен В было бы равно влиянию токена В на токен А

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 80

Механизм внимания - attention
Трансформер. Multi-head Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
N
d_attn
Q
N
d_attn
N
W = Q * KT
N
=
X
KT
A =SoftMax(QKT/√dattn) * V
N
влияние токена А на токен В было бы равно влиянию токена В на токен А
Я снимаю кино

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 81

Механизм внимания - attention
Трансформер. Multi-head Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 82

Механизм внимания - attention
Трансформер. Multi-head Attention
А почему он поедет в Египет, а я когда поеду туда вместо него

### Speaker notes

Показать реалистичную многослойную сеть и явно указать на дальний от выхода вес — как понять его влияние на loss? Мотивационный вопрос ко всей лекции.
‹#›

## Slide 83

Механизм внимания - attention
Трансформер. Multi-head Attention
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 84

Механизм внимания - attention
Трансформер. Multi-head Attention
emb_size
X
N

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 85

Механизм внимания - attention
Трансформер. Multi-head Attention
emb_size
X
N
dk
emb_size
dk
N
dk = emb_size / n
Wq
Wk
Wv
Q1
K1
V1

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 86

Механизм внимания - attention
Трансформер. Multi-head Attention
emb_size
X
N
dk
emb_size
dk
N
dk = emb_size / n
Wq
Wk
Wv
Q1
K1
V1
C1
dk

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 87

Механизм внимания - attention
Трансформер. Multi-head Attention
emb_size
X
N
dk
emb_size
dk
N
dk = emb_size / n
Wq
Wk
Wv
Q1
K1
V1
C1
dk
dk
dk
N
Wq
Wk
Wv
Qn
Kn
Vn
C1
dk
…
…
…
n голов внимания (multi-head)

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 88

Механизм внимания - attention
Трансформер. Multi-head Attention
dk
emb_size
dk
N
Wq
Wk
Wv
Q1
K1
V1
C1
dk
dk
dk
N
Wq
Wk
Wv
Qn
Kn
Vn
dk
…
…
…
…
dk * n = emb_size

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 89

Механизм внимания - attention
Трансформер. Multi-head Attention
dk
emb_size
dk
N
Wq
Wk
Wv
Q1
K1
V1
C1
dk
dk
dk
N
Wq
Wk
Wv
Qn
Kn
Vn
dk
…
…
…
…
dk * n = emb_size
…
emb_size

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 90

Механизм внимания - attention
Трансформер. Multi-head Attention
dk
emb_size
dk
N
Wq
Wk
Wv
Q1
K1
V1
C1
dk
dk
dk
N
Wq
Wk
Wv
Qn
Kn
Vn
dk
…
…
…
…
dk * n = emb_size
…
emb_size
emb_size
=
x
Z
W0

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 91

трансформеры
Трансформер. Блок Add & LayerNorm
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
emb_size
emb_size
N
N
Z
X

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 92

трансформеры
Трансформер. Блок Add & LayerNorm
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
Z =
z1z2
…
zN
X =
x1x2
…
xN
z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 93

трансформеры
Трансформер. Блок Add & LayerNorm
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
Z =
z1z2
…
zN
X =
x1x2
…
xN
z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1
x2
x3
x4
x5

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 94

трансформеры
Трансформер. Блок Add & LayerNorm
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
Z =
z1z2
…
zN
X =
x1x2
…
xN
z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1
x2
x3
x4
x5
LayerNorm

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 95

трансформеры
Трансформер. Блок Add & LayerNorm
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
Z =
z1z2
…
zN
X =
x1x2
…
xN
z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1
x2
x3
x4
x5
LayerNorm
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 96

трансформеры
Архитектуры post-norm и pre-norm
Embedding
skip (residual) connection
LayerNorm
Multi-head Attention
Add
post-norm

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 97

трансформеры
Архитектуры post-norm и pre-norm
Embedding
skip (residual) connection
LayerNorm
Multi-head Attention
Add
post-norm
Embedding
Add
LayerNorm
Multi-head Attention
pre-norm

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 98

трансформеры
Трансформер. Блок Feed Forward
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1
x2
x3
x4
x5
LayerNorm
Linear1
ReLU или GELU
Dropout
Linear2
embedding
Multi-head Attention
add
Feed Forward

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 99

трансформеры
Трансформер. Блок Feed Forward
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
Add & LayerNorm
Linear1
ReLU или GELU
Dropout
Linear2
embedding
Multi-head Attention
add
Feed Forward
Add & LayerNorm

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 100

трансформеры
Архитектуры post-norm и pre-norm
Embedding
skip (residual) connection
LayerNorm
Multi-head Attention
Add
post-norm
Embedding
Add
LayerNorm
Multi-head Attention
pre-norm
LayerNorm
Feed Forward
Add
Encoder
Add
Feed Forward
LayerNorm
Encoder

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 101

трансформеры
Трансформер. Блок Feed Forward
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
Add & LayerNorm
Linear1
ReLU или GELU
Dropout
Linear2
embedding
Multi-head Attention
add
Feed Forward
Add & LayerNorm

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 102

трансформеры
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
embedding
Кабан наступил на баклажан
баклажан наступил на Кабан

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 103

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
query
key
q = Wq * xi
Embedding
s
s
s
s
s
w = s(a,b) = aT * b = ∑ ai * bi
Linear, Wk
k1
k2
k3
k4
k5
w11
w12
w13
w14
w15
ki= Wk * xi
Кабан наступил на баклажан
баклажан наступил на Кабан

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 104

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
query
key
q = Wq * xi
Embedding
s
s
s
s
s
w = s(a,b) = aT * b = ∑ ai * bi
Linear, Wk
k1
k2
k3
k4
k5
w11
w12
w13
w14
w15
ki= Wk * xi
Кабан наступил на баклажан
баклажан наступил на Кабан
w = s(a,b) = s(b, a )

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 105

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Embedding
1
2
3
4
0
Positional Encoding

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 106

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Embedding
1
2
3
4
0
Positional Encoding
+
+
+
+
+
xi=xi + pi
i = 0, 1, …, N-1

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 107

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Embedding
1
2
3
4
0
Positional Encoding
+
+
+
+
+
xi=xi + pi
i = 0, 1, …, N-1
x = [0.1, 0.2, 0.3]
p = 100
x = [100.1, 100.2, 100.3]

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 108

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Embedding
1
2
3
4
0
Positional Encoding
+
+
+
+
+
xi=xi + pi
i = 0, 1, …, N-1
0
0.25
0.5
0.75
1.0
0
0.2
0.4
0.6
0.8
1.0
N=6 :
N=5 :

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 109

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Embedding
1
2
3
4
0
Positional Encoding
+
+
+
+
+
xi=xi + pi
i = 0, 1, …, N-1
N=4096 : [0.0, 0.000244, 0.000488, 0.00073, …]

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 110

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Embedding
1
2
3
4
0
Positional Encoding
+
+
+
+
+
xi=xi + pi
i = 0, 1, …, N-1
p0 = [1, 0, 0, …, 0, …, 0]T
p1 = [0, 1, 0, …, 0, …, 0]T
…
pi = [0, 0, 0, …, 1, …, 0]T
,,,
pN-1 = [0, 0, 0, …, 0, …, 1]T

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 111

Механизм внимания - attention
Трансформер. Позиционное кодирование
Positional Encoding
Embedding
+
Input
Encoder
Add & LayerNorm
Feed Forward
Multi-head Attention
Add & LayerNorm
Output
x2
x3
x4
x5
x1
<bos>
<eos>
я
снимаю
кино
Embedding
1
2
3
4
0
Positional Encoding
+
+
+
+
+
xi=xi + pi
i = 0, 1, …, N-1
sin(w0 * t)
cos(w0 * t)
sin(wi * t)
cos(wi * t)
…
sin(wd/2-1 * t)
cos(wd/2-1 * t)
pt=
Attention is All You Need

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 112

Механизм внимания - attention
Трансформер. Позиционное кодирование
sin(w0 * t)
cos(w0 * t)
sin(w1 * t)
cos(w1 * t)
sin(w2 * t)
cos(w2 * t)
…
sin(wd/2-1 * t)
cos(wd/2-1 * t)
pt=
sin(w0 * t)
cos(w0 * t)
sin(w1 * t)
cos(w1 * t)
sin(w2 * t)
cos(w2 * t)
…
sin(wd/2-1 * t)
cos(wd/2-1 * t)
position ,t
p0
p2
pi
p0 = [0,1,0,1,0,1,0,1]
p2 = [0.90, -0.42, 0.19 , 0.98, 0.20, 0.002, 0.99]T

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 113

Механизм внимания - attention
Трансформер. Позиционное кодирование
sin(w0 * t)
cos(w0 * t)
sin(w1 * t)
cos(w1 * t)
sin(w2 * t)
cos(w2 * t)
…
sin(wd/2-1 * t)
cos(wd/2-1 * t)
pt=
уникальный вектор для каждой позиции
возможность вычисления относительных расстояний между векторами
простота генерации векторов позиций для последовательной произвольной длины N
все векторы детерминированы и могут быть вычислены заранее

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 114

Механизм внимания - attention
Трансформер. Позиционное кодирование
sin(w0 * t)
cos(w0 * t)
sin(w1 * t)
cos(w1 * t)
sin(w2 * t)
cos(w2 * t)
…
sin(wd/2-1 * t)
cos(wd/2-1 * t)
pt=
уникальный вектор для каждой позиции
возможность вычисления относительных расстояний между векторами
простота генерации векторов позиций для последовательной произвольной длины N
все векторы детерминированы и могут быть вычислены заранее
BERT и первые версии ChatGPT использовали обучаемые векторы позиции
PaLM, LLaMA последние версии ChatGPT, применяется для относительнольного позиционирования - rotary Position Embedding (RoPE)

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 115

Трансформер. Декодер
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input
Decoder
Encoder output
+
p0
x0
LN
SM
argmax
SoftMax
Linear
Positional Encoding
Embedding

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 116

Трансформер. Декодер
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input
Decoder
Encoder output
+
p0
x0
LN
SM
argmax
SoftMax
Linear
Positional Encoding
Embedding
+
p1
x1
+
p2
x2
+
p3
x3
I
LN
SM
filming
LN
SM
absolute
LN
SM
cinema

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 117

z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
Multi-headAttention
Embedding
Трансформер. Декодер
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 118

Механизм внимания - attention
Вычисление QKV Self-Attention
x2
x3
x4
x5
x1
Linear, Wv
<bos>
<eos>
я
снимаю
кино
Linear, Wq
q1
q2
q3
q4
q5
querykeyvalue
q = Wq * xi
Embedding
s
s
s
s
s
SoftMax(w/√d)
Linear, Wk
k1
k2
k3
k4
k5
SoftMax
c1 = ∑ αi * vi
v1
v2
v3
v4
v5
ki= Wk * xi
vi= Wv * xi
X
N
Wq
emb_size
V = X * Wv
N
=
X
d_attn
Q
N
d_attn
N
N
=
X
KT
W = Q * KT
M =
0     -∞  …   -∞
0     0    …   -∞
…  …  …   …
0    0  …    0

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 119

z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
Multi-headAttention
Embedding
Трансформер. Декодер
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 120

z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1
x2
x3
x4
x5
LayerNorm
Masked Multi-head Attention
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 121

z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1
x2
x3
x4
x5
LayerNorm
Masked Multi-head Attention
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 122

трансформеры
Архитектуры post-norm и pre-norm
Embedding
skip (residual) connection
LayerNorm
Masked
Multi-head Attention
Add
post-norm
Embedding
LayerNorm
Masked
Multi-head Attention
Add
pre-norm

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 123

z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
x1+z1
x2+z2
x3+z3
x4+z4
x5+z5
x1
x2
x3
x4
x5
LayerNorm
Masked Multi-head Attention
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 124

z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
Add & LayerNorm
Masked Multi-head Attention
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input
Linear, Wq
q1
q2
q3
q4
q5

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 125

z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
Add & LayerNorm
Masked Multi-head Attention
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input
Linear, Wq
q1
q2
q3
q4
q5
Linear, Wk
Encode, Outpujt
k1
k2
k3
k4
k5
Linear, Wv
v1
v2
v3
v4
v5
S
S
S
S
S
Linear, Wq
c1 = ∑ αi * vi

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›

## Slide 126

z1
z2
z3
z4
z5
x1
x2
x3
x4
x5
<bos>
<eos>
я
снимаю
кино
Add & LayerNorm
Трансформер. Декодер
skip (residual) connection
Multi-head Attention
Masked
Multi-head Attention
Add & LayerNorm
output
Add & LayerNorm
Add & LayerNorm
Feed Forward
Decoder
Encoder output
Linear
SoftMax
Positional Encoding
Embedding
+
Input
Multi-head Attention
Add & LayerNorm
Feed Forward
Encoder output

### Speaker notes

Центральная идея слайда: задача «оцифровки» реальности = извлечение измеримых признаков → вектор. Это то самое x, которое мы использовали в формулах на предыдущих и следующих слайдах — явно навести мостик.
‹#›
