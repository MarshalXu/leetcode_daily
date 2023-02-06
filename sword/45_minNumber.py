# -*- coding: utf-8 -*-
'''
# Created on 01-31-23 10:29
# @Filename: 45_minNumber.py
# @Desp: 来源于https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

# 示例 1:
# 输入: [10,2]
# 输出: "102"

# 示例 2:
# 输入: [3,30,34,5,9]
# 输出: "3033459"

# 提示:
# 0 < nums.length <= 100

# 说明:
# 输出结果可能非常大，所以你需要返回一个字符串而不是整数
# 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
from functools import cmp_to_key
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(a,b):  # 每相邻的两个字符串进行比较 字符串与字符串比较，比较的是首个字符编码的大小 而不是字符串的大小 更不是字符串所代表的数字的大小
            print("comparing ", a, " and ", b)
            if a+b < b+a:
                return -1
            elif a+b > b+a:
                return 1
            else:
                return 0
        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(cmp))
        return ''.join(nums)

nums = [3,30,34,5,9]
print(Solution().minNumber(nums)) 