# -*- coding: utf-8 -*-
'''
# Created on 01-10-23 10:58
# @Filename: 32-II_levelOrder.py
# @Desp: 来源于https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
#   [20,9],
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
        line = 0
        while q:

            dont_reverse = line % 2
            while q:
                cur = q.pop(0)

                if cur.left:
                    this_row.append(cur.left)
                if cur.right:
                    this_row.append(cur.right)

            if not this_row:
                return res
            q += this_row
            if dont_reverse:
                res.append([e.val for e in this_row])
            else:
                res.append([e.val for e in this_row[::-1]])
            this_row = []
            line += 1
        return res


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
print(s.levelOrder(root))
