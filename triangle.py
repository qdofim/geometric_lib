def area(a, h):
    """Вычисляет площадь треугольника по основанию a и высоте h."""
    if not all(isinstance(x, (int, float)) for x in [a, h]):
        raise TypeError("Sides must be numbers")
    if any(x < 0 for x in [a, h]): 
        raise ValueError("Sides cannot be negative")  
    return 0.5 * a * h


def perimeter(a, b, c):
    """Вычисляет периметр треугольника по трём сторонам a, b и c."""
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("Sides must be numbers")
    if any(x <= 0 for x in [a, b, c]):
        raise ValueError("Sides cannot be zero or negative")
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        raise ValueError("Invalid triangle sides")
    return a + b + c
