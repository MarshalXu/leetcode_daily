# -*- coding: utf-8 -*-
'''
# Created on 01-09-23 15:32
# @Filename: 2018_placeWordInCrossword.py
# @Desp: 来源于https://leetcode.cn/problems/check-if-word-can-be-placed-in-crossword
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 给你一个 m x n 的矩阵 board ，它代表一个填字游戏 当前 的状态。填字游戏格子中包含小写英文字母（已填入的单词），表示 空 格的 ' ' 和表示 障碍 格子的 '#' 。
# 如果满足以下条件，那么我们可以 水平 （从左到右 或者 从右到左）或 竖直 （从上到下 或者 从下到上）填入一个单词：
# 该单词不占据任何 '#' 对应的格子。
# 每个字母对应的格子要么是 ' ' （空格）要么与 board 中已有字母 匹配 。
# 如果单词是 水平 放置的，那么该单词左边和右边 相邻 格子不能为 ' ' 或小写英文字母。
# 如果单词是 竖直 放置的，那么该单词上边和下边 相邻 格子不能为 ' ' 或小写英文字母。
# 给你一个字符串 word ，如果 word 可以被放入 board 中，请你返回 true ，否则请返回 false 。


# 示例 1：
# 输入：board = [
# ["#", " ", "#"], 
# [" ", " ", "#"], 
# ["#", "c", " "]], 
# word = "abc"
# 输出：true
# 解释：单词 "abc" 可以如上图放置（从上往下）。

# 示例 2：
# 输入：board = [
# [" ", "#", "a"], 
# [" ", "#", "c"], 
# [" ", "#", "a"]], word = "ac"
# 输出：false
# 解释：无法放置单词，因为放置该单词后上方或者下方相邻格会有空格。

# 示例 3：
# 输入：board = [
# ["#", " ", "#"], 
# [" ", " ", "#"], 
# ["#", " ", "c"]], word = "ca"
# 输出：true
# 解释：单词 "ca" 可以如上图放置（从右到左）。

# 提示：
# m == board.length
# n == board[i].length
# 1 <= m * n <= 2 * 10^5
# board[i][j] 可能为 ' ' ，'#' 或者一个小写英文字母。
# 1 <= word.length <= max(m, n)
# word 只包含小写英文字母。


#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution: 

    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        mr = len(board)
        if mr == 0:
            return False
        mc = len(board[0])
        cols = [[row[i] for row in board] for i in range(mc)]
        print(cols)
        for row in board:
            row = "".join(row).spit("#")
            for item in row:
                for i in range(len(item)):
                    if item[i] == " " or item[i] == word[i]:


                        
b = [["#"," ","#"],[" "," ","#"],["#","c"," "]]
w = "abc"

s = Solution()
print(s.placeWordInCrossword(b,w))
from itertools import chain

class Solution: 
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        match = lambda x, y: all(a in [' ', b] for a, b in zip(x, y))
        for row in chain(board, zip(*board)):
            for ss in ''.join(row).split('#'):
                if len(ss) == len(word) and (match(ss, word) or match(ss, word[::-1])):
                    return True
        return False

