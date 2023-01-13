# -*- coding: utf-8 -*-
'''
# Created on 12-26-22 11:26
# @Filename: 242_isAnagram.py
# @Desp: 来源于https://leetcode.cn/problems/valid-anagram
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

#  

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false
#  

# 提示:

# 1 <= s.length, t.length <= 5 * 104
# s 和 t 仅包含小写字母
#  

# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if collections.Counter(s) == collections.Counter(t):
            return True
        else:
            return False
