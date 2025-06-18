from typing import Any, Self


class Array:
    def __init__(self, size: int, init_value: Any = 0):
        self.__storage = [init_value for _ in range(size)]

    @property
    def storage(self: Self) -> list[Any]:
        return self.__storage

    @property
    def size(self) -> int:
        return len(self.__storage)


def validate_index(func):
    """Validates the index used in the functions operating on arrays"""

    def wrapper(*args, **kwargs):
        arr = args[0]
        idx = args[1]
        if idx < 0:
            raise IndexError(f"Index {idx} cannot be negative")
        size = arr.size
        if idx >= size:
            raise IndexError(
                f"Index {idx} is out of range for an Array of length {size}"
            )

        return func(*args, **kwargs)

    return wrapper


def array_length(array: Array):
    """Returns the length of an array"""
    return len(array.storage)


@validate_index
def array_ref(array: Array, index: int):
    """Returns the stored value of an array at the given index"""
    return array.storage[index]


@validate_index
def array_set(array: Array, index: int, new_value: Any):
    """Sets the value of an array at a given index"""
    array.storage[index] = new_value
    return array
