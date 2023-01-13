# -*- coding: utf-8 -*-
'''
# Created on 01-09-23 10:33
# @Filename: 53_search.py
# @Desp: 来源于https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 统计一个数字在排序数组中出现的次数。

# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2

# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0

# 提示：
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums 是一个非递减数组
# -10^9 <= target <= 10^9
#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int: #偷懒做法
        return nums.count(target)
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left0 = left = 0
        right0 = right = len(nums) - 1
        count = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        while left0 <= right0:
            mid = (left0 + right0) // 2
            if nums[mid] <= target:
                left0 = mid + 1
            else:
                right0 = mid - 1
        
        for num in nums[left: left0]:
            if num == target:
                count += 1
        
        return count