# -*- coding: utf-8 -*-
'''
# Created on 02-01-23 15:59
# @Filename: 57_findContinuousSequence.py
# @Desp: 来源于https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

# 示例 1：
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]

# 示例 2：
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]

# 限制：
# 1 <= target <= 10^5

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        



