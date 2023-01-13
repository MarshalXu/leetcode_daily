# -*- coding: utf-8 -*-
'''
# Created on 01-06-23 09:55
# @Filename: 24_reverseList.py
# @Desp: 来源于https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

#  

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#  

# 限制：

# 0 <= 节点个数 <= 5000

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
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
