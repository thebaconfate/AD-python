from typing import Any, Callable, Generic, Literal, Self, TypeVar, Union


T = TypeVar("T")
GenericList = list[T]
"""Requires union with int for the initialization"""
GenericEq = Callable[[T, T], bool]


class PositionalList(Generic[T]):
    """Class for Generic Positional List"""

    __eq: GenericEq
    __size: int
    __storage: GenericList

    def __init__(self, eq: GenericEq):
        """
        Requires an equality function to compare elements in the storage. The
        storage is automatically initiated with size 10 and a list of 0's
        """
        self.__eq = eq
        self.__size = 0
        self.__storage = []

    @property
    def eq(self) -> GenericEq:
        """
        Returns the equality function of the Positional List
        """
        return self.__eq

    @property
    def size(self) -> int:
        """
        Returns the size of the Positional List
        """
        return self.__size

    @size.setter
    def size(self, size: int) -> Self:
        """
        Sets the size of the Positional List and returns the Positional List
        """
        self.__size = size
        return self

    @property
    def storage(self) -> GenericList:
        """
        Returns the storage of the Positional List
        """
        return self.__storage

    @storage.setter
    def storage(self, storage: GenericList) -> Self:
        """
        Sets the storage of the Positional List and returns the Positional List
        """
        self.__storage = storage
        return self


def is_positional_list(arg: Any) -> bool:
    """Returns wether the argument is a Positional List or not"""
    return isinstance(arg, PositionalList)


def new(eq: GenericEq):
    return PositionalList(eq)


def attach_middle(plist: PositionalList[T], val: T, position: int) -> PositionalList[T]:
    size = plist.size
    storage = plist.storage
    storage.insert(position, val)
    plist.storage = storage
    plist.size = size + 1
    return plist


def attach_first(plist: PositionalList[T], val: T) -> PositionalList[T]:
    return attach_middle(plist, val, 0)


def attach_last(plist: PositionalList[T], val: T) -> PositionalList[T]:
    return attach_middle(plist, val, plist.size)
