# -*- coding: utf-8 -*-
'''
# Created on 01-12-23 10:16
# @Filename: 10-I_fib.py
# @Desp: 来源于https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 示例 1：
# 输入：n = 2
# 输出：1

# 示例 2：
# 输入：n = 5
# 输出：5

# 提示：

# 0 <= n <= 100

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        F = [0,1]
        for i in range(2,n+1):
            F.append(F[i-1]+F[i-2])
        return F[-1] % 1000000007
