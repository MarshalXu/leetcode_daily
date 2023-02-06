# -*- coding: utf-8 -*-
'''
# Created on 02-02-23 14:52
# @Filename: 64_sumNums.py
# @Desp: 来源于https://leetcode.cn/problems/qiu-12n-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

# 示例 1：
# 输入: n = 3
# 输出: 6

# 示例 2：
# 输入: n = 9
# 输出: 45

# 限制：
# 1 <= n <= 10000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def sumNums(self, n: int) -> int:
        x = n and (n + self.sumNums(n-1))
        return x

def fuc(x):
    res = 0
    for i in range(1,x+1):
        res += i
    return res
n = 5
print(Solution().sumNums(n))
print(fuc(n))



# 逻辑
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
