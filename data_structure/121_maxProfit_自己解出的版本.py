# -*- coding: utf-8 -*-
'''
# Created on 12-21-22 14:51
# @Filename: 121_maxProfit.py
# @Desp: 来源于https://leetcode.cn/problems/best-time-to-buy-and-sell-stock
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

# 示例 1：
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

# 示例 2：
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

# 提示：
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
# 动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        best_profit = 0
        #买入和卖出 的起始值是 prices[0] 和prices[1]
        buy_price = prices[0]
        sell_price = prices[1]
        cul_profit = lambda b,s: s-b
        
        i = 1
        while i < n:
            
            current_sell_price = prices[i]
            current_profit = cul_profit(buy_price,current_sell_price)
            lastest_profict = cul_profit(buy_price,sell_price)
            # if cul_profit(buy_price,current_sell_price) > cul_profit(buy_price,sell_price):
            if current_profit > lastest_profict:
                sell_price = current_sell_price
                i += 1
            else:
                if current_profit < 0:
                    buy_price = current_sell_price
                i += 1

            best_profit = max(best_profit,current_profit)
        
        return best_profit

s = Solution()
p = [7,6,4,3,1]
print(s.maxProfit(p))



