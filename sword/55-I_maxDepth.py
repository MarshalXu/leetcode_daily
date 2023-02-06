# -*- coding: utf-8 -*-
'''
# Created on 02-02-23 13:39
# @Filename: 55-I_maxDepth.py
# @Desp: 来源于https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

# 例如：
# 给定二叉树 [3,9,20,null,null,15,7]，
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# 提示：

# 节点总数 <= 10000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import math
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        return 0 if root == None else max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1