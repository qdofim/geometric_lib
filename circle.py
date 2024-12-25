import math

def area(r):
    '''Принимает радиус круга r, возвращает площадь круга'''
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")  # Изменено сообщение об ошибке
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус окружности r, возвращает длину окружности'''
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * r
