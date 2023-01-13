# -*- coding: utf-8 -*-
'''
# Created on 01-11-23 14:47
# @Filename: 43_multiply.py
# @Desp: 来源于https://leetcode.cn/problems/multiply-strings
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

#  

# 示例 1:

# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:

# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#  

# 提示：

# 1 <= num1.length, num2.length <= 200
# num1 和 num2 只能由数字组成。
# num1 和 num2 都不包含任何前导零，除了数字0本身。

#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List
class Solution:

    def __init__(self) -> None:
        
        self.base = ord("0")
    
    def str2int(self,x:str):
        """将一个数字字符串转为int"""
        res = 0
        for i,t in enumerate(x[::-1]):
            res += 10**i * (ord(t) - self.base)
        return res

    def multiply(self, num1: str, num2: str) -> str:
        # 0 的ascii 为48
        # chr ascii->string
        # ord string -> ascii
        num1,num2 = self.str2int(num1),self.str2int(num2)
        return str(num1*num2)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = self.addStrings(ans, curr)
        
        return ans
    
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])

