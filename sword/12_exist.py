# -*- coding: utf-8 -*-
'''
# Created on 01-29-23 14:03
# @Filename: 12_exist.py
# @Desp: 来源于https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）

# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true

# 示例 2：
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false

# 提示：
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class Solution:

    def walk(self,r,c,w_idx,word):
        mr = len(self.board)
        mc = len(self.board[0])
        if self.board[r][c] == word[w_idx]:
            if w_idx == len(word) - 1:
                return True
            self.board[r][c] = 0
            w_idx += 1
            for r1,c1 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0 <= r1 < mr and 0 <= c1 < mc and w_idx <= len(word) - 1:
                    self.walk(r1,c1,w_idx,word)
        else:
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        mr = len(board)
        if mr == 0:
            return False
        mc = len(board[0])
        if mr * mc < len(word):
            return False
        res = False

        for r in range(mr):
            for c in range(mc):
                self.board = board
                res = self.walk(r,c,0,word)
                if res:
                    return res
        return False if res == None else True


b = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]

word = "ABCB"

s = Solution()

print(s.exist(b,word))


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1: 
                return True

            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1) 
            board[i][j] = word[k]

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): 
                    return True
        return False
