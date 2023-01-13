# -*- coding: utf-8 -*-
'''
# Created on 12-26-22 13:55
# @Filename: 1091_shortestPathBinaryMatrix.py
# @Desp: 来源于https://leetcode.cn/problems/shortest-path-in-binary-matrix
# @software: vscode
# @author: xuchang0514@sina.com
'''

#
# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。
# 二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：
# 路径途经的所有单元格都的值都是 0 。
# 路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
# 畅通路径的长度 是该路径途经的单元格总数。

# 示例 1：
# 输入：grid = [
# [0,1],
# [1,0]]
# 输出：2

# 示例 2：
# 输入：grid = [
# [0,0,0],
# [1,1,0],
# [1,1,0]]
# 输出：4

# 示例 3：
# 输入：grid = [
# [1,0,0],
# [1,1,0],
# [1,1,0]]
# 输出：-1
 
# 提示：
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] 为 0 或 1

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        n = len(grid)
        if n == 1:
            return 1
        if grid[n-1][n-1] != 0:
            return -1
        # 8个方向
        directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        # BFS
        q = [(0,0)]
        # 记录已经访问过的节点
        visited = set()
        visited.add((0,0))
        step = 1
        while q:
            step += 1
            for _ in range(len(q)):
                x,y = q.pop(0)
                for dx,dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                        continue
                    if (new_x,new_y) in visited:
                        continue
                    if grid[new_x][new_y] == 1:
                        continue
                    if new_x == n-1 and new_y == n-1:
                        return step
                    q.append((new_x,new_y))
                    visited.add((new_x,new_y))
        return -1





grid = [
    [0,1,0,0,0,0],
    [0,1,0,1,1,0],
    [0,1,1,0,1,0],
    [0,0,0,0,1,0],
    [1,1,1,1,1,0],
    [1,1,1,1,1,0]]

s = Solution()
print(s.shortestPathBinaryMatrix(grid))
