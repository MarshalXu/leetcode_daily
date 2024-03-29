# -*- coding: utf-8 -*-
'''
# Created on 02-01-23 09:26
# @Filename: 61_isStraight.py
# @Desp: 来源于https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。


# 示例 1:
# 输入: [1,2,3,4,5]
# 输出: True


# 示例 2:
# 输入: [0,0,1,2,5]
# 输出: True


# 限制：
# 数组长度为 5 
# 数组的数取值为 [0, 13] .

"""
思考：
    根据题意顺子达成的条件是 
    1. 除了0以外不能有重复 
    2.手牌中的牌  除了0 要满足 max - min  < 5

"""

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if (n:=len(nums) != 5):
            return False
        r = set()
        ma,mi = 0,float("inf")
        for i in range(0,len(nums)):
            if nums[i] == 0:
                continue
            ma = max(nums[i],ma)
            mi = min(nums[i],mi)
            if nums[i] in r:
                return False
            r.add(nums[i])
        return ma - mi < 5
            


nums = [1,2,3,4,5]

print(Solution().isStraight(nums))



class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue # 跳过大小王
            ma = max(ma, num) # 最大牌
            mi = min(mi, num) # 最小牌
            if num in repeat: return False # 若有重复，提前返回 false
            repeat.add(num) # 添加牌至 Set
        return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子 
