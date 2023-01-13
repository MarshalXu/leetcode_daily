# -*- coding: utf-8 -*-
'''
# Created on 12-26-22 11:12
# @Filename: 383_canConstruct.py
# @Desp: 来源于https://leetcode.cn/problems/ransom-note
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 如果可以，返回 true ；否则返回 false 。
# magazine 中的每个字符只能在 ransomNote 中使用一次。

# 示例 1：
# 输入：ransomNote = "a", magazine = "b"
# 输出：false

# 示例 2：
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false

# 示例 3：
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true

# 提示：
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote 和 magazine 由小写英文字母组成

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = set(list(ransomNote))
        m = set(list(magazine))

        b = m.intersection(r)

        if r == b:
            rc = Counter(ransomNote)
            mc = Counter(magazine)
            for k,v in rc.items():
                if mc.get(k,0) < v:
                    return False
        else:
            return False
            
        return True

r = "aa"
m = "ab"

s = Solution()
print(s.canConstruct(r,m))