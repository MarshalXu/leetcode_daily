# -*- coding: utf-8 -*-
'''
# Created on 01-05-23 09:52
# @Filename: 30_MinStack.py
# @Desp: 来源于https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

# 示例:

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#  

# 提示：

# 各函数的调用总次数不超过 20000 次

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:

        return self.stack[-1]

    def min(self) -> int:
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]


["MinStack","push","push","push","min","pop","top","min"]
[[],[-2],[0],[-3],[],[],[],[]]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
