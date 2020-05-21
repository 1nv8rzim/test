from dataclasses import dataclass
from typing import Union, Any


class Queue:

    @dataclass
    class Node:
        value: Any
        tail: Union[None, 'Node']

    @dataclass()
    class Queue:
        front: Union[None, Node]
        back: Union[None, Node]
        size: int

    def __init__(self):
        self.queue = Queue(None, None, 0)

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
