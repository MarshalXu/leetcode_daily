# -*- coding: utf-8 -*-
'''
# Created on 12-23-22 14:32
# @Filename: 118_generate.py
# @Desp: 来源于https://leetcode.cn/problems/pascals-triangle
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

# 示例 1:
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# 示例 2:
# 输入: numRows = 1
# 输出: [[1]]

# 提示:
# 1 <= numRows <= 30

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows): 
            res.append([])
            for j in range(i+1):
                try:
                    if 0 <= i-1 and 0 <= j-1: 
                        res[i].append(res[i-1][j-1] + res[i-1][j])  
                    else:
                        raise ValueError()
                except:
                    res[i].append(1)
                
        return res

s = Solution()

print(s.generate(10))