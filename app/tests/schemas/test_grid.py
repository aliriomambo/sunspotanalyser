"""
Test Suite for the Grid Schema
"""
import pytest
from app.schemas.grid import Grid

sample_grid_values = "4, 2, 3, 2, 2, 1, 3, 2, 1"
sample_grid_size = 3


def test_grid():
    """
    Test normal Grid creation
    """
    grid = Grid(size=sample_grid_size, values=sample_grid_values)
    assert grid.size == 3
    assert grid.values == sample_grid_values


def test_grid_invalid_character():
    """
    Test grid creation with an non-numeric character
    """
    with pytest.raises(Exception):
        Grid(size=sample_grid_size, values="X 2, 3, 2, 2, 1, 3, 2, 1")


def test_grid_invalid_number_range():
    """
    Test grid creation with a number outside of the range [0,5]
    """
    with pytest.raises(Exception):
        Grid(size=sample_grid_size, values="14, 2, 3, 2, 2, 1, 3, 2, 1")


def test_grid_size_mismatch():
    """
    Test a grid creation with a mismatch between the size and the values
    """
    with pytest.raises(Exception):
        Grid(size=sample_grid_size, values="2, 3, 2, 2, 1, 3, 2, 1")
