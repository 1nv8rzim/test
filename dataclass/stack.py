from dataclasses import dataclass
from typing import Any, Union


@dataclass
class Node:
    __slots__ = 'value', 'tail'
    value: Any
    tail: Union[None, 'Node']


@dataclass
class LinkStack:
    __slots__ = 'front', 'size'
    front: Union[Node, None]
    size: int


class Stack:

    def __init__(self, *args):
        self.stack = LinkStack(None, 0)
        if len(args):
            for arg in args[::-1]:
                self.enqueue(arg)

    def enqueue(self, element):
        self.stack.front = Node(element, self.stack.front)
        self.stack.size += 1

    def dequeue(self):
        if len(self) == 0:
            raise IndexError("Cannot dequeue an empty stack")
        value = self.stack.front.value
        self.stack.front = self.stack.front.tail
        self.stack.size -= 1
        return value

    def pop(self):
        return self.dequeue()

    def front(self):
        return self.stack.front.value

    def __len__(self):
        return self.stack.size

    def __iter__(self):
        reference = self.queue.front
        values = []
        for i in range(len(self) - 1):
            values += [reference.value]
            reference = reference.tail
        return iter(values[::-1])

    def __str__(self):
        reference = self.queue.front
        values = []
        for i in range(len(self) - 1):
            values += [reference.value]
            reference = reference.tail
        return str(values[::-1])

    def __repr__(self):
        return "Stack({})".format(str(self)[1:-1] if len(self) > 0 else '')

    def __eq__(self, value):
        if isinstance(value, Stack):
            if self.size == value.size:
                for i, j in zip(self, value):
                    if i != j:
                        return False
                return True
        return False

    def __ne__(self, value):
        return not self.__eq__(value)

    def copy(self):
        clone = Stack()
        temp = []
        for i in reversed(self):
            clone.enqueue(i)
        return clone

    def __add__(self, value):
        clone = self.copy()
        if hasattr(value, '__iter__'):
            for i in reversed(value):
                clone.enqueue(i)
        else:
            clone.enqueue(value)
        return clone

    def __getitem__(self, position):
        if isinstance(position, int):
            temp_position = position
            if position < 0:
                position += len(self)
            if not (0 <= position < len(self)):
                raise IndexError(f'Index {temp_position} is out of bounds')
            reference = self.stack.front
            for i in range(position):
                reference = reference.tail
            return reference.value
        else:
            array = reversed([i for i in self])[position]
            return Stack() + array

    def __reversed__(self):
        array = [element for element in self]
        return Stack() + array
