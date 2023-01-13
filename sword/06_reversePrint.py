# -*- coding: utf-8 -*-
'''
# Created on 01-06-23 09:51
# @Filename: 06_reversePrint.py
# @Desp: 来源于https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

#  

# 示例 1：

# 输入：head = [1,3,2]
# 输出：[2,3,1]
#  

# 限制：

# 0 <= 链表长度 <= 10000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]