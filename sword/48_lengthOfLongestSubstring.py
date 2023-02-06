# -*- coding: utf-8 -*-
'''
# Created on 01-28-23 13:47
# @Filename: 48_lengthOfLongestSubstring.py
# @Desp: 来源于https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 提示：

# s.length <= 40000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        res = 0
        c = {}

        for window in range(n,0,-1):
            for start in range(n):
                end = start + window
                if end <= n:
                    piece = s[start:end]
                    c = dict(zip(piece,[1 for _ in range(len(piece))]))
                    if (a := len(piece)) == (b:= len(c.keys())):
                        res = max(a,res)
                    
        return res

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:0
#         book = set()
#         i = ans = 0
#         for j, c in enumerate(s):
#             while c in book:
#                 book.discard(s[i])
#                 i += 1
#             book.add(c)
#             if (d := j - i + 1) > ans:
#                 ans = d
#         return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res

s = "dvdf"
so = Solution()
print(so.lengthOfLongestSubstring(s))



