# -*- coding: utf-8 -*-
'''
# Created on 01-09-23 10:20
# @Filename: 05_replaceSpace.py
# @Desp: 来源于https://leetcode.cn/problems/ti-huan-kong-ge-lcof
# @software: vscode
# @author: xuchang0514@sina.com
# '''

# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

# 示例 1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

# 限制：

# 0 <= s 的长度 <= 10000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")

class Solution:
    def replaceSpace(self, s: str) -> str:
        return "%20".join(s.split(" "))