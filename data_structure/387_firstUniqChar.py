# -*- coding: utf-8 -*-
'''
# Created on 12-26-22 10:46
# @Filename: 387.py
# @Desp: 来源于https://leetcode.cn/problems/first-unique-character-in-a-string
# @software: vscode
# @author: xuchang0514@sina.com
'''
#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

# 示例 1：
# 输入: s = "leetcode"
# 输出: 0

# 示例 2:
# 输入: s = "loveleetcode"
# 输出: 2

# 示例 3:
# 输入: s = "aabb"
# 输出: -1

# 提示:
# 1 <= s.length <= 105
# s 只包含小写字母

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        if len(set(list(s))) == 1: return -1
        for i in range(0,len(s)):
            if not s[i] in s[0:i]+s[i+1:]:
                return i
        return -1

#个人理解
# 虽然是一道简单题 如果用counter直接hash出现次数，然后在找最小的 会快很多
# 因为hash一次遍历 找答案一次遍历 只需要遍历两次 时间复杂度是O(n)
# 我这里的办法可能最坏的情况 时间复杂度是O(n(n-1))
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1

