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

    def length(self) -> int:
        if self.__head is None:
            return 0
        else:
            list_length = 0
            node = self.__head
            while node.next is not None:
                list_length += 1
                node = node.next
            return list_length

    def insert_first(self, value) -> Self:
        """Inserts a value at the beginning of the linked list"""
        return self

    def insert_middle(self, value, idx) -> Self:
        """Inserts a value somewhere between the beginning or end of the linked list"""
        return self

    def insert_last(self, value) -> Self:
        """Inserts a value at the end of the linked list"""
        return self

    def delete_first(self) -> Self:
        """Deletes the first value of the linked list"""
        return self

    def delete_middle(self, value, idx) -> Self:
        """Deletes a value in between the first and end of the linked list"""
        return self

    def delete_last(self) -> Self:
        """Deletes the last value in the linked list"""
        return self

    def find(self, value) -> int | Literal[False]:
        found = False
        """Returns the index of the found element or false if it is not found in the linked list"""
        return found
