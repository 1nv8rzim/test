from dataclasses import dataclass
from typing import Union, Any


@dataclass
class Node:
    __slots__ = 'value', 'tail'
    value: Any
    tail: Union[None, 'Node']


@dataclass
class LinkQueue:
    __slots__ = 'front', 'back', 'size'
    front: Union[None, Node]
    back: Union[None, Node]
    size: int


class Queue:

    def __init__(self, *args):
        self.queue = LinkQueue(None, None, 0)
        if len(args):
            for arg in args:
                self.enqueue(arg)

    def enqueue(self, element):
        node = Node(element, None)
        if not len(self):
            self.queue.front = node
        else:
            self.queue.back.tail = node
        self.queue.back = node
        self.queue.size += 1

    def dequeue(self):
        if not len(self):
            raise IndexError("Cannot dequeue an empty queue")
        else:
            self.queue.size -= 1
            removed = self.queue.front
            self.queue.front = removed.value
            if not len(self):
                self.queue.back = None
            return removed.value

    def pop(self):
        return self.dequeue()

    def front(self):
        return self.queue.front.value

    def back(self):
        return self.queue.back.value

    def __len__(self):
        return self.queue.size

    def __iter__(self):
        reference = self.queue.front
        values = []
        for i in range(self.queue.size):
            values += [reference.value]
            reference = reference.tail
        return iter(values)

    def __str__(self):
        reference = self.queue.front
        values = []
        for i in range(self.queue.size):
            values += [reference.value]
            reference = reference.tail
        return str(values)

    def __repr__(self):
        return 'Queue({})'.format(str(self)[1:-1] if len(self) else '')

    def __eq__(self, value):
        if isinstance(value, Queue):
            if len(value) == len(self):
                for i, j in zip(value, self):
                    if i != j:
                        return False
                return True
        return False

    def __ne__(self, value):
        return not self == value

    def __add__(self, value):
        clone = self.copy()
        if hasattr(value, '__iter__'):
            for i in value:
                clone.enqueue(i)
        else:
            clone.enqueue(value)
        return clone

    def copy(self):
        return Queue(element for element in self)

    def __getitem__(self, position):
        if isinstance(position, int):
            temp_position = position
            if position < 0:
                position += len(self)
            if not (0 <= position < len(self)):
                raise IndexError(f'Index {temp_position} is out of bounds')
            reference = self.queue.front
            for i in range(position):
                reference = reference.tail
            return reference.value
        else:
            array = [i for i in self][position]
            return Queue() + array

    def __reversed__(self):
        return Queue() + reversed([element for element in self])
