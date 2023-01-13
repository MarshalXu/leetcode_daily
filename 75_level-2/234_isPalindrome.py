# -*- coding: utf-8 -*-
'''
# Created on 01-12-23 14:24
# @Filename: 234_isPalindrome.py
# @Desp: 来源于https://leetcode.cn/problems/palindrome-linked-list
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# 示例 1：
# 输入：head = [1,2,2,1]
# 输出：true

# 示例 2：
# 输入：head = [1,2]
# 输出：false

# 提示：

# 链表中节点数目在范围[1, 105] 内
# 0 <= Node.val <= 9

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List,Optional
import collections
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#  正反向记录下来的头铁写法
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = collections.deque()
        forward = []
        while head:
            reverse.appendleft(head.val)
            forward.append(head.val)
            head = head.next
        for i in list(map(set,zip(reverse,forward))):
            if len(i) > 1:
                return False
        return True
#  和上面的没啥区别。
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head
        stack = []

        while first:
            stack.append(first.val)
            first = first.next
        
        while second:
            if stack.pop() != second.val:
                return False
            second = second.next
        return True

#  双指针
#  这个思路的关键就是 快指针的速度是慢指针的两倍 当快指针走到最后的时候慢指针就是在中间
# TODO
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head

        while first:
            