from typing import Callable, Any
from functools import reduce

from src.datastructures.vector import Array, array, array_length


# TODO: Check out the API
class PositionalList:
    """Creates a positional list"""

    def __init__(self, size: int, equality: Callable[[Any, Any], bool]) -> None:
        """Expects the size of the positional list as a non-negative integer and an equality function"""
        self.__storage: Array = array(size)
        self.__size: int = size
        self.__equality: Callable[[Any, Any], bool] = equality

    @property
    def size(self) -> int:
        """Returns the size of the positional list"""
        return self.__size

    @size.setter
    def size(self, new_size):
        """Sets a new size for the positional list"""
        self.__size = new_size

    @property
    def equality(self) -> Callable[[Any, Any], bool]:
        """Returns the equality function"""
        return self.__equality

    @property
    def storage(self) -> Array:
        """returns the storage of the positional list"""
        return self.__storage

    @storage.setter
    def storage(self, new_storage: Any) -> None:
        """Sets a new storage for the positional list"""
        if isinstance(new_storage, Array):
            self.__storage = new_storage
        else:
            raise ValueError("new storage must be of type Vector")


def new(size: int, equality: Callable[[Any, Any], bool]):
    return PositionalList(size, equality=equality)


def from_list(lst: list[Any], equality: Callable[[Any, Any], bool]):
    result = new(len(lst), equality)
    for item in lst:
        add_after(result, item)
    return result


def length(plist: PositionalList) -> int:
    """Returns the length of the positional list"""
    return plist.size


def is_full(plist: PositionalList) -> bool:
    """Returns wether the positional list is full"""
    return (plist.size + 1) == array_length(plist.storage)


def is_empty(plist: PositionalList) -> bool:
    """Returns wether the positional list is empty"""
    return plist.size == 0


def map_adt():
    pass


def for_each():
    pass


def first(positional_list: PositionalList) -> int:
    """Returns the first index of the positional list"""
    if (positional_list.size) == 0:
        raise IndexError("Positional list is empty")
    else:
        return 0


def last(positional_list: PositionalList) -> int:
    """Returns the last position of the"""
    if positional_list.size == 0:
        raise IndexError("Positional list is empty")
    else:
        return positional_list.size


def has_next(plist: PositionalList, position: int) -> bool:
    """Returns wether or not the positional list has another element after a given position"""
    return (position + 1) < (plist.size)


def has_previous(_: PositionalList, position: int) -> bool:
    """returns wether or not the positional list has another element before the given position"""
    return position < 0


def next(plist: PositionalList, position: int) -> int:
    """returns the next position of the positional list given a position"""
    if not has_next(plist, position):
        raise IndexError("Positional list has no next")
    else:
        return position + 1


def previous():
    pass


def find():
    pass


def update():
    pass


def delete():
    pass


def peek():
    pass


def add_before():
    pass


def add_after(positional_list: PositionalList, value: Any, position: int | None = None):
    if position is not None and is_empty(positional_list):
        raise Exception(f"Illegal position add_after {position}")
    elif position is not None:
        pass
        # positional_list.attach_last(positional_list, value)
