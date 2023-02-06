# -*- coding: utf-8 -*-
'''
# Created on 02-01-23 10:35
# @Filename: 40_getLeastNumbers.py
# @Desp: 来源于https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

# 示例 1：
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]

# 示例 2：
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]

# 限制：
# 0 <= k <= arr.length <= 10000
# 0 <= arr[i] <= 10000

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# 偷懒方法 直接内置排序
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

# 利用双向列表实现
from collections import deque
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        q = deque()
        for a in arr:
            if len(q) == 0:
                q.append(a)
            elif len(q) < k:
                if a >= q[-1]:
                    q.append(a)
                else:
                    q.appendleft(a)
            else:
                
