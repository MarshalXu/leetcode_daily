# -*- coding: utf-8 -*-
'''
# Created on 01-28-23 16:31
# @Filename: 22_getKthFromEnd.py
# @Desp: 来源于https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

#  

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 k = 2.

# 返回链表 4->5.


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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = ListNode(0)
        fast.next = head
        slow.next = head
        for i in range(k):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        return slow