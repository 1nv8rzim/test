from dataclasses import dataclass
from typing import Union, Any


@dataclass
class TreeNode:
    value: Any
    left: Union[None, 'TreeNode']
    right: Union[None, 'TreeNode']


@dataclass
class LinkTree:
    root: Union[TreeNode, None]
    size: int
    kind: type


class BinarySearchTree:

    def __init__(self, kind, *args):
        if not (hasattr(kind, '__lt__') and hasattr(kind, '__gt__') and hasattr(kind, '__eq__')):
            raise TypeError(
                f'Type {kind} is not able to be compared to itself')
        self.link_tree = LinkTree(None, 0, kind)
        if len(args):
            for arg in args:
                self.enqueue(args)

    def enqueue(self, element):
        if type(element) != self.kind:
            raise TypeError(
                f'Element {element} is not of tree type {self.kind}')
        self.enqueue(element, self.root)

    def enqueue(self, element, reference):
        if reference.value is None:
            reference = TreeNode(element, None, None)
            self.size += 1
        elif element < reference.value:
            self.enqueue(element, reference.left)
        elif element > reference.value:
            self.enqueue(element, reference.right)
        else:
            pass

    def dequeue(self, element):
        if type(element) != self.kind:
            raise TypeError(
                f'Element {element} is not of tree type {self.kind}')
        self.dequeue(element, self.root)

    def dequeue(self, element, reference):
        if reference.value is None:
            pass
        elif element < reference.value:
            self.dequeue(element, reference.left)
        elif element > reference.value:
            self.dequeue(element, reference.right)
        else:
            left_tree = reference.left
            right_tree = reference.right
            reference = None
            for value in left_tree:
                self.enqueue(value)
                self.size -= 1
            for values in right_tree:
                self.enqueue(value)
                self.size -= 1
            self.size -= 1

    def add(self, element):
        self.enqueue(element)

    def remove(self, element):
        self.dequeue(element)

    def contains(self, element):
        if type(element) != self.kind:
            raise TypeError(
                f'Element {element} is not of tree type {self.kind}')
        return self.contains(element, self.root)

    def contains(self, element, reference):
        if reference.value is None:
            return False
        elif element < reference.value:
            return self.contains(element, reference.left)
        elif element > reference.value:
            return self.contains(element, reference.right)
        return True

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.convert_to_list(self, []))

    def convert_to_list(self, accumulator):
        pass
