from typing import Any, Literal, Self


empty_list = None


class LinkedListNode:
    def __init__(self, value: Any, next: Any | None = empty_list):
        self.__value: Any = value
        self.__next: Any | None = next

    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, value) -> Self:
        self.__value = value
        return self

    @property
    def next(self) -> Any:
        return self.__next

    @next.setter
    def next(self, next) -> Self:
        self.__next = next
        return self


class LinkedList:
    def __init__(self, init: LinkedListNode | None = empty_list) -> None:
        self.__head: LinkedListNode | None = init

    def __iter__(self):
        """help function to easily iterate over the linked list"""
        self.__current = self.__head
        return self

    def __next__(self):
        """help function to easily iterate over the linked list"""
        if self.__current is None:
            raise StopIteration
        else:
            value = self.__current.value
            self.__current = self.__current.next
            return value
