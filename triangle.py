
def area(a, h):
    '''Принимает основание a и высоту h треугольника, возвращает площадь треугольника'''
    if not all(isinstance(x, (int, float)) for x in [a, h]):
        raise TypeError("Sides must be numbers")
    if any(x < 0 for x in [a, h]):
        raise ValueError("Sides cannot be negative")
    return a * h / 2

def perimeter(a, b, c):
    '''Принимает длины сторон a, b и c треугольника, возвращает периметр треугольника'''
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("Sides must be numbers")
    if any(x < 0 for x in [a, b, c]):
        raise ValueError("Sides cannot be negative")
    if any(x == 0 for x in [a, b, c]):
        raise ValueError("Triangle cannot have zero sides")
    # Проверка неравенства треугольника
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        raise ValueError("Invalid triangle sides")

def area(a, b, c):
    return (a + b + c) / 2


def perimeter(a, b, c):
    return a + b + c
