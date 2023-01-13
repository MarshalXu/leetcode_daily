# -*- coding: utf-8 -*-
'''
# Created on 01-13-23 11:10
# @Filename: 42_maxSubArray.py
# @Desp: 来源于https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。

# 示例1:
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 提示：
# 1 <= arr.length <= 10^5
# -100 <= arr[i] <= 100


#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 这种问题还是得用动态规划来解决

        #动态规划的起点是
        dp = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            if dp > 0:
                dp = dp + nums[i]
            else:
                dp = nums[i]
            
            max_sum = max(dp,max_sum)
        
        return max_sum