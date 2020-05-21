from dataclasses import dataclass
from typing import Any, Union


@dataclass
class Node:
    __slots__ = 'value', 'tail'
    value: Any
    tail: Union[None, 'Node']


@dataclass
class Stack:
    __slots__ = 'front', 'size'
    front: Node
    size: int
