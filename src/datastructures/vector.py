from typing import Any


class Array:
    def __init__(self, size, value=0) -> None:
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.__storage = [value for _ in range(size)]

    @property
    def storage(self):
        return self.__storage


def array_ref(idx: int, vector: Array):
    vector.storage[idx]


def array_insert(index: int, new_value: Any, vector: Array):
    if index < 0:
        raise IndexError("Index must be a non-negative number")
    vector.storage[index] = new_value


def array_length(vector: Array):
    len(vector.storage)


def array(size: int, value=0):
    return Array(size, value)
