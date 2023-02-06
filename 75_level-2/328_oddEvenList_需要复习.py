# -*- coding: utf-8 -*-
'''
# Created on 01-13-23 14:51
# @Filename: 328_oddEvenList.py
# @Desp: 来源于https://leetcode.cn/problems/odd-even-linked-list
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
# 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
# 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
# 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。

# 示例 1:
# 输入: head = [1,2,3,4,5]
# 输出: [1,3,5,2,4]

# 示例 2:
# 输入: head = [2,1,3,5,6,4,7]
# 输出: [2,3,6,7,1,5,4]

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List,Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        tail_head = ListNode(0)
        count = 1
        while head:
            if count == 1:
                if head.val % 2 == 0:  # 如果第一个节点是偶数 
                     return
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
