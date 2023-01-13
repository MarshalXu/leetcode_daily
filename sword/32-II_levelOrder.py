# -*- coding: utf-8 -*-
'''
# Created on 01-10-23 10:58
# @Filename: 32-II_levelOrder.py
# @Desp: 来源于https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  

# 提示：

# 节点总数 <= 1000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, q, this_row = [[root.val]], [root], []
        while q:
            while q:
                cur = q.pop(0)
                if cur.left:
                    this_row.append(cur.left)
                if cur.right:
                    this_row.append(cur.right)
            if not this_row:
                return res
            q += this_row
            res.append([e.val for e in this_row])
            this_row = []
        return res