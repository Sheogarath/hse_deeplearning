# Visual review: lecture_08/transformery.pptx

OCR of fully rendered slides; also includes image-only labels. OCR may contain mistakes.

## Slide 1

КУРС «НЕЙРОННЫЕ СЕТИ»

Механизм внимания и
трансформеры

## Slide 2

Механизм внимания - attention

Архитектура Seq2Seq

Decoder
ыы НЫ
S
SM SM SM 5м|
и
Епсодег Е fe fe fe fe
i ft 4 1
Во Ay A № J hy по [oF he fg Fe И
» Jt 4 | 1 1
Е aS a 3 28 5 a Х› | |Хз a
ТТ] i ef 7 f i
<bos> A снимаю <eos> <bos> A снимаю <eos>

## Slide 3

Механизм внимания - attention

Архитектура Seq2Seq

в,

X

a + Decoder
8) 5
o | [| [вт] [в ] з
7 | fi | sM| |SM| |SM 5м|
: - и
=
Епсодег 8 c a C
Во Ay A № J hy по [oF he fg Fe И
» Jt 4 | || 1 1
3 aS a 3 28 3 a Х› | |Хз a
ТТ] i ef 7 f i
<bos> A снимаю <eos> <bos> A снимаю <eos>

## Slide 4

Механизм внимания - attention

Качество перевода сетью типа Seq2Seq

BLEU score

RNNsearch-30 [>

RNNenc-50
RNNenc-30

10

20

30 40 50 60
Sentence length

## Slide 5

Механизм внимания - attention

Механизм внимания (attention)

|

А почему он поедет в Египет, ая когда поеду туда вместо него

LS

Why is he going to Egypt, and when will | go there instead of him?

## Slide 6

Механизм внимания - attention

Архитектура Seq2Seq с attention

Fig вы hg | | а >, [>

2 ft ff f fF i

3 xX X) № |) | У © bos - begin of sentence
2 1 т ы 7 1 © eos - end of sentence
Ш <bos> Я снимаю <еоз>

<bos>

## Slide 7

Механизм внимания - attention

Архитектура Seq2Seq с attention

ый
s(hy по)
| |

Fig вы hg | | а >, [>
2 ft ff f fF i
3 xX X) № |) | У © bos - begin of sentence
2 1 т ы 7 1 © eos - end of sentence
Ш <bos> Я снимаю <еоз>

<bos>

## Slide 8

Механизм внимания - attention

Архитектура Seq2Seq с attention

м1 (р sho!) = (hy * hg, 1=1,2,..,5

а=[а, а, ...а

b= [b,, by БГ
w,
w=al*b=ya*b= |а| *|b| *cosa
s(hy ho)
t |
Fig вы hg | | а >, [>
7 tt i
3 xX X) № |) | У © bos - begin of sentence
2 ® eos - end of sentence
ee Fe 1
<bos> Я снимаю <eos> <bos>

## Slide 9

Механизм внимания - attention

Архитектура Seq2Seq с attention

5, hy’)

{—_— _ t
НЙ, В, || ht >}
tot ft 4 i
Хх | |X] [Xs] № У

fof of of 1

<bos> <eos>
bos: Я снимаю <eos: <bos>

w, = s(hs, hy) м, We
1=1,2,...5 $(вх, hg!)

=
t

=
|

>

is

Embedding

## Slide 10

Механизм внимания - attention

Архитектура Seq2Seq с attention

w, = (85, №) м, Wa Wat | We
1=1,2,...5 s(hy, hg?) | || вх, hg
ry

is

Хх | |X] [Xs] № У

fof of of 1

<bos> <eos>
bos: Я снимаю <eos: <bos>

Embedding

## Slide 11

Механизм внимания - attention

Архитектура Seq2Seq с attention

ЗойМах
w, = s(hg, hy’) м, м мА №№,
1=1,2,...5 (п, hy?) s(h;*, hy?)
+

is

Хх | |X] [Xs] № У

fof of of 1

<bos> <eos>
bos: Я снимаю <eos: <bos>

Embedding

## Slide 12

Механизм внимания - attention

Архитектура Seq2Seq с attention

C= Da; * hs

+7
а, |“ a, a,

SoftMax

w= (hs he) Pw, и, мк Pw,
1=1,2,...5 5,5, п) (ву, hg!)
+ +
(в, hy’) | s(hy*, hy?) |
f ae |

lh, bln, в
tot ft 4 i
Хх | |X] [Xs] № У

fof of of 1

<bos> <eos>
bos: Я снимаю <eos: <bos>

=
t

=
|

>

is

Embedding

## Slide 13

Механизм внимания - attention

Архитектура Seq2Seq с attention

C= Da; * hs

+7
а, |“ a, a,

SoftMax

w= shih, ты Тю ми
1=1,2,...5 s(hst, hy?) ||| $(в,°, ng’)
+ +
(в, hy’) | s(hy*, hy?) |
f ae “tf

| | ]
hy +h, | Ао ГАИ | № = ВММАм, с, hg!)

tot ft 4 i
Хх | |X] [Xs] № У

fof of of 1

<bos> Я снимаю <eos>

=
t

=
|

>

is

Embedding

## Slide 14

Механизм внимания - attention

Архитектура Seq2Seq с attention

= 2 а, * 1
x ae аготах
а, | a, a, a,

SoftMax 1

w= $, Ты W2 Wit] We SM | SoftMax
i=1,2,...,5 s(h,¢, hg?) s(h,°, hy’) i

hg |, hy hg В, | В id | В = ВММАУ, col, ho)

is

Хх | |X] [Xs] № У

fof of of 1

Embedding

## Slide 15

Механизм внимания - attention

Архитектура Seq2Seq с attention

= 2 а, * 1
x ae аготах
а, | a, a, a,

SoftMax 1

SoftMax

Attention (внимание)
>
=
га
>
Sa
|=
Sa
&
<
>
aB
2 |=
>
S
n
| =

Ви = RNN(Lv;, Go, hg’)

=
t
=
|
>
в
>
1
>
>
}
>

is

Хх | |X] [Xs] № У

fof of of 1

Embedding

## Slide 16

Механизм внимания - attention

Структура сети определяет ее функциональность

## Slide 17

Механизм внимания - attention

Структура сети определяет ее функциональность

Фрагмент
нейронной сети

Фрагмент
нейронной сети

Фрагмент
нейронной сети

## Slide 18

Механизм внимания - attention

Архитектура Seq2Seq с attention

= 2 а, * 1
x ae аготах
а, | a, a, a,

SoftMax 1

SoftMax

Attention (внимание)
>
=
га
>
Sa
|=
Sa
&
<
>
aB
2 |=
>
S
n
| =

Ви = RNN(Lv;, Go, hg’)

=
t
=
|
>
в
>
1
>
>
}
>

is

Хх | |X] [Xs] № У

fof of of 1

Embedding

## Slide 19

Механизм внимания - attention

Механизм внимания (attention)

agreement

on
European

Economic

The
the

la
zone
économique

européenne
a

été
signé
en

aotit
1992

<end>

=
G
Е
=
5
>
2
с.

Ш

convient

de

noter

que

r
environnement
marin|

environnement.

<end>|

environments

of

## Slide 20

Механизм внимания - attention

Архитектура Seq2Seq с attention

Attention (внимание)

и

Со

=Ха* в;

=

SoftMax

argmax

SoftMax

h,t | het = ЕМУ,» си, В)

Во | в, Fh В Fs ——| ht rh?

» _ ttf 1!
Е Хх | || || № У У
a etl 1 оао ele ae |

## Slide 21

Механизм внимания - attention

Качество работы механизма вниамния

Г =ya*he п п п

ЗойМах 1 | 1

Attention (внимание)
>
=
га
>
Sa
|=
Sa
&
<
>
aB
2 |=
>
S
n
| =
vn
He
n
y=

ho! ria? Py hg H hf

=
t
=
|
>
в
>
1
>

is

Хх | |X] [Xs] № У! У Уз

fof of of fof 1

<bos> Я снимаю <eos> <bos> 1 filming

Embedding

## Slide 22

Механизм внимания - attention

Архитектура Seq2Seq с attention

BLEU score

30

25

on

20

RNNsearch-50) |-.............--Ё

RNNsearch-30 |:
RNNenc-50
RNNenc-30

0

10 20

Sentence length

## Slide 23

Механизм внимания - attention

self-attention

h, В,
Г 1
x, Xp Хз x,

fof of of

<bos> Я снимаю <eos>

Е
t
=
|
=
в

is

Embedding

## Slide 24

Механизм внимания - attention

self-attention

|

А почему он поедет в Египет, ая когда поеду туда вместо него

LS

hy oh, phy № fg
ttt
хх № || №
3

5

a ale 1 оао ee

## Slide 25

Механизм внимания - attention

self-attention в кодере

h, В,
tit t ft +f
x, Xp Хз x,

fof of of

<bos> Я снимаю <eos>

Е
t
=
|
=
в

is

Embedding

## Slide 26

Механизм внимания - attention

self-attention в кодере

hy
28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

=
is

Embedding

## Slide 27

Механизм внимания - attention

self-attention в кодере

=
is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 28

Механизм внимания - attention

self-attention в кодере

=
is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 29

Механизм внимания - attention

self-attention в кодере

=
is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 30

Механизм внимания - attention

self-attention в кодере

=
is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 31

Механизм внимания - attention

self-attention в кодере

=
is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 32

Self-attention

Механизм внимания - attention

self-attention в кодере

hy }olh, в, в. | fh,
>» Jt ft ft

Е 28 2 5 28

a etl 1 оао ele

## Slide 33

Self-attention

Механизм внимания - attention

self-attention в кодере

Updated: | H,°

=a, hy + a, В. +a, В,

=
is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 34

Self-attention

Механизм внимания - attention

self-attention в кодере

Updated: | H,° | |H,°

c,=a, hy + a, Не +a, В?

=
is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 35

Self-attention

Механизм внимания - attention

self-attention в кодере

Updated: | H,° | |H,°

c=a, hy + a, В. +a, В?

Дао]

SoftMax
*

w, [№
6
1

th, >,

>
t

=
|

>

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 36

Self-attention

Механизм внимания - attention

self-attention в кодере

Updated:

AY

Hy | |H,°

c=a, hy + a, В. +a, В?

Дао]

SoftMax

м, tw,
Е
|

=
is

А, ihe | hs Phy

Embedding

X, | |X| || |X,
fof of of
<bos> Я снимаю <eos>

## Slide 37

Self-attention

Механизм внимания - attention

self-attention в кодере

Updated: Н’ | |H,° | |H,° | НР

=
t
=
>
ns
в
=>
5
|
у
>
FS

is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 38

Механизм внимания - attention

Механизм внимания (attention)

|

Why is he going to Egypt, and when will | go there instead of him?

LS

## Slide 39

Механизм внимания - attention

self-attention в декодере

copy
в; |+ ни |

Г

fof of of

<bos> Я снимаю <eos>

Е
t
=
|
=
в

is

Embedding

## Slide 40

Механизм внимания - attention

self-attention в декодере

pe

SM | SoftMax

и | >| ho! rh?
tot ft 4 t
Хх | |X] [Xs] № У

fof of of

<bos> <eos>
bos: Я снимаю <eos: <bos>

Е
t
=
|
=
в

h,4= RNN(y,,h,')

is

Embedding

## Slide 41

Механизм внимания - attention

self-attention
|
argmax ]
SoftMax SM
i
fe
1
hy ih, rh, = № Ра ——| ht rh? Г” hf
» _ ttf i i
Е Хх | || || № У У
a ale 1 маю ee <bos> 1

## Slide 42

Механизм внимания - attention

self-attention
C= a *h,!
1
а. =1 | sm
hy ih, rh, = № Ра ——| ht rh? Г” hf
» _ ttf i t
Е Хх | || || № У У
a etl 1 маю ee <bos> 1

## Slide 43

Механизм внимания - attention

self-attention
|
argmax ]
SoftMax SM
i
fe
1
hy ih, rh, = № Ра ——| ht rh? Г” hf
» _ ttf i i
Е Хх | || || № У У
a ale 1 маю ee <bos> 1

## Slide 44

Механизм внимания - attention

self-attention

р filming

argmax ] ]
SoftMax SM SM

| i
к К

i i

hy |e, fof }ofh bf, |} ig? GE, | [ne | hy

f ft ft 4 foot ft

хх У, У Уз

fof of of

<bos> Я снимаю <eos>

Embedding

<bos> 1 filming

## Slide 45

Механизм внимания - attention

self-attention
"O
hy both, bola, С Hh? + fhe | hy

f ft ft 4 fo of ft

хх У, У Уз

fof of of

<bos> Я снимаю <eos>

Embedding

filming

## Slide 46

Механизм внимания - attention

self-attention
C3= a, * ВА + a,*h,t
а, | %
SoftMax
w, @ w,
_

hy hy hy hg В, |} >| ht ht | ht ht
>» _ Jt t ft i i t
Е Хх | || || № У! У Уз
a зы 1 а ele <bos> | filming

## Slide 47

Механизм внимания - attention

self-attention
c,= a, * ВА + a, *h,t
a, |
SoftMax Ни
w, м, i
$n
hy hy hy hg > hy hot ва > Ва | ht
>» _ Jt t ft t i t
Е Хх | || || № У! У Уз
a oles 1 а ele <bos> | filming

## Slide 48

Механизм внимания - attention

self-attention
cinema
C,= a, * В + a, *h,t SM
а, | %
SoftMax НЕК
Ww, м, i
t
hy hy hy hg В, |} >| ht ht | ht ht
>» _ Jt t ft t i t
Е X,| |X| |X| 1X У! V2 Уз
a oles 1 а ele <bos> | filming

## Slide 49

Механизм внимания - attention

self-attention

<eos>
SM
c= a, * ВЯ + a, *h,+ a, *h,? | | fc
a.
а, | & a,
SoftMax H,
Ww, м, м,
о 5 5 c, ва
hy А, rts [в В hy! poh > ht | ра РАЯ
аа ttf 4
Е Хх | || || № У! У Уз Ya
2
eT tft a
<bos> Я снимаю <eos> <bos> | filming cinema

## Slide 50

Механизм внимания - attention

Attention с Self-attentiona декодера

А почему он поедет в Египет, а я когда поеду туда вместо него

ye
|
Cross-Attention

| Self-attention decoder NN

| { |
Why is he going to Egypt, and when will | go there instead of him?

| t

## Slide 51

Механизм внимания - attention

Attention с Self-attention декодера

C= da, *he у
SoftMax SM

PO OO а
I fc
h, hy hg +} hy |} ho! Ва |? = RNN(LY, ag], hy)

f ft ft 4 i

Хх | |X] [Xs] № У

fof of of 1

<bos> <eos>
bos: Я снимаю <eos: <bos>

Attention

=
t

Embedding

## Slide 52

Механизм внимания - attention

Attention с Self-attention декодера

c= ya, * йе р filming
SoftMax SM | |SM

т f
У? ® fe| lfc
h, ra Fs ft |} et st Pt
tot ft 4 i i

X,| |X] № |X, У! Yo

fof of of tof

<bos> <eos>
bos: Я снимаю <eos: <bos> \

Attention

=
t

Embedding

## Slide 53

Механизм внимания - attention

Attention с Self-attention декодера

c= ya, * йе р filming
SoftMax SM | |SM

POO? aE
| КО в puny al ho
h

Attention

Во FA [№ № | й ——| ht НЯ phat pe hy?
» _ ttf i 1“
Е Хх | || || № У! Y2 Уз
Ё р 1 оао ele ae hg

## Slide 54

Механизм внимания - attention

Attention с Self-attention декодера

стета
= ©=Х а * йе
5 C= >. а, *he 22 ] 1 5М
3 5 |
В SofMax = | |SoftMax fe
< 8

РРР О

мВ, | | |} >| И
tot ft 4 i
Хх | |X] [Xs] № У! Y2 Уз

fof of of fof 1

<bos> Я снимаю <eos> а
<bos> | filming

=
t

>
=
|
>
=
|
|
>.
Py
=
Е
=

Embedding

## Slide 55

Механизм внимания - attention

Attention с Self-attention декодера

<eos>
= c,= La, *he

= C= >. а, *he 22 ] 1 В SM
© У 1

= =

SoftM

5 me = | |SoftMax fe
< 8

ва

оФо® '©

1
5 Cy
|
| а Ни h,
i | |

2
д
|

=
Sa

hy bh, th, bh, |
tot ft 4
Хх | |X] [Xs] № У! Y2 Уз Уз

fof of of fof 1

<bos> Я снимаю <е0з> ‘mi it
<bos> 1 filming cinema

=
t

a

Embedding

## Slide 56

Механизм внимания - attention

Механизм внимания (attention)

Self-attention decoder

+ |
А почему он поедет в Египет, а я когда поеду туда вместо него

a J

Cross-Attention

| Self-attention decoder NN

| { |
Why is he going to Egypt, and when will | go there instead of him?

t J

## Slide 57

Механизм внимания - attention

self-attention в кодере

Updated: Н’ | |H,° | |H,° | НР

=
t
=
>
ns
в
=>
5
|
у
>
FS

is

28 2%) xe 28

fof of of

<bos> Я снимаю <eos>

Embedding

## Slide 58

Self-attention

Механизм внимания - attention

Attention с Self-attention

5 c= da, *he
Е SoftMax
< @ cinema
= *he
® Ф 9 М | Су
| 5 | | т
$ ic
Updated: |H,? | |H,° | |H,° | НР = SoftMax iP
hy |B, hy |} hy |} hy па вы в вы
тт tote
Е % | || [Xa] [м У У Уз
ттт ттт
<bos> Я снимаю <еоз> <bos> ; timing

## Slide 59

Механизм внимания - attention

Архитектура Seq2Seq

® цепочки данных обрабатываются
последовательно и эти Decoder
вычисления не x
распараллеливаются Е
5
® при обучении возникает известная ©
проблема взрывающихся или SM SM SM 5м|
затухающих градиентов 1 i 1 1
5
ЕК |fc| |fe ic
Encoder 8 fe f f f
i ft 4 1
О }th, |. С п О О О ИА
*
» Jt 4 | || 1 1
= =
| №] № 28 № № № a
5 5
ef 4 1 eff 4 i
<bos> A снимаю <eos> <bos> A снимаю <eos>

## Slide 60

Механизм внимания - attention

Трансформер. Архитектура

могут обрабатывать последовательности данных в параллельном режиме

## Slide 61

Механизм внимания - attention

Трансформер. Архитектура

могут обрабатывать последовательности данных в параллельном режиме

ChatGPT (OpenAl)
Gemini (Google DeepMind)
Claude (Anthropic)

Llama (Meta)

DeepSeek

YandexGPT

Transformer Output
EncoderN DecoderM
fg
o
8 Encoder3 Decoder3
о
a Encoder2 Decoder2
Encoder1 Decoder1
Input Output

siapos0q

## Slide 62

Трансформер. Архитектура

Output
Probabilities

Tinear

Fee

ECrES

Multi-Head
Attention,

У

Positional b Positional
Encoding fae) Encoding

Input Output
Embedding Embedding
Inputs Outputs

(shifted right)

## Slide 63

Механизм внимания - attention

Трансформер. ОКУ Self-Attention

Output
4

т
Add & LayerNorm

Feed Forward

Encoder

Add & LayerNorm

wwe)
Positional Encoding =)
4}

Embedding

ify

Input

ры

Е

X

Xs

<bos>

A

снимаю

кино

<eos>

## Slide 64

Механизм внимания - attention

Трансформер. ОКУ Self-Attention

Output
4

Encoder

Add & LayerNorm

Feed Forward

Add & LayerNorm

Positional Encoding

a [ %
=>)
<P

Embedding

ify

Input

Embedding

9 @ @® ®@
х, х х. x, Xs
<bos> я снимаю кино <eos>

## Slide 65

Механизм внимания - attention

Трансформер. ОКУ Self-Attention

Output
4

Encoder

Add & LayerNorm

Feed Forward

Add & LayerNorm

Positional Encoding

a [ %
=>)
<P

Embedding

ify

Input

query
ЧЕМ. *х
Embedding

м = s(a,b) = a" *b = У a; *b,

tte aa

W,*x, | Wy x, | Wes | Wa" Xe | Wa Xs
Linear, Wq
|
х, х, Xs х №
<bos> я снимаю кино <eos>

## Slide 66

Механизм внимания - attention

Трансформер. ОКУ Self-Attention

Output
И м = s(a,b) = a" *b = У а, *b,

т
Add & LayerNorm

Feed Forward

Encoder

Add & LayerNorm query | || K |] a] ke вк кю

k= W,*x, Linear, Wk
Positional Encoding =) ‘ + Le Г + Г* Le

ЧЕМ, *x, Linear, Wq
t 1
Embedding x " . : . 1
a 3 3 5

uN Embedding

Input <bos> A снимаю кино <eos>

## Slide 67

Механизм внимания - attention

Трансформер. ОКУ Self-Attention

Output
4 м = s(a,b) = a" *b = У a; *b,
Add & LayerNorm

Е Уи Wi Wi3 Мы Wis
5 Feed Forward 5 $ 5 5 5
8
2
Ш Add & LayerNorm query ||] Ki |[ de |] Ko | aa }| Ke |] Qe] | Ke || as |] Ks

k= W,*x, Linear, Wk
Positional Encoding =) ‘ + Le Г + Г* Le

ЧЕМ, *x, Linear, Wq
t 1
Embedding x " . : . 1
a 3 3 5

uN Embedding

Input <bos> A снимаю кино <eos>

## Slide 68

Механизм внимания - attention

Трансформер. ОКУ Self-Attention

Output
4

Encoder

Add & LayerNorm

Feed Forward

Add & LayerNorm

Positional Encoding

a [ %
=>)
<P

Embedding

ify

Input

SoftMax(w/Vd)

query

k= W, *x,

ЧЕМ. *х

Embedding

9, Ge || Ke | Gs |] Ks || da} | Ke | | a5 |] Ks
| | | |
Linear, Wk
Lt La Lt | Lt
Linear, Wq
С
д х, X X Xs
<bos> я снимаю кино <eos>

## Slide 69

Механизм внимания - attention

Трансформер. ОКУ Self-Attention

Output
4

Encoder

Add & LayerNorm

Feed Forward

Add & LayerNorm

Positional Encoding

a [ %
=>)
<P

Embedding

ify

Input

SoftMax(w/Vd)

query

k= W, *x,

ЧЕМ. *х

Embedding

9, Ge || Ke | Gs |] Ks || da} | Ke | | a5 |] Ks
| | | |
Linear, Wk
Lt La Lt | Lt
Linear, Wq
С
д х, X X Xs
<bos> я снимаю кино <eos>

## Slide 70

Механизм внимания - attention

Трансформер. ОКУ Self-Attention

Output
4

Encoder

Add & LayerNorm

Feed Forward

Add & LayerNorm

Positional Encoding

a [ %
=>)
<P

Embedding

ify

Input

SoftMax(w/Vd)

query
key
value

v= М, *х,

k= и, *х,

ЧЕМ. *х

Embedding

Gs |] Ki J] Ge Ke J def] Ke J] Qa | | Ks |] os |} Ks
¥ = 7
+ + 1 4
Linear, Wv |

т
Linear, Wk
Lt La Г * | Lt
Linear, Wq
С
д х, X X Xs
<bos> я снимаю кино <eos>

## Slide 71

Механизм внимания - attention

Вычисление ОКУ Self-Attention

emb_size

SoftMax(w/Vd) SoftMax

query | % || ki |G |} K. | as || Ks || da |] Ke || as

ЕЕ

key + А
value “ У | № Es
Я + + +
v= W, *x, Linear, Wv
k= W,*x, Linear, Wk
Lt La Lt | Lt
q=W,*x, Linear, Wq
t Ы 11 1 f
x x XG Xq Xs
Embedding
<bos> я снимаю кино <eos>

## Slide 72

Механизм внимания - attention

Вычисление ОКУ Self-Attention

emb_size d_attn d_attn
Я
x 4 _ с=У а *м,
Е N
о SoftMax(w/Vd) SoftMax
x Ww,
=XFW,
©
Я query | 4 || Ki || de |) ke | as || Ks |) Ge] | Ke || as |) ks
x = key ¥ + р
Е N value \ val | у У [=]
[5 + ry с
x м, v= М, *х, Linear, Wv
=XFW,
k= М, *х, Linear, Wk
< ‘| [ [4 [+ [+ [+
К. а=и, *х Linear, Wq
ха = ‘
Е м t f| tl 1 f
2h ре XG Xq Xs
x Ww, ОНИ Embedding
- . <bos> я снимаю кино <eos>

## Slide 73

Механизм внимания - attention

Вычисление ОКУ Self-Attention

d_attn

SoftMax(w/Vd)

ЧЕМ. *х

у Embedding

<bos> A снимаю кино <eos>

## Slide 74

Механизм внимания - attention

Вычисление ОКУ Self-Attention

d_attn N N
Е
Е _ = a,*y,
= N
SoftMax(w/Vd) SoftMax
=Q¥KT
query | |] K || G | ke | de || Ke |) Ga | | Ke || as |} Ks
N key + 1
value У У ] Ms te [=]
Я + + +
В v= W, *х, Linear, ММ
k= W,*x, Linear, Wk
Lt La Lt | Lt
N q=W,*x, Linear, Wq
i Ы 11 f f
x ра x, x Xs
у Embedding
<bos> я снимаю кино <eos>

## Slide 75

Механизм внимания - attention

Вычисление ОКУ Self-Attention

d_attn N N

9 ат

A=SoftMax(QK'Ndy.,) = |

SoftMax(w/Vd)

ЧЕМ. *х

Embedding

ky
+ р
+ +
Linear, Wv
Linear, Wk
Lt La Г * | Lt
Linear, Wq
t Ы 11 1 f
x x XG Xq Xs
<bos> я снимаю кино <eos>

## Slide 76

Механизм внимания - attention

Вычисление ОКУ Self-Attention

d_attn N N
Е *
В с =), а, ту,
ха _ 1= La, * у,
N
SoftMax(w/Vd) SoftMax
=Q¥KT
N
query | 4% |] ki || a |] kK. | as |] Ks || ae || Ka || as |] Ks
key + 1
value У У ] Ms te [=]
A=SoftMax(QK'Ndy.,) = | + + *
v= W, *x, Linear, Wv
k= W,*x, Linear, Wk
Lt [T+ т + [+ [+
хм м q=W,*x, Linear, Wq
i ill tl i f
х, xX Хх: Xy Xs
А у = Embedding
<bos> я снимаю кино <eos>

## Slide 77

Механизм внимания - attention

Вычисление ОКУ Self-Attention

d_attn N N
£ уа*
В с =), а, ту,
ха _ a hoi
N
SoftMax(w/Vd) SoftMax
=Q¥KT
N “2
query | 4% |] ki || a |] kK. | as |] Ks || ae || Ka || as |] Ks
key + 1
value У У ] Ms te [=]
A =бойМажОктАа „) *У я с * +
v= W, *х, Linear, ММ
k= W,*x, Linear, Wk
Lt La Lt | Lt
q=W,*x, Linear, Wq
t Ы 11 1 f
xX, х, х, Xq Xs
Embedding
<bos> я снимаю кино <eos>

## Slide 78

Механизм внимания - attention

Вычисление ОКУ Self-Attention

d_attn N N

9 ат

А =боМах(ОКТА/„) * У

СРТ-4: 32768 токенов
LLaMA 3.1 : 128000 токенов

SoftMax(w/Vd)
query
key
value

v= W, *х,
k= W, *x,
ЧЕМ. *х
Embedding

9, Ge || Ke | Gs |] Ks || da} | Ke | | a5 |] Ks

¥ = 7
+ + +
Linear, Wv
Linear, Wk

Lt La Г * | Lt
Linear, Wq

t Ы 11 1 f

х, X x, x Xs

<bos> я снимаю кино <eos>

## Slide 79

Механизм внимания - attention

Трансформер. Multi-head Attention

d_attn N N
Е
ХЕ - ee La*y,
° N
SoftMax(w/Vd) SoftMax
=Q*KT
N “2
query | 4% |] ki || a |] kK. | as |] Ks || ae || Ka || as |] Ks
A =SoftMax(QK'Nd,,,) * У. key + — +
value je у | % Ye [=]
+ + +
влияние токена А на токен В ve W,*x, Linbar, Ww
было бы равно влиянию
токена В на токен А. k= W,*X, Linear, Wk
[ * [T+ т + т + [+
ЧЕМ, *x, Linear, Wq
t Ы 11 f f
2h x XG Xq Xs
Embedding

<bos> A снимаю кино <eos>

## Slide 80

Механизм внимания - attention

Трансформер. Multi-head Attention

d_attn N

N

d_attn
1

A =SoftMax(QK' doy,,) * У

влияние токена A Ha токен В
было бы равно влиянию
токена В на токен А.

Я снимаю кино

SoftMax(w/Vd)
query
key
value

v= W, *х,
k= W, *x,
ЧЕМ. *х
Embedding

9 | ke | Ga || Ke || % || ks

¥ = 7
+ + +
Linear, Wv
Linear, Wk

Lt La Lt | Lt
Linear, Wq

t Ы 11 f f

ро х, Xs Xq №

<bos> я снимаю кино <eos>

## Slide 81

Механизм внимания - attention

Трансформер. Multi-head Attention

Output
4
Add & LayerNorm SoftMax(w/Vd)

5 Feed Forward

3

Е

2

ui Add & LayerNorm query

key
Positional Encoding =) k= W,*X,

Embedding

uN Embedding

Input

ЧЕМ. *х

Gs |] Ki J] Ge Ke J def] Ke J] Qa | | Ks |] os |} Ks
¥ = 7
+ + 1 4
Linear, Wv |

т
Linear, Wk
Lt La Г * | Lt
Linear, Wq
С
д х, X X Xs
<bos> я снимаю кино <eos>

## Slide 82

Механизм внимания - attention

Трансформер. Multi-head Attention

$ ]
А почему он поедет в ЕГИПЕТ, а я когда поеду туда вместо него

t J

## Slide 83

Механизм внимания - attention

Трансформер. Multi-head Attention

Output
4
Add & LayerNorm SoftMax(w/Vd)

5 Feed Forward

3

Е

2

ui Add & LayerNorm query

key
Positional Encoding =) k= W,*X,

Embedding

uN Embedding

Input

ЧЕМ. *х

Gs |] Ki J] Ge Ke J def] Ke J] Qa | | Ks |] os |} Ks
¥ = 7
+ + 1 4
Linear, Wv |

т
Linear, Wk
Lt La Г * | Lt
Linear, Wq
С
д х, X X Xs
<bos> я снимаю кино <eos>

## Slide 84

'Механизм внимания - attention

Трансформер. Multi-head Attention

emb_size

## Slide 85

'Механизм внимания - attention

Трансформер. Multi-head Attention

dk dk ©,

dk = emb_size /п

emb_size

XY emb_size

## Slide 86

'Механизм внимания - attention

Трансформер. Multi-head Attention

dk dk ©,

dk

dk = emb_size /n

emb_size

XY emb_size

## Slide 87

Механизм внимания - attention

Трансформер. Multi-head Attention

dk = emb_size/n

emb_size

№ emb_size
Vv

<
=
я
=
я

п голов внимания (multi-head)

## Slide 88

emb_size

Механизм внимания - attention

Трансформер. Multi-head Attention

dk *n = emb_size
A

dk w, dk Q к,
м, =
С,
|.
dk w, dk 2 к
м, =

## Slide 89

Механизм внимания - attention

Трансформер. Multi-head Attention

У ть size

dk Q
и к dk
о Ир и, И У,
8 A
= w,
o 2
| =—>
с,
dh 1
dk dk Q,
р и, И у,
м,
2
| =—>

## Slide 90

Механизм внимания - attention

Трансформер. Multi-head Attention

У ть size

emb_size

dk Q
и к dk
о Ир и, И У,
8 A
= w,
o 2
| =—>
с,
dh
dk dk Q,
р и, И у,
м,
2
| =—>

## Slide 91

трансформеры

Трансформер. Блок Add & LayerNorm

Output
a

Encoder

emb_size

Add & LayerNorm
Feed Forward

Add & LayerNorm

=

Positional Encoding

emb_size

=
‘fi

Embedding N

ify

Input

## Slide 92

трансформеры

Трансформер. Блок Add & LayerNorm

Output

Encoder

4
т

Add & LayerNorm
Feed Forward
Add & LayerNorm

и

ых

Positional Encoding

=
‘fi

Embedding

ify

Input

Xs

Xs

снимаю

кино

<eos>

## Slide 93

трансформеры

Трансформер. Блок Add & LayerNorm

Output
4

Add & LayerNorm
Feed Forward г

5
3
3 й
ui Add & LayerNorm
|. 7 =| 22
— Z=
we x4 xt xt x xt
я 2
~~ i x,+Z, XtZy ] о | 4 XitZ, Xst25
= + у * ry *
Positional Encoding => x
1 2 Z, 5 2, 2,
fi X=} №
Embedding a
we x, х, Хх, x №
a} XN,
input м <bos> я снимаю кино — <е03>

## Slide 94

трансформеры

Трансформер. Блок Add & LayerNorm

Output
4

Add & LayerNorm
Feed Forward г

5
3
3 й
ui Add & LayerNorm 2
ж——— И =| 22
LayerNorm
we x4 xP xt xt xd
я 2
~~ i x, +2, XtZy ] о | 4 XitZ, Xst25
= т у * ry *
Positional Encoding => x
1 2, 2, 2: 24 55
fi X=} №
Embedding a
we x, х, Хх, x №
a} XN,
input м <bos> я снимаю кино — <е03>

## Slide 95

трансформеры

Трансформер. Блок Add & LayerNorm

Output
4

Encoder

Add & LayerNorm
Feed Forward
Add & LayerNorm

и

ых

Positional Encoding

=
‘fi

Embedding

ify

Input

LayerNorm
т * 7 у
x, х, х х,
i i i i i
X,+Z, XZ, ха р х,+25
т I I I I
% 2, % 2 25
x Х № № Xs
<bos> A снимаю кино <eos>

## Slide 96

трансформеры

Архитектуры post-norm и pre-norm

post-norm ‘

LayerNorm

| ‘Add
| Mult-head Attention |
[A] 7

skip (residual) Embedding
connection

## Slide 97

трансформеры

Архитектуры post-norm и pre-norm

jost-norm
р 4 pre-norm й

LayerNorm Add

| ‘Add
| Mult-head Attention | Laem
|

skip (residual) Embedding Embedding

connection

## Slide 98

трансформеры

Трансформер. Блок Feed Forward

ft of

Output Ya
4 Linear2
и з
Add & LayerNorm 8 Dropout
5
с ReLU или GELU
5 Feed Forward 3 =
3 iva Linear1
2 + + + +
w Add & LayerNorm 1
LayerNorm
Af? х, | xf xf xi xt
т у * ry *
Positional Encoding =>
Multi-head 2 2, 4; % 25
4} Attention
Embedding =
> embedding xX xX № № 55

Input <bos> я снимаю кино <eos>

## Slide 99

трансформеры

Трансформер. Блок Feed Forward

t 4 4 4 4
Output
4 к Add & LayerNorm
Add & LayerNorm 1 1 1 1 1
Linear2
5 Feed Forward з
3 g Dropout
8 Е
5
a Add & LayerNorm cs ReLU или GELU
Е
2 Linear1.
ry ry ry
т | |
add Add & LayerNorm
тт + ¥ + ¥
Positional Encoding =>
Multi-head 2 2, 4; % 25
4} Attention
Embedding I
© embedding xX X № Xa aS

Input <bos> A снимаю кино <eos>

## Slide 100

трансформеры

Архитектуры post-norm и pre-norm

skip (residual)
connection

Encoder

post-norm

ry

LayerNorm

Feed Forward

LayerNorm
т

Embedding

Encoder

pre-norm

Add

Feed Forward

LayerNorm

Add

Embedding

## Slide 101

трансформеры

Трансформер. Блок Feed Forward

t 4 4 4 4
Output
4 к Add & LayerNorm
Add & LayerNorm 1 1 1 1 1
Linear2
5 Feed Forward з
3 g Dropout
8 Е
5
a Add & LayerNorm cs ReLU или GELU
Е
2 Linear1.
ry ry ry
т | |
add Add & LayerNorm
тт + ¥ + ¥
Positional Encoding =>
Multi-head 2 2, 4; % 25
4} Attention
Embedding I
© embedding xX X № Xa aS

Input <bos> A снимаю кино <eos>

## Slide 102

трансформеры

Трансформер. Позиционное кодирование

Кабан наступил на баклажан
Output
4

Add & LayerNorm баклажан наступил Ha Кабан
Feed Forward

Add & LayerNorm

——=

Positional Encoding =)
4}

Encoder

Embedding
> embedding х, х & ay &
Input <bos> A снимаю кино <eos>

## Slide 103

Механизм внимания - attention

Трансформер. Позиционное кодирование

Кабан наступил на баклажан баклажан наступил на Кабан
Output
А м = s(a,b) = a" *b = У а, *b,
т
Add & LayerNorm

Е Уи Wi Wi3 Мы Wis
5 Feed Forward
3
Е
2
Ш Add & LayerNorm query ||] Ki |[ de |] Ko | aa }| Ke |] Qe] | Ke || as |] Ks

key | T т | т т

— я k= М, *х, Linear, Wk
Positional Encoding =) Lt Г * LF L+ т *

ЧЕМ, *х Linear, Wq
Embeddin i il n 1 i
ы Xx X Х Xq Xs

uN Embedding

Input <bos> A снимаю кино <eos>

## Slide 104

Механизм внимания - attention

Трансформер. Позиционное кодирование

Кабан наступил на баклажан баклажан наступил на Кабан
Output
А w = s(a,b) = a *b = У а, *b, w = s(a,b) = s(b, а)
т
Add & LayerNorm

Е Уи Wi Wi3 Мы Wis
5 Feed Forward
3
Е
2
Ш Add & LayerNorm query ||] Ki |[ de |] Ko | aa }| Ke |] Qe] | Ke || as |] Ks

key | T т | т =

— я k= М, *х, Linear, Wk
Positional Encoding =) Lt Г * LF L+ т *

а=и, *х Linear, Wq
Embeddin i il n 1 i
ы Xx X Х Xq Xs

uN Embedding

Input <bos> A снимаю кино <eos>

## Slide 105

Механизм внимания - attention

Трансформер. Позиционное кодирование

Output

Encoder

4
т

Add & LayerNorm
Feed Forward
Add & LayerNorm

——=

Positional Encoding

=
‘fi

Embedding

ify

Input

Positional
Encoding

Embedding

0 at 2 3 4
х, х х. x, Xs
<bos> я снимаю кино <eos>

## Slide 106

Механизм внимания - attention

Трансформер. Позиционное кодирование

Output
4

Encoder

Add & LayerNorm
Feed Forward
Add & LayerNorm

——=

Positional Encoding

=
‘fi

Embedding

ify

Input

хх, + р
i=0,1,...,N-l

Positional
Encoding

Embedding

©
:

© ©

о йе м
|
\ | |
xX, Xs №
<bos> A снимаю кино <eos>

## Slide 107

Механизм внимания - attention

Трансформер. Позиционное кодирование

Output
4

Encoder

Add & LayerNorm
Feed Forward
Add & LayerNorm

——=

Positional Encoding

=
‘fi

Embedding

ify

Input

x = (0.1, 0.2, 0.3]

p= 100

хх, + р
i=0,1,...,N-l

Positional
Encoding

Embedding

x = [100.1, 100.2, 100.3]

© © ©
J №] №

©
:

0
|
\ | | |
1, х, Xq №
<bos> я — снимаю кино <eos>

## Slide 108

Механизм внимания - attention

Трансформер. Позиционное кодирование

Output
4

Encoder

Add & LayerNorm
Feed Forward
Add & LayerNorm

——=

Positional Encoding

=
‘fi

Embedding

ify

Input

№=5: |0 | 02

5 | 0.5

0.75 | 1.0

04

06 |08

1.0

ХХ, + р!
i=0,1,...,N-1

Positional
Encoding

Embedding

©
:

@
:

о йе м
|
\ | |
xX, Xs №
<bos> A снимаю кино <eos>

## Slide 109

Механизм внимания - attention

Трансформер. Позиционное кодирование

Output
4

Encoder

Add & LayerNorm
Feed Forward
Add & LayerNorm

——=

Positional Encoding

=
‘fi

Embedding

ify

Input

N=4096 : [0.0, 0.000244, 0.000488, 0.00073, ...]

хх, + р
i=0,1,...,N-l

Positional
Encoding

Embedding

©
:

@
:

о йе м
|
\ | |
xX, Xs №
<bos> A снимаю кино <eos>

## Slide 110

Механизм внимания - attention

Трансформер. Позиционное кодирование
= [1, 0, 0,...,0,..., OJ”

ouput р, = [0,1,0,...,0,..., 0"

Add & TayerNorm

Feed Forward р, = [0, 0, 0, .. .„ OJ"

Encoder

Add & LayerNorm

A] X=X, + D;

yr

19

Positional

Positional Encoding =) i=0,1,..

Encoding

Smee Embedding ‚ i

5

ify

Input <bos> a

снимаю

## Slide 111

Механизм внимания - attention

Трансформер. Позиционное кодирование

Attention is All You Need

Output sin(w, *0)
+ cos(w, * t)
т ° й
Add & LayerNorm Ц sin(w, * 0
Р. cos(w, * t)
5 Feed Forward ...
8 Sin(Wy., *0
a Add & LayerNorm COS(W yp. * 0)
Af? ХХ, + р!

Positional 0

Encoding \

Embedding

Embedding х,

Positional Encoding =) i=0,1,...,N-1 < ©
Е :
№

©

ify

Input <bos>

|
| |
5 Xs
я снимаю кино <eos>

## Slide 112

Механизм внимания - attention

Трансформер. Позиционное кодирование

sin(w, * 0) ООО ОО A
sin(w, *0) О ee
ee
cos(w, * t) eee
sin(w, * 0) sin(w, * 0 —_| о —
| И
_ cos(w, * t) cos(w, * t) ae
PE sin(w, * t) po —_
cos(w, * t) sin(w, * 0) = |
a cos(w, * t) УОЪХ—
sin(Wao.. * t) eo
COS(Wiyp., * И). 7 | с пи
И И
cos(Wyp., * И) _
>
Po = [0,1,0,1,0,1,0,1] Ро Р> Pi Position ,t

р> = [0.90, -0.42, 0.19 , 0.98, 0.20, 0.002, 0.99]*

## Slide 113

Механизм внимания - attention

Трансформер. Позиционное кодирование

sin(w, * t)
cos(w, *t) ® уникальный вектор для каждой позиции
sin(w, *0
cos(w, * t) . возможность вычисления относительных расстояний
= . между векторами
Pr sin(w, * t) У р.
cos(w, * t) 7
2 ® простота генерации векторов позиций для
ри последовательной произвольной длины N
$т(м ара *0

Cos(Waz.1 * 0 e
2 все векторы детерминированы и могут быть вычислены

заранее

## Slide 114

Механизм внимания - attention

Трансформер. Позиционное кодирование

sin(w, * t)
cos(w, *t) ® уникальный вектор для каждой позиции
sin(w, *0
cos(w, * t) . возможность вычисления относительных расстояний
= . между векторами
Pr sin(w, * t) У р.
cos(w, * t) 7
2 ® простота генерации векторов позиций для
ри последовательной произвольной длины N
$т(м ара *0

Cos(Waz.1 * 0 e
2 все векторы детерминированы и могут быть вычислены

заранее

@ BERT и первые версии ChatGPT использовали обучаемые
векторы позиции

® PaLM, LLaMA последние версии ChatGPT, применяется
для относительнольного позиционирования - rotary
Position Embedding (РоРЕ)

## Slide 115

Трансформер. Декодер.»

SoftMax

Linear

Decoder

ry

Add & LayerNorm

Feed Forward

Add & LayerNorm

р

Encoder output

skip (residual)

argmax Ы

SoftMax SM
Linear LN

Encoder output |}———*}

Add & LayerNorm

connection

Positional Encoding

=®

Embedding

ка

Input

Positional
Encoding

Embedding

Decoder

Po

## Slide 116

Трансформер. Декодер.»

SoftMax р filming absolute стета.
Linear
Е Add & LayerNorm 9
®
5 Feed Forward SoftMax SM SM SM SM
|
| i i 11
‘Add & LayerNorm Linear LN LN LN LN
+ Ly + +
Encoder output 1 Епсодегошрш || Decoder
Add & LayerNorm
tof t 4
Positional
р. р.
Encoding ° im be
skip (residual) (+) (+) (+) (+)
connection
Positional Encoding = Embedding Xp х, 5 Xs
Co

Embedding

ка

Input

## Slide 117

Трансформер. Декодер.»

SoftMax

Linear

Decoder

ry

Add & LayerNorm

Feed Forward

Add & LayerNorm

р

Encoder output

skip (residual)

Add & LayerNorm

connection

Positional Encoding

=®

Embedding

ка

Input

Multi-head
Attention

Embedding

Xs

Xs

<bos>

A

снимаю

кино

<eos>

## Slide 118

'Механизм внимания - attention

Вычисление ОКУ Self-Attention

d_attn

N
&
Xo!

SoftMax(w/Vd)

х

Ф
я
г
2
Е
Ф

query
key
value

v= W, *X,

a=W, *х

Embedding

‘SoftMax
5 5 5 5
a 9 a a qs
+ ry Е
Linear, Wq
он
х, х, x, x Xs
<bos> я снимаю кино <eos>

## Slide 119

Трансформер. Декодер.»

SoftMax

Linear

Decoder

ry

Add & LayerNorm

Feed Forward

Add & LayerNorm

р

Encoder output

skip (residual)

Add & LayerNorm

connection

Positional Encoding

=®

Embedding

ка

Input

Multi-head
Attention

Embedding

Xs

Xs

<bos>

A

снимаю

кино

<eos>

## Slide 120

Masked Multi-head Attention

output

SoftMax

Linear

ry

Add & LayerNorm

Decoder

Feed Forward

Add & LayerNorm

Encoder output 1

Add & LayerNorm

skip (residual)

connection
Positional Encoding =
Co

Embedding
ка

Input

LayerNorm
т ry * 7 у
x, % х, х х,
X,+2, XZ, ха р х,+25
т * * ry *
% 2, % 2 25
x Х № № Xs
<bos> я снимаю кино <eos>

## Slide 121

Masked Multi-head Attention

output

SoftMax

Linear

ry

Add & LayerNorm

Decoder

Feed Forward

Add & LayerNorm

Encoder output 1

Add & LayerNorm

skip (residual)

connection
Positional Encoding =
Co

Embedding
ка

Input

LayerNorm
т ry * 7 у
x, % х, х х,
X,+2, XZ, ха р х,+25
т * * ry *
% 2, % 2 25
x Х № № Xs
<bos> я снимаю кино <eos>

## Slide 122

трансформеры

Архитектуры post-norm и pre-norm

post-norm pre-norm

LayerNorm Add

Add

LayerNorm

cai

skip (residual) ny

connection

Embedding Embedding

## Slide 123

Masked Multi-head Attention

output

SoftMax

Linear

ry

Add & LayerNorm

Decoder

Feed Forward

Add & LayerNorm

Encoder output 1

Add & LayerNorm

skip (residual)

connection
Positional Encoding =
Co

Embedding
ка

Input

LayerNorm
т ry * 7 у
x, % х, х х,
X,+2, XZ, ха р х,+25
т * * ry *
% 2, % 2 25
x Х № № Xs
<bos> я снимаю кино <eos>

## Slide 124

Masked Multi-head Attention

output

SoftMax

Linear

ry

Add & LayerNorm

Decoder

Feed Forward

Add & LayerNorm

Encoder output 1

Add & LayerNorm

skip (residual)

connection
Positional Encoding =
Co

Embedding
ка

Input

9: 92 9: Ч 95

T ¥ т ¥ ¥

Linear, Wq
1 ¥ + ¥ +
Add & LayerNorm

+ + 1 + р
В 2. 2: 2, 25
р % % № 5

<bos> я снимаю кино <eos>

## Slide 125

Masked Multi-head Attention

output
SoftMax
Linear
c=) a, *У,
Е Add & LayerNorm и
3 я
5 Feed Forward Ith
| Linear, Wv
teen >S © < G&S
Add & LayerNorm 1 1
=
| |
Ky he | Be |e |] к
Encoder output 1 + | i > + Ч Ч Ч: Ч:
Add & LayerNorm i | -
Linear, Wk Linear, Wq
ry 1 1 1 ry f + + + +
Encode, Outpujt Add & LayerNorm
. * + + р
skip (residual) il
connection 2 р 2 р 2
Я 2 я 5
Positional Encoding = Zs —
Co —
Embedding Bi th eS Xe 5%
con <bos> Яя снимаю кино — <е05>

Input

## Slide 126

Трансформер. Декодер

output

SoftMax

Linear

Decoder

ry

Add & LayerNorm

Feed Forward

Add & LayerNorm

р

Encoder output

skip (residual)

Feed Forward

i

Add & LayerNorm

Add & LayerNorm

Encoder output

+

*

connection

Positional Encoding

=®

Embedding

ка

Input

Multi-head Attention

+

+

Add & LayerNorm

+

+

2, 2 2, 24 25
2 % Sy a A
<bos> я снимаю кино <eos>
