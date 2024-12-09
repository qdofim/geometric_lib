import pytest
from rectangle import area, perimeter

def test_rectangle_area():
    """Test rectangle area calculation with standard case"""
    # Arrange
    width = 4
    height = 6
    
    # Act
    result = area(width, height)
    
    # Assert
    assert result == 24

def test_rectangle_area_negative():
    """Test rectangle area with negative sides"""
    # Arrange
    width = -4
    height = 6
    
    # Act & Assert
    with pytest.raises(ValueError, match="Sides cannot be negative"):
        area(width, height)

def test_rectangle_perimeter():
    """Test rectangle perimeter calculation"""
    # Arrange
    width = 4
    height = 6
    
    # Act
    result = perimeter(width, height, width, height)
    
    # Assert
    assert result == 20

def test_rectangle_invalid_type():
    """Test rectangle calculations with invalid input type"""
    # Arrange
    width = "4"
    height = 6
    
    # Act & Assert
    with pytest.raises(TypeError, match="Sides must be numbers"):
        area(width, height)
