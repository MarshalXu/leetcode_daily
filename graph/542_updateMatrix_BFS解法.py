# -*- coding: utf-8 -*-
'''
# Created on 12-26-22 17:41
# @Filename: 542_updateMatrix.py
# @Desp: 来源于https://leetcode.cn/problems/01-matrix
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
# 两个相邻元素间的距离为 1 。

# 示例 1：
# 输入：mat = [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出：[
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]

# 示例 2：
# 输入：mat = [
# [0,0,0],
# [0,1,0],
# [1,1,1]
# ]
# 输出：[
# [0,0,0],
# [0,1,0],
# [1,2,1]
# ]

# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# mat 中至少有一个 0 

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
import collections
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        Q = collections.deque([])
        visited = set()
        # 初始化队列，将所有起始点加入
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    Q.append((i, j))
                    visited.add((i, j))
        # 将所有相邻节点加入队列
        while Q:
            i, j = Q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1
                    visited.add((x, y))
                    Q.append((x, y))
        return matrix

m = [
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0]]

s = Solution()
print(s.updateMatrix(m))