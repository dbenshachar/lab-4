import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BinTree : TypeAlias = Optional["Node[T]"]

T = TypeVar("T")

@dataclass(frozen=True)
class Node(Generic[T]):
    val : T
    left : BinTree
    right : BinTree

@dataclass(frozen=True)
class BinarySearchTree(Generic[T]):
    comes_before : Callable[[T, T],bool]
    tree : BinTree

    def is_empty(self) -> bool:
        """Returns if tree is empty."""
        return self.tree is None
    
    def insert(self, val : T) -> "BinarySearchTree[T]":
        """Returns Binary Search Tree with val inserted."""
        def _insert(tree : BinTree, val : T) -> BinTree:
            if tree is None:
                return Node(val, None, None)

        return BinarySearchTree[T](self.comes_before, _insert(self.tree, val))
    
    def lookup(self, val : T) -> bool:
        """Returns if value exists within tree."""
        def _lookup(tree : BinTree, val : T) -> bool:
            while tree:
                if not self.comes_before(tree.val, val) and not self.comes_before(val, tree.val):
                    return True
                elif self.comes_before(tree.val, val):
                    tree = tree.right
                else:
                    tree = tree.left
            
            return False
        
        return _lookup(self.tree, val)
    
    def delete(self, val : T) -> "BinarySearchTree":
        """Returns Binary Search Tree with val deleted."""
        ...

    @property
    def height(self) -> int:
        """Returns the height of the tree."""
        def _height(tree : BinTree) -> int:
            if not tree: return 0
            return 1 + max(_height(tree.left), _height(tree.right))
        
        return _height(self.tree)