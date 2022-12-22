# -*- coding: utf-8 -*-
'''
# Created on 09-17-22 17:39
# @Filename: 1905_countSubIslands.py
# @Desp: 来源于https://leetcode.cn/problems/count-sub-islands
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向 （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。
# 如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，那么我们称 grid2 中的这个岛屿为 子岛屿 。
# 请你返回 grid2 中 子岛屿 的 数目 。

# 示例 1：
# 输入：grid1 = [[1,1,1,0,0],
#                [0,1,1,1,1],
#                [0,0,0,0,0],
#                [1,0,0,0,0],
#                [1,1,0,1,1]], 
#       grid2 = [[1,1,1,0,0],
#                [0,0,1,1,1],
#                [0,1,0,0,0],
#                [1,0,1,1,0],
#                [0,1,0,1,0]]
# 输出：3
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。

# 示例 2：
# 输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# 输出：2 
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。

# 提示：
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] 和 grid2[i][j] 都要么是 0 要么是 1 。

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:

    def dfs(self, r, c):
        #如果同样的位置在grid1中为0，那么就不是子岛屿
        if self.grid1[r][c] == 0:
            self.inside_flag = False

        #将grid2中的1置为0，防止重复遍历
        self.grid2[r][c] = 0
        #遍历grid2中的上下左右四个位置
        for r,c in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0 <= r < self.mr2 and 0 <= c < self.mc2 and self.grid2[r][c] == 1:
                self.dfs(r, c)
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.mr1 = len(grid1)
        self.mr2 = len(grid2)
        if self.mr1 + self.mr2 == 0 or self.mr1 * self.mr2 == 0:
            return 0
        self.mc2 = len(grid1[0])
        self.mc1 = len(grid2[0])
        self.grid1 = grid1
        self.grid2 = grid2

        self.sub_num = 0
        #遍历grid2
        for r in range(self.mr2):
            for c in range(self.mc2):
                self.inside_flag = True
                if self.grid2[r][c] == 1: #如果grid2中的位置为1，那么就开始遍历
                    self.dfs(r, c)
                    if self.inside_flag:
                        self.sub_num += 1

        return self.sub_num


g1 = [
    [1,1,1,0,0],
    [0,1,1,1,1],
    [0,0,0,0,0],
    [1,0,0,0,0],
    [1,1,0,1,1]]
g2 = [
    [1,1,1,0,0],
    [0,0,1,1,1],
    [0,1,0,0,0],
    [1,0,1,1,0],
    [0,1,0,1,0]]

s = Solution()
print(s.countSubIslands(g1, g2))