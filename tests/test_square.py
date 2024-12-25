import pytest
from square import area, perimeter


def test_square_area():
    """Test square area calculation with standard case."""
    # Arrange
    side = 4

    # Act
    result = area(side)

    # Assert
    assert result == 16


def test_square_area_negative():
    """Test square area with negative side."""
    # Arrange
    side = -4

    # Act & Assert
    with pytest.raises(ValueError, match="Side length cannot be negative"):
        area(side)


def test_square_perimeter():
    """Test square perimeter calculation."""
    # Arrange
    side = 4

    # Act
    result = perimeter(side)

    # Assert
    assert result == 16


def test_square_invalid_type():
    """Test square calculations with invalid input type."""
    # Arrange
    side = "4"

    # Act & Assert
    with pytest.raises(TypeError, match="Side length must be a number"):
        area(side)
