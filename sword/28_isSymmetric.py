# -*- coding: utf-8 -*-
'''
# Created on 01-11-23 10:46
# @Filename: 28_isSymmetric.py
# @Desp: 来源于https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# 示例 1：
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true

# 示例 2：
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false

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
    def isSymmetric(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """
            if root == None:
                return True
            return self.helper(root.left,root.right)
        
    def helper(self,node1,node2):
        # 若两个节点非空且数值相同，则用递归判断两个节点的子节点是否相同
        if node1 != None and node2 != None and node1.val == node2.val:
            return self.helper(node1.left,node2.right) and self.helper(node1.right,node2.left)
        # 边界条件，若两个节点均为空，则返回True
        if node1 == None and node2 == None:
            return True
        
        return False
