# -*- coding: utf-8 -*-
'''
# Created on 12-27-22 10:54
# @Filename: 21_mergeTwoLists.py
# @Desp: 来源于https://leetcode.cn/problems/merge-two-sorted-lists
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# 示例 1：
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]

# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]

# 示例 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]

# 提示：

# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List,Optional,

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         res = ListNode(None)
#         node = res
#         while list1 and list2:
#             if list1.val < list2.val:
#                 node.next,list1 = list1,list1.next
#             else:
#                 node.next,list2 = list2,list2.next
#             node = node.next
#         if list1: # 看看哪个还剩下
#             node.next = list1
#         else:
#             node.next = list2
#         return res.next

    

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个空的指针头
        res = ListNode(None)
        node = res
        while list1 and list2:
            if list1.val < list2.val:
                node.next,list1 = list1,list1.next
            else:
                node.next,list2 = list2,list2.next
            node = node.next
        
        if list1:
            node.next = list1
        else:
            node.next = list2
        
        return res.next 