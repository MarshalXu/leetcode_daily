# -*- coding: utf-8 -*-
'''
# Created on 01-29-23 09:52
# @Filename: 21_exchange.py
# @Desp: 来源于https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

#  

# 示例：

# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。
#  

# 提示：

# 0 <= nums.length <= 50000
# 0 <= nums[i] <= 10000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
import collections
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        que = collections.deque()
        for n in nums:
            if n % 2 == 0:
                que.append(n)
            else:
                que.appendleft(n)
        return list(que)
