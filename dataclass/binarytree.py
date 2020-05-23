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
        if not isinstance(kind, type):
            raise TypeError(f'{kind} is not a type')
        if not (hasattr(kind, '__lt__') and hasattr(kind, '__gt__') and hasattr(kind, '__eq__')):
            raise TypeError(
                f'Type {kind} is not able to be compared to itself')
        self.link_tree = LinkTree(None, 0, kind)
        if len(args):
            for arg in args:
                self.enqueue(arg)

    def enqueue(self, element):
        if type(element) != self.link_tree.kind:
            raise TypeError(
                f'Element {element} is not of tree type {self.link_tree.kind}')
        self.enqueuer(element, self.link_tree.root)

    def enqueuer(self, element, reference):
        if reference is None:
            reference = TreeNode(element, None, None)
            self.link_tree.size += 1
        elif element < reference.value:
            self.enqueuer(element, reference.left)
        elif element > reference.value:
            self.enqueuer(element, reference.right)
        else:
            pass

    def dequeue(self, element):
        if type(element) != self.link_tree.kind:
            raise TypeError(
                f'Element {element} is not of tree type {self.link_tree.kind}')
        self.dequeuer(element, self.link_tree.root)

    def dequeue(self, element, reference):
        if reference is None:
            pass
        elif element < reference.value:
            self.dequeuer(element, reference.left)
        elif element > reference.value:
            self.dequeuer(element, reference.right)
        else:
            left_tree = reference.left
            right_tree = reference.right
            reference = None
            for value in iter(self.prefix_list()):
                self.enqueue(value)
                self.link_tree.size -= 1
            for values in iter(self.prefix_list()):
                self.enqueue(value)
                self.link_tree.size -= 1
            self.link_tree.size -= 1

    def add(self, element):
        self.enqueue(element)

    def remove(self, element):
        self.dequeue(element)

    def contains(self, element):
        if type(element) != self.link_tree.kind:
            raise TypeError(
                f'Element {element} is not of tree type {self.link_tree.kind}')
        return self.container(element, self.link_tree.root)

    def container(self, element, reference):
        if reference.value is None:
            return False
        elif element < reference.value:
            return self.container(element, reference.left)
        elif element > reference.value:
            return self.container(element, reference.right)
        return True

    def __len__(self):
        return self.link_tree.size

    def __iter__(self):
        return iter(self.infix_list(self))

    def prefix_list(self):
        return self.prefix_lister(self.link_tree.root)

    def prefix_lister(self, reference):
        if reference is None:
            return []
        else:
            return [reference.value] + self.prefix_lister(reference.left) + self.prefix_lister(reference.right)

    def infix_list(self):
        return self.infix_lister(self.link_tree.root, [])

    def infix_lister(self, reference, accumulator):
        if reference is None:
            return accumulator
        accumulator = self.infix_lister(reference.left, accumulator)
        return self.infix_lister(reference.right, accumulator.append(reference.value))

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

    def __getitem__(self, position):
        return self.infix_list()[position]
