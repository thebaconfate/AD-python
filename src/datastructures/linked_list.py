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

    def attach_first(self, value) -> Self:
        """Inserts a value at the beginning of the linked list"""
        if self.__head is None:
            self.__head = LinkedListNode(value)
        else:
            self.__head = LinkedListNode(value, self.__head)
        return self

    def attach_middle(self, value, idx) -> Self:
        """Inserts a value somewhere between the beginning or end of the linked list"""
        indexError = IndexError("Index exceeds size of linked list")
        if self.__head is None:
            if idx > 0:
                raise indexError
            else:
                self.__head = LinkedListNode(value)
        else:
            i = 0
            node = self.__head
            while node.next is not None and i < idx:
                node.next
            if i != idx:
                raise indexError
            else:
                new_node = LinkedListNode(value, node.next)
                node.next = new_node
        return self

    def attach_last(self, value) -> Self:
        """Inserts a value at the end of the linked list"""
        new_node = LinkedListNode(value)
        if self.__head is None:
            self.__head = new_node
        else:
            node = self.__head
            while node.next is not None:
                node = self.__head.next
            node.next = new_node
        return self

    def delete_first(self) -> Self:
        """Deletes the first value of the linked list"""
        if self.__head is None:
            raise ValueError(
                "Cannot remove first element of a linked list if there is none"
            )
        else:
            self.__head = self.__head.next
        return self

    def delete_middle(self, value, idx) -> Self:
        """Deletes a value in between the first and end of the linked list"""
        indexError = IndexError("Index exceeds size of linked list")
        if self.__head is None:
            raise indexError
        else:
            node = self.__head
            i = 0
            while node.next is not None and i < idx - 1:
                node = node.next
            node.next = node.next.next
        return self

    def delete_last(self) -> Self:
        """Deletes the last value in the linked list"""
        if self.__head is None:
            raise ValueError(
                "Cannot remove last element of a linked list if there is none"
            )
        else:
            node = self.__head
            while node.next is not None and node.next.next is not None:
                node = node.next
            node.next = None
        return self

    def find(self, value) -> int | Literal[False]:
        """Tries to find the position of a value in the linked list. Returns the index if found, False otherwise"""
        found = False
        if self.__head is not None:
            node = self.__head
            idx = 0
            while not found and node.next is not None:
                if node.value is value:
                    found = True
                    break
                node = node.next
                idx += 1
        return idx if found else found
