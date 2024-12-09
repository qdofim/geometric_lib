from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

def calc(shape_type: str, operation: str, *args) -> float:
    """Вычисляет площадь или периметр геометрической фигуры."""
    if operation not in ['area', 'perimeter']:
        raise ValueError("Operation must be 'area' or 'perimeter'")

    if shape_type not in ['circle', 'rectangle', 'square', 'triangle']:
        raise ValueError("Unknown shape type")

    operations = {
        'circle': {'area': circle_area, 'perimeter': circle_perimeter},
        'rectangle': {'area': rectangle_area, 'perimeter': rectangle_perimeter},
        'square': {'area': square_area, 'perimeter': square_perimeter},
        'triangle': {'area': triangle_area, 'perimeter': triangle_perimeter}
    }

    expected_args = {
        'circle': 1,
        'rectangle': 2,
        'square': 1,
        'triangle': {'area': 2, 'perimeter': 3}
    }

    required_args = expected_args[shape_type][operation] if shape_type == 'triangle' else expected_args[shape_type]

    if len(args) != required_args:
        raise ValueError(f"Invalid number of arguments for {shape_type} {operation}")

    return operations[shape_type][operation](*args)
