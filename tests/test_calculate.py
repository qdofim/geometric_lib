import pytest
from calculate import calc

class TestCalculate:
    def test_circle_area(self):
        result = calc('circle', 'area', 5)
        assert result == pytest.approx(78.5398, 0.0001)

    def test_square_perimeter(self):
        result = calc('square', 'perimeter', 4)
        assert result == 16

    def test_invalid_shape(self):
        with pytest.raises(ValueError, match="Unknown shape type"):
            calc('hexagon', 'area', 5)

    def test_invalid_operation(self):
        with pytest.raises(ValueError, match="Operation must be 'area' or 'perimeter'"):
            calc('circle', 'volume', 5)

    def test_invalid_args_count(self):
        with pytest.raises(ValueError, match="Invalid number of arguments"):
            calc('rectangle', 'area', 5)

    def test_triangle_different_args(self):
        area_result = calc('triangle', 'area', 6, 4)
        perimeter_result = calc('triangle', 'perimeter', 3, 4, 5)
        assert area_result == 12
        assert perimeter_result == 12

    def test_invalid_argument_type(self):
        with pytest.raises(TypeError, match="Arguments must be numbers"):
            calc('circle', 'area', "5")


    def test_negative_values(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            calc('square', 'area', -5)

    def test_zero_values(self):
        assert calc('square', 'area', 0) == 0
