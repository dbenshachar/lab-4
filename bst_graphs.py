import sys
import unittest
from typing import *
from dataclasses import dataclass
import math

import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)
from bst import *

def random_tree(n : int) -> BinarySearchTree[float]:
    tree : BinarySearchTree[float] = BinarySearchTree[float](lambda x,y : x<y, None)
    for _ in range(n):
        tree.insert(random.random())

    return tree

def generate_tree_heights(n_max : int = 200, num_trees : int = 1_000) -> List[int]:
    res = []
    for n in range(n_max):
        avg = 0
        for _ in range(num_trees):
            avg += random_tree(n).height
        res.append(avg / num_trees)
    return res

if (__name__ == '__main__'):
    ...