# -*- coding: utf-8 -*-
'''
# Created on 01-03-23 14:11
# @Filename: frog.py
# @Desp: 
# @software: vscode
# @author: xuchang0514@sina.com
'''
#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from loguru import logger
logger.configure(handlers=[{"sink": sys.stderr, "level": "DEBUG"}])


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1] % 1000000007

if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.numWays(n))