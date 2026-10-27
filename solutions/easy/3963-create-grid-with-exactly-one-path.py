"""
LeetCode 3963. Create Grid With Exactly One Path [Easy]
https://leetcode.com/problems/create-grid-with-exactly-one-path/
Topics: 
Solved: 2026-10-27
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


# Pattern: Greedy construction
# Approach: Create a forced path by making free cells form a single staircase pattern. Go right across the first row (except last column), then go down the last column. Mark all other cells as obstacles.
# Time: O(m*n)
# Space: O(m*n)

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Create a grid where we force exactly one path
        # Path: go right along row 0, then down along column n-1
        
        grid = [['#'] * n for _ in range(m)]
        
        # Mark the path: all of row 0
        for j in range(n):
            grid[0][j] = '.'
        
        # Mark the path: all of column n-1 (except we already did row 0)
        for i in range(1, m):
            grid[i][n-1] = '.'
        
        # Convert to list of strings
        return [''.join(row) for row in grid]


def test_create_grid():
    solution = Solution()
    
    # Example 1: m=2, n=3
    result = solution.createGrid(2, 3)
    assert len(result) == 2
    assert len(result[0]) == 3
    # Verify path exists: (0,0) -> (0,1) -> (0,2) -> (1,2)
    assert result[0][0] == '.'
    assert result[0][1] == '.'
    assert result[0][2] == '.'
    assert result[1][2] == '.'
    # Verify uniqueness by checking structure
    print(f"Example 1: {result}")
    
    # Example 2: m=3, n=3
    result = solution.createGrid(3, 3)
    assert len(result) == 3
    assert len(result[0]) == 3
    # Path should be: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
    assert result[0][0] == '.'
    assert result[0][1] == '.'
    assert result[0][2] == '.'
    assert result[1][2] == '.'
    assert result[2][2] == '.'
    print(f"Example 2: {result}")
    
    # Example 3: m=1, n=4
    result = solution.createGrid(1, 4)
    assert len(result) == 1
    assert result[0] == "....", f"Expected '....', got {result[0]}"
    print(f"Example 3: {result}")
    
    # Edge case: m=1, n=1
    result = solution.createGrid(1, 1)
    assert result[0] == "."
    print(f"Edge case m=1, n=1: {result}")
    
    # Edge case: m=4, n=1
    result = solution.createGrid(4, 1)
    assert len(result) == 4
    assert all(len(row) == 1 for row in result)
    assert result[0][0] == '.'
    assert result[1][0] == '.'
    assert result[2][0] == '.'
    assert result[3][0] == '.'
    print(f"Edge case m=4, n=1: {result}")
    
    # Edge case: m=3, n=1
    result = solution.createGrid(3, 1)
    assert result == [".", ".", "."]
    print(f"Edge case m=3, n=1: {result}")
    
    # Verify path count for a sample
    def count_paths(grid):
        m, n = len(grid), len(grid[0])
        if grid[0][0] == '#' or grid[m-1][n-1] == '#':
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '#':
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    continue
                else:
                    up = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + left
        
        return dp[m-1][n-1]
    
    # Test path uniqueness
    for m, n in [(2, 3), (3, 3), (1, 4), (5, 5), (3, 1), (1, 3)]:
        grid = solution.createGrid(m, n)
        paths = count_paths([list(row) for row in grid])
        assert paths == 1, f"Expected exactly 1 path for {m}x{n} grid, got {paths}"
    
    print("ALL TESTS PASSED")

if __name__ == "__main__":
    test_create_grid()
