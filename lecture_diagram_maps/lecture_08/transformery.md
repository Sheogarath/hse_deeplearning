# lecture_08/transformery.pptx

Automatically inferred reading order and possible connections. **Connections are heuristic**, not verified semantic claims.

## Slide 1

Native text objects: 4; connectors: 7; embedded pictures: 0

- (0.6in, 1.6in) КУРС «НЕЙРОННЫЕ СЕТИ»
- (0.6in, 2.1in) Механизм внимания и трансформеры
- (0.6in, 6.5in) Лекция 4 · Модуль 1
- (12.0in, 7.0in) 2/19

### Possible connector endpoints (spatial inference)


## Slide 2

Native text objects: 46; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq
- (5.0in, 1.5in) De coder
- (6.5in, 2.2in) argmax
- (7.3in, 2.8in) SM
- (8.0in, 2.8in) SM
- (8.7in, 2.8in) SM
- (10.1in, 2.8in) SM
- (1.4in, 3.7in) Encoder
- (6.5in, 3.6in) SoftMax
- (7.3in, 3.5in) fc
- (8.0in, 3.5in) fc
- (8.7in, 3.5in) fc
- (10.1in, 3.5in) fc
- (1.6in, 4.4in) h 0
- (2.3in, 4.4in) h 1
- (3.0in, 4.4in) h 2
- (3.7in, 4.4in) h 3
- (4.4in, 4.3in) …
- (5.0in, 4.4in) h l
- (6.6in, 4.4in) h 0
- (7.3in, 4.4in) h 1
- (8.0in, 4.4in) h 2
- (8.7in, 4.4in) h 3
- (9.4in, 4.3in) …
- (10.1in, 4.4in) h l
- (1.2in, 5.3in) Embedding
- (2.3in, 5.1in) x 1
- (3.0in, 5.1in) x 2
- (3.7in, 5.1in) x 3
- (4.4in, 5.1in) …
- (5.0in, 5.1in) x 1
- (6.2in, 5.3in) Embedding
- (7.3in, 5.1in) x 1
- (8.0in, 5.1in) x 2
- (8.7in, 5.1in) x 3
- (9.4in, 5.1in) …
- (10.1in, 5.1in) x 1
- (2.1in, 5.8in) <bos>
- (3.0in, 5.8in) Я
- (3.5in, 5.8in) снимаю
- (4.9in, 5.8in) <eos>
- (7.1in, 5.8in) <bos>
- (8.1in, 5.8in) Я
- (8.6in, 5.8in) снимаю
- (9.9in, 5.8in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> … (unverified)
- h l -> h 0 (unverified)
- … -> h l (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h l -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> … (unverified)
- … -> h l (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h l -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- fc -> h 1 (unverified)
- fc -> h 2 (unverified)
- fc -> h 3 (unverified)
- fc -> h l (unverified)

## Slide 3

Native text objects: 61; connectors: 44; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq
- (3.3in, 1.4in) h t
- (5.0in, 1.5in) Decoder
- (0.5in, 1.9in) C t-1
- (1.4in, 2.0in) x
- (2.3in, 2.0in) +
- (3.7in, 1.9in) C t
- (2.3in, 2.3in) x
- (3.1in, 2.1in) tanh
- (3.2in, 2.4in) x
- (6.5in, 2.2in) argmax
- (0.6in, 2.8in) h t-1
- (1.3in, 2.6in) σ
- (1.8in, 2.6in) σ
- (2.2in, 2.6in) tanh
- (2.7in, 2.6in) σ
- (3.9in, 2.7in) h t
- (7.3in, 2.8in) SM
- (8.0in, 2.8in) SM
- (8.7in, 2.8in) SM
- (10.1in, 2.8in) SM
- (1.5in, 3.3in) x t
- (1.4in, 3.7in) Encoder
- (6.5in, 3.6in) SoftMax
- (7.3in, 3.5in) fc
- (8.0in, 3.5in) fc
- (8.7in, 3.5in) fc
- (10.1in, 3.5in) fc
- (1.6in, 4.4in) h 0
- (2.3in, 4.4in) h 1
- (3.0in, 4.4in) h 2
- (3.7in, 4.4in) h 3
- (4.4in, 4.3in) …
- (5.0in, 4.4in) h l
- (6.6in, 4.4in) h 0
- (7.3in, 4.4in) h 1
- (8.0in, 4.4in) h 2
- (8.7in, 4.4in) h 3
- (9.4in, 4.3in) …
- (10.1in, 4.4in) h l
- (1.2in, 5.3in) Embedding
- (2.3in, 5.1in) x 1
- (3.0in, 5.1in) x 2
- (3.7in, 5.1in) x 3
- (4.4in, 5.1in) …
- (5.0in, 5.1in) x 1
- (6.2in, 5.3in) Embedding
- (7.3in, 5.1in) x 1
- (8.0in, 5.1in) x 2
- (8.7in, 5.1in) x 3
- (9.4in, 5.1in) …
- (10.1in, 5.1in) x 1
- (2.1in, 5.8in) <bos>
- (3.0in, 5.8in) Я
- (3.5in, 5.8in) снимаю
- (4.9in, 5.8in) <eos>
- (7.1in, 5.8in) <bos>
- (8.1in, 5.8in) Я
- (8.6in, 5.8in) снимаю
- (9.9in, 5.8in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> … (unverified)
- h l -> h 0 (unverified)
- … -> h l (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h l -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> … (unverified)
- … -> h l (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h l -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- fc -> h 1 (unverified)
- fc -> h 2 (unverified)
- fc -> h 3 (unverified)
- fc -> h l (unverified)
- C t-1 -> C t (unverified)
- + -> tanh (unverified)
- x -> σ (unverified)
- h t-1 -> σ (unverified)
- σ -> x t (unverified)
- h t -> x (unverified)

## Slide 4

Native text objects: 2; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Качество перевода сетью типа Seq2Seq

## Slide 5

Native text objects: 4; connectors: 8; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Механизм внимания (attention)
- (0.6in, 2.1in) А почему он поедет в Египет, а я когда поеду туда вместо него
- (2.7in, 3.7in) Why is he going to Egypt, and when will I go there instead of him?

### Possible connector endpoints (spatial inference)

- А почему он поедет в Египет, а я когда поеду туда вместо него -> Why is he going to Egypt, and when will I go there instead of him? (unverified)
- Механизм внимания (attention) -> Why is he going to Egypt, and when will I go there instead of him? (unverified)
- А почему он поедет в Египет, а я когда поеду туда вместо него -> Механизм внимания (attention) (unverified)

## Slide 6

Native text objects: 21; connectors: 17; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.1in, 4.9in) h 0
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (6.7in, 5.8in) bos - begin of sentence eos - end of sentence
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 (unverified)
- y -> <bos> (unverified)

## Slide 7

Native text objects: 23; connectors: 21; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.5in, 3.2in) w 1
- (1.4in, 4.1in) s(h t , h 0 )
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.1in, 4.9in) h 0
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (6.7in, 5.8in) bos - begin of sentence eos - end of sentence
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (12.0in, 7.0in) 4/25

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 (unverified)
- y -> <bos> (unverified)
- s(h t , h 0 ) -> h 1 (unverified)
- w 1 -> <eos> (unverified)
- w 1 -> s(h t , h 0 ) (unverified)

## Slide 8

Native text objects: 29; connectors: 27; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (0.6in, 1.6in) w i = s(h i e ,h 0 d ) = (h i e ) T * h 0 d ,      i = 1,2, …, 5
- (9.5in, 2.0in) a
- (11.3in, 2.4in) b
- (3.3in, 2.6in) a = [ a 1 , a 2 , ..., a n ] T b = [ b 1 , b 2 , ..., b n ] T
- (9.5in, 2.9in) α
- (1.5in, 3.2in) w 1
- (10.1in, 3.2in) w
- (3.2in, 3.5in) w = a T * b = ∑ a * b = |a| * |b| * cos α
- (1.4in, 4.1in) s(h t , h 0 )
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.1in, 4.9in) h 0
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (6.7in, 5.8in) bos - begin of sentence eos - end of sentence
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 (unverified)
- y -> <bos> (unverified)
- s(h t , h 0 ) -> h 1 (unverified)
- a = [ a 1 , a 2 , ..., a n ] T b = [ b 1 , b 2 , ..., b n ] T -> <eos> (unverified)
- w 1 -> s(h t , h 0 ) (unverified)
- a -> α (unverified)
- α -> w (unverified)
- a -> w (unverified)
- α -> w (unverified)
- a -> w (unverified)
- α -> b (unverified)

## Slide 9

Native text objects: 24; connectors: 24; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (0.1in, 3.2in) w i = s(h i e , h 0 d ) i = 1, 2, …, 5
- (1.5in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- y -> <bos> (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- w 2 -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 3 (unverified)
- w 2 -> s(h 2 e , h 0 d ) (unverified)

## Slide 10

Native text objects: 28; connectors: 31; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (0.1in, 3.2in) w i = s(h i e , h 0 d ) i = 1, 2, …, 5
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- y -> <bos> (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- w 3 -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)
- w i = s(h i e , h 0 d ) i = 1, 2, …, 5 -> w 4 (unverified)

## Slide 11

Native text objects: 33; connectors: 34; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.4in, 2.4in) α 1
- (2.7in, 2.3in) α 2
- (3.4in, 2.3in) α 3
- (4.1in, 2.3in) α 4
- (1.4in, 2.8in) SoftMax
- (0.1in, 3.2in) w i = s(h i e , h 0 d ) i = 1, 2, …, 5
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- y -> <bos> (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- SoftMax -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)

## Slide 12

Native text objects: 34; connectors: 34; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.4in, 2.0in) c 0 = ∑ α i * h i e
- (1.4in, 2.4in) α 1
- (2.7in, 2.3in) α 2
- (3.3in, 2.4in) α 3
- (4.1in, 2.3in) α 4
- (1.4in, 2.8in) SoftMax
- (0.1in, 3.2in) w i = s(h i e , h 0 d ) i = 1, 2, …, 5
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- y -> <bos> (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- SoftMax -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)

## Slide 13

Native text objects: 37; connectors: 34; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.4in, 2.0in) c 0 = ∑ α i * h i e
- (1.4in, 2.4in) α 1
- (2.7in, 2.3in) α 2
- (3.3in, 2.4in) α 3
- (4.1in, 2.3in) α 4
- (1.4in, 2.8in) SoftMax
- (0.1in, 3.2in) w i = s(h i e , h 0 d ) i = 1, 2, …, 5
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (5.6in, 4.3in) c 0
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.4in, 4.8in) h 1 d = RNN( [ v 1 , c 0 ] , h 0 d )
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y (unverified)
- y -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- c 0 -> h 1 d (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- SoftMax -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)

## Slide 14

Native text objects: 41; connectors: 36; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.4in, 2.0in) c 0 = ∑ α i * h i e
- (1.4in, 2.4in) α 1
- (2.7in, 2.3in) α 2
- (3.3in, 2.4in) α 3
- (4.1in, 2.3in) α 4
- (6.3in, 2.2in) argmax
- (1.4in, 2.8in) SoftMax
- (0.1in, 3.2in) w i = s(h i e , h 0 d ) i = 1, 2, …, 5
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (5.7in, 3.2in) SM
- (6.5in, 3.2in) SoftMax
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (5.8in, 4.1in) fc
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (5.6in, 4.3in) c 0
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.4in, 4.8in) h 1 d = RNN( [ v 1 , c 0 ] , h 0 d )
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y (unverified)
- y -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- SoftMax -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)
- SM -> fc (unverified)

## Slide 15

Native text objects: 41; connectors: 36; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.4in, 2.0in) c 0 = ∑ α i * h i e
- (1.4in, 2.4in) α 1
- (2.7in, 2.3in) α 2
- (3.3in, 2.4in) α 3
- (4.1in, 2.3in) α 4
- (6.3in, 2.2in) argmax
- (-0.7in, 3.1in) Attention (внимание)
- (1.4in, 2.8in) SoftMax
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (5.7in, 3.2in) SM
- (6.5in, 3.2in) SoftMax
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (5.8in, 4.1in) fc
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (5.6in, 4.3in) c 0
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.4in, 4.8in) h 1 d = RNN( [ v 1 , c 0 ] , h 0 d )
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y (unverified)
- y -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- SoftMax -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)
- SM -> fc (unverified)

## Slide 16

Native text objects: 8; connectors: 3; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Структура сети определяет ее функциональность
- (6.6in, 3.3in) x 1
- (7.6in, 3.5in) 1
- (9.6in, 3.9in) y
- (8.1in, 4.2in) ∑
- (6.6in, 4.5in) x 2
- (7.6in, 4.7in) 1

### Possible connector endpoints (spatial inference)

- ∑ -> y (unverified)
- x 1 -> ∑ (unverified)
- x 2 -> 1 (unverified)

## Slide 17

Native text objects: 13; connectors: 10; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Структура сети определяет ее функциональность
- (5.1in, 2.9in) Фрагмент нейронной сети
- (4.2in, 3.3in) …
- (7.2in, 3.2in) x 1
- (7.6in, 3.5in) 1
- (9.2in, 3.9in) y
- (9.8in, 3.9in) Фрагмент нейронной сети
- (8.1in, 4.2in) ∑
- (5.2in, 4.7in) Фрагмент нейронной сети
- (7.1in, 4.4in) x 2
- (7.6in, 4.7in) 1
- (4.2in, 5.1in) …

### Possible connector endpoints (spatial inference)

- ∑ -> y (unverified)
- x 1 -> ∑ (unverified)
- x 2 -> 1 (unverified)

## Slide 18

Native text objects: 41; connectors: 36; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.4in, 2.0in) c 0 = ∑ α i * h i e
- (1.4in, 2.4in) α 1
- (2.7in, 2.3in) α 2
- (3.3in, 2.4in) α 3
- (4.1in, 2.3in) α 4
- (6.3in, 2.2in) argmax
- (-0.7in, 3.1in) Attention (внимание)
- (1.4in, 2.8in) SoftMax
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (5.7in, 3.2in) SM
- (6.5in, 3.2in) SoftMax
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (5.8in, 4.1in) fc
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (5.6in, 4.3in) c 0
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.4in, 4.8in) h 1 d = RNN( [ v 1 , c 0 ] , h 0 d )
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y (unverified)
- y -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- SoftMax -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)
- SM -> fc (unverified)

## Slide 19

Native text objects: 2; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Механизм внимания (attention)

## Slide 20

Native text objects: 44; connectors: 39; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention
- (1.4in, 2.0in) c 0 = ∑ α i * h i e
- (1.4in, 2.4in) α 1
- (2.7in, 2.3in) α 2
- (3.3in, 2.4in) α 3
- (4.1in, 2.3in) α 4
- (6.3in, 2.2in) argmax
- (-0.7in, 3.1in) Attention (внимание)
- (1.4in, 2.8in) SoftMax
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (5.7in, 3.2in) SM
- (6.5in, 3.2in) SoftMax
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (5.8in, 4.1in) fc
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (5.6in, 4.3in) c 0
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.2in, 4.8in) h 2 d = RNN( [ v 2 , c 1 ] , h 1 d )
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (6.6in, 5.6in) y 2
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (6.7in, 6.4in) I

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y (unverified)
- y -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- SoftMax -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)
- SM -> fc (unverified)
- h 1 d -> h 2 d (unverified)
- h 2 d -> y 2 (unverified)
- y 2 -> I (unverified)

## Slide 21

Native text objects: 47; connectors: 48; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Качество работы механизма вниамния
- (1.4in, 2.0in) c 0 = ∑ α i * h i e
- (1.4in, 2.4in) α 1
- (2.7in, 2.3in) α 2
- (3.3in, 2.4in) α 3
- (4.1in, 2.3in) α 4
- (-0.7in, 3.1in) Attention (внимание)
- (1.4in, 2.8in) SoftMax
- (2.0in, 3.2in) w 1
- (2.9in, 3.1in) w 2
- (3.4in, 3.1in) w 3
- (4.1in, 3.1in) w 4
- (5.7in, 3.2in) SM
- (6.5in, 3.2in) SM
- (7.3in, 3.2in) SM
- (2.5in, 3.5in) s(h 2 e , h 0 d )
- (3.9in, 3.5in) s(h 2 e , h 0 d )
- (5.8in, 4.1in) fc
- (6.6in, 4.1in) fc
- (7.4in, 4.1in) fc
- (1.4in, 4.1in) s(h 1 e , h 0 d )
- (2.8in, 4.1in) s(h 1 e , h 0 d )
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.3in, 4.9in) h 3 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.4in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (6.7in, 6.4in) I
- (7.5in, 6.4in) filming

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y 1 (unverified)
- y 1 -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- s(h 1 e , h 0 d ) -> h 1 (unverified)
- SoftMax -> <eos> (unverified)
- w 1 -> s(h 1 e , h 0 d ) (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 2 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- s(h 1 e , h 0 d ) -> h 3 (unverified)
- s(h 2 e , h 0 d ) -> h 4 (unverified)
- w 3 -> s(h 1 e , h 0 d ) (unverified)
- SM -> fc (unverified)
- h 1 d -> h 2 d (unverified)
- h 2 d -> y 2 (unverified)
- y 2 -> I (unverified)
- fc -> h 2 d (unverified)
- SM -> fc (unverified)
- h 2 d -> h 3 d (unverified)
- h 3 d -> y 3 (unverified)
- y 3 -> filming (unverified)
- fc -> h 3 d (unverified)
- SM -> fc (unverified)

## Slide 22

Native text objects: 2; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq с attention

## Slide 23

Native text objects: 16; connectors: 12; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)

## Slide 24

Native text objects: 17; connectors: 18; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (0.6in, 2.1in) А почему он поедет в Египет, а я когда поеду туда вместо него
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- А почему он поедет в Египет, а я когда поеду туда вместо него -> self-attention (unverified)
- А почему он поедет в Египет, а я когда поеду туда вместо него -> h 2 (unverified)
- А почему он поедет в Египет, а я когда поеду туда вместо него -> self-attention (unverified)

## Slide 25

Native text objects: 18; connectors: 15; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (1.7in, 3.6in) w 1
- (2.3in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- w 1 -> h 2 (unverified)

## Slide 26

Native text objects: 20; connectors: 18; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (1.7in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (2.3in, 4.0in) s
- (3.0in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- w 1 -> h 2 (unverified)
- w 2 -> s (unverified)
- s -> h 3 (unverified)
- w 1 -> h 3 (unverified)
- w 2 -> s (unverified)

## Slide 27

Native text objects: 22; connectors: 21; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (1.7in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (2.3in, 4.0in) s
- (3.0in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- w 1 -> h 2 (unverified)
- w 2 -> s (unverified)
- s -> h 3 (unverified)
- w 1 -> h 3 (unverified)
- w 2 -> s (unverified)
- s -> h 4 (unverified)
- w 1 -> h 4 (unverified)
- w 3 -> s (unverified)

## Slide 28

Native text objects: 26; connectors: 24; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (1.9in, 2.7in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (2.3in, 3.2in) SoftMax
- (1.7in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (2.3in, 4.0in) s
- (3.0in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- w 1 -> h 2 (unverified)
- w 2 -> s (unverified)
- s -> h 3 (unverified)
- w 1 -> h 3 (unverified)
- SoftMax -> s (unverified)
- s -> h 4 (unverified)
- w 1 -> h 4 (unverified)
- w 3 -> s (unverified)
- α 1 -> α 2 (unverified)
- α 2 -> SoftMax (unverified)

## Slide 29

Native text objects: 27; connectors: 24; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (2.3in, 2.3in) c 1 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e
- (1.9in, 2.7in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (2.3in, 3.2in) SoftMax
- (1.7in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (2.3in, 4.0in) s
- (3.0in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- w 1 -> h 2 (unverified)
- w 2 -> s (unverified)
- s -> h 3 (unverified)
- w 1 -> h 3 (unverified)
- SoftMax -> s (unverified)
- s -> h 4 (unverified)
- w 1 -> h 4 (unverified)
- w 3 -> s (unverified)
- α 1 -> α 2 (unverified)
- α 2 -> SoftMax (unverified)

## Slide 30

Native text objects: 29; connectors: 25; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (1.7in, 2.4in) c 1
- (2.3in, 2.3in) c 1 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e
- (2.3in, 2.8in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (1.7in, 2.8in) h 1
- (2.3in, 3.2in) SoftMax
- (2.1in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (2.3in, 4.0in) s
- (3.0in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- w 1 -> h 2 (unverified)
- w 1 -> s (unverified)
- s -> h 3 (unverified)
- w 1 -> h 3 (unverified)
- SoftMax -> s (unverified)
- s -> h 4 (unverified)
- w 1 -> h 4 (unverified)
- w 3 -> s (unverified)
- α 2 -> SoftMax (unverified)

## Slide 31

Native text objects: 31; connectors: 26; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (1.1in, 2.2in) W
- (1.7in, 2.4in) c 1
- (2.3in, 2.3in) c 1 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e
- (0.4in, 2.5in) H 1 e
- (2.3in, 2.8in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (1.6in, 2.8in) h 1 e
- (2.3in, 3.2in) SoftMax
- (2.1in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (2.3in, 4.0in) s
- (3.0in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- w 1 -> h 2 (unverified)
- w 1 -> s (unverified)
- s -> h 3 (unverified)
- w 1 -> h 3 (unverified)
- SoftMax -> s (unverified)
- s -> h 4 (unverified)
- w 1 -> h 4 (unverified)
- w 3 -> s (unverified)
- α 2 -> SoftMax (unverified)
- h 1 e -> h 1 (unverified)
- H 1 e -> W (unverified)

## Slide 32

Native text objects: 32; connectors: 26; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (1.1in, 2.2in) W
- (1.7in, 2.4in) c 1
- (2.3in, 2.3in) c 1 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e
- (0.4in, 2.5in) H 1 e
- (2.3in, 2.8in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (1.6in, 2.8in) h 1 e
- (-0.7in, 3.1in) Self-attention
- (2.3in, 3.2in) SoftMax
- (2.1in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (2.3in, 4.0in) s
- (3.0in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- w 1 -> h 2 (unverified)
- w 1 -> s (unverified)
- s -> h 3 (unverified)
- w 1 -> h 3 (unverified)
- SoftMax -> s (unverified)
- s -> h 4 (unverified)
- w 1 -> h 4 (unverified)
- w 3 -> s (unverified)
- α 2 -> SoftMax (unverified)
- h 1 e -> h 1 (unverified)
- H 1 e -> W (unverified)

## Slide 33

Native text objects: 30; connectors: 24; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (0.8in, 1.7in) Updated:
- (1.9in, 1.6in) H 1 e
- (1.8in, 2.4in) c 2 = α 1 h 2 e + α 2 h 3 e + α 3 h 4
- (2.3in, 2.8in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (-0.7in, 3.1in) Self-attention
- (1.8in, 3.2in) SoftMax
- (2.1in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (1.8in, 4.0in) s
- (3.0in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- s -> h 1 (unverified)
- w 1 -> s (unverified)
- s -> h 3 (unverified)
- s -> h 3 (unverified)
- SoftMax -> s (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- w 3 -> s (unverified)
- c 2 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 -> SoftMax (unverified)

## Slide 34

Native text objects: 31; connectors: 24; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (0.8in, 1.7in) Updated:
- (1.9in, 1.6in) H 1 e
- (2.6in, 1.6in) H 2 e
- (1.8in, 2.4in) c 2 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e
- (2.3in, 2.8in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (-0.7in, 3.1in) Self-attention
- (1.8in, 3.2in) SoftMax
- (2.1in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (1.8in, 4.0in) s
- (3.0in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 2 (unverified)
- s -> h 1 (unverified)
- w 1 -> s (unverified)
- s -> h 3 (unverified)
- s -> h 3 (unverified)
- SoftMax -> s (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- w 3 -> s (unverified)
- c 2 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e -> SoftMax (unverified)

## Slide 35

Native text objects: 31; connectors: 24; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (0.8in, 1.7in) Updated:
- (1.9in, 1.6in) H 1 e
- (2.6in, 1.6in) H 2 e
- (1.8in, 2.4in) c 1 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e
- (2.3in, 2.8in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (-0.7in, 3.1in) Self-attention
- (1.8in, 3.2in) SoftMax
- (2.1in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (1.8in, 4.0in) s
- (2.5in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 3 (unverified)
- s -> h 1 (unverified)
- w 1 -> s (unverified)
- s -> h 2 (unverified)
- s -> h 3 (unverified)
- w 2 -> s (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- w 3 -> s (unverified)
- c 1 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e -> SoftMax (unverified)

## Slide 36

Native text objects: 32; connectors: 24; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (0.8in, 1.7in) Updated:
- (1.9in, 1.6in) H 1 e
- (2.6in, 1.6in) H 2 e
- (3.5in, 1.6in) H 3 e
- (1.8in, 2.4in) c 1 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e
- (2.3in, 2.8in) α 1
- (2.7in, 2.7in) α 2
- (3.4in, 2.7in) α 3
- (-0.7in, 3.1in) Self-attention
- (1.8in, 3.2in) SoftMax
- (2.1in, 3.6in) w 1
- (2.7in, 3.5in) w 2
- (3.4in, 3.5in) w 3
- (1.8in, 4.0in) s
- (2.5in, 4.0in) s
- (3.7in, 4.0in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- s -> h 3 (unverified)
- s -> h 1 (unverified)
- w 1 -> s (unverified)
- s -> h 2 (unverified)
- s -> h 3 (unverified)
- w 2 -> s (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- w 3 -> s (unverified)
- c 1 = α 1 h 2 e + α 2 h 3 e + α 3 h 4 e -> SoftMax (unverified)

## Slide 37

Native text objects: 22; connectors: 28; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (-0.7in, 3.1in) Self-attention
- (0.4in, 3.6in) Updated:
- (1.5in, 3.5in) H 1 e
- (2.3in, 3.5in) H 2 e
- (3.1in, 3.5in) H 3 e
- (3.8in, 3.4in) H 4 e
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- H 1 e -> h 1 (unverified)
- H 1 e -> h 2 (unverified)
- H 1 e -> h 3 (unverified)
- H 1 e -> h 4 (unverified)
- H 1 e -> h 2 (unverified)
- H 2 e -> h 2 (unverified)
- H 2 e -> h 3 (unverified)
- H 2 e -> h 4 (unverified)
- H 1 e -> h 3 (unverified)
- H 2 e -> h 3 (unverified)
- H 3 e -> h 3 (unverified)
- H 3 e -> h 4 (unverified)
- H 1 e -> h 4 (unverified)
- H 2 e -> h 4 (unverified)
- H 3 e -> h 4 (unverified)
- H 4 e -> h 4 (unverified)

## Slide 38

Native text objects: 3; connectors: 6; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Механизм внимания (attention)
- (2.7in, 3.7in) Why is he going to Egypt , and when will I go there instead of him ?

### Possible connector endpoints (spatial inference)

- Механизм внимания - attention -> Why is he going to Egypt , and when will I go there instead of him ? (unverified)
- Механизм внимания - attention -> Why is he going to Egypt , and when will I go there instead of him ? (unverified)

## Slide 39

Native text objects: 18; connectors: 14; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в декодере
- (4.2in, 4.5in) copy
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)

## Slide 40

Native text objects: 25; connectors: 17; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в декодере
- (5.9in, 2.4in) argmax
- (5.7in, 3.2in) SM
- (6.5in, 3.2in) SoftMax
- (5.8in, 4.1in) fc
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (8.2in, 4.9in) h 1 d = RNN(y 1 ,h 0 d )
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- SM -> fc (unverified)
- h 1 d -> y (unverified)

## Slide 41

Native text objects: 28; connectors: 19; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (5.8in, 1.9in) I
- (4.4in, 2.6in) argmax
- (4.3in, 3.3in) SoftMax
- (5.7in, 3.2in) SM
- (5.8in, 4.1in) fc
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (6.6in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- SM -> fc (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y (unverified)
- h 2 d -> y (unverified)

## Slide 42

Native text objects: 27; connectors: 21; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (5.3in, 2.9in) c 1 = α 1 * h 1 d
- (4.8in, 3.4in) α 1 = 1
- (5.8in, 3.6in) SM
- (5.8in, 4.1in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (6.6in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y (unverified)
- h 2 d -> y (unverified)
- s -> h 1 d (unverified)
- s -> h 2 d (unverified)
- SM -> s (unverified)
- c 1 = α 1 * h 1 d -> SM (unverified)

## Slide 43

Native text objects: 28; connectors: 19; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (5.8in, 1.9in) I
- (4.4in, 2.6in) argmax
- (4.3in, 3.3in) SoftMax
- (5.7in, 3.2in) SM
- (5.8in, 4.1in) fc
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (6.6in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- SM -> fc (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y (unverified)
- h 2 d -> y (unverified)

## Slide 44

Native text objects: 34; connectors: 23; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (5.8in, 1.8in) I
- (6.4in, 1.9in) filming
- (4.6in, 2.5in) argmax
- (4.5in, 3.3in) SoftMax
- (5.7in, 3.2in) SM
- (6.6in, 3.2in) SM
- (5.8in, 4.1in) fc
- (6.7in, 4.1in) fc
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.5in, 4.9in) h 2 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.5in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (7.4in, 6.3in) filming
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- SM -> fc (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y 1 (unverified)
- h 2 d -> y 2 (unverified)
- fc -> h 2 d (unverified)
- SM -> fc (unverified)
- h 2 d -> y 3 (unverified)

## Slide 45

Native text objects: 30; connectors: 25; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (5.5in, 3.8in) w 1
- (6.3in, 3.9in) w 2
- (5.8in, 4.1in) s
- (6.7in, 4.1in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.5in, 4.9in) h 3 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.5in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (7.4in, 6.3in) filming
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y 1 (unverified)
- h 2 d -> y 2 (unverified)
- h 3 d -> y 3 (unverified)
- h 2 d -> h 3 d (unverified)
- s -> h 1 d (unverified)
- s -> h 3 d (unverified)
- w 1 -> s (unverified)
- s -> h 2 d (unverified)
- s -> h 3 d (unverified)
- w 2 -> s (unverified)

## Slide 46

Native text objects: 34; connectors: 27; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (5.1in, 2.5in) c 3 = α 1 * h 1 d + α 2 *  h 2 d
- (5.2in, 3.1in) α 1
- (7.0in, 2.9in) α 2
- (5.8in, 3.4in) SoftMax
- (5.5in, 3.8in) w 1
- (6.3in, 3.9in) w 2
- (5.8in, 4.1in) s
- (6.7in, 4.1in) s
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.5in, 4.9in) h 3 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.5in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (7.4in, 6.3in) filming
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y 1 (unverified)
- h 2 d -> y 2 (unverified)
- h 3 d -> y 3 (unverified)
- h 2 d -> h 3 d (unverified)
- s -> h 1 d (unverified)
- s -> h 3 d (unverified)
- w 1 -> s (unverified)
- s -> h 2 d (unverified)
- s -> h 3 d (unverified)
- w 2 -> s (unverified)
- c 3 = α 1 * h 1 d + α 2 *  h 2 d -> SoftMax (unverified)

## Slide 47

Native text objects: 37; connectors: 29; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (5.1in, 2.5in) c 3 = α 1 * h 1 d + α 2 *  h 2 d
- (5.2in, 3.1in) α 1
- (7.0in, 2.9in) α 2
- (5.8in, 3.4in) SoftMax
- (7.5in, 3.5in) H 3 d
- (5.5in, 3.8in) w 1
- (6.3in, 3.9in) w 2
- (5.8in, 4.1in) s
- (6.7in, 4.1in) s
- (7.4in, 4.1in) c 3
- (7.7in, 4.1in) h 3 d
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.5in, 4.9in) h 3 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.5in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (7.4in, 6.3in) filming
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y 1 (unverified)
- h 2 d -> y 2 (unverified)
- h 3 d -> y 3 (unverified)
- h 2 d -> h 3 d (unverified)
- s -> h 1 d (unverified)
- s -> h 3 d (unverified)
- w 1 -> s (unverified)
- s -> h 2 d (unverified)
- s -> h 3 d (unverified)
- w 2 -> s (unverified)
- c 3 = α 1 * h 1 d + α 2 *  h 2 d -> SoftMax (unverified)
- c 3 -> h 3 d (unverified)
- H 3 d -> c 3 (unverified)

## Slide 48

Native text objects: 40; connectors: 31; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (8.4in, 1.4in) cinema
- (5.1in, 2.5in) c 3 = α 1 * h 1 d + α 2 *  h 2 d
- (8.4in, 2.6in) SM
- (5.2in, 3.1in) α 1
- (7.0in, 2.9in) α 2
- (5.8in, 3.4in) SoftMax
- (7.5in, 3.5in) H 3 d
- (8.5in, 3.5in) fc
- (5.5in, 3.8in) w 1
- (6.3in, 3.9in) w 2
- (5.8in, 4.1in) s
- (6.7in, 4.1in) s
- (7.4in, 4.1in) c 3
- (7.7in, 4.1in) h 3 d
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.5in, 4.9in) h 3 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.5in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (7.4in, 6.3in) filming
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y 1 (unverified)
- h 2 d -> y 2 (unverified)
- h 3 d -> y 3 (unverified)
- h 2 d -> h 3 d (unverified)
- s -> h 1 d (unverified)
- s -> h 2 d (unverified)
- w 1 -> s (unverified)
- s -> h 2 d (unverified)
- s -> h 3 d (unverified)
- w 2 -> s (unverified)
- c 3 = α 1 * h 1 d + α 2 *  h 2 d -> SoftMax (unverified)
- c 3 -> h 3 d (unverified)
- H 3 d -> c 3 (unverified)
- H 3 d -> fc (unverified)
- SM -> fc (unverified)

## Slide 49

Native text objects: 52; connectors: 41; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention
- (8.7in, 0.8in) <eos>
- (8.7in, 2.1in) SM
- (8.7in, 2.0in) SM
- (5.1in, 2.5in) c 3 = α 1 * h 1 d + α 2 *  h 2 d + α 3 *  h 3 d
- (8.8in, 2.6in) fc
- (8.8in, 2.6in) fc
- (5.2in, 3.1in) α 1
- (7.0in, 2.9in) α 2
- (7.9in, 3.0in) α 3
- (5.8in, 3.4in) SoftMax
- (8.4in, 3.5in) H 4 d
- (5.5in, 3.8in) w 1
- (6.3in, 3.9in) w 2
- (7.2in, 3.9in) w 3
- (5.8in, 4.1in) s
- (6.7in, 4.1in) s
- (7.5in, 4.1in) s
- (8.2in, 4.2in) c 4
- (8.2in, 4.1in) c 4
- (8.3in, 4.2in) c 4
- (8.6in, 4.2in) h 4 d
- (8.6in, 4.1in) h 4 d
- (8.6in, 4.1in) h 4 d
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.5in, 4.9in) h 3 d
- (8.5in, 4.9in) h 4 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.5in, 5.6in) y 3
- (8.4in, 5.6in) y 4
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (6.7in, 6.4in) I
- (7.4in, 6.3in) filming
- (8.3in, 6.3in) cinema
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 0 d -> h 1 d (unverified)
- h 1 d -> h 2 d (unverified)
- h 1 d -> y 1 (unverified)
- h 2 d -> y 2 (unverified)
- h 3 d -> y 3 (unverified)
- h 2 d -> h 3 d (unverified)
- h 4 d -> y 4 (unverified)
- h 3 d -> h 4 d (unverified)
- s -> h 1 d (unverified)
- s -> h 4 d (unverified)
- s -> h 2 d (unverified)
- s -> h 4 d (unverified)
- s -> h 4 d (unverified)
- s -> h 3 d (unverified)
- s -> h 4 d (unverified)
- w 1 -> s (unverified)
- SoftMax -> s (unverified)
- w 3 -> s (unverified)
- c 3 = α 1 * h 1 d + α 2 *  h 2 d + α 3 *  h 3 d -> SoftMax (unverified)
- s -> h 4 d (unverified)
- c 4 -> h 4 d (unverified)
- H 4 d -> c 4 (unverified)
- fc -> H 4 d (unverified)
- c 4 -> h 4 d (unverified)
- fc -> H 4 d (unverified)
- c 4 -> h 4 d (unverified)

## Slide 50

Native text objects: 6; connectors: 7; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Attention c Self-attentiona  декодера
- (0.6in, 2.1in) А почему он поедет в Египет , а я когда поеду туда вместо него
- (3.2in, 3.1in) Cross-Attention
- (4.2in, 4.2in) Self-attention decoder
- (0.7in, 4.9in) Why is he going to Egypt , and when will I go there instead of him ?

### Possible connector endpoints (spatial inference)

- Why is he going to Egypt , and when will I go there instead of him ? -> Self-attention decoder (unverified)
- Why is he going to Egypt , and when will I go there instead of him ? -> Self-attention decoder (unverified)

## Slide 51

Native text objects: 32; connectors: 27; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Attention с Self-attention декодера
- (1.5in, 2.9in) c 0 = ∑ α i * h i e
- (6.0in, 2.9in) I
- (0.2in, 3.3in) Attention
- (1.5in, 3.3in) SoftMax
- (5.8in, 3.3in) SM
- (1.8in, 3.8in) s
- (2.4in, 3.8in) s
- (3.1in, 3.8in) s
- (3.8in, 3.8in) s
- (5.6in, 4.3in) c 0
- (5.9in, 4.2in) fc
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.4in, 4.8in) h 1 d = RNN( [ y 1 , a 0 ] , h 0 d )
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y (unverified)
- y -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- s -> h 1 (unverified)
- c 0 = ∑ α i * h i e -> <eos> (unverified)
- s -> h 3 (unverified)
- s -> h 2 (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- SM -> fc (unverified)

## Slide 52

Native text objects: 36; connectors: 32; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Attention с Self-attention декодера
- (1.5in, 2.9in) c 0 = ∑ α i * h i e
- (6.0in, 2.9in) I
- (6.5in, 2.9in) filming
- (0.2in, 3.3in) Attention
- (1.5in, 3.3in) SoftMax
- (5.8in, 3.3in) SM
- (6.5in, 3.3in) SM
- (1.8in, 3.8in) s
- (2.4in, 3.8in) s
- (3.1in, 3.8in) s
- (3.8in, 3.8in) s
- (5.9in, 4.2in) fc
- (6.6in, 4.2in) fc
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (6.7in, 6.5in) I

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y 1 (unverified)
- y 1 -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- s -> h 1 (unverified)
- c 0 = ∑ α i * h i e -> <eos> (unverified)
- s -> h 3 (unverified)
- s -> h 2 (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- SM -> fc (unverified)
- h 1 d -> h 2 d (unverified)
- fc -> h 2 d (unverified)
- SM -> fc (unverified)
- h 2 d -> y 2 (unverified)
- y 2 -> I (unverified)

## Slide 53

Native text objects: 41; connectors: 36; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Attention с Self-attention декодера
- (1.5in, 2.9in) c 0 = ∑ α i * h i e
- (6.0in, 2.9in) I
- (6.5in, 2.9in) filming
- (0.2in, 3.3in) Attention
- (1.5in, 3.3in) SoftMax
- (5.8in, 3.3in) SM
- (6.5in, 3.3in) SM
- (1.8in, 3.8in) s
- (2.4in, 3.8in) s
- (3.1in, 3.8in) s
- (3.8in, 3.8in) s
- (5.9in, 4.2in) fc
- (6.6in, 4.1in) fc
- (7.1in, 4.3in) h 3 d = RNN( [ y 3 , a 2 ] , h 2 d )
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.3in, 4.9in) h 3 d
- (7.0in, 5.2in) a 2
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.4in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (6.7in, 6.5in) I
- (7.2in, 6.5in) filming

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y 1 (unverified)
- y 1 -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- fc -> h 1 d (unverified)
- s -> h 1 (unverified)
- c 0 = ∑ α i * h i e -> <eos> (unverified)
- s -> h 3 (unverified)
- s -> h 2 (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- SM -> fc (unverified)
- h 1 d -> h 2 d (unverified)
- fc -> h 2 d (unverified)
- SM -> fc (unverified)
- h 2 d -> y 2 (unverified)
- y 2 -> I (unverified)
- h 3 d -> y 3 (unverified)
- y 3 -> filming (unverified)
- h 2 d -> h 3 d (unverified)

## Slide 54

Native text objects: 44; connectors: 42; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Attention с Self-attention декодера
- (7.6in, 2.2in) cinema
- (5.7in, 2.5in) c 3 = ∑ α i * h i e
- (7.6in, 2.7in) SM
- (1.5in, 2.9in) c 0 = ∑ α i * h i e
- (0.2in, 3.3in) Attention
- (1.5in, 3.3in) SoftMax
- (4.5in, 3.2in) Self-attention
- (5.8in, 3.4in) SoftMax
- (7.7in, 3.3in) fc
- (1.8in, 3.8in) s
- (2.4in, 3.8in) s
- (3.1in, 3.8in) s
- (3.8in, 3.8in) s
- (5.8in, 4.1in) s
- (6.7in, 4.1in) s
- (7.2in, 4.1in) c 3
- (7.6in, 4.1in) h 3 d
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.3in, 4.9in) h 3 d
- (7.0in, 5.2in) a 2
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.4in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (6.7in, 6.5in) I
- (7.2in, 6.5in) filming

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y 1 (unverified)
- y 1 -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- s -> h 1 (unverified)
- c 0 = ∑ α i * h i e -> <eos> (unverified)
- s -> h 3 (unverified)
- s -> h 2 (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- h 1 d -> h 2 d (unverified)
- h 2 d -> y 2 (unverified)
- y 2 -> I (unverified)
- h 3 d -> y 3 (unverified)
- y 3 -> filming (unverified)
- h 2 d -> h 3 d (unverified)
- s -> h 1 d (unverified)
- s -> h 2 d (unverified)
- s -> h 2 d (unverified)
- s -> h 3 d (unverified)
- c 3 = ∑ α i * h i e -> SoftMax (unverified)
- c 3 = ∑ α i * h i e -> SoftMax (unverified)
- fc -> h 3 d (unverified)
- c 3 -> h 3 d (unverified)

## Slide 55

Native text objects: 48; connectors: 47; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Attention с Self-attention декодера
- (8.5in, 2.2in) <eos>
- (5.7in, 2.5in) c 3 = ∑ α i * h i e
- (8.5in, 2.8in) SM
- (1.5in, 2.9in) c 0 = ∑ α i * h i e
- (0.2in, 3.3in) Attention
- (1.5in, 3.3in) SoftMax
- (4.5in, 3.2in) Self-attention
- (5.8in, 3.4in) SoftMax
- (8.6in, 3.3in) fc
- (1.8in, 3.8in) s
- (2.4in, 3.8in) s
- (3.1in, 3.8in) s
- (3.8in, 3.8in) s
- (5.8in, 4.1in) s
- (6.7in, 4.1in) s
- (7.4in, 4.2in) s
- (8.1in, 4.2in) c 4
- (8.5in, 4.2in) h 4 d
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.3in, 4.9in) h 3 d
- (8.3in, 4.9in) h 3 d
- (7.0in, 5.2in) a 2
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.4in, 5.6in) y 3
- (8.3in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (6.7in, 6.5in) I
- (7.2in, 6.5in) filming
- (8.1in, 6.5in) cinema

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 4 -> h 0 d (unverified)
- h 1 d -> y 1 (unverified)
- y 1 -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- s -> h 1 (unverified)
- c 0 = ∑ α i * h i e -> <eos> (unverified)
- s -> h 3 (unverified)
- s -> h 2 (unverified)
- s -> h 4 (unverified)
- s -> h 4 (unverified)
- h 1 d -> h 2 d (unverified)
- h 2 d -> y 2 (unverified)
- y 2 -> I (unverified)
- h 3 d -> y 3 (unverified)
- y 3 -> filming (unverified)
- h 2 d -> h 3 d (unverified)
- s -> h 1 d (unverified)
- s -> h 2 d (unverified)
- s -> h 2 d (unverified)
- s -> h 3 d (unverified)
- SoftMax -> s (unverified)
- c 3 = ∑ α i * h i e -> SoftMax (unverified)
- c 3 = ∑ α i * h i e -> SoftMax (unverified)
- s -> h 3 d (unverified)
- h 3 d -> y 3 (unverified)
- s -> h 3 d (unverified)
- fc -> h 4 d (unverified)
- c 4 -> h 3 d (unverified)
- c 3 = ∑ α i * h i e -> SoftMax (unverified)

## Slide 56

Native text objects: 7; connectors: 13; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Механизм внимания (attention)
- (4.4in, 1.5in) Self-attention decoder
- (0.6in, 2.1in) А почему он поедет в Египет , а я когда поеду туда вместо него
- (3.2in, 3.1in) Cross-Attention
- (4.2in, 4.2in) Self-attention decoder
- (0.7in, 4.9in) Why is he going to Egypt , and when will I go there instead of him ?

### Possible connector endpoints (spatial inference)

- Why is he going to Egypt , and when will I go there instead of him ? -> Self-attention decoder (unverified)
- Why is he going to Egypt , and when will I go there instead of him ? -> Self-attention decoder (unverified)
- А почему он поедет в Египет , а я когда поеду туда вместо него -> Механизм внимания (attention) (unverified)
- Cross-Attention -> Механизм внимания (attention) (unverified)

## Slide 57

Native text objects: 21; connectors: 28; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) self-attention в кодере
- (0.4in, 3.6in) Updated:
- (1.5in, 3.5in) H 1 e
- (2.3in, 3.5in) H 2 e
- (3.1in, 3.5in) H 3 e
- (3.8in, 3.4in) H 4 e
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- H 1 e -> h 1 (unverified)
- H 1 e -> h 2 (unverified)
- H 1 e -> h 3 (unverified)
- H 1 e -> h 4 (unverified)
- H 1 e -> h 2 (unverified)
- H 2 e -> h 2 (unverified)
- H 2 e -> h 3 (unverified)
- H 2 e -> h 4 (unverified)
- H 1 e -> h 3 (unverified)
- H 2 e -> h 3 (unverified)
- H 3 e -> h 3 (unverified)
- H 3 e -> h 4 (unverified)
- H 1 e -> h 4 (unverified)
- H 2 e -> h 4 (unverified)
- H 3 e -> h 4 (unverified)
- H 4 e -> h 4 (unverified)

## Slide 58

Native text objects: 51; connectors: 58; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Attention  с Self-attention
- (1.5in, 1.5in) c 0 = ∑ α i * h i e
- (0.2in, 1.9in) Attention
- (1.5in, 1.9in) SoftMax
- (1.8in, 2.4in) s
- (2.4in, 2.4in) s
- (3.1in, 2.4in) s
- (3.8in, 2.4in) s
- (7.6in, 2.2in) cinema
- (5.7in, 2.5in) c 3 = ∑ α i * h i e
- (7.6in, 2.7in) SM
- (-0.7in, 3.1in) Self-attention
- (4.5in, 3.2in) Self-attention
- (5.8in, 3.4in) SoftMax
- (7.7in, 3.3in) fc
- (0.4in, 3.6in) Updated:
- (1.5in, 3.5in) H 1 e
- (2.3in, 3.5in) H 2 e
- (3.1in, 3.5in) H 3 e
- (3.8in, 3.4in) H 4 e
- (4.6in, 4.3in) copy
- (5.8in, 4.1in) s
- (6.7in, 4.1in) s
- (7.2in, 4.1in) c 4
- (7.6in, 4.1in) h 4 d
- (1.0in, 4.9in) h 0
- (1.7in, 4.9in) h 1
- (2.4in, 4.9in) h 2
- (3.1in, 4.9in) h 3
- (3.8in, 4.9in) h 4
- (5.0in, 4.9in) h 0 d
- (5.8in, 4.9in) h 1 d
- (6.6in, 4.9in) h 2 d
- (7.3in, 4.9in) h 3 d
- (7.0in, 5.2in) a 2
- (1.7in, 5.6in) x 1
- (2.4in, 5.6in) x 2
- (3.1in, 5.6in) x 3
- (3.8in, 5.6in) x 1
- (5.7in, 5.6in) y 1
- (6.6in, 5.6in) y 2
- (7.4in, 5.6in) y 3
- (0.6in, 5.8in) Embedding
- (1.4in, 6.3in) <bos>
- (2.4in, 6.3in) Я
- (2.8in, 6.3in) снимаю
- (3.6in, 6.3in) <eos>
- (5.6in, 6.4in) <bos>
- (6.7in, 6.5in) I
- (7.2in, 6.5in) filming

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> h 4 (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h 4 -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- H 1 e -> h 1 (unverified)
- H 1 e -> h 2 (unverified)
- H 1 e -> h 3 (unverified)
- H 1 e -> h 4 (unverified)
- H 1 e -> h 2 (unverified)
- H 2 e -> h 2 (unverified)
- H 2 e -> h 3 (unverified)
- H 2 e -> h 4 (unverified)
- H 1 e -> h 3 (unverified)
- H 2 e -> h 3 (unverified)
- H 3 e -> h 3 (unverified)
- H 3 e -> h 4 (unverified)
- H 1 e -> h 4 (unverified)
- H 2 e -> h 4 (unverified)
- H 3 e -> h 4 (unverified)
- H 4 e -> h 4 (unverified)
- s -> H 1 e (unverified)
- c 0 = ∑ α i * h i e -> x 1 (unverified)
- s -> H 3 e (unverified)
- s -> H 2 e (unverified)
- s -> H 4 e (unverified)
- h 1 d -> y 1 (unverified)
- y 1 -> <bos> (unverified)
- h 0 d -> h 1 d (unverified)
- h 1 d -> h 2 d (unverified)
- h 2 d -> y 2 (unverified)
- y 2 -> I (unverified)
- h 3 d -> y 3 (unverified)
- y 3 -> filming (unverified)
- h 2 d -> h 3 d (unverified)
- s -> h 1 d (unverified)
- s -> h 2 d (unverified)
- s -> h 2 d (unverified)
- s -> h 3 d (unverified)
- c 3 = ∑ α i * h i e -> SoftMax (unverified)
- c 3 = ∑ α i * h i e -> SoftMax (unverified)
- fc -> h 4 d (unverified)
- c 4 -> h 3 d (unverified)
- H 4 e -> h 0 d (unverified)

## Slide 59

Native text objects: 47; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Архитектура Seq2Seq
- (0.6in, 1.5in) цепочки данных обрабатываются последовательно и эти вычисления не распараллеливаются  при обучении возникает известная проблема взрывающихся или затухающих град
- (5.0in, 1.5in) Decoder
- (6.5in, 2.2in) argmax
- (7.3in, 2.8in) SM
- (8.0in, 2.8in) SM
- (8.7in, 2.8in) SM
- (10.1in, 2.8in) SM
- (1.4in, 3.7in) Encoder
- (6.5in, 3.6in) SoftMax
- (7.3in, 3.5in) fc
- (8.0in, 3.5in) fc
- (8.7in, 3.5in) fc
- (10.1in, 3.5in) fc
- (1.6in, 4.4in) h 0
- (2.3in, 4.4in) h 1
- (3.0in, 4.4in) h 2
- (3.7in, 4.4in) h 3
- (4.4in, 4.3in) …
- (5.0in, 4.4in) h l
- (6.6in, 4.4in) h 0
- (7.3in, 4.4in) h 1
- (8.0in, 4.4in) h 2
- (8.7in, 4.4in) h 3
- (9.4in, 4.3in) …
- (10.1in, 4.4in) h l
- (1.2in, 5.3in) Embedding
- (2.3in, 5.1in) x 1
- (3.0in, 5.1in) x 2
- (3.7in, 5.1in) x 3
- (4.4in, 5.1in) …
- (5.0in, 5.1in) x 1
- (6.2in, 5.3in) Embedding
- (7.3in, 5.1in) x 1
- (8.0in, 5.1in) x 2
- (8.7in, 5.1in) x 3
- (9.4in, 5.1in) …
- (10.1in, 5.1in) x 1
- (2.1in, 5.8in) <bos>
- (3.0in, 5.8in) Я
- (3.5in, 5.8in) снимаю
- (4.9in, 5.8in) <eos>
- (7.1in, 5.8in) <bos>
- (8.1in, 5.8in) Я
- (8.6in, 5.8in) снимаю
- (9.9in, 5.8in) <eos>

### Possible connector endpoints (spatial inference)

- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> … (unverified)
- h l -> h 0 (unverified)
- … -> h l (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h l -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- h 0 -> h 1 (unverified)
- h 1 -> h 2 (unverified)
- h 2 -> h 3 (unverified)
- h 3 -> … (unverified)
- … -> h l (unverified)
- h 1 -> x 1 (unverified)
- h 2 -> x 2 (unverified)
- h 3 -> x 3 (unverified)
- h l -> x 1 (unverified)
- x 1 -> <bos> (unverified)
- x 2 -> Я (unverified)
- x 3 -> снимаю (unverified)
- x 1 -> <eos> (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- SM -> fc (unverified)
- fc -> h 1 (unverified)
- fc -> h 2 (unverified)
- fc -> h 3 (unverified)
- fc -> h l (unverified)

## Slide 60

Native text objects: 3; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Архитектура
- (0.7in, 2.2in) могут обрабатывать последовательности данных в параллельном режиме

## Slide 61

Native text objects: 3; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Архитектура
- (0.7in, 2.2in) могут обрабатывать последовательности данных в параллельном режиме  ChatGPT (OpenAI)  Gemini (Google DeepMind)  Claude (Anthropic)  Llama (Meta)  DeepSeek  Yand

## Slide 62

Native text objects: 2; connectors: 0; embedded pictures: 1

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Архитектура

## Slide 63

Native text objects: 22; connectors: 7; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер.  QKV Self-Attention
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)

## Slide 64

Native text objects: 28; connectors: 17; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер.  QKV Self-Attention
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (8.5in, 5.8in) s
- (9.3in, 5.8in) s
- (10.1in, 5.8in) s
- (10.9in, 5.8in) s
- (11.8in, 5.8in) s
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.7in, 7.0in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- s -> x 1 (unverified)
- s -> x 1 (unverified)
- s -> x 2 (unverified)
- s -> x 3 (unverified)
- s -> x 4 (unverified)
- s -> x 5 (unverified)
- s -> x 2 (unverified)
- s -> x 2 (unverified)
- s -> x 4 (unverified)
- s -> x 5 (unverified)

## Slide 65

Native text objects: 42; connectors: 27; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер.  QKV Self-Attention
- (4.3in, 1.9in) Output
- (8.6in, 2.1in) w = s(a,b) = a T * b = ∑ a i * b i
- (3.7in, 2.6in) Add & LayerNorm
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query
- (8.3in, 3.7in) q 1
- (9.2in, 3.7in) q 2
- (9.9in, 3.7in) q 3
- (10.8in, 3.7in) q 4
- (11.7in, 3.7in) q 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (8.5in, 5.0in) W q * x 1
- (9.3in, 5.0in) W q * x 2
- (10.1in, 5.0in) W q * x 3
- (11.0in, 5.0in) W q * x 4
- (11.9in, 5.0in) W q * x 5
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> W q * x 1 (unverified)
- q 2 -> W q * x 1 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> W q * x 3 (unverified)
- q 5 -> W q * x 5 (unverified)
- s -> q 1 (unverified)
- s -> q 1 (unverified)
- s -> q 2 (unverified)
- s -> q 3 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)

## Slide 66

Native text objects: 49; connectors: 37; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер.  QKV Self-Attention
- (4.3in, 1.9in) Output
- (8.6in, 2.1in) w = s(a,b) = a T * b = ∑ a i * b i
- (3.7in, 2.6in) Add & LayerNorm
- (8.4in, 2.6in) w 11
- (9.2in, 2.6in) w 12
- (10.0in, 2.6in) w 13
- (10.8in, 2.6in) w 14
- (11.7in, 2.6in) w 15
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> Linear, Wk (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 67

Native text objects: 49; connectors: 37; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер.  QKV Self-Attention
- (4.3in, 1.9in) Output
- (8.6in, 2.1in) w = s(a,b) = a T * b = ∑ a i * b i
- (3.7in, 2.6in) Add & LayerNorm
- (8.4in, 2.6in) w 11
- (9.2in, 2.6in) w 12
- (10.0in, 2.6in) w 13
- (10.8in, 2.6in) w 14
- (11.7in, 2.6in) w 15
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 3 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 3 (unverified)
- s -> q 3 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> Linear, Wk (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 68

Native text objects: 45; connectors: 37; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер.  QKV Self-Attention
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> Linear, Wk (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 69

Native text objects: 46; connectors: 37; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер.  QKV Self-Attention
- (4.3in, 1.9in) Output
- (8.4in, 2.0in) c 1 = ∑ α i * ?
- (3.7in, 2.6in) Add & LayerNorm
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> Linear, Wk (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 70

Native text objects: 53; connectors: 42; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер.  QKV Self-Attention
- (4.3in, 1.9in) Output
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (3.7in, 2.6in) Add & LayerNorm
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 71

Native text objects: 46; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Вычисление QKV Self-Attention
- (0.7in, 1.2in) emb_size
- (0.0in, 2.1in) N
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.8in, 2.9in) X
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 72

Native text objects: 70; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Вычисление QKV Self-Attention
- (0.7in, 1.2in) emb_size
- (3.3in, 1.2in) d_attn
- (5.3in, 1.2in) d_attn
- (0.0in, 2.1in) N
- (2.5in, 2.1in) emb_size
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (2.6in, 2.2in) X
- (4.6in, 2.2in) =
- (4.9in, 2.3in) N
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.8in, 2.9in) X
- (4.6in, 2.9in) W q
- (5.4in, 3.1in) Q = X * W q
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (0.1in, 4.0in) N
- (2.6in, 3.9in) emb_size
- (2.7in, 4.0in) X
- (4.6in, 4.0in) =
- (4.9in, 4.2in) N
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (4.6in, 4.8in) W q
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (0.9in, 4.8in) X
- (5.4in, 5.0in) K = X * W k
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (0.2in, 5.9in) N
- (2.7in, 5.8in) emb_size
- (2.8in, 5.9in) X
- (4.7in, 5.9in) =
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (5.0in, 6.1in) N
- (1.0in, 6.7in) X
- (4.7in, 6.7in) W q
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (5.5in, 6.9in) V = X * W v
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 73

Native text objects: 50; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Вычисление QKV Self-Attention
- (0.5in, 1.2in) d_attn
- (0.0in, 2.1in) N
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (0.1in, 4.0in) N
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (0.9in, 4.8in) K
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (0.2in, 5.9in) N
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (0.9in, 6.8in) V
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 74

Native text objects: 58; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Вычисление QKV Self-Attention
- (0.5in, 1.2in) d_attn
- (2.6in, 1.2in) N
- (4.5in, 1.2in) N
- (0.0in, 2.1in) N
- (1.7in, 1.8in) d_attn
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (1.8in, 2.1in) X
- (3.8in, 2.1in) =
- (4.1in, 2.3in) N
- (2.8in, 2.7in) K T
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (4.6in, 3.1in) W = Q * K T
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (0.1in, 4.0in) N
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (0.9in, 4.8in) K
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (0.2in, 5.9in) N
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (0.9in, 6.8in) V
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 75

Native text objects: 61; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Вычисление QKV Self-Attention
- (0.5in, 1.2in) d_attn
- (2.6in, 1.2in) N
- (4.5in, 1.2in) N
- (0.0in, 2.1in) N
- (1.7in, 1.8in) d_attn
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (1.8in, 2.1in) X
- (3.8in, 2.1in) =
- (4.1in, 2.3in) N
- (2.8in, 2.7in) K T
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (4.6in, 3.1in) W = Q * K T
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (4.7in, 3.4in) N
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (1.6in, 4.3in) A = SoftMax(QK T /√d attn )
- (3.9in, 4.3in) =
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (4.2in, 4.5in) N
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (5.0in, 5.2in) A
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (0.2in, 5.9in) N
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (0.9in, 6.8in) V
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 76

Native text objects: 67; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Вычисление QKV Self-Attention
- (0.5in, 1.2in) d_attn
- (2.6in, 1.2in) N
- (4.5in, 1.2in) N
- (0.0in, 2.1in) N
- (1.7in, 1.8in) d_attn
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (1.8in, 2.1in) X
- (3.8in, 2.1in) =
- (4.1in, 2.3in) N
- (2.8in, 2.7in) K T
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (4.6in, 3.1in) W = Q * K T
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (4.7in, 3.4in) N
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (1.6in, 4.3in) A =SoftMax(QK T /√d attn )
- (3.9in, 4.3in) =
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (4.2in, 4.5in) N
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (5.0in, 5.2in) A
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (0.1in, 6.0in) N
- (1.7in, 5.9in) X
- (2.1in, 5.8in) N
- (4.0in, 5.9in) =
- (4.4in, 5.9in) N
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (0.9in, 6.7in) A
- (2.8in, 6.7in) V
- (5.2in, 6.8in) С
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 77

Native text objects: 56; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Вычисление QKV Self-Attention
- (0.5in, 1.2in) d_attn
- (2.6in, 1.2in) N
- (4.5in, 1.2in) N
- (0.0in, 2.1in) N
- (1.7in, 1.8in) d_attn
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (1.8in, 2.1in) X
- (3.8in, 2.1in) =
- (4.1in, 2.3in) N
- (2.8in, 2.7in) K T
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (4.6in, 3.1in) W = Q * K T
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (4.7in, 3.4in) N
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (1.6in, 4.3in) A =SoftMax(QK T /√d attn ) * V
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 78

Native text objects: 59; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Вычисление QKV Self-Attention
- (0.5in, 1.2in) d_attn
- (2.6in, 1.2in) N
- (4.5in, 1.2in) N
- (0.0in, 2.1in) N
- (1.7in, 1.8in) d_attn
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (1.8in, 2.1in) X
- (3.8in, 2.1in) =
- (4.1in, 2.3in) N
- (2.8in, 2.7in) K T
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (4.6in, 3.1in) W = Q * K T
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (4.7in, 3.4in) N
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (1.7in, 3.9in) A =SoftMax(QK T /√d attn ) * V
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (0.6in, 4.5in) GPT-4: 32768 токенов LLaMA 3.1 : 128000 токенов
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (0.2in, 5.9in) N
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (0.9in, 6.8in) V
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 79

Native text objects: 57; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (0.5in, 1.2in) d_attn
- (2.6in, 1.2in) N
- (4.5in, 1.2in) N
- (0.0in, 2.1in) N
- (1.7in, 1.8in) d_attn
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (1.8in, 2.1in) X
- (3.8in, 2.1in) =
- (4.1in, 2.3in) N
- (2.8in, 2.7in) K T
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (4.6in, 3.1in) W = Q * K T
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (4.7in, 3.4in) N
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (1.7in, 3.9in) A =SoftMax(QK T /√d attn ) * V
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (0.6in, 4.5in) влияние токена А на токен В было бы равно влиянию токена В на токен А
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 80

Native text objects: 58; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (0.5in, 1.2in) d_attn
- (2.6in, 1.2in) N
- (4.5in, 1.2in) N
- (0.0in, 2.1in) N
- (1.7in, 1.8in) d_attn
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (1.8in, 2.1in) X
- (3.8in, 2.1in) =
- (4.1in, 2.3in) N
- (2.8in, 2.7in) K T
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (4.6in, 3.1in) W = Q * K T
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (4.7in, 3.4in) N
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (1.7in, 3.9in) A =SoftMax(QK T /√d attn ) * V
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (0.6in, 4.5in) влияние токена А на токен В было бы равно влиянию токена В на токен А
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (0.7in, 5.9in) Я  снимаю кино
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 81

Native text objects: 53; connectors: 42; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Multi-head Attention
- (4.3in, 1.9in) Output
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (3.7in, 2.6in) Add & LayerNorm
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 82

Native text objects: 3; connectors: 6; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Multi-head Attention
- (0.7in, 3.3in) А почему он поедет в Египет , а я когда поеду туда вместо него

### Possible connector endpoints (spatial inference)

- Трансформер. Multi-head Attention -> А почему он поедет в Египет , а я когда поеду туда вместо него (unverified)
- А почему он поедет в Египет , а я когда поеду туда вместо него -> Трансформер. Multi-head Attention (unverified)

## Slide 83

Native text objects: 53; connectors: 42; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Multi-head Attention
- (4.3in, 1.9in) Output
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (3.7in, 2.6in) Add & LayerNorm
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 84

Native text objects: 5; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (0.8in, 2.7in) emb_size
- (0.0in, 3.6in) N
- (0.9in, 4.5in) X

## Slide 85

Native text objects: 16; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (3.3in, 1.2in) dk
- (4.7in, 1.4in) W q
- (6.7in, 1.3in) dk
- (7.5in, 1.2in) Q 1
- (8.0in, 1.4in) K 1
- (0.4in, 1.7in) dk = emb_size / n
- (5.1in, 1.8in) W k
- (8.3in, 1.7in) V 1
- (2.5in, 2.1in) emb_size
- (5.8in, 2.1in) N
- (5.3in, 2.3in) W v
- (0.8in, 2.7in) emb_size
- (0.0in, 3.6in) N
- (0.9in, 4.5in) X

## Slide 86

Native text objects: 18; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (3.3in, 1.2in) dk
- (4.7in, 1.4in) W q
- (6.7in, 1.3in) dk
- (7.5in, 1.2in) Q 1
- (8.0in, 1.4in) K 1
- (0.4in, 1.7in) dk = emb_size / n
- (5.1in, 1.8in) W k
- (8.3in, 1.7in) V 1
- (9.6in, 1.6in) dk
- (2.5in, 2.1in) emb_size
- (5.8in, 2.1in) N
- (5.3in, 2.3in) W v
- (0.8in, 2.7in) emb_size
- (0.0in, 3.6in) N
- (9.7in, 3.8in) C 1
- (0.9in, 4.5in) X

## Slide 87

Native text objects: 33; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (3.3in, 1.2in) dk
- (4.7in, 1.4in) W q
- (6.7in, 1.3in) dk
- (7.5in, 1.2in) Q 1
- (8.0in, 1.4in) K 1
- (0.4in, 1.7in) dk = emb_size / n
- (5.1in, 1.8in) W k
- (8.3in, 1.7in) V 1
- (9.6in, 1.6in) dk
- (2.5in, 2.1in) emb_size
- (5.8in, 2.1in) N
- (5.3in, 2.3in) W v
- (0.8in, 2.7in) emb_size
- (0.0in, 3.6in) N
- (9.7in, 3.8in) C 1
- (4.1in, 4.1in) …
- (6.6in, 4.1in) …
- (9.3in, 4.3in) …
- (9.7in, 4.2in) n голов внимания (multi-head)
- (0.9in, 4.5in) X
- (3.3in, 4.9in) dk
- (4.7in, 5.0in) W q
- (6.7in, 4.9in) dk
- (7.5in, 4.9in) Q n
- (8.0in, 5.1in) K n
- (8.3in, 5.3in) V n
- (9.6in, 5.3in) dk
- (5.1in, 5.4in) W k
- (5.3in, 5.9in) W v
- (5.8in, 5.7in) N
- (9.7in, 7.5in) C 1

## Slide 88

Native text objects: 29; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (0.5in, 1.2in) dk
- (1.9in, 1.4in) W q
- (3.9in, 1.3in) dk
- (4.7in, 1.2in) Q 1
- (5.2in, 1.4in) K 1
- (2.3in, 1.8in) W k
- (5.5in, 1.7in) V 1
- (6.8in, 1.6in) dk
- (-0.3in, 2.1in) emb_size
- (3.0in, 2.1in) N
- (2.5in, 2.3in) W v
- (6.9in, 3.8in) C 1
- (1.3in, 4.1in) …
- (3.8in, 4.1in) …
- (6.5in, 4.3in) …
- (0.5in, 4.9in) dk
- (1.9in, 5.0in) W q
- (3.9in, 4.9in) dk
- (4.7in, 4.8in) Q n
- (5.2in, 5.1in) K n
- (10.3in, 4.9in) dk * n = emb_size
- (5.5in, 5.3in) V n
- (6.8in, 5.3in) dk
- (2.3in, 5.4in) W k
- (2.5in, 5.9in) W v
- (3.0in, 5.7in) N
- (11.5in, 6.3in) …

## Slide 89

Native text objects: 31; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (0.5in, 1.2in) dk
- (1.9in, 1.4in) W q
- (3.9in, 1.3in) dk
- (4.7in, 1.2in) Q 1
- (5.2in, 1.4in) K 1
- (2.3in, 1.8in) W k
- (5.5in, 1.7in) V 1
- (6.8in, 1.6in) dk
- (-0.3in, 2.1in) emb_size
- (3.0in, 2.1in) N
- (2.5in, 2.3in) W v
- (10.8in, 3.4in) …
- (8.4in, 3.7in) emb_size
- (6.9in, 3.8in) C 1
- (1.3in, 4.1in) …
- (3.8in, 4.1in) …
- (6.5in, 4.3in) …
- (0.5in, 4.9in) dk
- (1.9in, 5.0in) W q
- (3.9in, 4.9in) dk
- (4.7in, 4.8in) Q n
- (5.2in, 5.1in) K n
- (10.3in, 4.9in) dk * n = emb_size
- (5.5in, 5.3in) V n
- (6.8in, 5.3in) dk
- (2.3in, 5.4in) W k
- (2.5in, 5.9in) W v
- (3.0in, 5.7in) N
- (11.5in, 6.3in) …

## Slide 90

Native text objects: 36; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (10.6in, 0.2in) emb_size
- (0.6in, 0.6in) Трансформер. Multi-head Attention
- (0.5in, 1.2in) dk
- (1.9in, 1.4in) W q
- (3.9in, 1.3in) dk
- (4.7in, 1.2in) Q 1
- (5.2in, 1.4in) K 1
- (2.3in, 1.8in) W k
- (5.5in, 1.7in) V 1
- (6.8in, 1.6in) dk
- (-0.3in, 2.1in) emb_size
- (3.0in, 2.1in) N
- (2.5in, 2.3in) W v
- (10.9in, 2.3in) =
- (12.7in, 2.3in) Z
- (10.8in, 3.4in) …
- (8.4in, 3.7in) emb_size
- (6.9in, 3.8in) C 1
- (1.3in, 4.1in) …
- (3.8in, 4.1in) …
- (6.5in, 4.3in) …
- (0.5in, 4.9in) dk
- (1.9in, 5.0in) W q
- (3.9in, 4.9in) dk
- (4.7in, 4.8in) Q n
- (5.2in, 5.1in) K n
- (10.3in, 5.1in) dk * n = emb_size
- (11.0in, 4.8in) x
- (12.7in, 4.9in) W 0
- (5.5in, 5.3in) V n
- (6.8in, 5.3in) dk
- (2.3in, 5.4in) W k
- (2.5in, 5.9in) W v
- (3.0in, 5.7in) N
- (11.5in, 6.3in) …

## Slide 91

Native text objects: 18; connectors: 9; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Блок Add & LayerNorm
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (7.2in, 2.9in) emb_size
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (6.3in, 3.7in) N
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (8.9in, 4.5in) Z
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.2in, 5.2in) emb_size
- (3.2in, 6.3in) Embedding
- (6.3in, 6.2in) N
- (8.9in, 6.7in) X
- (4.0in, 7.0in) Input

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Multi-head Attention -> N (unverified)
- + -> N (unverified)

## Slide 92

Native text objects: 31; connectors: 34; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Блок Add & LayerNorm
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (6.7in, 3.4in) z 1 z 2 … z N
- (3.7in, 3.8in) Add & LayerNorm
- (6.1in, 3.9in) Z =
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.7in, 5.4in) x 1 x 2 … x N
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (6.1in, 6.0in) X =
- (3.2in, 6.3in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (4.0in, 7.0in) Input
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Z = (unverified)
- Multi-head Attention -> X = (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 2 -> x 3 (unverified)
- z 2 -> x 4 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 3 -> x 4 (unverified)
- z 3 -> x 5 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 4 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 5 (unverified)

## Slide 93

Native text objects: 41; connectors: 49; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Блок Add & LayerNorm
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (6.7in, 3.4in) z 1 z 2 … z N
- (3.7in, 3.8in) Add & LayerNorm
- (6.1in, 3.9in) Z =
- (3.7in, 4.4in) Multi-head Attention
- (8.0in, 4.5in) x 1
- (9.0in, 4.5in) x 2
- (9.9in, 4.5in) x 3
- (10.9in, 4.5in) x 4
- (11.8in, 4.5in) x 5
- (8.1in, 4.9in) x 1 + z 1
- (9.0in, 4.9in) x 2 +z 2
- (9.9in, 4.9in) x 3 +z 3
- (10.9in, 4.9in) x 4 +z 4
- (11.8in, 4.9in) x 5 +z 5
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.7in, 5.4in) x 1 x 2 … x N
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (6.1in, 6.0in) X =
- (3.2in, 6.3in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (4.0in, 7.0in) Input
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Z = (unverified)
- Multi-head Attention -> X = (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 2 -> x 3 (unverified)
- z 2 -> x 4 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 3 -> x 4 (unverified)
- z 3 -> x 5 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 4 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 5 (unverified)
- x 1 + z 1 -> z 1 (unverified)
- x 2 +z 2 -> z 2 (unverified)
- x 3 +z 3 -> z 3 (unverified)
- x 4 +z 4 -> z 4 (unverified)
- x 5 +z 5 -> z 5 (unverified)
- x 1 -> x 1 + z 1 (unverified)
- x 2 -> x 2 +z 2 (unverified)
- x 3 -> x 3 +z 3 (unverified)
- x 4 -> x 4 +z 4 (unverified)
- x 5 -> x 5 +z 5 (unverified)
- x 1 + z 1 -> x 1 (unverified)
- x 2 +z 2 -> x 2 (unverified)
- x 3 +z 3 -> x 3 (unverified)
- x 4 +z 4 -> x 4 (unverified)
- x 5 +z 5 -> x 5 (unverified)

## Slide 94

Native text objects: 42; connectors: 49; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Блок Add & LayerNorm
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (6.7in, 3.4in) z 1 z 2 … z N
- (3.7in, 3.8in) Add & LayerNorm
- (6.1in, 3.9in) Z =
- (3.7in, 4.4in) Multi-head Attention
- (8.1in, 4.1in) LayerNorm
- (8.0in, 4.5in) x 1
- (9.0in, 4.5in) x 2
- (9.9in, 4.5in) x 3
- (10.9in, 4.5in) x 4
- (11.8in, 4.5in) x 5
- (8.1in, 4.9in) x 1 +z 1
- (9.0in, 4.9in) x 2 +z 2
- (9.9in, 4.9in) x 3 +z 3
- (10.9in, 4.9in) x 4 +z 4
- (11.8in, 4.9in) x 5 +z 5
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.7in, 5.4in) x 1 x 2 … x N
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (6.1in, 6.0in) X =
- (3.2in, 6.3in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (4.0in, 7.0in) Input
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Z = (unverified)
- Multi-head Attention -> X = (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 2 -> x 3 (unverified)
- z 2 -> x 4 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 3 -> x 4 (unverified)
- z 3 -> x 5 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 4 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 5 (unverified)
- x 1 +z 1 -> z 1 (unverified)
- x 2 +z 2 -> z 2 (unverified)
- x 3 +z 3 -> z 3 (unverified)
- x 4 +z 4 -> z 4 (unverified)
- x 5 +z 5 -> z 5 (unverified)
- x 1 -> x 1 +z 1 (unverified)
- x 2 -> x 2 +z 2 (unverified)
- x 3 -> x 3 +z 3 (unverified)
- x 4 -> x 4 +z 4 (unverified)
- x 5 -> x 5 +z 5 (unverified)
- x 1 +z 1 -> x 1 (unverified)
- x 2 +z 2 -> x 2 (unverified)
- x 3 +z 3 -> x 3 (unverified)
- x 4 +z 4 -> x 4 (unverified)
- x 5 +z 5 -> x 5 (unverified)

## Slide 95

Native text objects: 57; connectors: 49; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Блок Add & LayerNorm
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (6.7in, 3.4in) z 1 z 2 … z N
- (3.7in, 3.8in) Add & LayerNorm
- (6.1in, 3.9in) Z =
- (3.7in, 4.4in) Multi-head Attention
- (8.1in, 4.1in) LayerNorm
- (8.0in, 4.5in) x 1
- (9.0in, 4.5in) x 2
- (9.9in, 4.5in) x 3
- (10.9in, 4.5in) x 4
- (11.8in, 4.5in) x 5
- (8.0in, 5.0in) x 1 +z 1
- (8.0in, 5.0in) x 1 +z 1
- (8.1in, 4.9in) x 1 +z 1
- (8.9in, 5.0in) x 2 +z 2
- (8.9in, 5.0in) x 2 +z 2
- (9.0in, 4.9in) x 2 +z 2
- (9.8in, 5.0in) x 3 +z 3
- (9.9in, 5.0in) x 3 +z 3
- (9.9in, 4.9in) x 3 +z 3
- (10.8in, 5.0in) x 4 +z 4
- (10.8in, 5.0in) x 4 +z 4
- (10.9in, 4.9in) x 4 +z 4
- (11.7in, 5.0in) x 5 +z 5
- (11.8in, 5.0in) x 5 +z 5
- (11.8in, 4.9in) x 5 +z 5
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.9in, 5.1in) x 1 +z 1
- (8.8in, 5.1in) x 2 +z 2
- (9.8in, 5.1in) x 3 +z 3
- (10.7in, 5.1in) x 4 +z 4
- (11.7in, 5.1in) x 5 +z 5
- (6.7in, 5.4in) x 1 x 2 … x N
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (6.1in, 6.0in) X =
- (3.2in, 6.3in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (4.0in, 7.0in) Input
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Z = (unverified)
- Multi-head Attention -> X = (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 2 -> x 3 (unverified)
- z 2 -> x 4 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 3 -> x 4 (unverified)
- z 3 -> x 5 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 4 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 5 (unverified)
- x 1 +z 1 -> z 1 (unverified)
- x 2 +z 2 -> z 2 (unverified)
- x 3 +z 3 -> z 3 (unverified)
- x 4 +z 4 -> z 4 (unverified)
- x 5 +z 5 -> z 5 (unverified)
- x 1 -> x 1 +z 1 (unverified)
- x 2 -> x 2 +z 2 (unverified)
- x 3 -> x 3 +z 3 (unverified)
- x 4 -> x 4 +z 4 (unverified)
- x 5 -> x 5 +z 5 (unverified)
- x 1 +z 1 -> x 1 (unverified)
- x 2 +z 2 -> x 2 (unverified)
- x 3 +z 3 -> x 3 (unverified)
- x 4 +z 4 -> x 4 (unverified)
- x 5 +z 5 -> x 5 (unverified)

## Slide 96

Native text objects: 8; connectors: 6; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Архитектуры post-norm и pre-norm
- (2.4in, 2.0in) post-norm
- (3.7in, 2.7in) LayerNorm
- (3.7in, 3.6in) Add
- (3.7in, 4.4in) Multi-head Attention
- (0.8in, 5.4in) skip (residual) connection
- (3.6in, 5.3in) Embedding

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> Embedding (unverified)
- Add -> Multi-head Attention (unverified)
- LayerNorm -> Add (unverified)
- skip (residual) connection -> Embedding (unverified)
- Add -> Multi-head Attention (unverified)

## Slide 97

Native text objects: 13; connectors: 11; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Архитектуры post-norm и pre-norm
- (2.4in, 2.0in) post-norm
- (7.9in, 2.1in) pre-norm
- (3.7in, 2.7in) LayerNorm
- (9.2in, 2.8in) Add
- (3.7in, 3.6in) Add
- (9.2in, 3.6in) Multi-head Attention
- (3.7in, 4.4in) Multi-head Attention
- (9.2in, 4.4in) LayerNorm
- (0.8in, 5.4in) skip (residual) connection
- (3.6in, 5.3in) Embedding
- (9.1in, 5.4in) Embedding

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> Embedding (unverified)
- Add -> Multi-head Attention (unverified)
- LayerNorm -> Add (unverified)
- skip (residual) connection -> Embedding (unverified)
- Add -> Multi-head Attention (unverified)
- LayerNorm -> Embedding (unverified)
- Multi-head Attention -> LayerNorm (unverified)
- Add -> Multi-head Attention (unverified)
- pre-norm -> LayerNorm (unverified)

## Slide 98

Native text objects: 46; connectors: 57; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Блок Feed Forward
- (4.3in, 1.9in) Output
- (8.1in, 2.2in) Linear2
- (3.7in, 2.6in) Add & LayerNorm
- (8.1in, 2.6in) Dropout
- (6.5in, 2.8in) Feed Forward
- (8.1in, 3.0in) ReLU или GELU
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (8.1in, 3.3in) Linear1
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (8.1in, 4.1in) LayerNorm
- (8.0in, 4.5in) x 1
- (9.0in, 4.5in) x 2
- (9.9in, 4.5in) x 3
- (10.9in, 4.5in) x 4
- (11.8in, 4.5in) x 5
- (6.5in, 5.0in) add
- (8.1in, 4.9in) x 1 +z 1
- (9.0in, 4.9in) x 2 +z 2
- (9.9in, 4.9in) x 3 +z 3
- (10.9in, 4.9in) x 4 +z 4
- (11.8in, 4.9in) x 5 +z 5
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.7in) Multi-head Attention
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (3.2in, 6.3in) Embedding
- (6.4in, 6.5in) embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (4.0in, 7.0in) Input
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 2 -> x 3 (unverified)
- z 2 -> x 4 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 3 -> x 4 (unverified)
- z 3 -> x 5 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 4 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 5 (unverified)
- x 1 +z 1 -> z 1 (unverified)
- x 2 +z 2 -> z 2 (unverified)
- x 3 +z 3 -> z 3 (unverified)
- x 4 +z 4 -> z 4 (unverified)
- x 5 +z 5 -> z 5 (unverified)
- x 1 -> x 1 +z 1 (unverified)
- x 2 -> x 2 +z 2 (unverified)
- x 3 -> x 3 +z 3 (unverified)
- x 4 -> x 4 +z 4 (unverified)
- x 5 -> x 5 +z 5 (unverified)
- x 1 +z 1 -> x 1 (unverified)
- x 2 +z 2 -> x 2 (unverified)
- x 3 +z 3 -> x 3 (unverified)
- x 4 +z 4 -> x 4 (unverified)
- x 5 +z 5 -> x 5 (unverified)
- Linear1 -> LayerNorm (unverified)
- Linear1 -> x 4 (unverified)

## Slide 99

Native text objects: 37; connectors: 58; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Блок Feed Forward
- (4.3in, 1.9in) Output
- (8.1in, 2.2in) Add & LayerNorm
- (3.7in, 2.6in) Add & LayerNorm
- (8.1in, 3.0in) Linear2
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (8.1in, 3.4in) Dropout
- (6.5in, 3.6in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (8.1in, 3.8in) ReLU или GELU
- (3.7in, 4.4in) Multi-head Attention
- (8.1in, 4.2in) Linear1
- (6.5in, 5.0in) add
- (8.1in, 4.9in) Add & LayerNorm
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.7in) Multi-head Attention
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (3.2in, 6.3in) Embedding
- (6.4in, 6.5in) embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (4.0in, 7.0in) Input
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 2 -> x 3 (unverified)
- z 2 -> x 4 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 3 -> x 4 (unverified)
- z 3 -> x 5 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 4 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 5 (unverified)
- Add & LayerNorm -> z 3 (unverified)
- z 1 -> x 1 (unverified)
- z 1 -> z 2 (unverified)
- z 2 -> z 3 (unverified)
- z 3 -> z 4 (unverified)
- z 4 -> z 5 (unverified)
- Linear1 -> z 2 (unverified)
- Linear1 -> Add & LayerNorm (unverified)
- Linear1 -> z 4 (unverified)
- Add & LayerNorm -> Linear2 (unverified)
- Add & LayerNorm -> Linear2 (unverified)
- Add & LayerNorm -> Linear2 (unverified)
- Add & LayerNorm -> Linear2 (unverified)
- Трансформер. Блок Feed Forward -> Add & LayerNorm (unverified)
- Feed Forward -> z 5 (unverified)

## Slide 100

Native text objects: 21; connectors: 18; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Архитектуры post-norm и pre-norm
- (7.6in, 1.1in) pre-norm
- (2.4in, 1.2in) post-norm
- (9.2in, 1.8in) Add
- (3.7in, 1.8in) LayerNorm
- (3.7in, 2.6in) Add
- (9.1in, 2.7in) Feed Forward
- (1.3in, 3.0in) Encoder
- (6.8in, 2.8in) Encoder
- (9.1in, 3.4in) LayerNorm
- (3.7in, 3.5in) Feed Forward
- (9.2in, 4.1in) Add
- (3.7in, 4.2in) LayerNorm
- (3.7in, 5.0in) Add
- (9.2in, 4.9in) Multi-head Attention
- (9.2in, 5.7in) LayerNorm
- (3.7in, 5.8in) Multi-head Attention
- (0.5in, 6.2in) skip (residual) connection
- (9.1in, 6.7in) Embedding
- (3.7in, 6.8in) Embedding

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> Embedding (unverified)
- Add -> Multi-head Attention (unverified)
- LayerNorm -> Add (unverified)
- Add -> Multi-head Attention (unverified)
- LayerNorm -> Embedding (unverified)
- Multi-head Attention -> LayerNorm (unverified)
- Add -> Multi-head Attention (unverified)
- Multi-head Attention -> LayerNorm (unverified)
- Add -> Feed Forward (unverified)
- LayerNorm -> Add (unverified)
- Feed Forward -> LayerNorm (unverified)
- Add -> Feed Forward (unverified)
- Add -> Feed Forward (unverified)
- Feed Forward -> LayerNorm (unverified)
- pre-norm -> LayerNorm (unverified)
- LayerNorm -> Add (unverified)

## Slide 101

Native text objects: 37; connectors: 58; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Блок Feed Forward
- (4.3in, 1.9in) Output
- (8.1in, 2.2in) Add & LayerNorm
- (3.7in, 2.6in) Add & LayerNorm
- (8.1in, 3.0in) Linear2
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (8.1in, 3.4in) Dropout
- (6.5in, 3.6in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (8.1in, 3.8in) ReLU или GELU
- (3.7in, 4.4in) Multi-head Attention
- (8.1in, 4.2in) Linear1
- (6.5in, 5.0in) add
- (8.1in, 4.9in) Add & LayerNorm
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.7in) Multi-head Attention
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (3.2in, 6.3in) Embedding
- (6.4in, 6.5in) embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (4.0in, 7.0in) Input
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 2 -> x 3 (unverified)
- z 2 -> x 4 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 3 -> x 4 (unverified)
- z 3 -> x 5 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 4 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 5 (unverified)
- Add & LayerNorm -> z 3 (unverified)
- z 1 -> x 1 (unverified)
- z 1 -> z 2 (unverified)
- z 2 -> z 3 (unverified)
- z 3 -> z 4 (unverified)
- z 4 -> z 5 (unverified)
- Linear1 -> z 2 (unverified)
- Linear1 -> Add & LayerNorm (unverified)
- Linear1 -> z 4 (unverified)
- Add & LayerNorm -> Linear2 (unverified)
- Add & LayerNorm -> Linear2 (unverified)
- Add & LayerNorm -> Linear2 (unverified)
- Add & LayerNorm -> Linear2 (unverified)
- Трансформер. Блок Feed Forward -> Add & LayerNorm (unverified)
- Feed Forward -> z 5 (unverified)

## Slide 102

Native text objects: 25; connectors: 7; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (6.5in, 1.6in) Кабан наступил на баклажан
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (8.4in, 2.6in) баклажан наступил на Кабан
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (3.2in, 6.3in) Embedding
- (6.4in, 6.5in) embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (4.0in, 7.0in) Input
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)

## Slide 103

Native text objects: 51; connectors: 37; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (6.4in, 1.6in) Кабан наступил на баклажан
- (10.0in, 1.6in) баклажан наступил на Кабан
- (4.3in, 1.9in) Output
- (6.5in, 2.1in) w = s(a,b) = a T * b = ∑ a i * b i
- (3.7in, 2.6in) Add & LayerNorm
- (8.4in, 2.6in) w 11
- (9.2in, 2.6in) w 12
- (10.0in, 2.6in) w 13
- (10.8in, 2.6in) w 14
- (11.7in, 2.6in) w 15
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query key
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> Linear, Wk (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 104

Native text objects: 52; connectors: 37; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (6.4in, 1.6in) Кабан наступил на баклажан
- (10.0in, 1.6in) баклажан наступил на Кабан
- (4.3in, 1.9in) Output
- (6.5in, 2.1in) w = s(a,b) = a T * b = ∑ a i * b i
- (10.0in, 2.1in) w = s(a,b) = s(b, a )
- (3.7in, 2.6in) Add & LayerNorm
- (8.4in, 2.6in) w 11
- (9.2in, 2.6in) w 12
- (10.0in, 2.6in) w 13
- (10.8in, 2.6in) w 14
- (11.7in, 2.6in) w 15
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.5in, 3.7in) query key
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (3.2in, 6.3in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> Linear, Wk (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 105

Native text objects: 29; connectors: 7; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (7.0in, 5.7in) Positional Encoding
- (8.3in, 5.7in) 0
- (9.2in, 5.7in) 1
- (9.9in, 5.7in) 2
- (10.8in, 5.7in) 3
- (11.7in, 5.7in) 4
- (3.2in, 6.3in) Embedding
- (6.9in, 6.4in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)

## Slide 106

Native text objects: 36; connectors: 22; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (6.8in, 4.7in) x i =x i + p i
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.2in) i = 0, 1, …, N-1
- (8.4in, 5.1in) +
- (9.2in, 5.1in) +
- (10.0in, 5.1in) +
- (10.8in, 5.1in) +
- (11.8in, 5.1in) +
- (7.0in, 5.7in) Positional Encoding
- (8.3in, 5.7in) 0
- (9.2in, 5.7in) 1
- (9.9in, 5.7in) 2
- (10.8in, 5.7in) 3
- (11.7in, 5.7in) 4
- (3.2in, 6.3in) Embedding
- (6.9in, 6.4in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- + -> 0 (unverified)
- + -> 1 (unverified)
- + -> 2 (unverified)
- + -> 3 (unverified)
- + -> 4 (unverified)
- Positional Encoding -> 1 (unverified)
- 0 -> 2 (unverified)
- 1 -> 3 (unverified)
- 2 -> 3 (unverified)
- 3 -> 4 (unverified)

## Slide 107

Native text objects: 38; connectors: 22; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (9.5in, 3.1in) x = [10 0.1, 100.2, 100.3 ]
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (7.3in, 3.1in) x = [ 0.1, 0.2, 0.3 ] p = 100
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (6.8in, 4.7in) x i =x i + p i
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.2in) i = 0, 1, …, N-1
- (8.4in, 5.1in) +
- (9.2in, 5.1in) +
- (10.0in, 5.1in) +
- (10.8in, 5.1in) +
- (11.8in, 5.1in) +
- (7.0in, 5.7in) Positional Encoding
- (8.3in, 5.7in) 0
- (9.2in, 5.7in) 1
- (9.9in, 5.7in) 2
- (10.8in, 5.7in) 3
- (11.7in, 5.7in) 4
- (3.2in, 6.3in) Embedding
- (6.9in, 6.4in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- + -> 0 (unverified)
- + -> 1 (unverified)
- + -> 2 (unverified)
- + -> 3 (unverified)
- + -> 4 (unverified)
- Positional Encoding -> 1 (unverified)
- 0 -> 2 (unverified)
- 1 -> 3 (unverified)
- 2 -> 3 (unverified)
- 3 -> 4 (unverified)

## Slide 108

Native text objects: 38; connectors: 22; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (6.9in, 2.8in) N=5 :
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (6.8in, 3.3in) N=6 :
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (6.8in, 4.7in) x i =x i + p i
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.2in) i = 0, 1, …, N-1
- (8.4in, 5.1in) +
- (9.2in, 5.1in) +
- (10.0in, 5.1in) +
- (10.8in, 5.1in) +
- (11.8in, 5.1in) +
- (7.0in, 5.7in) Positional Encoding
- (8.3in, 5.7in) 0
- (9.2in, 5.7in) 1
- (9.9in, 5.7in) 2
- (10.8in, 5.7in) 3
- (11.7in, 5.7in) 4
- (3.2in, 6.3in) Embedding
- (6.9in, 6.4in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- + -> 0 (unverified)
- + -> 1 (unverified)
- + -> 2 (unverified)
- + -> 3 (unverified)
- + -> 4 (unverified)
- Positional Encoding -> 1 (unverified)
- 0 -> 2 (unverified)
- 1 -> 3 (unverified)
- 2 -> 3 (unverified)
- 3 -> 4 (unverified)

## Slide 109

Native text objects: 37; connectors: 22; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (6.9in, 2.8in) N=4096 : [0.0, 0.000244, 0.000488, 0.00073, …]
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (6.8in, 4.7in) x i =x i + p i
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.2in) i = 0, 1, …, N-1
- (8.4in, 5.1in) +
- (9.2in, 5.1in) +
- (10.0in, 5.1in) +
- (10.8in, 5.1in) +
- (11.8in, 5.1in) +
- (7.0in, 5.7in) Positional Encoding
- (8.3in, 5.7in) 0
- (9.2in, 5.7in) 1
- (9.9in, 5.7in) 2
- (10.8in, 5.7in) 3
- (11.7in, 5.7in) 4
- (3.2in, 6.3in) Embedding
- (6.9in, 6.4in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- + -> 0 (unverified)
- + -> 1 (unverified)
- + -> 2 (unverified)
- + -> 3 (unverified)
- + -> 4 (unverified)
- Positional Encoding -> 1 (unverified)
- 0 -> 2 (unverified)
- 1 -> 3 (unverified)
- 2 -> 3 (unverified)
- 3 -> 4 (unverified)

## Slide 110

Native text objects: 37; connectors: 22; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (7.0in, 1.3in) p 0 = [1, 0, 0, …, 0, …, 0] T  p 1 = [0, 1, 0, …, 0, …, 0] T  …  p i = [0, 0, 0, …, 1, …, 0] T  ,,,  p N-1 = [0, 0, 0, …, 0, …, 1] T
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (6.8in, 4.7in) x i =x i + p i
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.2in) i = 0, 1, …, N-1
- (8.4in, 5.1in) +
- (9.2in, 5.1in) +
- (10.0in, 5.1in) +
- (10.8in, 5.1in) +
- (11.8in, 5.1in) +
- (7.0in, 5.7in) Positional Encoding
- (8.3in, 5.7in) 0
- (9.2in, 5.7in) 1
- (9.9in, 5.7in) 2
- (10.8in, 5.7in) 3
- (11.7in, 5.7in) 4
- (3.2in, 6.3in) Embedding
- (6.9in, 6.4in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- + -> 0 (unverified)
- + -> 1 (unverified)
- + -> 2 (unverified)
- + -> 3 (unverified)
- + -> 4 (unverified)
- Positional Encoding -> 1 (unverified)
- 0 -> 2 (unverified)
- 1 -> 3 (unverified)
- 2 -> 3 (unverified)
- 3 -> 4 (unverified)

## Slide 111

Native text objects: 39; connectors: 22; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (5.8in, 1.4in) Attention is All You Need
- (7.3in, 1.8in) sin(w 0 * t) cos (w 0 * t) sin(w i * t) cos(w i * t) … sin(w d/2-1 * t) cos(w d/2-1 * t)
- (4.3in, 1.9in) Output
- (3.7in, 2.6in) Add & LayerNorm
- (6.5in, 2.6in) p t =
- (1.3in, 3.3in) Encoder
- (3.7in, 3.2in) Feed Forward
- (3.7in, 3.8in) Add & LayerNorm
- (3.7in, 4.4in) Multi-head Attention
- (6.8in, 4.7in) x i =x i + p i
- (1.2in, 5.4in) Positional Encoding
- (4.3in, 5.3in) +
- (6.4in, 5.2in) i = 0, 1, …, N-1
- (8.4in, 5.1in) +
- (9.2in, 5.1in) +
- (10.0in, 5.1in) +
- (10.8in, 5.1in) +
- (11.8in, 5.1in) +
- (7.0in, 5.7in) Positional Encoding
- (8.3in, 5.7in) 0
- (9.2in, 5.7in) 1
- (9.9in, 5.7in) 2
- (10.8in, 5.7in) 3
- (11.7in, 5.7in) 4
- (3.2in, 6.3in) Embedding
- (6.9in, 6.4in) Embedding
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (4.0in, 7.0in) Input
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Output -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Feed Forward (unverified)
- + -> 0 (unverified)
- + -> 1 (unverified)
- + -> 2 (unverified)
- + -> 3 (unverified)
- + -> 4 (unverified)
- Positional Encoding -> 1 (unverified)
- 0 -> 2 (unverified)
- 1 -> 3 (unverified)
- 2 -> 3 (unverified)
- 3 -> 4 (unverified)

## Slide 112

Native text objects: 11; connectors: 4; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (4.2in, 1.6in) sin(w 0 * t) cos(w 0 * t)  sin(w 1 * t) cos(w 1 * t)  sin(w 2 * t) cos(w 2 * t) …  sin(w d/2-1 * t) cos(w d/2-1 * t)
- (1.6in, 2.2in) sin(w 0 * t) cos(w 0 * t) sin(w 1 * t) cos(w 1 * t) sin(w 2 * t) cos(w 2 * t) … sin(w d/2-1 * t) cos(w d/2-1 * t)
- (0.8in, 3.3in) p t =
- (1.2in, 6.5in) p 0 = [0,1,0,1,0,1,0,1]
- (5.7in, 6.5in) p 0
- (6.3in, 6.5in) p 2
- (8.1in, 6.6in) p i
- (11.5in, 6.6in) position ,t
- (5.5in, 6.9in) p 2 = [0.90, -0.42, 0.19 , 0.98, 0.20, 0.002, 0.99] T

### Possible connector endpoints (spatial inference)

- p 0 -> position ,t (unverified)
- Трансформер. Позиционное кодирование -> p 0 (unverified)
- Трансформер. Позиционное кодирование -> p 2 (unverified)
- Трансформер. Позиционное кодирование -> p i (unverified)

## Slide 113

Native text objects: 5; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (1.6in, 2.2in) sin(w 0 * t) cos(w 0 * t) sin(w 1 * t) cos(w 1 * t) sin(w 2 * t) cos(w 2 * t) … sin(w d/2-1 * t) cos(w d/2-1 * t)
- (4.7in, 2.4in) уникальный вектор для каждой позиции  возможность вычисления относительных расстояний между векторами  простота генерации векторов позиций для последовательной 
- (0.8in, 3.3in) p t =

## Slide 114

Native text objects: 6; connectors: 0; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.7in) Трансформер. Позиционное кодирование
- (1.6in, 2.2in) sin(w 0 * t) cos(w 0 * t) sin(w 1 * t) cos(w 1 * t) sin(w 2 * t) cos(w 2 * t) … sin(w d/2-1 * t) cos(w d/2-1 * t)
- (4.7in, 2.4in) уникальный вектор для каждой позиции  возможность вычисления относительных расстояний между векторами  простота генерации векторов позиций для последовательной 
- (0.8in, 3.3in) p t =
- (4.6in, 5.8in) BERT и первые версии ChatGPT использовали обучаемые векторы позиции PaLM , LLaMA последние версии ChatGPT , применяется для относительнольного позиционирования 

## Slide 115

Native text objects: 29; connectors: 12; embedded pictures: 0

- (0.1in, 0.0in) Трансформер. Декодер
- (4.7in, 0.2in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (8.0in, 1.4in) argmax
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (8.1in, 1.8in) SoftMax
- (9.2in, 1.9in) SM
- (4.1in, 2.6in) Add & LayerNorm
- (8.1in, 2.5in) Linear
- (9.2in, 2.6in) LN
- (4.1in, 3.2in) Multi-head Attention
- (9.2in, 3.2in) Decoder
- (0.8in, 3.6in) Encoder output
- (6.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (4.1in, 4.6in) Masked Multi-head Attention
- (8.2in, 4.5in) Positional Encoding
- (10.0in, 4.5in) p 0
- (0.9in, 5.3in) skip (residual) connection
- (10.4in, 5.1in) +
- (10.0in, 5.7in) x 0
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (8.1in, 5.9in) Embedding
- (3.7in, 6.6in) Embedding
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- Encoder output -> Positional Encoding (unverified)
- SM -> LN (unverified)

## Slide 116

Native text objects: 48; connectors: 21; embedded pictures: 0

- (0.1in, 0.0in) Трансформер. Декодер
- (4.7in, 0.2in) output
- (4.1in, 0.6in) SoftMax
- (9.1in, 0.6in) I
- (10.0in, 0.6in) filming
- (10.8in, 0.6in) absolute
- (11.7in, 0.6in) cinema
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (8.0in, 1.4in) argmax
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (7.9in, 1.8in) SoftMax
- (9.2in, 1.9in) SM
- (10.1in, 1.9in) SM
- (10.9in, 1.9in) SM
- (11.7in, 1.9in) SM
- (4.1in, 2.6in) Add & LayerNorm
- (7.9in, 2.5in) Linear
- (9.2in, 2.6in) LN
- (10.1in, 2.6in) LN
- (10.9in, 2.6in) LN
- (11.7in, 2.6in) LN
- (4.1in, 3.2in) Multi-head Attention
- (9.2in, 3.2in) Decoder
- (0.8in, 3.6in) Encoder output
- (6.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (4.1in, 4.6in) Masked Multi-head Attention
- (7.6in, 4.6in) Positional Encoding
- (9.3in, 4.7in) p 0
- (10.1in, 4.7in) p 1
- (11.0in, 4.7in) p 2
- (11.9in, 4.7in) p 3
- (0.9in, 5.3in) skip (residual) connection
- (9.3in, 5.2in) +
- (10.1in, 5.2in) +
- (11.0in, 5.2in) +
- (11.9in, 5.2in) +
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (7.8in, 5.9in) Embedding
- (9.3in, 5.9in) x 0
- (10.1in, 5.9in) x 1
- (11.0in, 5.9in) x 2
- (11.9in, 5.8in) x 3
- (3.7in, 6.6in) Embedding
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- Encoder output -> LN (unverified)
- SM -> LN (unverified)
- SM -> LN (unverified)
- SM -> LN (unverified)
- SM -> LN (unverified)

## Slide 117

Native text objects: 34; connectors: 33; embedded pictures: 0

- (0.1in, 0.0in) Трансформер. Декодер
- (4.7in, 0.2in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (4.1in, 2.6in) Add & LayerNorm
- (4.1in, 3.2in) Multi-head Attention
- (0.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (4.1in, 4.6in) Masked Multi-head Attention
- (0.9in, 5.3in) skip (residual) connection
- (6.5in, 5.1in) Multi-head Attention
- (8.1in, 5.1in) z 1
- (9.0in, 5.1in) z 2
- (9.9in, 5.1in) z 3
- (10.9in, 5.1in) z 4
- (11.8in, 5.1in) z 5
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (3.7in, 6.6in) Embedding
- (6.6in, 6.5in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- z 1 -> x 1 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 2 -> x 3 (unverified)
- z 2 -> x 4 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 3 -> x 4 (unverified)
- z 3 -> x 5 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 4 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 1 -> x 5 (unverified)
- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)

## Slide 118

Native text objects: 63; connectors: 35; embedded pictures: 0

- (0.6in, 0.3in) Механизм внимания - attention
- (0.6in, 0.6in) Вычисление QKV Self-Attention
- (0.5in, 1.2in) d_attn
- (2.6in, 1.2in) N
- (4.5in, 1.2in) N
- (1.7in, 1.8in) d_attn
- (8.4in, 2.0in) c 1 = ∑ α i * v i
- (1.8in, 2.1in) X
- (3.8in, 2.1in) =
- (4.1in, 2.3in) N
- (2.8in, 2.7in) K T
- (6.6in, 2.6in) SoftMax(w/√d)
- (8.4in, 2.6in) SoftMax
- (0.7in, 3.0in) Q
- (4.5in, 3.0in) W = Q * K T
- (8.5in, 3.1in) s
- (9.3in, 3.1in) s
- (10.1in, 3.1in) s
- (10.9in, 3.1in) s
- (11.8in, 3.1in) s
- (3.9in, 3.4in) 0     -∞  …   - ∞ 0     0    …   -∞ …  …  …   … 0    0  …    0
- (7.5in, 3.7in) query key value
- (8.3in, 3.7in) q 1
- (8.7in, 3.7in) k 1
- (9.2in, 3.7in) q 2
- (9.5in, 3.7in) k 2
- (9.9in, 3.7in) q 3
- (10.4in, 3.7in) k 3
- (10.8in, 3.7in) q 4
- (11.3in, 3.7in) k 4
- (11.7in, 3.7in) q 5
- (12.1in, 3.7in) k 5
- (2.9in, 4.2in) M =
- (8.9in, 4.2in) v 1
- (9.7in, 4.2in) v 2
- (10.6in, 4.2in) v 3
- (11.5in, 4.2in) v 4
- (12.4in, 4.2in) v 5
- (7.0in, 4.7in) v i = W v * x i
- (8.2in, 4.7in) Linear, Wv
- (7.0in, 5.2in) k i = W k * x i
- (8.2in, 5.2in) Linear, Wk
- (0.2in, 5.9in) N
- (2.7in, 5.8in) emb_size
- (2.8in, 5.9in) X
- (4.7in, 5.9in) =
- (7.0in, 5.8in) q = W q * x i
- (8.2in, 5.8in) Linear, Wq
- (5.0in, 6.1in) N
- (1.0in, 6.7in) X
- (4.7in, 6.7in) W q
- (8.3in, 6.4in) x 1
- (9.2in, 6.4in) x 2
- (9.9in, 6.4in) x 3
- (10.8in, 6.4in) x 4
- (11.7in, 6.4in) x 5
- (5.5in, 6.9in) V = X * W v
- (6.9in, 6.7in) Embedding
- (8.2in, 7.0in) <bos>
- (9.2in, 7.0in) я
- (9.8in, 6.9in) снимаю
- (10.7in, 7.0in) кино
- (11.6in, 7.0in) <eos>

### Possible connector endpoints (spatial inference)

- Linear, Wq -> x 3 (unverified)
- q 1 -> x 1 (unverified)
- q 2 -> x 2 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 4 -> Linear, Wq (unverified)
- q 5 -> x 5 (unverified)
- s -> q 1 (unverified)
- s -> k 1 (unverified)
- s -> k 2 (unverified)
- s -> k 3 (unverified)
- s -> k 4 (unverified)
- s -> k 5 (unverified)
- s -> q 2 (unverified)
- s -> q 2 (unverified)
- s -> q 4 (unverified)
- s -> q 5 (unverified)
- k 1 -> v 1 (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> v 4 (unverified)
- k 5 -> v 5 (unverified)
- Linear, Wk -> x 2 (unverified)
- Linear, Wk -> x 3 (unverified)
- Linear, Wk -> x 4 (unverified)

## Slide 119

Native text objects: 34; connectors: 23; embedded pictures: 0

- (0.1in, 0.0in) Трансформер. Декодер
- (4.7in, 0.2in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (4.1in, 2.6in) Add & LayerNorm
- (4.1in, 3.2in) Multi-head Attention
- (0.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (4.1in, 4.6in) Masked Multi-head Attention
- (0.9in, 5.3in) skip (residual) connection
- (6.5in, 5.1in) Multi-head Attention
- (8.1in, 5.1in) z 1
- (9.0in, 5.1in) z 2
- (9.9in, 5.1in) z 3
- (10.9in, 5.1in) z 4
- (11.8in, 5.1in) z 5
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (3.7in, 6.6in) Embedding
- (6.6in, 6.5in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 4 -> x 5 (unverified)

## Slide 120

Native text objects: 43; connectors: 33; embedded pictures: 0

- (-0.0in, -0.0in) Masked Multi-head Attention
- (4.9in, 0.3in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (4.1in, 2.6in) Add & LayerNorm
- (4.1in, 3.2in) Multi-head Attention
- (0.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (8.1in, 4.1in) LayerNorm
- (4.1in, 4.6in) Masked Multi-head Attention
- (8.0in, 4.5in) x 1
- (9.0in, 4.5in) x 2
- (9.9in, 4.5in) x 3
- (10.9in, 4.5in) x 4
- (11.8in, 4.5in) x 5
- (8.1in, 4.9in) x 1 +z 1
- (9.0in, 4.9in) x 2 +z 2
- (9.9in, 4.9in) x 3 +z 3
- (10.9in, 4.9in) x 4 +z 4
- (11.8in, 4.9in) x 5 +z 5
- (0.9in, 5.3in) skip (residual) connection
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (3.7in, 6.6in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- x 1 +z 1 -> z 1 (unverified)
- x 2 +z 2 -> z 2 (unverified)
- x 3 +z 3 -> z 3 (unverified)
- x 4 +z 4 -> z 4 (unverified)
- x 5 +z 5 -> z 5 (unverified)
- x 1 -> x 1 +z 1 (unverified)
- x 2 -> x 2 +z 2 (unverified)
- x 3 -> x 3 +z 3 (unverified)
- x 4 -> x 4 +z 4 (unverified)
- x 5 -> x 5 +z 5 (unverified)
- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 4 -> x 5 (unverified)

## Slide 121

Native text objects: 43; connectors: 33; embedded pictures: 0

- (-0.0in, -0.0in) Masked Multi-head Attention
- (4.9in, 0.3in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (4.1in, 2.6in) Add & LayerNorm
- (4.1in, 3.2in) Multi-head Attention
- (0.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (8.1in, 4.1in) LayerNorm
- (4.1in, 4.6in) Masked Multi-head Attention
- (8.0in, 4.5in) x 1
- (9.0in, 4.5in) x 2
- (9.9in, 4.5in) x 3
- (10.9in, 4.5in) x 4
- (11.8in, 4.5in) x 5
- (8.1in, 4.9in) x 1 +z 1
- (9.0in, 4.9in) x 2 +z 2
- (9.9in, 4.9in) x 3 +z 3
- (10.9in, 4.9in) x 4 +z 4
- (11.8in, 4.9in) x 5 +z 5
- (0.9in, 5.3in) skip (residual) connection
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (3.7in, 6.6in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- x 1 +z 1 -> z 1 (unverified)
- x 2 +z 2 -> z 2 (unverified)
- x 3 +z 3 -> z 3 (unverified)
- x 4 +z 4 -> z 4 (unverified)
- x 5 +z 5 -> z 5 (unverified)
- x 1 -> x 1 +z 1 (unverified)
- x 2 -> x 2 +z 2 (unverified)
- x 3 -> x 3 +z 3 (unverified)
- x 4 -> x 4 +z 4 (unverified)
- x 5 -> x 5 +z 5 (unverified)
- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 4 -> x 5 (unverified)

## Slide 122

Native text objects: 13; connectors: 11; embedded pictures: 0

- (0.6in, 0.3in) трансформеры
- (0.6in, 0.7in) Архитектуры post-norm и pre-norm
- (2.6in, 3.6in) post-norm
- (8.8in, 3.6in) pre-norm
- (3.7in, 4.5in) LayerNorm
- (10.0in, 4.6in) Add
- (3.7in, 5.0in) Add
- (10.0in, 5.2in) Masked Multi-head Attention
- (3.7in, 5.5in) Masked Multi-head Attention
- (10.0in, 6.1in) LayerNorm
- (0.5in, 6.2in) skip (residual) connection
- (3.7in, 6.8in) Embedding
- (9.9in, 6.8in) Embedding

### Possible connector endpoints (spatial inference)

- Masked Multi-head Attention -> Embedding (unverified)
- Add -> Masked Multi-head Attention (unverified)
- LayerNorm -> Add (unverified)
- Add -> Masked Multi-head Attention (unverified)
- skip (residual) connection -> Embedding (unverified)
- Add -> Masked Multi-head Attention (unverified)
- Masked Multi-head Attention -> LayerNorm (unverified)
- LayerNorm -> Embedding (unverified)
- pre-norm -> LayerNorm (unverified)

## Slide 123

Native text objects: 43; connectors: 33; embedded pictures: 0

- (-0.0in, -0.0in) Masked Multi-head Attention
- (4.9in, 0.3in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (4.1in, 2.6in) Add & LayerNorm
- (4.1in, 3.2in) Multi-head Attention
- (0.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (8.1in, 4.1in) LayerNorm
- (4.1in, 4.6in) Masked Multi-head Attention
- (8.0in, 4.5in) x 1
- (9.0in, 4.5in) x 2
- (9.9in, 4.5in) x 3
- (10.9in, 4.5in) x 4
- (11.8in, 4.5in) x 5
- (8.1in, 4.9in) x 1 +z 1
- (9.0in, 4.9in) x 2 +z 2
- (9.9in, 4.9in) x 3 +z 3
- (10.9in, 4.9in) x 4 +z 4
- (11.8in, 4.9in) x 5 +z 5
- (0.9in, 5.3in) skip (residual) connection
- (8.1in, 5.6in) z 1
- (9.0in, 5.6in) z 2
- (9.9in, 5.6in) z 3
- (10.9in, 5.6in) z 4
- (11.8in, 5.6in) z 5
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (3.7in, 6.6in) Embedding
- (8.1in, 6.5in) x 1
- (9.0in, 6.5in) x 2
- (9.9in, 6.5in) x 3
- (10.9in, 6.5in) x 4
- (11.8in, 6.5in) x 5
- (8.0in, 6.9in) <bos>
- (9.0in, 7.0in) я
- (9.6in, 6.9in) снимаю
- (10.9in, 6.9in) кино
- (11.7in, 7.0in) <eos>
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- x 1 +z 1 -> z 1 (unverified)
- x 2 +z 2 -> z 2 (unverified)
- x 3 +z 3 -> z 3 (unverified)
- x 4 +z 4 -> z 4 (unverified)
- x 5 +z 5 -> z 5 (unverified)
- x 1 -> x 1 +z 1 (unverified)
- x 2 -> x 2 +z 2 (unverified)
- x 3 -> x 3 +z 3 (unverified)
- x 4 -> x 4 +z 4 (unverified)
- x 5 -> x 5 +z 5 (unverified)
- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 4 -> x 5 (unverified)

## Slide 124

Native text objects: 39; connectors: 38; embedded pictures: 0

- (-0.0in, -0.0in) Masked Multi-head Attention
- (4.9in, 0.3in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (4.1in, 2.6in) Add & LayerNorm
- (4.1in, 3.2in) Multi-head Attention
- (8.5in, 3.4in) q 1
- (9.4in, 3.4in) q 2
- (10.3in, 3.4in) q 3
- (11.3in, 3.4in) q 4
- (12.2in, 3.4in) q 5
- (0.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (8.5in, 4.2in) Linear, Wq
- (4.1in, 4.6in) Masked Multi-head Attention
- (8.5in, 4.9in) Add & LayerNorm
- (0.9in, 5.3in) skip (residual) connection
- (8.5in, 5.6in) z 1
- (9.4in, 5.6in) z 2
- (10.4in, 5.6in) z 3
- (11.3in, 5.6in) z 4
- (12.3in, 5.6in) z 5
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (3.7in, 6.6in) Embedding
- (8.5in, 6.5in) x 1
- (9.4in, 6.5in) x 2
- (10.4in, 6.5in) x 3
- (11.3in, 6.5in) x 4
- (12.3in, 6.5in) x 5
- (8.5in, 6.9in) <bos>
- (9.5in, 7.0in) я
- (10.1in, 6.9in) снимаю
- (11.3in, 6.9in) кино
- (12.2in, 7.0in) <eos>
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- Add & LayerNorm -> z 3 (unverified)
- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 1 -> z 1 (unverified)
- q 2 -> z 2 (unverified)
- Linear, Wq -> Add & LayerNorm (unverified)
- Linear, Wq -> Add & LayerNorm (unverified)
- q 5 -> z 5 (unverified)

## Slide 125

Native text objects: 59; connectors: 82; embedded pictures: 0

- (-0.0in, -0.0in) Masked Multi-head Attention
- (4.9in, 0.3in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (8.6in, 1.1in) c 1 = ∑ α i * v i
- (1.8in, 1.4in) Decoder
- (6.6in, 1.4in) v 1
- (7.0in, 1.4in) v 2
- (7.3in, 1.4in) v 3
- (7.7in, 1.4in) v 4
- (8.0in, 1.4in) v 5
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (8.6in, 1.8in) Linear, Wq
- (6.6in, 2.2in) Linear, Wv
- (8.6in, 2.2in) S
- (9.5in, 2.2in) S
- (10.4in, 2.2in) S
- (11.4in, 2.2in) S
- (12.3in, 2.2in) S
- (4.1in, 2.6in) Add & LayerNorm
- (4.1in, 3.2in) Multi-head Attention
- (6.6in, 3.4in) k 1
- (7.0in, 3.4in) k 2
- (7.3in, 3.4in) k 3
- (7.7in, 3.4in) k 4
- (8.0in, 3.4in) k 5
- (8.5in, 3.4in) q 1
- (9.4in, 3.4in) q 2
- (10.3in, 3.4in) q 3
- (11.3in, 3.4in) q 4
- (12.2in, 3.4in) q 5
- (0.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (6.6in, 4.2in) Linear, Wk
- (8.5in, 4.2in) Linear, Wq
- (4.1in, 4.6in) Masked Multi-head Attention
- (6.6in, 4.9in) Encode, Outpujt
- (8.5in, 4.9in) Add & LayerNorm
- (0.9in, 5.3in) skip (residual) connection
- (8.5in, 5.6in) z 1
- (9.4in, 5.6in) z 2
- (10.4in, 5.6in) z 3
- (11.3in, 5.6in) z 4
- (12.3in, 5.6in) z 5
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (3.7in, 6.6in) Embedding
- (8.5in, 6.5in) x 1
- (9.4in, 6.5in) x 2
- (10.4in, 6.5in) x 3
- (11.3in, 6.5in) x 4
- (12.3in, 6.5in) x 5
- (8.5in, 6.9in) <bos>
- (9.5in, 7.0in) я
- (10.1in, 6.9in) снимаю
- (11.3in, 6.9in) кино
- (12.2in, 7.0in) <eos>
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- Add & LayerNorm -> z 3 (unverified)
- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- q 3 -> Linear, Wq (unverified)
- q 1 -> z 1 (unverified)
- q 2 -> z 2 (unverified)
- Linear, Wq -> Add & LayerNorm (unverified)
- Linear, Wq -> Add & LayerNorm (unverified)
- q 5 -> z 5 (unverified)
- Linear, Wk -> Encode, Outpujt (unverified)
- Linear, Wk -> Encode, Outpujt (unverified)
- Linear, Wk -> Encode, Outpujt (unverified)
- Linear, Wk -> Encode, Outpujt (unverified)
- k 2 -> Linear, Wk (unverified)
- k 3 -> Linear, Wk (unverified)
- k 4 -> Linear, Wk (unverified)
- Linear, Wk -> Encode, Outpujt (unverified)
- Linear, Wv -> k 1 (unverified)
- Linear, Wv -> k 2 (unverified)
- Linear, Wv -> k 3 (unverified)
- Linear, Wv -> k 4 (unverified)
- Linear, Wv -> k 5 (unverified)
- S -> q 1 (unverified)
- S -> q 2 (unverified)
- S -> q 3 (unverified)
- S -> q 4 (unverified)
- S -> q 5 (unverified)
- Linear, Wv -> q 1 (unverified)
- Linear, Wv -> q 1 (unverified)
- Linear, Wv -> q 1 (unverified)
- Linear, Wv -> q 1 (unverified)
- S -> q 1 (unverified)
- Linear, Wv -> q 2 (unverified)
- Linear, Wv -> q 2 (unverified)
- Linear, Wv -> q 2 (unverified)
- Linear, Wv -> q 2 (unverified)
- k 5 -> q 2 (unverified)
- Linear, Wv -> q 3 (unverified)
- Linear, Wv -> q 3 (unverified)
- Linear, Wv -> q 3 (unverified)
- Linear, Wv -> q 3 (unverified)
- S -> q 3 (unverified)
- Linear, Wv -> q 4 (unverified)
- Linear, Wv -> q 4 (unverified)
- Linear, Wv -> q 4 (unverified)
- Linear, Wv -> q 4 (unverified)
- S -> q 4 (unverified)
- S -> q 5 (unverified)
- Linear, Wv -> q 5 (unverified)

## Slide 126

Native text objects: 37; connectors: 44; embedded pictures: 0

- (-0.0in, -0.0in) Трансформер. Декодер
- (4.9in, 0.3in) output
- (4.1in, 0.6in) SoftMax
- (4.1in, 1.0in) Linear
- (1.8in, 1.4in) Decoder
- (4.1in, 1.5in) Add & LayerNorm
- (4.1in, 2.0in) Feed Forward
- (4.1in, 2.6in) Add & LayerNorm
- (8.5in, 2.7in) Feed Forward
- (4.1in, 3.2in) Multi-head Attention
- (8.5in, 3.4in) Add & LayerNorm
- (0.8in, 3.6in) Encoder output
- (4.1in, 4.0in) Add & LayerNorm
- (6.4in, 4.0in) Encoder output
- (8.5in, 4.2in) Multi-head Attention
- (4.1in, 4.6in) Masked Multi-head Attention
- (8.5in, 4.9in) Add & LayerNorm
- (0.9in, 5.3in) skip (residual) connection
- (8.5in, 5.6in) z 1
- (9.4in, 5.6in) z 2
- (10.4in, 5.6in) z 3
- (11.3in, 5.6in) z 4
- (12.3in, 5.6in) z 5
- (1.7in, 5.9in) Positional Encoding
- (4.8in, 5.8in) +
- (3.7in, 6.6in) Embedding
- (8.5in, 6.5in) x 1
- (9.4in, 6.5in) x 2
- (10.4in, 6.5in) x 3
- (11.3in, 6.5in) x 4
- (12.3in, 6.5in) x 5
- (8.5in, 6.9in) <bos>
- (9.5in, 7.0in) я
- (10.1in, 6.9in) снимаю
- (11.3in, 6.9in) кино
- (12.2in, 7.0in) <eos>
- (4.5in, 7.1in) Input

### Possible connector endpoints (spatial inference)

- Add & LayerNorm -> z 3 (unverified)
- Masked Multi-head Attention -> + (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Masked Multi-head Attention (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Linear -> Add & LayerNorm (unverified)
- Encoder output -> Multi-head Attention (unverified)
- z 1 -> x 1 (unverified)
- z 2 -> x 2 (unverified)
- z 3 -> x 3 (unverified)
- z 4 -> x 4 (unverified)
- z 5 -> x 5 (unverified)
- z 1 -> x 2 (unverified)
- z 1 -> x 3 (unverified)
- z 2 -> x 3 (unverified)
- z 1 -> x 4 (unverified)
- z 2 -> x 4 (unverified)
- z 3 -> x 4 (unverified)
- z 1 -> x 5 (unverified)
- z 2 -> x 5 (unverified)
- z 3 -> x 5 (unverified)
- z 4 -> x 5 (unverified)
- Multi-head Attention -> z 2 (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Multi-head Attention -> Add & LayerNorm (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Add & LayerNorm -> Multi-head Attention (unverified)
- Add & LayerNorm -> z 5 (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
- Feed Forward -> Add & LayerNorm (unverified)
