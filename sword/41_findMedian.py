# -*- coding: utf-8 -*-
'''
# Created on 02-01-23 11:45
# @Filename: 41_findMedian.py
# @Desp: 来源于https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

# 例如，
# [2,3,4] 的中位数是 3
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 设计一个支持以下两种操作的数据结构：

# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。

# 示例 1：
# 输入：
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]

# 示例 2：
# 输入：
# ["MedianFinder","addNum","findMedian","addNum","findMedian"]
# [[],[2],[],[3],[]]
# 输出：[null,null,2.00000,null,2.50000]

# 限制：
# 最多会对 addNum、findMedian 进行 50000 次调用。


#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
from math import floor,ceil
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = []


    def addNum(self, num: int) -> None:
        if isinstance(num,int):
            self.d.append(num)
            self.d.sort()

    def findMedian(self) -> float:
        n = len(self.d)

        return (self.d[floor(n/2)] + self.d[ceil(n/2)]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
from heapq import *

class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
