# -*- coding: utf-8 -*-
'''
# Created on 01-09-23 11:20
# @Filename: 53-II_missingNumber.py
# @Desp: 来源于https://leetcode.cn/problems/que-shi-de-shu-zi-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

# 示例 1:
# 输入: [0,1,3]
# 输出: 2

# 示例 2:
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8

# 限制：
# 1 <= 数组长度 <= 10000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# 方法1 暴力求解
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0] - 1 if nums[0] > 0 else nums[0] + 1
        for idx, num in enumerate(nums):
            if idx != num:
                return idx
        return n

#方法2 理论总和减去实际和

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        # if n == 1:
        #     return nums[0] - 1 if nums[0] > 0 else nums[0] + 1
        sum1 = sum([x for x in range(n+1)])
        sum2 = sum(nums)
        return sum1 - sum2