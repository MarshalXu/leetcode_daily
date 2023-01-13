# -*- coding: utf-8 -*-
'''
# Created on 01-09-23 17:03
# @Filename: 1540_canConvertString.py
# @Desp: 来源于https://leetcode.cn/problems/can-convert-string-in-k-moves
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给你两个字符串 s 和 t ，你的目标是在 k 次操作以内把字符串 s 转变成 t 。
# 在第 i 次操作时（1 <= i <= k），你可以选择进行如下操作：
#   1.选择字符串 s 中满足 1 <= j <= s.length 且之前未被选过的任意下标 j （下标从 1 开始），并将此位置的字符切换 i 次。
#   2.不进行任何操作。
# 切换 1 个字符的意思是用字母表中该字母的下一个字母替换它（字母表环状接起来，所以 'z' 切换后会变成 'a'）。第 i 次操作意味着该字符应切换 i 次
# 请记住任意一个下标 j 最多只能被操作 1 次。
# 如果在不超过 k 次操作内可以把字符串 s 转变成 t ，那么请你返回 true ，否则请你返回 false 。


# 示例 1：
# 输入：s = "input", t = "ouput", k = 9
# 输出：true
# 解释：第 6 次操作时，我们将 'i' 切换 6 次得到 'o' 。第 7 次操作时，我们将 'n' 切换 7 次得到 'u' 。

# 示例 2：
# 输入：s = "abc", t = "bcd", k = 10
# 输出：false
# 解释：我们需要将每个字符切换 1 次才能得到 t 。我们可以在第 1 次操作时将 'a' 切换成 'b' ，但另外 2 个字母在剩余操作中无法再转变为 t 中对应字母。

# 示例 3：
# 输入：s = "aab", t = "bbb", k = 27
# 输出：true
# 解释：第 1 次操作时，我们将第一个 'a' 切换 1 次得到 'b' 。在第 27 次操作时，我们将第二个字母 'a' 切换 27 次得到 'b' 。

# 提示：

# 1 <= s.length, t.length <= 10^5
# 0 <= k <= 10^9
# s 和 t 只包含小写英文字母。

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

#t 是目标字符  s是原始字符

class Solution:

    def __init__(self) -> None:
        self.table = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.idx_dict = dict([(x,self.table.index(x)) for x in self.table])
        
        # self.distance = lambda x,y: self.idx_dict.get(y) - self.idx_dict.get(x) if self.

    def distance(self,x,y):
        if x == y:
            return 0
        x_idx = self.idx_dict.get(x)
        y_idx = self.idx_dict.get(y)
        if y_idx >= x_idx:
            dis = y_idx - x_idx
        else:
            dis = min(26+abs(y_idx-x_idx),26-min(y_idx,x_idx)+min(y_idx,x_idx))
        return dis
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        sn = len(s) 
        st = len(t)
        if sn != st:
            return False
        used = {}
        step = 0
        for i in range(sn):
            d = self.distance(s[i],t[i])
            if d == 0 :
                continue
            if used.get(d,0) == 0:
                step += d
                used[d] = 1
            else: 
                d += 26
                if used.get(d,0) == 0:
                    step += d
                    used[d] = 1
                else:
                    return False
            if d > k:
                return False

        if step <= sum([x for x in range(1,k+1)]):
            return True
        else:
            return False
q=[
"hxvcyvn",
"xbzgtou",
28
]
so = Solution()
s,t,k = q[0],q[1],q[2]
print(so.canConvertString(s,t,k))
from collections import Counter
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        book = Counter(val if val > 0 else 26 + val for x, y in zip(s, t) if (val := ord(y) - ord(x)))
        return all(26 * (cnt - 1) + diff <= k for diff, cnt in book.items())