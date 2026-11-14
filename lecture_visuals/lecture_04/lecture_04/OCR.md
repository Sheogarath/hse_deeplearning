# Visual review: lecture_04/lecture_04.pptx

OCR of fully rendered slides; also includes image-only labels. OCR may contain mistakes.

## Slide 1

КУРС «НЕЙРОННЫЕ СЕТИ»

Тема 4. Сверточные
нейронные сети

## Slide 2

Сверточные нейронные сети - CNN

Зрительная кора

Ассоциативные
области

Вторичная
зрительная кора

Первичная
зрительная кора

Тема 1- Нейронные сети

6/19

## Slide 3

Сверточные нейронные сети - CNN

Ядра свертки

21 22 23 24 25 26 27

31 32 33 34 35 36 37

41 4243 4445 46 47

51 52 53 54 55 56 57

61 62 63 64 65 66 67

71 172 13. 14 | 75 6 п

fea 1. Нейронные сети 6/19

## Slide 4

Сверточные нейронные сети - CNN

Ядра свертки

x
1415 16 17
24 25 26 27
34 35 36 37
41 42 43 44 45 46 47
51 52 53 54 55 56 57
61 62 63 64 65 66 67
71 172 13. 14 | 75 6 п

fea 1. Нейронные сети

Zy-Wyy + Хи Мрт Хр +... F Was + Хз + Wo

U,,=9(Z,,)

6/19

## Slide 5

Сверточные нейронные сети - CNN

Ядра свертки

x

1 15 16 17
21 25 26 27
31 35 36 37
41 42 43 44 45 46 47
51 52 53 54 55 56 57
61 62 63 64 65 66 67
71 172 13. 14 | 75 6 п

ема1

Нейронные сети

ТЕМ + Хо + Wy + X13 +... + Wag Ха + М

U,=9(Z,))

6/19

## Slide 6

Сверточные нейронные сети - CNN

Ядра свертки

x
м 12 16 17 237 + Хз + Ма Хз... + Wag Хз + Wo
21 22 26 | 27 _
U,3=0(Z,3)
31 32 36 | 37
41 42 43 44 45 46 47
51 52 53 54 55 56 57 У
61 62 63 64 65 66 67
71 172 13. 14 | 75 6 п

fea 1. Нейронные сети 6/19

## Slide 7

Сверточные нейронные сети - CNN

Ядра свертки

12

22

32

43

52

i

21

13

23

33

53

12

22

14

24

34

45

54

13 14

23 24

15

25

35

45

55

15

25

35

45

55

## Slide 8

Сверточные нейронные сети - CNN

Ядра свертки

width =7

пана о

64

74

fea 1. Нейронные сети

По умолчанию ядра сжимают
размерность исходного изображения

11 | 12| 13 | 14 | 15
21 | 22 | 23 | 24 | 25
31 | 32 | 33 | 34 | 35
41 | 43 | 44 | 45 45
51 | 52 | 53 | 54 | 55

## Slide 9

Сверточные нейронные сети - CNN

Ядра свертки

fea 1. Нейронные сети

Padding - способ сохранить

исходную размерность

11 | 12 | 13 | 14 | 15 | 16 | 17
21 | 22 | 23 | 24 | 25 | 26 | 27
31 | 32 | 33 | 34 | 35 | 36 | 37
41 42 43 44 45 46 47
51 52 53 54 55 56 | 57
61 62 63 64 65 66 67
71 | 72 | 73 | 74 | 75 | 76 | 77

19

## Slide 10

Сверточные нейронные сети - CNN

MaxPooling, MinPooling, AveragePooling

MaxPooling - отбор наибольших значений
MinPooling - отбор наименьших значений

AveragePooling - отбор средних значений

ема 1. Нейронные сети

6/19

## Slide 11

Сверточные нейронные сети - CNN

MaxPooling, MinPooling, AveragePooling

MaxPooling - отбор наибольших значений
MinPooling - отбор наименьших значений

AveragePooling - отбор средних значений

## Slide 12

Сверточные нейронные сети - CNN

MaxPooling, MinPooling, AveragePooling

fea 1. Нейронные сети

6/

19

## Slide 13

Сверточные нейронные сети - CNN

Общая
архитектура
MaxPooling
MaxPooling
10
(10, 32, 32) (10, 32, 32) (10, 16, 16) (20, 16, 16) (20, 8,8) 1280

fea 1. Нейронные сети

## Slide 14

Сверточные нейронные сети - CNN

Класс пп.Сопу2а

Тема 1- Нейронные сети

пп.Соп\14 - для одномерной свертки
nn.Conv2d - для двумерной свертки (изображение)

nn.Conv3d - для трехмерной свертки (снимок МРТ)

пп.МахРоо!14 - для одномерного канала
nn.MaxPool2d - для двумерного канала

nn.MaxPool3d - для трехмерного канала

6/19

## Slide 15

Сверточные нейронные сети - CNN

Класс пп.Сопу2а

Тема 1- Нейронные сети

(batch, channels, H, W)

Conv2d

(batch, out_channels, Hm, Wm)

> Conv2d | (in_channels, out_channels,

6/19

## Slide 16

Сверточные нейронные сети - CNN

Класс пп.Сопу2а

(batch, channels, H, W) > Conv2d | (in_channels, out_channels, kernel_size

1 | 12 | 13 21 | 12 | 13

21 | 22 | 23 21 | 22 | 23

31 | 32 | 33

kernel_size kernel_size = (2, 3)

kernel_size = (3, 3)

eS

М

Тема 1- Нейронные сети 6/19

## Slide 17

Сверточные нейронные сети - CNN

Класс пп.Сопу2а

(batch, channels, H, W) > Conv2d | (in_channels, out_channels, kernel_size,
stride=1, padding=0)

1 | 12 | 13 21 | 12 | 13

21 | 22 | 23 21 | 22 | 23

31 | 32 | 33

kernel_size kernel_size = (2, 3)

kernel_size = (3, 3)

padding='valid’ - то же самое что и padding=0
padding='same’

eS

М

Тема 1- Нейронные сети 6/19

## Slide 18

Сверточные нейронные сети - CNN

Класс пп.Сопу2а

(batch, channels, Н, W) > MaxPool2d (kernel_size, stride=None, ...)

|

torch.nn.MaxPool2d(kernel_size,
stride=None, padding=0, dilation=1,
return_indices=False, ceil_mode=False)

fea 1. Нейронные сети 6/19

## Slide 19

Сверточные нейронные сети - CNN

Класс пп.Сопу2а

(batch, channels, H,W) | [>> Махрооеа | (kemnel_size, sride=None, ..)

xo)
N
88 | 54 | 65
a 7 8
=> o => 72 | 38 | 22
pete te Е
3 15 | 10 | 55
4 8
о 78

(batch, channels, Н // 2, М/// 2)

Тема 1. Нейронные сети 6/19

## Slide 20

Сверточные нейронные сети - CNN

Общая
архитектура
MaxPooling
MaxPooling
10
(10, 32, 32) (10, 32, 32) (10, 16, 16) (20, 16, 16) (20, 8,8) 1280

fea 1. Нейронные сети

## Slide 21

Сверточные нейронные сети - CNN

Проблема затухающих градиентов

Проблема затухающих
(исчезающих) градиентов
(vanishing gradients)

error (%)

Splain-18 18-layer
—plain-34
a 0 10 20 30 40 50

iter. (1e4)

fea 1. Нейронные сети

## Slide 22

Сверточные нейронные сети - CNN

Архитектура ResNet

F(x)
A

> ReLU

Conv, _1, 3x3
Conv, _2, 3x3

fea 1. Нейронные сети

## Slide 23

Сверточные нейронные сети - CNN

Архитектура ResNet

H(x) = F(x) +x
F(x)

г ^ y = F(x, М)

но) F(x) = Н® -х

Batch i»
Norm, rot 5 веш }—> ан) =1+ F(x)

Ox Ox

Batch

ReLU

>»)
Cony, _1, 3x3
Cony, _2, 3x3

## Slide 24

Сверточные нейронные сети - CNN

Базовый блок

H(x) = F(x) +x
F(x)

г ^ y = F(x, М)

но) F(x) = Н® -х

Batch i»
Norm, rot 5 веш }—> ан) =1+ F(x)

Ox Ox

Batch

ReLU

Cony, _2, 3x3

х
NX
Cony, _1, 3x3

остаточные сети (residual networks) - ResNet (152 слоя)

fea 1. Нейронные сети

## Slide 25

Сверточные нейронные сети - CNN

Базовый блок v2

F(x)

Conv, _1, 3x3

Conv, _2, 3x3

fea 1. Нейронные сети

## Slide 26

Сверточные нейронные сети - CNN

Bottleneck Block

F(x)

Conv, _1, 3x3

Conv, _2, 3x3

Batch
Norm

ReLU

Cony, _2, 3x3

Batch
Norm

fea 1. Нейронные сети

ReLU

## Slide 27

Сверточные нейронные сети - CNN

Bottleneck Block

F(x)

Conv, _1, 3x3

Conv, _2, 3x3

Batch
Norm

ReLU

Conv, _2, 3x3

Batch
Norm

1-й слой: 1 * 1 * 128 * 64 = 8192
2-й слой: 1 * 1 * 64 * 64 = 36864
3-й слой: 1 * 1 * 64* 128 = 8192

fea 1. Нейронные сети

итого: 8192+36864+8192 = 53248

3*3* 128 * 128 = 147456

ReLU

## Slide 28

‘Сверточные нейронные сети - CNN

Общая архитектура сетей ResNet

Conv2d: 3, 64, 7x7, s=2, р:
b=False

BatchNorm: 64

MaxPool2d: 3x3, s=2, p=1

AdaptiveAvgPool2d

Linear: 512*factor, out=1000, b=True

Тема 1- Нейронные сети

resnet18 resnet34 гезпе{50 resnet101
2 3 3 3
2 4 4 4
2 6 6 23
2 3 3 3

6/19

## Slide 29

Архитектура сети ResNet-18

Conv2d: 3, 64, 7x7, s=2, p=3,
b=False

BatchNorm: 64
MaxPool2d: 3x3, s=2, p=1
Layer1: 64, H, W
Layer2: 128, Н/2, WI2
Layer3: 128, НА, WI4
Layer4: 512, Н/З, WI8
AdaptiveAvgPool2d

Linear: 512*factor, out=1000, b=True

—

L1_

(64, H, М)

Conv2d: 64, 3x3, s=1, p=1, b=False
BatchNorm: 64
ReLU
Conv2d: 64, 3x3, s=1, p=1, b=False

BatchNorm: 64

ReLU

(64, H, W)

## Slide 30

Сверточные нейронные сети - CNN

Архитектура сети ResNet-18

ема 1

Conv2d: 3, 64, 7x7, s=2, p=3,
b=False

BatchNorm: 64

MaxPool2d: 3x3, s=2, p=1

AdaptiveAvgPool2d

Linear: 512*factor, out=1000, b=True

12.1

(128, Н/2, WI2)

Conv2d: 128, 3x3, s=2, p=1, b=False

BatchNorm: 128

Conv2d: 128, 1x1,
3=2, p=0, b=False

ReLU

BatchNorm: 128

Conv2d: 128, 3x3, s=1, p=1, b=False

BatchNorm: 128

— ©

ReLU

(128, H/2, WI2)

## Slide 31

Сверточные нейронные сети - CNN

Архитектура сети ResNet-18

ема 1

Conv2d: 3, 64, 7x7, s=2, p=3,
b=False

BatchNorm: 64

MaxPool2d: 3x3, s=2, p=1

AdaptiveAvgPool2d

Linear: 512*factor, out=1000, b=True

(128, Н/2, WI2)

Conv2d: 256, 3x3, s=2, p=1, b=False

Conv2d: 256, 1x1,
3=2, p=0, b=False

BatchNorm: 256

ReLU

BatchNorm: 256

Conv2d: 256, 3x3, s=1, p=1, b=False

BatchNorm: 256

| <

ReLU

(256, Н/Д, Wi4)

## Slide 32

Сверточные нейронные сети - CNN

Архитектура сети ResNet-18

Conv2d: 3, 64, 7x7, s=2, p=3,
b=False L4.1 > (256, Н/4, w/4)

BatchNorm: 64 Conv2d: 512, 3x3, s=2, p=1, b=False

MaxPool2d: 3x3, s=2, p=1

BatchNorm: 512

ReLU

Conv2d: 512, 3x3, s=1, p=1, b=False

BatchNorm: 512

| <

AdaptiveAvgPool2d ReLU

(512, H/8, WI8)

Linear: 512*factor, out=1000, b=True

fea 1. Нейронные сети

## Slide 33

‘Сверточные нейронные сети - CNN

Архитектура сети ResNet-18

Conv2d: 3, 64, 7x7, s=2, p=3,
b=False

BatchNorm: 64

512

MaxPool2d: 3x3, s=2, p=1

HI8

wis

AdaptiveAvgPool2d =>

Linear: 512*factor, out=1000, b=True

Тема 1- Нейронные сети 6/19

## Slide 34

‘Сверточные нейронные сети - CNN

Архитектура сети ResNet-18

Conv2d: 3, 64, 7x7, s=2, p=3,
b=False

BatchNorm: 64

512

MaxPool2d: 3x3, s=2, p=1

AdaptiveAvgPool2d

Linear: 512*factor, out=1000, b=True

Тема 1- Нейронные сети

wis

м

м

(512, 1, 1)

6/19

## Slide 35

‘Сверточные нейронные сети - CNN

Общая архитектура сетей ResNet

Conv2d: 3, 64, 7x7, s=2, р:
b=False

BatchNorm: 64

MaxPool2d: 3x3, s=2, p=1

AdaptiveAvgPool2d

Linear: 512*factor, out=1000, b=True

Тема 1- Нейронные сети

resnet18 resnet34 гезпе{50 resnet101
2 3 3 3
2 4 4 4
2 6 6 23
2 3 3 3

6/19

## Slide 36

Сверточные нейронные сети - CNN

Архитектура сети ResNet-50

11 (64*4, Н, W)
Conv2d: 3, 64, 7x7, s=2, p=3, Conv2d: 64, 1x1, s=1, p=0, b=False
b=False
BatchNorm: 64

BatchNorm: 64

ReLU

Conv2d: 64*4, 1x1,

MaxPool2d: 3x3, s=2, p=1 s=1, p=0, b=False

Conv2d: 64, 3x3, s=1, p=1, b=False

BatchNorm: 64*4 BatchNorm: 64

ReLU

Conv2d: 64, 1x1, s=1, p=0, b=False

BatchNorm: 64

о

AdaptiveAvgPool2d

ReLU

+ r=4
Linear: 512*factor, out=1000, b=True вс (64*4, Н, W)
4H,

## Slide 37

Сверточные нейронные сети - CNN

Архитектура сети ResNet-50

121 (64*4, H, W)

Conv2d: 3, 64, 7x7, s=2, p=3,

Conv2d: 128, 1x1, s=1, p=0, b=False
b=False

BatchNorm: 128
BatchNorm: 64

ReLU
Conv2d: 128*4, 1x1,
MaxPool2d: 3x3, s=2, p=1 s=2, p=0, b=False Conv2d: 128, 3x3, s=2, p=1, b=False
BatchNorm: 128*4 BatchNorm: 128
ReLU

Conv2d: 128*4, 1x1, s=1, p=0, b=False

BatchNorm: 128*4

AdaptiveAvgPool2d

ReLU

factor=4

Linear: 512*factor, out=1000, b=True

(128*4, Н/2, WI2)

## Slide 38

Сверточные нейронные сети - CNN

Архитектура сети ResNet-50

131 (128*4, Н/2, WI2)

Conv2d: 3, 64, 7x7, s=2, p=3, Conv2d: 256, 1x1, s=1, p=0, b=False
b=False

BatchNorm: 256
BatchNorm: 64

ReLU
Conv2d: 256*4, 1x1,
MaxPool2d: 3x3, s=2, p=1 3=2, p=0, b=False Conv2d: 256, 3x3, s=2, p=1, b=False
BatchNorm: 256*4 BatchNorm: 256
ReLU

Conv2d: 256*4, 1x1, s=1, p=0, b=False

BatchNorm: 256*4

AdaptiveAvgPool2d

ReLU

factor=4

Linear: 512*factor, out=1000, b=True

(256*4, НИ, Wi4)

## Slide 39

Сверточные нейронные сети - CNN

Архитектура сети ResNet-50

13а (256*4, H/4, W/4)

Conv2d: 3, 64, 7x7, s=2, p=3,

Conv2d: 512, 1x1, s=1, p=0, b=False
b=False

BatchNorm: 512
BatchNorm: 64

ReLU
Conv2d: 512*4, 1x1,
MaxPool2d: 3x3, s=2, p=1 3=2, p=0, b=False Conv2d: 512, 3x3, s=2, p=1, b=False
BatchNorm: 512*4 BatchNorm: 512
ReLU

Conv2d: 512*4, 1x1, s=1, p=0, b=False

BatchNorm: 512*4

AdaptiveAvgPool2d

ReLU

factor=4

Linear: 512*factor, out=1000, b=True

(256*4, НИ, Wi4)

## Slide 40

‘Сверточные нейронные сети - CNN

Архитектура сети ResNet-18

Conv2d: 3, 64, 7x7, s=2, p=3,
b=False

BatchNorm: 64

512

MaxPool2d: 3x3, s=2, p=1

AdaptiveAvgPool2d

Linear: 512*factor, out=1000, b=True

Тема 1- Нейронные сети

wis

м

м

(512, 1, 1)

6/19

## Slide 41

Сверточные нейронные сети - CNN

Развертка сетей ResNet в ширину

Гут тете
