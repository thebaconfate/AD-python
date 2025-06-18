from datastructures.array import Array, array_ref, array_length, array_set
import pytest
import math


@pytest.fixture
def size():
    return 5


@pytest.fixture
def init():
    return 69


def test_array_creation_length(size):
    arry = Array(size)
    assert arry.size == size


def test_array_creation_init(size, init):
    arr = Array(size, init)
    assert all(lambda x: x == init for _ in arr.storage)


def test_array_length(size):
    arr = Array(size)
    assert array_length(arr) == size


def test_array_ref(size, init):
    arr = Array(size, init)
    assert array_ref(arr, math.ceil(size / 2)) == init


def test_array_ref_negative_idx_error(size):
    arr = Array(size)
    with pytest.raises(IndexError) as _:
        array_ref(arr, -size)


def test_array_ref_out_of_range_idx_error(size):
    arr = Array(size)
    with pytest.raises(IndexError) as _:
        array_ref(arr, size)


def test_array_set(size, init):
    arr = Array(size, init)
    idx = math.ceil(size / 2)
    new_value = "potato"
    array_set(arr, idx, new_value)
    assert array_ref(arr, idx) == new_value


def test_array_set_out_of_range_idx_error(size):
    arr = Array(size)
    new_value = "potato"
    with pytest.raises(IndexError) as _:
        array_set(arr, size, new_value)


def test_array_set_negative_idx_error(size):
    arr = Array(size)
    new_value = "potato"
    with pytest.raises(IndexError) as _:
        array_set(arr, -size, new_value)
