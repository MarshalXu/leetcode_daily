# -*- coding: utf-8 -*-
'''
# Created on 01-13-23 11:48
# @Filename: 47_maxValue.py
# @Desp: 来源于https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

# 示例 1:
# 输入: 
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

# 提示：

# 0 < grid.length <= 200
# 0 < grid[0].length <= 200

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
# 还是得动态规划啊
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: 
                    continue
                if i == 0: 
                    grid[i][j] += grid[i][j - 1]
                elif j == 0: 
                    grid[i][j] += grid[i - 1][j]
                else: 
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
        