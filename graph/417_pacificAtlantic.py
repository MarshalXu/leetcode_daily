# -*- coding: utf-8 -*-
'''
# Created on 12-22-22 14:45
# @Filename: 417_pacificAtlantic.py
# @Desp: 来源于https://leetcode.cn/problems/pacific-atlantic-water-flow
# @software: vscode
# @author: xuchang0514@sina.com
'''

# 有一个 m × n 的矩形岛屿，与 太平洋 和 大西洋 相邻。 “太平洋” 处于大陆的左边界和上边界，而 “大西洋” 处于大陆的右边界和下边界。
# 这个岛被分割成一个由若干方形单元格组成的网格。给定一个 m x n 的整数矩阵 heights ， heights[r][c] 表示坐标 (r, c) 上单元格 高于海平面的高度 。
# 岛上雨水较多，如果相邻单元格的高度 小于或等于 当前单元格的高度，雨水可以直接向北、南、东、西流向相邻单元格。水可以从海洋附近的任何单元格流入海洋。
# 返回网格坐标 result 的 2D 列表 ，其中 result[i] = [ri, ci] 表示雨水从单元格 (ri, ci) 流动 既可流向太平洋也可流向大西洋 。
#  

# 示例 1：
# 输入: heights = [
# [1,2,2,3,5],
# [3,2,3,4,4],
# [2,4,5,3,1],
# [6,7,1,4,5],
# [5,1,1,2,4]
# ]
# 输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# 示例 2：
# 输入: heights = [
# [2,1],
# [1,2]
# ]
# 输出: [[0,0],[0,1],[1,0],[1,1]]

# 提示：

# m == heights.length
# n == heights[r].length 
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

# 还没有搞定

#lib moduls:

import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List,Tuple,Set

class Solution:
    
    #向太平洋流 ↑ ←
    def _sprade_pac(self,r,c):
        height0 = self.heights[r][c]
        flag = 2
        for i,j in [[r-1,c],[r,c-1]]:
            if 0 <= i < self.mr and 0 <= j < self.mc:
                if height0 >= self.heights[i][j]:
                    self._sprade_pac(i,j)
                else:
                    flag -= 1
                
        if flag == 0:
            self._reach_pac = False

    #向大西洋流 ↓ →
    def _sprade_atl(self,r,c):
        height0 = self.heights[r][c]
        flag = 2
        for i,j in [[r+1,c],[r,c+1]]:
            if 0 <= i < self.mr and 0 <= j < self.mc:
                if height0 >= self.heights[i][j]:
                    self._sprade_atl(i,j)
                else:
                    flag -= 1
                
        if flag == 0:
            self._reach_atl = False


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.mr = len(heights)
        if self.mr == 0:
            return []
        self.mc = len(heights[0])

        self.heights = heights
        
        res = []

        for r in range(self.mr):
            for c in range(self.mc):

                self._reach_pac = True 
                self._reach_atl = True

                self._sprade_pac(r,c)
                self._sprade_atl(r,c)

                if self._reach_pac and self._reach_atl:
                    res.append([r,c])

        return res


# heights = [
# [1,2,2,3,5],
# [3,2,3,4,4],
# [2,4,5,3,1],
# [6,7,1,4,5],
# [5,1,1,2,4]
# ]
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# [[0, 4], [1, 3], [2, 2], [3, 0], [3, 1], [4, 0]]

heights = [
    [10,10,10],
    [10,1,10],
    [10,10,10]]
s = Solution()
[[10,10,10],[10,1,10],[10,10,10]]
print(s.pacificAtlantic(heights))


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def search(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set()
            def dfs(x: int, y: int):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)
            for x, y in starts:
                dfs(x, y)
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, search(pacific) & search(atlantic)))