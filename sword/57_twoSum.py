# -*- coding: utf-8 -*-
'''
# Created on 01-29-23 10:23
# @Filename: 57_twoSum.py
# @Desp: 来源于https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]

# 示例 2：
# 输入：nums = [10,26,30,31,47,60], target = 40
# 输出：[10,30] 或者 [30,10]

# 限制：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if nums[0] >= target or n <= 1:
            return []
        # 双指针

        left = 0
        right = n-1

        while left < right:
            if (sum := nums[left] + nums[right]) == target:
                return [nums[left],nums[right]]
            elif sum > target:
                right -= 1
            else:
                left += 1
        
        return []

