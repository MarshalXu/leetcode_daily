# -*- coding: utf-8 -*-
'''
# Created on 01-12-23 13:41
# @Filename: 19_removeNthFromEnd.py
# @Desp: 来源于https://leetcode.cn/problems/remove-nth-node-from-end-of-list
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 

# 示例 1：

# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]

# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]

# 示例 3：
# 输入：head = [1,2], n = 1
# 输出：[1]

# 提示：
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#  快慢指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # 这是一个预备node 指向head的开始
        first = head
        second = dummy
        for i in range(n): #先让快指针先走 走到n的位置
            first = first.next

        while first: #一直走 直到快指针走到头的时候
            first = first.next
            second = second.next
        
        second.next = second.next.next #此时慢指针正好在n的位置 删除 
        return dummy.next
