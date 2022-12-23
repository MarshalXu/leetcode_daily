# -*- coding: utf-8 -*-
'''
# Created on 12-23-22 14:12
# @Filename: 566_matrixReshape.py
# @Desp: 来源于https://leetcode.cn/problems/reshape-the-matrix
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
# 给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
# 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
# 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

# 示例 1：
# 输入：mat = [[1,2],[3,4]], r = 1, c = 4
# 输出：[[1,2,3,4]]

# 示例 2：
# 输入：mat = [[1,2],[3,4]], r = 2, c = 4
# 输出：[[1,2],[3,4]]

# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List


class Solution:

    def __pick(self,mat):
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                yield mat[r][c]

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        r0 = len(mat)
        if r0 == 0:
            return [[]]
        c0 = len(mat[0])
        
        if r0*c0 != r*c:
            return mat

        new_mat = [[0 for _ in range(c)] for __ in range(r)]
        pick = self.__pick(mat)
        for i in range(r):
            for j in range(c):
                
                new_mat[i][j] = pick.__next__()

        return new_mat

s = Solution()
mat = [[1,2]]
r = 1
c = 1

print(s.matrixReshape(mat,r,c))