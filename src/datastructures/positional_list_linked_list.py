from typing import Any
from ..datastructures.node import Node


class LinkedList(Node):
    def __init__(self, current=None, next=None) -> None:
        super.__init__(current, next)


def current(linked_list: LinkedList):
    linked_list.current


def next(linked_list: LinkedList):
    linked_list.next


def cons(item: Any, linked_list: LinkedList):
    return LinkedList(item, linked_list)


def empty(linked_list: LinkedList):
    return linked_list.next is None

def
