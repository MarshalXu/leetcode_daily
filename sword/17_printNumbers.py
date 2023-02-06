# -*- coding: utf-8 -*-
'''
# Created on 02-03-23 09:30
# @Filename: 17_printNumbers.py
# @Desp: 来源于https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

# 示例 1:
# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]

# 说明：
# 用返回一个整数列表来代替打印
# n 为正整数

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        maxn = int("9" * n)
        res = []
        for i in range(maxn):
            res.append(i+1)
        return res