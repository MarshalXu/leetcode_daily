# -*- coding: utf-8 -*-
'''
# Created on 01-30-23 09:38
# @Filename: 13_movingCount.py
# @Desp: 来源于https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），
# 也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
# 因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

# 示例 1：
# 输入：m = 2, n = 3, k = 1
# 输出：3

# 示例 2：
# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：

# 1 <= n,m <= 100
# 0 <= k <= 20

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    
    def movingCount(self, m: int, n: int, k: int) -> int:

        def dfs(r,c):
            if not 0 <= r < m or not 0 <= c < n or (r,c) in self.count or r + c > k: #结束
                return
            self.count.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        if m + n <= k: #如果k大于最大值直接返回
            return m * n
            
        self.count = set()
        # board = [[0 for _ in range(n)] for __ in range(m)]

        dfs(0,0)

        return len(self.count)

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def dfs(i, j, si, sj):

            if i >= m or j >= n or k < si + sj or (i, j) in visited: 
                return 0

            visited.add((i,j))
            
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

