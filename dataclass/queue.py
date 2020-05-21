from dataclasses import dataclass
from typing import Union, Any


@dataclass
class Node:
    value: Any
    tail: Union[None, 'Node']


@dataclass
class LinkQueue:
    front: Union[None, Node]
    back: Union[None, Node]
    size: int


class Queue:

    def __init__(self, *args):
        self.queue = LinkQueue(None, None, 0)
        if not len(args):
            for idx in range(len(args), 0, -1):
                self.enqueue(args[idx])

    def __len__(self):
        return self.queue.size

    def enqueue(self, element):
        self.queue.size += 1
        element = Node(element, None)
        if not len(self):
            self.queue.front = element
        else:
            self, queue.back.tail = element
        self.queue.back = element

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

    def __str__(self):
        return str(self.queue)

    def __repr__(self):
        return 'Queue({})'.format(str(self) if len(str) else '')
