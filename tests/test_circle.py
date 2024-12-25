import pytest
from circle import area, perimeter


def test_circle_area():
    """Test circle area calculation with standard and edge cases."""
    # Arrange
    radius = 5

    # Act
    result = area(radius)

    # Assert
    assert result == pytest.approx(78.5398, 0.0001)


def test_circle_area_negative():
    """Test circle area with negative radius."""
    # Arrange
    radius = -5

    # Act & Assert
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area(radius)


def test_circle_perimeter():
    """Test circle perimeter calculation with standard case."""
    # Arrange
    radius = 5

    # Act
    result = perimeter(radius)

    # Assert
    assert result == pytest.approx(31.4159, 0.0001)


def test_circle_invalid_type():
    """Test circle calculations with invalid input type."""
    # Arrange
    radius = "5"

    # Act & Assert
    with pytest.raises(TypeError, match="Radius must be a number"):
        area(radius)
