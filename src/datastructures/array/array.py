from typing import Any


class Array:
    def __init__(self, size: int, init_value: Any = 0) -> None:
        self.__storage = [init_value for _ in range(size)]

    @property
    def storage(self):
        return self.__storage


def array_length(array: Array):
    return len(array.__storage)


def array_ref(array: Array, index: int):
    array.storage[index]
    return array


def array_set(array: Array, index: int, new_value: Any):
    array.storage[index] = new_value
    return array
