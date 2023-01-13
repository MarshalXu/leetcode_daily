# -*- coding: utf-8 -*-
'''
# Created on 01-11-23 13:56
# @Filename: 14_longestCommonPrefix.py
# @Desp: 来源于https://leetcode.cn/problems/longest-common-prefix
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"

# 示例 2：
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。

# 提示：

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        ss = list(map(set, zip(*strs))) #把每个字符串当成一个list，然后把整个字符串list当成一个二维list，然后zip压缩
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res