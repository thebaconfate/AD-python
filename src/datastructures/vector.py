from typing import Any


class Vector:
    def __init__(self, size, value=0) -> None:
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.__storage = [value for _ in range(size)]

    @property
    def storage(self):
        return self.__storage


def vector_ref(idx: int, vector: Vector):
    vector.storage[idx]


def vector_insert(index: int, new_value: Any, vector: Vector):
    if index < 0:
        raise IndexError("Index must be a non-negative number")
    vector.storage[index] = new_value


def vector_length(vector: Vector):
    len(vector.storage)


def vector(size: int, value=0):
    return Vector(size, value)
