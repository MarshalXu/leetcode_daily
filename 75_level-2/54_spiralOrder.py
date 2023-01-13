# -*- coding: utf-8 -*-
'''
# Created on 01-10-23 16:49
# @Filename: 54_spiralOrder.py
# @Desp: 来源于https://leetcode.cn/problems/spiral-matrix
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

#  

# 示例 1：


# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：


# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  

# 提示：

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
from math import ceil
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        mr = len(matrix)
        if mr == 0:
            return []
        mc = len(matrix[0])
        layer = min(ceil(mr/2),ceil(mc/2))
        print("layer",layer)
        seq = []
        for l in range(layer):
            # top
            seq.extend([[l,y] for y in range(l,mc - l) if [l,y] not in seq])
            # right
            seq.extend([[x,mc-l-1] for x in range(l,mr - l) if [x,mc-l-1] not in seq])
            # bottom
            seq.extend([[mr-l-1,y] for y in range(mc-l-1,l-1,-1) if [mr-l-1,y] not in seq])
            # left
            seq.extend([[x,l] for x in range(mr-l-1,l-1,-1) if [x,l] not in seq])
            
        res = [matrix[r][c] for r,c in seq]
        return res

s = Solution()
m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(m))
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        r, i, j, di, dj = [], 0, 0, 0, 1
        if matrix != []:
            for _ in range(len(matrix) * len(matrix[0])):
                r.append(matrix[i][j])
                matrix[i][j] = 0
                if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
                    di, dj = dj, -di
                i += di
                j += dj
        return r