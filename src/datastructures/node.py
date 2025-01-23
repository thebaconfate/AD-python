from typing import Any


class Node:
    def __init__(self, current: Any = None, next: Any = None) -> None:
        self.__current = current
        self.__next = next

    @property
    def current(self):
        return self.__current

    @property
    def next(self):
        return self.__next
