# Visual review: lecture_07/lecture_LSTM_GRU.pptx

OCR of fully rendered slides; also includes image-only labels. OCR may contain mistakes.

## Slide 1

Tema 7. RNN, LSTM, GRU

## Slide 2

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Сети прямого распространения

x

—>

Тема 1. Нейронные сети

|
=

Al A
a ie

## Slide 3

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Сети прямого распространения

x

—>

Тема 1. Нейронные сети

|
=

Al A
a ie

## Slide 4

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Сети прямого распространения

x, Император

x, Петр =»

x, Великий

fea 1. Нейронные сети 19/2:

## Slide 5

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Сети прямого распространения

x, Император
x, Петр
x, Великий

х, Император
x, Петр
x, Великий

Император Император Император
Петр Петр Великий

fea 1. Нейронные сети 19/23

## Slide 6

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Сети прямого распространения

Император х,

Петр х,

Великий х,

Ох

fea 1. Нейронные сети 19/23

## Slide 7

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Способ обработки последовательностей

Хи ХХ,

hy = Кр hyd

## Slide 8

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Способ обработки последовательностей

Хи ХХ,

h, = f(x, hy,
FO Pad hy, = (x, + 0) a + x) a@ + x,)a =
h, = К» hy) = A(X,» hy) = азх, + 0PX, + ах,

## Slide 9

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Рекуррентная нейронная сеть

м
Xx, У o(z)
* x $ | o(2)
X3
} a(z) |-4
Xn
+1 o(2)

Тема 2 . Васкргор и PyTorch

+1

hy = К» Ву)

| м

## Slide 10

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Рекуррентная нейронная сеть

h

t-1 21
м
Xx, У ®— o(z)
ы x $ | o(2)
X3
} a(z) |-4
Xn
+1 o(2)

а, = Wx,+h,, +b

Тема 2 . Васкргор и PyTorch

+1

В, = о(а)

hy = К» Ву)

Ea.

## Slide 11

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Рекуррентная нейронная сеть

he ; hy = f%o yD
я
и у
x, z > o(z) y,
ыы x @®—| o(z)
X3
} a(z) |-4

Xn
+1 + o(2)

+1
a,=Wx,+h,, +b h, = o(a,) 0,=Vh,+c

Тема 2 . Backprop и PyTorch У, s(0,)

## Slide 12

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Рекуррентная нейронная сеть

he ; hy = f%o yD
ре
w у
x, z 2 o(2) у,
* > Ф | of)
X3
® a(z) |-4

Xn
+1 + 0(2)

+1
а, = Wx, + h,, + b h, = o(a,) 0,=Vh,+c
ve bein aioe В, = [0,0,0,...,0,] Ye = S(0)

## Slide 13

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Рекуррентная нейронная сеть ha
h hy = f% ed a

У

1-1 gi zt

М У x h,
x, x D+ o(z) ‹ = ВЕ
Xx.
° > Ф | of)
Хз

® a(z) |-4

xX,
+1 + 0(2)

+1
а, = Wx, + h,, + b h, = o(a,) 0,=Vh,+c
Tema 2 - Backprop и PyTorch hy = [0, 0, 0, seey 0,1] У = s(0,)

## Slide 14

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Рекуррентная нейронная сеть ha
h hy = f% ed a

1 7 zi

и у х h у
x, у D4 o(z) Е с RNN |ot r |
Х.
° > ©—| o@)
X3

® a(z) |-4
x, h, У
x
>| RNN .

+1 +) 0(2)

+1
а, = Wx, + h,, + b h, = o(a,) 0,=Vh,+c
Tema 2 - Backprop и PyTorch hy = [0, 0, 0, seey 0,1] У = s(0,)

## Slide 15

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Развертка рекуррентной сети во времени

Г
RNN J ho 1 o В а ЕН, tht а +В д

Тема 2 . Васкргор и PyTorch

## Slide 16

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектуры Many-to-One и One-to-Many

y
y
: i

~

RNN => Bylo HAR, д НВ, > вн д д
i t t t t
x Ry, х, Xe af
; У, Ye Vet У,
1 f 1
aw |) >> Heel. о

Тема 2 . Васкргор и PyTorch

## Slide 17

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектуры рекуррентных сетей

Many-to-Many - перевод текста

Many-to-One - анализ эмоциональной окраски текста (на входе
текст, на выходе категория - положительный, нейтральный,
отрицательный)

@ One-to-Many - генерация изображений - на вход карты признаков
изображения - на выходе описание (текст)

@ One-to-One - Сеть принимает на вход один образец и выдаёт одну
метку класса (например, определение спама в электронном
письме: «это спам» или «это не спам»)

Васкргор и PyTorch

## Slide 18

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Развертка рекуррентной сети во времени

Г
RNN J ho 1 o В а ЕН, tht а +В д

Тема 2 . Васкргор и PyTorch

## Slide 19

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Реализация рекуррентного слоя в PyTorch

р, е, к, у, P,P, ©, H >| RNN > TT

Тема 2 . Васкргор и PyTorch

## Slide 20

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Реализация рекуррентного слоя в PyTorch

р, е, к, у, P,P, ©, H > ВММ > т

torch.nn.RNN

a h.,
7
У
м h,
x, Е» >| tanh = у,

Тема 2 . Васкргор и PyTorch

## Slide 21

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Реализация рекуррентного слоя в PyTorch

р, е, к, у, P,P, ©, H

Тема 2 . Васкргор и PyTorch

=>

RNN > TT

torch.nn.RNN

a h.,
7
У
и
—» >| tanh ===

У

t

a=Wx,+Vh,, + b, + 5,
h, = tanh(a,)

yah,

## Slide 22

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Реализация рекуррентного слоя в PyTorch

torch.nn.RNN(input_size, hidden_size,
num_layers=1,

nonlinearity='tanh’, bias=True,
р, е, к, у, р, ре, H >| ВММ > T batch_first=False)

torch.nn.RNN

и h

tl a=Wx,+ Vh,, +В, +b,

Vv в, = tanh(a,)
x, = >| tanh = у, y=h,

Тема 2 . Васкргор и PyTorch

## Slide 23

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Реализация рекуррентного слоя в PyTorch

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

hy a=Wx,+ УВ, +В, + b,

h, = tanh(a,)

va
У
м h,
x, = >} tanh —-,> У, y=h,

X, (seq_length, batch_size, d_sieze)

@ seq_length - длина подаваемой последовательности (число элементов)
® batch_size - размер батча
@ d_size - размер каждого подаваемого элемента последовательности

Тема 2 . Васкргор и PyTorch

## Slide 24

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Исчезающие и взрывающиеся градиенты

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

У
Ww

xX, —— >G)=>

h

t-1

7!

tanh

].
Cc

a=Wx,+Vh,, +В, +b,

h, = tanh(a,)

yah,

Тема 2 . Васкргор и PyTorch

t

У! У У:
i | т
h, oh, д ph, В, o
i i a
29 Х ag

## Slide 25

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Исчезающие и взрывающиеся градиенты

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

oH]

h
ee У! У
7 i *
У eli ..— Jin
У h, h, ~ ; th, 9 h, >... h,
x, Е» >) tanh = У, x x
1 2
а= их +Vh,, +b, +b, LSTM, GRU Г
5, 6] <A
h ит) 5=-
A, 6] =A
yah,

Тема 2 . Васкргор и PyTorch

[=

## Slide 26

Прогноз символов

Формирование обучающей выборки

Предыдущие символы

д и p и ж а 6 л b

Тема 2 - Backprop  PyTorch

## Slide 27

Прогноз символов

Формирование обучающей выборки

Предыдущие символы

д и p и ж а 6 л b

Тема 2 . Васкргор и PyTorch

## Slide 28

Прогноз символов

Формирование обучающей выборки

Предыдущие символы

д и p u ж

Тема 2 . Васкргор и PyTorch

## Slide 29

Прогноз символов

Формирование обучающей выборки

Предыдущие символы

op и PyTorch

## Slide 30

Прогноз символов

Формирование обучающей выборки

Предыдущие символы

д и p и ж а 6 л b
д и p u
и р и ж

Many-to-One

Тема 2 . Васкргор и PyTorch

## Slide 31

Прогноз символов

Формирование обучающей выборки

Предыдущие символы

Many-to-One

Тема 2 . Васкргор и PyTorch

д и и ж а 6 b a г а
д и и
: 2 x, h,
ри a в: > .| RNN
и | ж 6 я: 32
9:33

## Slide 32

Прогноз символов

Формирование обучающей выборки

Предыдущие символы

xX
д и p и а: [1, 0, 0, ..., 0] ——— Е
и р и ж 6: [0, 1, 0, ..., 0]
р ж | а в: [0,0,1,. о
и ж а 6
Many-to-One О ©

One Hot Encoding

## Slide 33

Прогноз символов

Формирование обучающей выборки

x У.

а: [1, 0, 0, ..., 0]
6: [0, 1, 0, ..., 0]

в: [0, 0, 1, ..., 0]

x; (batch_size, seq_length, d_size) seq_length

## Slide 34

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Класс torch.nn.RNN

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

hes rn = nn.RNN(d_size, hidden_size,
21 batch_first=True)
у x = torch.randn(8, 3, 33)
WwW h, y, h = rnn(x)
x, Е» >) tanh = У,

x, (batch_size, seq_length, d_size)

Тема 2 . Васкргор и PyTorch

## Slide 35

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Класс torch.nn.RNN

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

h

tl rn = nn.RNN(d_size, hidden_size,
21 batch_first=True)
у x = torch.randn(8, 3, 33)
WwW h y, h = rnn(x)
t
x, Е» >) tanh = У,

У, Yo У

i i i
р ой но Hab ГЫ
x, (batch_size, seq_length, d_size) o 4 "т 2 7 3

У xX Х2 x,

Тема 2 . Васкргор и PyTorch

## Slide 36

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Модель рекурентной нейронной сети

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

he,
ri
У
Хх, > tanh iar = У,

a=Wx,+Vh,, + b, +b,

h, = tanh(a,)

y=Uh,+b,

Тема 2 . Васкргор и PyTorch

## Slide 37

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Модель рекурентной нейронной сети

пеаг А

a=Wx,+Vh,, + b, +b,

h, = tanh(a,)

y=Uh,+b,

Тема 2 - Васкргор и PyTorch 4/25

## Slide 38

Прогноз символов

Формирование обучающей выборки

x У.

6: [0, 1, 0,

seq_length

class CharsDataset (data.Dataset):

def _ init__(self, prev_chars=3):
self prev_chars = prev_chars

with open(path, ‘r’, encoding="utf-8) as f:
selftext = fread()
selftext = selftext.replace(‘\ufeff’, )

selftext = ге.зиб([^А-яА-20-9.2; |, ", selfitext)

selftext = selfitext.lower()
self.alphabet = set(self. text)

self.int_to_alpha = dict(enumerate(sorted(self.alphabet)))
selfinum_characters = len(self.alphabet)

selfonehots = torch.eye(selfinum_characters)

def __getitem__(self, item):
_data =
torchstack([selfonehots{self.alpha_to_int[selftext[x]]]
for x in range(item, item+selfprev_chars)])
ch = selftext[item+self prev_chars]
t= self.alpha_to_int[ch]
return _data, t

## Slide 39

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Модель для прогноза слов

‘машина: [1, 0, 0, ..., 0]

желтый: [0, 1, 0, ..., 0]

дирижабль: [0, 0, 1, ..., 0]

Embedding

h,
>

e, = Emb* x,

лес: [0, 0, 0, ..., 1]

a=Wx,+Vh,, + b, +b,
h, = tanh(a,)

yv=Uh+b

## Slide 40

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Модель для прогноза слов

машина: [1, 0, 0, ..., 0]
D h

желтый: [0, 1, 0, ..., 0] ‚Е “
5

дирижабль: [0, 0, 1, ..., 0] xe} У
Ф и h
t
Е =| ФЕ
ш
лес: [0, 0, 0, ..., 1]
torch.nn.Embedding (num_embeddings, embedding_dim, ...) e, = Emb* x,
@ num_embedding - размер словаря a=Wx,+ Vh,, + b, + b,

@ embedding_dim - размер вектора эмбедингов

h, = tanh(a,)

t

yv=Uh+b

## Slide 41

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Модель для прогноза слов

‘машина: [1, 0, 0, ..., 0]

желтый: [0, 1, 0, ..., 0]

дирижабль: [0, 0, 1, ..., 0]

Embedding

лес: [0, 0, 0, ..., 1]

## Slide 42

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Модель для прогноза слов

машина: [1, 0, 0, ..., 0]

желтый: [0, 1, 0, ..., 0]

дирижабль: [0, 0, 1, ..., 0]

Embedding

лес: [0, 0, 0, ..., 1]

vocab_size

## Slide 43

Прогноз символов

Формирование обучающей выборки

x У.

6: [0, 1, 0,

seq_length

class CharsDataset (data.Dataset):

def _ init__(self, prev_chars=3):
self prev_chars = prev_chars

with open(path, ‘r’, encoding="utf-8) as f:
selftext = fread()
selftext = selftext.replace(‘\ufeff’, )

selftext = ге.зиб([^А-яА-20-9.2; |, ", selfitext)

selftext = selfitext.lower()
self.alphabet = set(self. text)

self.int_to_alpha = dict(enumerate(sorted(self.alphabet)))
selfinum_characters = len(self.alphabet)

selfonehots = torch.eye(selfinum_characters)

def __getitem__(self, item):
_data =
torchstack([selfonehots{self.alpha_to_int[selftext[x]]]
for x in range(item, item+selfprev_chars)])
ch = selftext[item+self prev_chars]
t= self.alpha_to_int[ch]
return _data, t

## Slide 44

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Исчезающие и взрывающиеся градиенты

va
У
м h,
x, = >| tanh => у

t raw

В, = tanh(Wx, + УВ. + b, + b,) WA

yHh, /-

Тема 2 . Васкргор и PyTorch

## Slide 45

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Исчезающие и взрывающиеся градиенты

hs У! У
У 7
и ] h, hy | ° HH
x, = >} tanh —-,> У, x x

РАНЕН

В, = tanh(Wx, + УВ. + b, +Ь,)

yah, /

## Slide 46

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Исчезающие и взрывающиеся градиенты

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

h о
ee У! У У
z i ] ва
У eli ..— Jin
и h, hy | о th, a} et -— 0-10
x, Е» >) tanh = У, x x x
1 2 t
в, = ReLU(Wx, + Vh,, + b, + b,) и
/
y=h, и
И
/

## Slide 47

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Исчезающие и взрывающиеся градиенты

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

h
tel У! 2
21 1 +
Vv Lt Wb ..— |+
У h, h, ~ ; th, 9 h, >... h,
х= > >) tanh =
У, x %

h, = tanh(Wx, + Ув. + b, + b,)

yah,

РАНЕН

## Slide 48

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Исчезающие и взрывающиеся градиенты

torch.nn.RNN(input_size, hidden_size, num_layers=1, nonlinearity='tanh’, bias=True, batch_first=False)

h
tel У! 2
21 1 +
Vv Lt Wb ..— |+
У h, h, ~ ; th, 9 h, >... h,
х= > >) tanh =
У, x %

h, = sigma(W x, + УВ, + b, + b,)

yah,

РАНЕН

## Slide 49

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Задачи с известной последовательностью

Продолжайте учиться. Трудности в конце концов создают сильных людей.

Пацаны ваще ребята, внатуре четко... Умеете, могете!

ДАТИВАЩЕВЫ ВСЕ
«МОЛОДЦЫ!

Мне публично выступить? Что вы?! Это точно не мое!

Чего тебе надо у меня дома?

Nn

## Slide 50

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Двунаправленные (bidirectional) RNN

У! Yo a Sei У:
i t i fo
0 o б б
¥ U тиц il U 1 U
concat concat ” concat concat
| | й |
и у, у,
У | У, “Ча 9
are 9: 47) 9ы | oO 9: g 0
+
w,
У. | w VE Woy. у оу Ww,
о Н НВ о НН | В, д Heth, я д
1 м 1 м | и т |
xX, Х Хх x,

## Slide 51

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ h, = sigma(W, x, + V,h,, + b, + b,)

red
Двунаправленные (bidirectional) RNN р
9, = sigma(W, x, + V,g,. +b, +b)

о, = [h, g,]
у, = sigma(U * 0, + b
У, У Yea Lanes rb)
т f i t
o д д б
т то 1‘ jiu
concat concat ” concat concat
У У У
у у f f
д < и 32 * о 93k =| Graf oF 9 то < Go
+ Ww. т
у у. \ у у у W,
A ; № lhe КН o HHA, | а
wt м 1 м | м 1

1

## Slide 52

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ
Двунаправленные (bidirectional) RNN
torch.nn.RNN(input_size, hidden_size, batch_first=True, bidirectional=True., ...)

rnn = nn.RNN(input_size, hidden_size, batch_first=True, bidirectional=True)
у, В = rnn(x, hO)

concat concat concat concat
= ] — +
й
у |
V, у,
у у, f [
оао gy) 9ы* о 994%
ы
=
м м м |
У. : ! У А У У. lv
Го Но Hing о o Hh Lo
„Тит м] „т

1 t

## Slide 53

Модель RNN-CeTH для сентимент-анализа

## Slide 54

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Формат обучающей выборки

seq_lenght
A

о мне нравится работа

&

a Это шедевр изобразительного искусства

о

2

8 Жизнь слишком коротка чтобы быть несчастной

## Slide 55

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Простой ВМ№-слой

h

t-1

a=Wx,+ УВ, +В, + b,

h, = tanh(a,)

yeh,

Тема 2 . Васкргор и PyTorch

РУ

t

Я очень люблю программировать, ...,
поэтому в будущем хочу стать
программистом.

## Slide 56

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Простой ВМ№-слой

п, Я очень люблю программировать, ...,
ri поэтому в будущем хочу стать
у программистом.
м h,
x, oc) >) tanh = У,

а= Ух, + Vh,, +В, + b,

LSTM (Long Short-Term Memory) -
h, = tanh(a,) долга краткосрочная память

yeh,

Тема 2 . Васкргор и PyTorch

## Slide 57

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура LSTM

## Slide 58

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура LSTM

забывание запоминание
ненужного нового

## Slide 59

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура LSTM

забывание запоминание
ненужного нового

f= 0(W,[h,, xX] + bp) f= 0,2;0,3;0,9;0, 150,5.

## Slide 60

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура LSTM

забывание запоминание забывание запоминание
ненужного нового h, ненужного нового h,
At
o
hes

f= OCW; [he Xe] + by) {= [0, 2; 0, 3; 0, 9; 0, 1; 0,5,...]" i,= o(W, [h,,, X] + bp) С, = tanh (We [hy XJ) + bo)

## Slide 61

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура LSTM

забывание запоминание забывание запоминание
ненужного нового h, ненужного нового h

f= OW [ha х +b) f= [0, 2; 0, 3; 0,9; 0,1; 0,5,.J" | i,= o(W, [h.1, Xd + Bp) C,= tanh (We [h,, x] + be)

а. = i, ®C, C,= f, OC, + a,

## Slide 62

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура LSTM

забывание запоминание
ненужного нового h

i,= o(W, [h,.,, X,] + b,)
a, = 0, ® tanh(C,)

[= o(W, Ch... X + b,) [= [0, 2; 0, 3; 0, 9; 0, 1; 0, 5,...]"

## Slide 63

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура LSTM

забывание
ненужного

запоминание
нового

f= o(W; В, x] + b)

i= ow, [h,.,, X,] + b)
С, = tanh (Мс [h,,, X,] + be)
a, = i, ®C,

С. =f, ®C,,+ 4,

0, = o(W, [h,,, X,] + b,)

В, = 0, ® tanh(C,)

## Slide 64

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура GRU

hes

У,

Gated Recurrent Units (GRU)

## Slide 65

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура GRU

забывание запоминание
ненужного нового

hes

У,

Gated Recurrent Units (GRU)

## Slide 66

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура GRU

забывание запоминание
ненужного нового

2, = o(W, [h,, X,] + b,)

hes

У | f=h,e-2)

## Slide 67

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура GRU

Gated Recurrent Units (GRU)

z,= o(W, Th, х] + b,)

f=h., ® (1-2)

и = o(W, [h.. xd + b,)

В, = tanh (W,, X, + Win (Е ®В, ,) + b,)

h,=h,, ® (1-2) +1 ® z,

## Slide 68

РЕКУРЕНТНЫЕ НЕЙРОННЫЕ СЕТИ

Архитектура GRU

Gated Recurrent Units (GRU)

z,= o(W, Th, х] + b,)

f=h., ® (1-2)

и = o(W, [h.. xd + b,)

В, = tanh (Wy, X, + Win Bh.) + by)

h,=h,, ® (1-2) +1 ® z,

torch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True,
batch_first=False, dropout=0.0, bidirectional=False., ...)
