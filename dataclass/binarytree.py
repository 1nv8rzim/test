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
        self.link_tree.root = self.enqueuer(element, self.link_tree.root)

    def enqueuer(self, element, reference):
        if reference is None:
            self.link_tree.size += 1
            return TreeNode(element, None, None)
        elif element < reference.value:
            reference.left = self.enqueuer(element, reference.left)
        elif element > reference.value:
            reference.right = self.enqueuer(element, reference.right)
        return reference

    def dequeue(self, element):
        if type(element) != self.link_tree.kind:
            raise TypeError(
                f'Element {element} is not of tree type {self.link_tree.kind}')
        self.link_tree.root, branch = self.dequeuer(
            element, self.link_tree.root)
        if branch is not None:
            branch_tree = BinaryTree(self.link_tree.kind)
            branch_tree.root = branch
            for element in branch_tree:
                self.enqueue(element)

    def dequeuer(self, element, reference):
        if reference is None:
            return reference, None
        elif element < reference.value:
            reference.left, branch = self.dequeuer(element, reference.left)
        elif element > reference.value:
            reference.right, branch = self.dequeuer(element, reference.right)
        else:
            if reference.left is None:
                return reference, reference.right
            return reference, reference.left
        return reference, branch

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
        return iter(self.infix_list())

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
            return []
        else:
            return [] + self.prefix_lister(reference.left) + [reference.value] + self.prefix_lister(reference.right)

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
