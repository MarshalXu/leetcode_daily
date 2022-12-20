# -*- coding: utf-8 -*-
'''
# Created on 09-17-22 17:39
# @Filename: best_time.py
# @Desp: 
# @software: vscode
# @author: xuchang0514@sina.com
'''
#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

"""
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。
示例 1:

输入:prices = [7,1,5,3,6,4]
输出:7
解释:在第 2 天（股票价格 = 1:的时候买入，在第 3 天（股票价格 = 5:的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
    随后，在第 4 天（股票价格 = 3:的时候买入，在第 5 天（股票价格 = 6:的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
    总利润为 4 + 3 = 7 。

"""

class Solution:
    def best_reward(self, seq: List[int]):
        return sum([seq[i] - seq[i-1] if seq[i] - seq[i-1] > 0 else 0 for i in range(1,len(seq))])


seq = [7,1,5,3,6,4]
s = Solution()
print(s.best_reward(seq))