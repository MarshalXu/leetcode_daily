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

class Solution:

    def __calDis(self,x0,y0,x1,y1): #曼哈顿距离
        
        return abs(x0-x1) + abs(y0-y1)

    def search(self,mat,r,c):
        mr = len(mat)
        mc = len(mat[0])
        # for i in range( max([r,c,mr-r,mc-c]) ):
        for x,y in [[r,c+1],[r,c-1],[r-1,c],[r+1,c],[r+1,c+1],[r-1,c-1],[r+1,c-1],[r-1,c+1]]:
            if 0 <= x < mr and 0 <= y < mc:
                if mat[x][y] == 0:
                    return x,y
                else:
                    return self.search(mat,x,y)


    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        mr = len(mat)
        mc = len(mat[0])
        if mr == 1 or mc == 1:
            return mat

        res = [[0 for _ in range(mc)] for __ in range(mr)]
        for r in range(mr):
            for c in range(mc):
                if mat[r][c] == 0: # 如果是0
                    continue 
                else:
                    r1,c1 = self.search(mat,r,c)
                    res[r][c] = self.__calDis(r,c,r1,c1)

        return res

m = [
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,0]]

s = Solution()
print(s.updateMatrix(m))