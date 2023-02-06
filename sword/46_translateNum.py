# -*- coding: utf-8 -*-
'''
# Created on 01-28-23 10:38
# @Filename: 46_translateNum.py
# @Desp: 来源于https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
# 请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

#  

# 示例 1:

# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#  

# 提示：

# 0 <= num < 2^31

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# 其实就是爬楼梯 每一级有两种 多了一个判断条件是 小于等于25 

class Solution:
    
    def translateNum(self, num: int) -> int:
        num = str(num)
        n = len(num)
        if n == 1:
            return 1
        c = [0 for _ in range(n+1)]
        for i in range(0,n+1):
            if i == 0:
                c[i] = 1
            elif i == 1:
                c[i] = 1
            else:
                if num[i-2] != "0" and int(num[i-2:i]) < 26:
                    c[i] = c[i-2] + c[i-1]
                else:
                    c[i] = c[i-1]
            
        return c[-1]
