"""
LeetCode 3841. Palindromic Path Queries in a Tree [Hard]
https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
Topics: Array, String, Divide and Conquer, Bit Manipulation, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree
Solved: 2026-10-29
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


# Pattern: Tree traversal + Bitmask
# Approach: Use DFS to find path between two nodes, represent character parities as bitmask
# Time: O(n) per query in worst case, O(m*n) for processing all queries where m is query count
# Space: O(n) for adjacency list and recursion stack

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Convert s to list for easy updates
        chars = list(s)
        
        def find_path(start, end):
            """Find path from start to end using DFS"""
            if start == end:
                return [start]
            
            visited = [False] * n
            path = []
            
            def dfs(node, target):
                visited[node] = True
                path.append(node)
                
                if node == target:
                    return True
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        if dfs(neighbor, target):
                            return True
                
                path.pop()
                return False
            
            dfs(start, end)
            return path
        
        def can_form_palindrome(char_list):
            """Check if characters can form a palindrome"""
            # Use bitmask to track odd/even parity of each character
            bitmask = 0
            for char in char_list:
                bit = ord(char) - ord('a')
                bitmask ^= (1 << bit)
            
            # A string can form palindrome if at most 1 character has odd count
            # This means bitmask should have at most 1 bit set
            # A number has at most 1 bit set if it's 0 or (bitmask & (bitmask - 1)) == 0
            return (bitmask & (bitmask - 1)) == 0
        
        result = []
        
        for query in queries:
            parts = query.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                chars[u] = c
            else:  # query
                u = int(parts[1])
                v = int(parts[2])
                path = find_path(u, v)
                path_chars = [chars[node] for node in path]
                if can_form_palindrome(path_chars):
                    result.append(True)
                else:
                    result.append(False)
        
        return result


def test_palindromic_path():
    solution = Solution()
    
    # Test case 1 from problem
    n = 3
    edges = [[0,1],[1,2]]
    s = "aac"
    queries = ["query 0 2","update 1 b","query 0 2"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [True, False], f"Test 1 failed: {result}"
    
    # Test case 2 from problem
    n = 4
    edges = [[0,1],[0,2],[0,3]]
    s = "abca"
    queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [False, False, True], f"Test 2 failed: {result}"
    
    # Edge case: single node
    n = 1
    edges = []
    s = "a"
    queries = ["query 0 0"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [True], f"Test 3 failed: {result}"
    
    # Edge case: two nodes with same character
    n = 2
    edges = [[0,1]]
    s = "aa"
    queries = ["query 0 1"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [True], f"Test 4 failed: {result}"
    
    # Edge case: two nodes with different characters (both appear once - cannot form palindrome)
    n = 2
    edges = [[0,1]]
    s = "ab"
    queries = ["query 0 1"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [False], f"Test 5 failed: {result}"
    
    # Edge case: three different characters (3 odd counts - cannot form palindrome)
    n = 3
    edges = [[0,1],[1,2]]
    s = "abc"
    queries = ["query 0 2"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [False], f"Test 6 failed: {result}"
    
    # Test with update and query at same node
    n = 2
    edges = [[0,1]]
    s = "ab"
    queries = ["update 0 b", "query 0 1"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [True], f"Test 7 failed: {result}"
    
    # Edge case: path with even number of same characters
    n = 4
    edges = [[0,1],[1,2],[2,3]]
    s = "aaaa"
    queries = ["query 0 3"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [True], f"Test 8 failed: {result}"
    
    # Edge case: path with two pairs of characters
    n = 4
    edges = [[0,1],[1,2],[2,3]]
    s = "aabb"
    queries = ["query 0 3"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [True], f"Test 9 failed: {result}"
    
    # Edge case: path with all different characters (4 odd - cannot form palindrome)
    n = 5
    edges = [[0,1],[1,2],[2,3],[3,4]]
    s = "abcde"
    queries = ["query 0 4"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [False], f"Test 10 failed: {result}"
    
    # Edge case: single character path (always palindrome)
    n = 3
    edges = [[0,1],[1,2]]
    s = "abc"
    queries = ["query 1 1"]
    result = solution.palindromePath(n, edges, s, queries)
    assert result == [True], f"Test 11 failed: {result}"

    print("ALL TESTS PASSED")

if __name__ == "__main__":
    test_palindromic_path()
