from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

figs = ['circle', 'rectangle', 'square', 'triangle']
funcs = ['area', 'perimeter']
expected_args = {
    'circle': 1,
    'rectangle': 2,
    'square': 1,
    'triangle': {'area': 2, 'perimeter': 3}
}

operations = {
    'circle': {'area': circle_area, 'perimeter': circle_perimeter},
    'rectangle': {'area': rectangle_area, 'perimeter': rectangle_perimeter},
    'square': {'area': square_area, 'perimeter': square_perimeter},
    'triangle': {'area': triangle_area, 'perimeter': triangle_perimeter}
}


def calc(shape_type: str, operation: str, *args) -> float:
    """Вычисляет площадь или периметр геометрической фигуры."""
    if operation not in funcs:
        raise ValueError("Operation must be 'area' or 'perimeter'")

    if shape_type not in figs:
        raise ValueError("Unknown shape type")

    required_args = (
        expected_args[shape_type][operation]
        if isinstance(expected_args[shape_type], dict)
        else expected_args[shape_type]
    )

    if len(args) != required_args:
        raise ValueError(
            f"Invalid number of arguments for {shape_type} {operation}. "
            f"Expected {required_args}."
        )

    return operations[shape_type][operation](*args)


if __name__ == "__main__":
    fig = ''
    func = ''
    sizes = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n").strip()

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n").strip()

    required_args = (
        expected_args[fig][func] if fig == 'triangle' else expected_args[fig]
    )

    while len(sizes) != required_args:
        try:
            sizes = list(
                map(
                    float,
                    input(
                        f"Enter {required_args} size(s) for {fig} (separated by space):\n"
                    ).split()
                )
            )
            if len(sizes) != required_args:
                print("Incorrect number of sizes provided.")
        except ValueError:
            print("Please enter valid numbers.")
            sizes = []

    try:
        result = calc(fig, func, *sizes)
        print(f"The {func} of the {fig} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
