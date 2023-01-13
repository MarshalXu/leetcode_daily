# -*- coding: utf-8 -*-
'''
# Created on 01-12-23 10:54
# @Filename: 63_maxProfit.py
# @Desp: 来源于https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 限制：
# 0 <= 数组长度 <= 10^5

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        bottom = float("inf")
        res = 0
        for i,p in enumerate(prices):
            
            bottom = min(p,bottom)

            res = max(p-bottom,res)

        return res
