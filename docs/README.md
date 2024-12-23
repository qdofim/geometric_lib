
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Общее описание решения
Этот проект содержит функции для вычисления площадей и периметров различных геометрических фигур(квадрат, треугольник , окружность). Функции разработаны с использованием Python.

## Описание функций

### circle

#### `area(r)`
Принимает радиус круга `r`, возвращает площадь круга.

**Пример вызова:**
```python```
area(3)  # Возвращает примерно 28.27

#### `perimeter(r)`
Принимает радиус окружности `r`, возвращает длину окружности.

**Пример вызова:**
```python```
perimeter(3)  # Возвращает примерно 18.85

### rectangle

#### `area(a, b)`
Принимает два числа `a` и `b`, возвращает их произведение.

**Пример вызова:**
```python```
area(4, 5)  # Возвращает 20

#### `perimeter(a, b, c, d)`
Принимает четыре числа `a`, `b`, `c` и `d`, возвращает их сумму.

**Пример вызова:**
```python```
perimeter(1, 2, 3, 4)  # Возвращает 10

### square

#### `area(a)`
Принимает длину стороны квадрата `a`, возвращает площадь квадрата.

**Пример вызова:**
```python```
area(5)  # Возвращает 25

#### `perimeter(a)`
Принимает длину стороны квадрата `a`, возвращает периметр квадрата.

**Пример вызова:**
```python```
perimeter(5)  # Возвращает 20

### triangle

#### `area(a, h)`
Принимает основание `a` и высоту `h` треугольника, возвращает площадь треугольника.

**Пример вызова:**
```python```
area(5, 10)  # Возвращает 25

#### `perimeter(a, b, c)`
Принимает длины сторон `a`, `b` и `c` треугольника, возвращает периметр треугольника.

**Пример вызова:**
```python```
perimeter(3, 4, 5)  # Возвращает 12

## История изменений
- `b917493` - error fixed
- `8c3c369` - + new file
- `d078c8d` - L-03: Docs added
- `8ba9aeb` - L-03: Circle and square added















- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`


