def area(a, b):
    """Принимает длины сторон прямоугольника a и b, возвращает площадь прямоугольника."""
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise TypeError("Sides must be numbers")
    if any(x < 0 for x in [a, b]):
        raise ValueError("Sides cannot be negative")
    return a * b


def perimeter(a, b, c, d):
    """Принимает четыре числа a, b, c и d, возвращает их сумму."""
    if not all(isinstance(x, (int, float)) for x in [a, b, c, d]):
        raise TypeError("Sides must be numbers")
    if any(x < 0 for x in [a, b, c, d]):
        raise ValueError("Sides cannot be negative")
    if a != c or b != d:
        raise ValueError("Opposite sides must be equal")
    return a + b + c + d
