# -*- coding: utf-8 -*-
'''
# Created on 01-09-23 14:46
# @Filename: 50_firstUniqChar.py
# @Desp: 来源于https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

# 示例 1:
# 输入：s = "abaccdeff"
# 输出：'b'

# 示例 2:
# 输入：s = "" 
# 输出：' '

# 限制：
# 0 <= s 的长度 <= 50000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s == "":
            return " "
        
        s = dict(Counter(list(s)))

        for k,v in s.items():
            if v == 1:
                return k

        return " "