# -*- coding: utf-8 -*-
'''
# Created on 01-12-23 10:29
# @Filename: 10-II_numWays.py
# @Desp: 来源于https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 示例 1：
# 输入：n = 2
# 输出：2

# 示例 2：
# 输入：n = 7
# 输出：21

# 示例 3：
# 输入：n = 0
# 输出：1

# 提示：
# 0 <= n <= 100

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:

    def numWays(self, n: int) -> int:
        F = [1,1,2]
        if n <= 2:
            return F[n]
        

        for i in range(3,n+1):
            F.append(F[i-1]+F[i-2])
        
        return F[-1] % 1000000007