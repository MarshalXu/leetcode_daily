# -*- coding: utf-8 -*-
'''
# Created on 09-17-22 17:39
# @Filename: 695_maxAreaOfIsland.py
# @Desp: 来源于https://leetcode.cn/problems/max-area-of-island
# @software: vscode
# @author: xuchang0514@sina.com
'''
#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# 给你一个大小为 m x n 的二进制矩阵 grid 。
# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
# 岛屿的面积是岛上值为 1 的单元格的数目。
# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
# 示例 2：

# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
class Solution:

    def dfs(self, grid, r, c):
        grid[r][c] = 0
        self.lastest_area += 1
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == 1:
                self.dfs(grid, x, y)

    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
          return 0
        nc = len(grid[0])

        self.area = 0
        self.lastest_area = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    self.dfs(grid, r, c)
                    if self.lastest_area > self.area:
                        self.area = self.lastest_area
                    self.lastest_area = 0

        return self.area

g = [[1]]

s = Solution()
print(s.maxAreaOfIsland(g))