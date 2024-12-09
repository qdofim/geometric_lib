def area(a):
    '''Принимает длину стороны квадрата a, возвращает площадь квадрата'''
    if not isinstance(a, (int, float)):
        raise TypeError("Side length must be a number")
    if a < 0:
        raise ValueError("Side length cannot be negative")
    return a * a

def perimeter(a):
    '''Принимает длину стороны квадрата a, возвращает периметр квадрата'''
    if not isinstance(a, (int, float)):
        raise TypeError("Side length must be a number")
    if a < 0:
        raise ValueError("Side length cannot be negative")
    return 4 * a
