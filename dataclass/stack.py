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
