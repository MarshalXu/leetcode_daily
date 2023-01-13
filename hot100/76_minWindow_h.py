# -*- coding: utf-8 -*-
'''
# Created on 01-12-23 15:33
# @Filename: 76_minWindow_h.py
# @Desp: 来源于https://leetcode.cn/problems/minimum-window-substring
# @software: vscode
# @author: xuchang0514@sina.com
'''
#lib moduls:
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。

# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

# 示例 2：
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。

# 示例 3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。

# 提示：
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s 和 t 由英文字母组成

import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sl = len(s)
        tl = len(t)

        if tl > sl:
            return ""
        if t in s:
            return t
        dt = collections.Counter(t)
        
        window = tl
        for w in range(window,sl+1):
            for start in range(sl-w+1):
                end = start + w
                d_sw = collections.Counter(s[start:end])
                c = 0
                for k in dt.keys():
                    if d_sw.get(k,0) >= dt[k]:
                        c += 1
                if c == len(dt.keys()):
                    return s[start:end]
                
        
        return ""

class solution:
    def minWindow(self, s:str, t:str) -> str:


        

s = "bbaa"
t = "aba"
so = Solution()
print(so.minWindow(s,t))