# -*- coding: utf-8 -*-
'''
# Created on 01-11-23 11:12
# @Filename: 1706_findBall.py
# @Desp: 来源于https://leetcode.cn/problems/where-will-the-ball-fall
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 用一个大小为 m x n 的二维网格 grid 表示一个箱子。你有 n 颗球。箱子的顶部和底部都是开着的。
# 箱子中的每个单元格都有一个对角线挡板，跨过单元格的两个角，可以将球导向左侧或者右侧。
# 将球导向右侧的挡板跨过左上角和右下角，在网格中用 1 表示。
# 将球导向左侧的挡板跨过右上角和左下角，在网格中用 -1 表示。
# 在箱子每一列的顶端各放一颗球。每颗球都可能卡在箱子里或从底部掉出来。如果球恰好卡在两块挡板之间的 "V" 形图案，或者被一块挡导向到箱子的任意一侧边上，就会卡住。

# 返回一个大小为 n 的数组 answer ，其中 answer[i] 是球放在顶部的第 i 列后从底部掉出来的那一列对应的下标，如果球卡在盒子里，则返回 -1 。

# 示例 1：

# 输入：grid = [
# [1,1,1,-1,-1],
# [1,1,1,-1,-1],
# [-1,-1,-1,1,1],
# [1,1,1,1,-1],
# [-1,-1,-1,-1,-1]
# ]
# 输出：[1,-1,-1,-1,-1]

# 解释：示例如图：
# b0 球开始放在第 0 列上，最终从箱子底部第 1 列掉出。
# b1 球开始放在第 1 列上，会卡在第 2、3 列和第 1 行之间的 "V" 形里。
# b2 球开始放在第 2 列上，会卡在第 2、3 列和第 0 行之间的 "V" 形里。
# b3 球开始放在第 3 列上，会卡在第 2、3 列和第 0 行之间的 "V" 形里。
# b4 球开始放在第 4 列上，会卡在第 2、3 列和第 1 行之间的 "V" 形里。

# 示例 2：
# 输入：grid = [[-1]]
# 输出：[-1]
# 解释：球被卡在箱子左侧边上。

# 示例 3：
# 输入：grid = [
# [1,1,1,1,1,1],
# [-1,-1,-1,-1,-1,-1],
# [1,1,1,1,1,1],
# [-1,-1,-1,-1,-1,-1]
# ]
# 输出：[0,1,2,3,4,-1]

# 提示：

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] 为 1 或 -1

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def fall(self,grid,r,c):
        mr = len(grid)
        mc = len(grid[0])
        if r >= mr:
            return c
        if grid[r][c] == 1: #如果是\

            #卡在右侧墙上
            if c+1 >= mc:
                return -1
            #卡在v上
            if grid[r][c+1] == -1:
                return -1
            #正常走了
            else:
                return self.fall(grid,r+1,c+1)

        else: #如果是/
            #卡在左侧墙上
            if c-1 < 0:
                return -1
            #卡在v上
            if grid[r][c-1] == 1:
                return -1
            #正常走了
            else:
                return self.fall(grid,r+1,c-1)



    def findBall(self, grid: List[List[int]]) -> List[int]:
        mr = len(grid)
        mc = len(grid[0])
        if mr * mc == 1:
            return [-1]
        res = []
        for r,c in [[0,x] for x in range(mc)]:
            res.append(self.fall(grid,r,c))
        
        return res

x = [
    [1,1,1,-1,-1],
    [1,1,1,-1,-1],
    [-1,-1,-1,1,1],
    [1,1,1,1,-1],
    [-1,-1,-1,-1,-1]
    ]
s = Solution()
print(s.findBall(x))