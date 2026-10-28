"""
LeetCode 3882. Minimum XOR Path in a Grid [Medium]
https://leetcode.com/problems/minimum-xor-path-in-a-grid/
Topics: Array, Dynamic Programming, Bit Manipulation, Matrix
Solved: 2026-10-28
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


# Pattern: Dynamic Programming with Set Tracking
# Approach: Track all possible XOR values reachable at each cell using DP. At each cell, combine XOR values from adjacent cells (top and left). The answer is the minimum XOR value at the destination.
# Time: O(m*n*k) where k is the average number of distinct XOR values per cell (bounded by 1024)
# Space: O(m*n*k)

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] stores all possible XOR values that can reach cell (i,j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Base case: starting cell
        dp[0][0].add(grid[0][0])
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                # From top cell
                if i > 0:
                    for xor_val in dp[i-1][j]:
                        dp[i][j].add(xor_val ^ grid[i][j])
                
                # From left cell
                if j > 0:
                    for xor_val in dp[i][j-1]:
                        dp[i][j].add(xor_val ^ grid[i][j])
        
        # Return minimum XOR value at destination
        return min(dp[m-1][n-1])


def test_minCost():
    sol = Solution()
    
    # Example 1
    assert sol.minCost([[1,2],[3,4]]) == 6
    
    # Example 2
    assert sol.minCost([[6,7],[5,8]]) == 9
    
    # Example 3
    assert sol.minCost([[2,7,5]]) == 0
    
    # Edge case: 1x1 grid
    assert sol.minCost([[5]]) == 5
    
    # Edge case: single row
    assert sol.minCost([[1,2,3,4]]) == (1 ^ 2 ^ 3 ^ 4)
    
    # Edge case: single column
    assert sol.minCost([[1],[2],[3],[4]]) == (1 ^ 2 ^ 3 ^ 4)
    
    # Edge case: all zeros
    assert sol.minCost([[0,0],[0,0]]) == 0
    
    # Edge case: 2x3 grid with various values
    grid = [[1,3],[2,4],[5,6]]
    result = sol.minCost(grid)
    # Valid paths (right/down only):
    # 1->3->4->6 = 1^3^4^6 = 2
    # 1->2->4->6 = 1^2^4^6 = 3
    # 1->2->5->6 = 1^2^5^6 = 0
    assert result == 0
    
    # Edge case: all same values (odd number on path means result is that value)
    assert sol.minCost([[7,7],[7,7]]) == 7
    
    # Edge case: larger grid with single path
    assert sol.minCost([[1,2,3]]) == (1 ^ 2 ^ 3)
    
    # Edge case: 2x2 grid with zeros
    assert sol.minCost([[0,1],[2,3]]) == min(0^1^3, 0^2^3)
    
    # Edge case: values that allow for 0 XOR result
    # grid = [[1,2],[3,0]] -> 1^2^0=3 or 1^3^0=2, min=2
    assert sol.minCost([[1,2],[3,0]]) == 2
    
    print("ALL TESTS PASSED")

if __name__ == "__main__":
    test_minCost()
