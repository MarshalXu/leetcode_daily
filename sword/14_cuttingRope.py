# -*- coding: utf-8 -*-
'''
# Created on 02-01-23 15:19
# @Filename: 14_cuttingRope.py
# @Desp: 来源于https://leetcode.cn/problems/jian-sheng-zi-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
# 每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

# 示例 1：

# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1
# 示例 2:

# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
# 提示：

# 2 <= n <= 58

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n-1
        if n == 4: 
            return 4
        
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        
        res *= n

        return res

n = 10
print(Solution().cuttingRope(n))