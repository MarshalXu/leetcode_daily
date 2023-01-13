# -*- coding: utf-8 -*-
'''
# Created on 01-09-23 10:25
# @Filename: 58_reverseLeftWords.py
# @Desp: 来源于https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

# 示例 1：
# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"

# 示例 2：
# 输入: s = "lrloseumgh", k = 6
# 输出: "umghlrlose"

# 限制：

# 1 <= k < s.length <= 10000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_len = len(s)
        if s_len == 1:
            return s
        r = n % s_len

        return s[r:] + s[:r]