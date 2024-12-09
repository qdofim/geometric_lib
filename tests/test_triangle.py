import pytest
from triangle import area, perimeter

def test_triangle_area():
    """Test triangle area calculation with standard case"""
    # Arrange
    base = 6
    height = 4
    
    # Act
    result = area(base, height)
    
    # Assert
    assert result == 12

def test_triangle_area_negative():
    """Test triangle area with negative sides"""
    # Arrange
    base = -6
    height = 4
    
    # Act & Assert
    with pytest.raises(ValueError, match="Sides cannot be negative"):
        area(base, height)

def test_triangle_perimeter():
    """Test triangle perimeter calculation with Pythagorean triple"""
    # Arrange
    a, b, c = 3, 4, 5  
    
    # Act
    result = perimeter(a, b, c)
    
    # Assert
    assert result == 12

def test_triangle_invalid():
    """Test triangle with invalid sides (violates triangle inequality)"""
    # Arrange
    a, b, c = 1, 1, 3 
    
    # Act & Assert
    with pytest.raises(ValueError, match="Invalid triangle sides"):
        perimeter(a, b, c)
