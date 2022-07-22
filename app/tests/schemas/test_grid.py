import pytest
from app.schemas.grid import Grid
from uuid import UUID


def test_grid():
    grid = Grid(size=3, values="4, 2, 3, 2, 2, 1, 3, 2, 1")
    assert grid.size == 3
    assert grid.values == "4, 2, 3, 2, 2, 1, 3, 2, 1"


# def test_grid_create_with_valid_uuid():
#     grid_create = GridCreate(size=3, values="4, 2, 3, 2, 2, 1, 3, 2, 1")
#     uuid_obj = UUID(grid_create.id, version=4)
#     is_valid_uuid = (grid_create.id == str(uuid_obj))
#     assert grid_create.size == 3
#     assert grid_create.values == "4, 2, 3, 2, 2, 1, 3, 2, 1"
#     assert is_valid_uuid


def test_grid_invalid_character():
    with pytest.raises(Exception):
        Grid(size=3, values="X 2, 3, 2, 2, 1, 3, 2, 1")


def test_grid_invalid_number_range():
    with pytest.raises(Exception):
        Grid(size=3, values="14, 2, 3, 2, 2, 1, 3, 2, 1")


def test_grid_size_mismatch():
    with pytest.raises(Exception):
        Grid(size=3, values="2, 3, 2, 2, 1, 3, 2, 1")
