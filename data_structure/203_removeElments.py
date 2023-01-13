# -*- coding: utf-8 -*-
'''
# Created on 12-27-22 13:52
# @Filename: 203_removeElments.py
# @Desp: 来源于https://leetcode.cn/problems/remove-linked-list-elements
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# 示例 1：
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]

# 示例 2：
# 输入：head = [], val = 1
# 输出：[]

# 示例 3：
# 输入：head = [7,7,7,7], val = 7
# 输出：[]

# 提示：
# 列表中的节点数目在范围 [0, 104] 内
# 1 <= Node.val <= 50
# 0 <= val <= 50

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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #创建一个虚拟的头节点 指向head
        pre_node = ListNode(next = head)
        node = pre_node
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return pre_node.next