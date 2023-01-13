# -*- coding: utf-8 -*-
'''
# Created on 01-10-23 10:33
# @Filename: 32-I_levelOrder.py
# @Desp: 来源于https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
#lib moduls:
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
#  

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：

# [3,9,20,15,7]
#  

# 提示：

# 节点总数 <= 1000

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

    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        que = collections.deque() #用这个deque 他是实现了一个双向list 可以实现双向时间复杂度O(1)的pop和append
        
        que.append(root)

        while que:
            node = que.popleft()
            res.append(node.val)

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)


        return res
