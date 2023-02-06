# -*- coding: utf-8 -*-
'''
# Created on 02-03-23 09:42
# @Filename: 51_reversePairs_H.py
# @Desp: 来源于https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

# 示例 1:
# 输入: [7,5,6,4]
# 输出: 5


# 限制：
# 0 <= 数组长度 <= 50000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        