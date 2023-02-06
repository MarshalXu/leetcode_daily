# -*- coding: utf-8 -*-
'''
# Created on 01-28-23 16:52
# @Filename: 04_mergeTwoLists.py
# @Desp: 来源于https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

# 示例1：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 限制：

# 0 <= 链表长度 <= 1000

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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = dummy = ListNode(0)
        if not l1:
            return l2
        if not l2:
            return l1
        
        while 1:

            if not (l1 and l2):
                if not l1:
                    dummy.next = l2
                
                if not l2:
                    dummy.next = l1
                
                break

            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            

            dummy = dummy.next

        return h.next