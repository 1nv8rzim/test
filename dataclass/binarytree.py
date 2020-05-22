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


class BinaryTree:

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
            for value in iter(self.prefix_list()):
                self.enqueue(value)
                self.size -= 1
            for values in iter(self.prefix_list()):
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
        return iter(self.infix_list(self))

    def prefix_list(self):
        return self.prefix_list(self.root, [])

    def prefix_list(self, reference, accumulator):
        if reference is None:
            return accumulator
        accumulator = self.prefix_list(
            reference.left, accumulator.append(reference.value))
        return self.prefix_list(reference.right, accumulator)

    def infix_list(self):
        return self.infix_list(self.root, [])

    def infix_list(self, reference, accumulator):
        if reference is None:
            return accumulator
        accumulator = self.infix_list(reference.left, accumulator)
        return self.infix_list(reference.right, accumulator.append(reference.value))

    def __str__(self):
        return str(self.prefix_list())

    def __repr__(self):
        return 'BinaryTree({})'.format(str(self.prefix_list())[1:-1] if len(self) else '')

    def __eq__(self, value):
        if isinstance(value, BinaryTree):
            if len(value) == len(self):
                for i, j in zip(self, value):
                    if i != j:
                        return False
                return True
        return True

    def __ne__(self, value):
        return not self == value

    def copy(self):
        return BinaryTree(element for element in self)

    def __add__(self, value):
        clone = self.copy()
        if hasattr(value, '__iter__'):
            for i in value:
                clone.enqueue(i)
        else:
            clone.enqueue(value)
        return clone
