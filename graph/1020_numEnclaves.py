# -*- coding: utf-8 -*-
'''
# Created on 09-17-22 17:39
# @Filename: 1020_numEnclaves.py
# @Desp: 来源于https://leetcode.cn/problems/number-of-enclaves
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

# 示例 1：
# 输入：grid = [[0,0,0,0],
#               [1,0,1,0],
#               [0,1,1,0],
#               [0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

# 示例 2：
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
class Solution:
    
    def __walk(self,r,c):
        self._inside_num += 1
        self.grid[r][c] = 0
        if r == 0 or r == len(self.grid)-1 or c == 0 or c == len(self.grid[0])-1:
            self._no_edge_flag = False
        for r,c in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]: # 上下左右
            if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] == 1:
                self.__walk(r,c)
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        mr = len(grid)
        if mr == 0:
            return 0
        mc = len(grid[0])

        self.grid = grid
        self._inside_num = 0
        self._total_num = 0
        
        for r in range(mr):
            for c in range(mc):
                self._no_edge_flag = True
                self._inside_num = 0
                if grid[r][c] == 1:
                    self.__walk(r,c)
                if self._no_edge_flag:
                    self._total_num += self._inside_num

        return self._total_num