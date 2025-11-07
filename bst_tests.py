import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *

class BSTTests(unittest.TestCase):
    bst_empty : BinarySearchTree = BinarySearchTree[float](lambda x,y : x<y, None)
    bst_one : BinarySearchTree = BinarySearchTree[float](lambda x,y : x<y, Node(1, None, None))
    bst_seven : BinarySearchTree = BinarySearchTree[float](lambda x,y : x<y, Node(1, 
                                                                                Node(2,
                                                                                    Node(4, None, None),
                                                                                    Node(5, None, None)),
                                                                                Node(3,
                                                                                    Node(6, None, None),
                                                                                    Node(7, None, None))))

    def test_is_empty(self):
        self.assertEqual(self.bst_empty.is_empty(), True)
        self.assertEqual(self.bst_one.is_empty(), False)
        self.assertEqual(self.bst_seven.is_empty(), False)
    
    def test_height(self):
        self.assertEqual(self.bst_empty.height, 0)
        self.assertEqual(self.bst_one.height, 1)
        self.assertEqual(self.bst_seven.height, 3)

    def test_lookup(self):
        self.assertEqual(self.bst_empty.lookup(0), False)
        self.assertEqual(self.bst_one.lookup(0), False)
        self.assertEqual(self.bst_one.lookup(1), True)
        self.assertEqual(self.bst_seven.lookup(-1), False)
        self.assertEqual(self.bst_seven.lookup(3), True)
        self.assertEqual(self.bst_seven.lookup(1), True)
        self.assertEqual(self.bst_seven.lookup(7), True)
    
    def test_insert(self):
        self.assertEqual(self.bst_empty.insert(1).tree, Node(1, None, None))
        self.assertEqual(self.bst_one.insert(0).tree, Node(1, Node(0, None, None), None))
        self.assertEqual(self.bst_one.insert(2).tree, Node(1, None, Node(2, None, None)))

        self.assertEqual(self.bst_seven.insert(0).tree, Node(1, 
                                                            Node(2,
                                                                Node(4, Node(0, None, None), None),
                                                                Node(5, None, None)),
                                                            Node(3,
                                                                Node(6, None, None),
                                                                Node(7, None, None))))
        
        with self.assertRaises(ValueError):
            self.bst_one.insert(1)
            self.bst_seven.insert(4)
            self.bst_seven.insert(7)
    
if (__name__ == '__main__'):
    unittest.main()