from dataclasses import dataclass
from typing import Union, Any


@dataclass
class TreeNode:
    value: Any
    left: Union[None, 'TreeNode']
    right: Union[None, 'TreeNode']


class LinkTree:
    root: Union[TreeNode, None]
    size: int
    kind: type


class BinarySearchTree:

    def __init__(self, kind, *args):
        if not (hasattr(kind, '__lt__') and hasattr(kind, '__gt__') and hasattr(kind, '__eq__')):
            raise TypeError(
                f'Type {kind} is not able to be compared to itself')
        self.link_tree = LinkTree(None, 0, type(kind))
        if len(args):
            for arg in args:
                self.enqueue(args)

    def enqueue(self, element):
        if type(element) != self.kind:
            raise TypeError(
                f'Element {element} is not of tree type {self.kind}')
        if self.link_tree.root == None:
            self.link_tree.root = element
