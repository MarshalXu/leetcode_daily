# -*- coding: utf-8 -*-
'''
# Created on 12-27-22 10:49
# @Filename: 934_shortestBridge.py
# @Desp: 来源于https://leetcode.cn/problems/shortest-bridge
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。
# 岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。
# 你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。
# 返回必须翻转的 0 的最小数目。

# 示例 1：
# 输入：grid = [
# [0,1],
# [1,0]]
# 输出：1

# 示例 2：
# 输入：grid = [
# [0,1,0],
# [0,0,0],
# [0,0,1]]
# 输出：2

# 示例 3：
# 输入：grid = [
# [1,1,1,1,1],
# [1,0,0,0,1],
# [1,0,1,0,1],
# [1,0,0,0,1],
# [1,1,1,1,1]]
# 输出：1

# 提示：
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] 为 0 或 1
# grid 中恰有两个岛

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

from collections import deque
from itertools import pairwise
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            q.append((i, j))
            grid[i][j] = 2
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        n = len(grid)
        dirs = (-1, 0, 1, 0, -1)
        q = deque()
        i, j = next((i, j) for i in range(n) for j in range(n) if grid[i][j])
        dfs(i, j)
        ans = 0
        while 1:
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return ans
                        if grid[x][y] == 0:
                            grid[x][y] = 2
                            q.append((x, y))
            ans += 1