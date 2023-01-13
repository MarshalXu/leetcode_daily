# -*- coding: utf-8 -*-
'''
# Created on 09-17-22 17:39
# @Filename: 1254_closedIsland.py
# @Desp: 来源于https://leetcode.cn/problems/number-of-closed-islands
# @software: vscode
# @author: xuchang0514@sina.com
'''
# lib moduls:
import os, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List


# 二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。
# 请返回 封闭岛屿 的数目。

# 示例 1：
# 输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。

# 示例 2：
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1

# 示例 3：
# 输入：grid = [[1,1,1,1,1,1,1],
#              [1,0,0,0,0,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,1,0,1,0,1],
#              [1,0,1,1,1,0,1],
#              [1,0,0,0,0,0,1],
#              [1,1,1,1,1,1,1]]
# 输出：2

# 提示：

# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1

class Solution:

    def __judge(self, r, c):

        mr, mc = len(self.grid), len(self.grid[0])

        if r == 0 or c == 0 or r == mr - 1 or c == mc - 1:  # 如果在边界上
            self.no_edge_flag = False

        self.grid[r][c] = 2  # set成2

        for r, c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= r < mr and 0 <= c < mc and self.grid[r][c] == 0:
                self.__judge(r, c)

    def closedIsland(self, grid: List[List[int]]) -> int:

        mr = len(grid)
        if mr == 0:
            return 0
        mc = len(grid[0])
        self.grid = grid

        num = 0
        for r in range(mr):
            for c in range(mc):

                if self.grid[r][c] == 0:  # 是陆地

                    self.no_edge_flag = True

                    self.__judge(r, c)

                    if self.no_edge_flag:
                        num += 1

        return num


g = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0]]

s = Solution()

print(s.closedIsland(g))
