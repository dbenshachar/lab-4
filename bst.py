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
            if not tree:
                return Node(val, None, None)
            
            if self.comes_before(tree.val, val):
                return Node(tree.val, tree.left, _insert(tree.right, val))
            elif self.comes_before(val, tree.val):
                return Node(tree.val, _insert(tree.left, val), tree.right)
            
            raise ValueError("Duplicates not allowed in Binary Search Tree")

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
        def _delete(tree: BinTree, val: T) -> BinTree:
            if not tree: return None
            
            if self.comes_before(tree.val, val):
                return Node(tree.val, tree.left, _delete(tree.right, val))
            elif self.comes_before(val, tree.val):
                return Node(tree.val, _delete(tree.left, val), tree.right)
            
            if tree.left is None:
                return tree.right
            if tree.right is None:
                return tree.left
                        
            max_node = tree.left
            while max_node.right:
                max_node = max_node.right
            
            return Node(
                max_node.val,
                _delete(tree.left, max_node.val),
                tree.right
            )
        
        return BinarySearchTree[T](self.comes_before, _delete(self.tree, val))
    
    @property
    def height(self) -> int:
        """Returns the height of the tree."""
        def _height(tree : BinTree) -> int:
            if not tree: return 0
            return 1 + max(_height(tree.left), _height(tree.right))
        
        return _height(self.tree)