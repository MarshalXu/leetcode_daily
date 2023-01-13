# -*- coding: utf-8 -*-
'''
# Created on 01-11-23 10:11
# @Filename: 27_mirrorTree.py
# @Desp: 来源于https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

# 例如输入：
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

# 镜像输出：
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


# 示例 1：
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]

# 限制：
# 0 <= 节点个数 <= 1000

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
import collections
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        que = collections.deque()
        que.append(root)
        res = []
        while que:
            node = que.popleft()
            res.append(node.val)
            if node.right:
                que.append(node.right)
            if node.left:
                que.append(node.left)
        
        return res

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left, root.right = right, left
        return root
