"""
LeetCode 462. Minimum Moves to Equal Array Elements II [Medium]
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
Topics: Array, Math, Sorting
Solved: 2026-11-02
"""
import sys
import re
import math
import heapq
import bisect
import itertools
import functools
import collections
from typing import *
from collections import *
from heapq import *
from bisect import *
from functools import *
from itertools import *
from math import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Pattern: Median/Math
# Approach: The sum of absolute deviations is minimized at the median. Sort the array, find the median, and calculate the total moves needed.
# Time: O(n log n)
# Space: O(1) excluding sorting space

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)


def test_minMoves2():
    solution = Solution()
    
    # Test case 1: [1,2,3]
    assert solution.minMoves2([1, 2, 3]) == 2
    
    # Test case 2: [1,10,2,9]
    assert solution.minMoves2([1, 10, 2, 9]) == 16
    
    # Edge case: single element
    assert solution.minMoves2([5]) == 0
    
    # Edge case: two elements
    # [1, 3] -> median at index 1 is 3, moves = |1-3| + |3-3| = 2
    assert solution.minMoves2([1, 3]) == 2
    
    # Edge case: all same elements
    assert solution.minMoves2([5, 5, 5, 5]) == 0
    
    # Edge case: negative numbers
    # [-5, -1, 0, 1, 5] -> median at index 2 is 0
    # moves: |-5-0| + |-1-0| + |0-0| + |1-0| + |5-0| = 5+1+0+1+5 = 12
    assert solution.minMoves2([-5, -1, 0, 1, 5]) == 12
    
    # Edge case: large spread with zeros
    # [0, 0, 0, 1] -> median at index 2 is 0
    # moves = |0-0| + |0-0| + |0-0| + |1-0| = 1
    assert solution.minMoves2([0, 0, 0, 1]) == 1
    
    # Edge case: negative to positive range
    # [-10, 10] -> median at index 1 is 10
    # moves = |-10-10| + |10-10| = 20 + 0 = 20
    assert solution.minMoves2([-10, 10]) == 20
    
    # Edge case: more complex even case
    # [1, 2, 3, 4] -> median at index 2 is 3
    # moves = |1-3| + |2-3| + |3-3| + |4-3| = 2+1+0+1 = 4
    assert solution.minMoves2([1, 2, 3, 4]) == 4
    
    # Edge case: duplicates
    # [1, 1, 1, 5] -> median at index 2 is 1
    # moves = |1-1| + |1-1| + |1-1| + |5-1| = 0+0+0+4 = 4
    assert solution.minMoves2([1, 1, 1, 5]) == 4
    
    print("ALL TESTS PASSED")

if __name__ == "__main__":
    test_minMoves2()
