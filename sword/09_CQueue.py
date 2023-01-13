# -*- coding: utf-8 -*-
'''
# Created on 01-05-23 09:21
# @Filename: 09_CQueue.py
# @Desp: 来源于https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

#  

# 示例 1：

# 输入：
# ["CQueue","appendTail","deleteHead","deleteHead","deleteHead"]
# [[],[3],[],[],[]]
# 输出：[null,null,3,-1,-1]
# 示例 2：

# 输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
# 提示：

# 1 <= values <= 10000
# 最多会对 appendTail、deleteHead 进行 10000 次调用

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

class CQueue:

    def __init__(self):
        self.stack = []
        return None

    def appendTail(self, value: int) -> None:
        self.stack.append(value)
        return None

    def deleteHead(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack.pop(0)
        


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
