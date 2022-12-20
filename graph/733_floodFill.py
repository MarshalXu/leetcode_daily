# -*- coding: utf-8 -*-
'''
# Created on 09-17-22 17:39
# @Filename: 733_floodFill.py
# @Desp: 
# @software: vscode
# @author: xuchang0514@sina.com
'''
# 链接：https://leetcode.cn/problems/flood-fill
#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# 有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。

# 你也被给予三个整数 sr ,  sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。

# 为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上 像素值与初始坐标相同的相连像素点，……，重复该过程。
# 将所有有记录的像素点的颜色值改为 newColor 。

# 最后返回 经过上色渲染后的图像 。

# 示例 1:
# 输入: image = [[1,1,1],[1,1,0],[1,0,1]]，sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析: 在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。
# 示例 2:

# 输入: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# 输出: [[2,2,2],[2,2,2]]
# 
# 提示:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 2^16
# 0 <= sr < m
# 0 <= sc < n

a = \
    [
    [1,1,1],
    [1,1,0],
    [1,0,1]
    ]

b = [
    [2,2,2],
    [2,2,0],
    [2,0,1]
    ]

class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def __fill(r,c):
            #判断一个点周围是否联通，然后填充
            if r < 0 or c < 0 or r > m-1 or c > n-1: 
                return 
                
            if image[r][c] == start:
                image[r][c] = color
                __fill(r-1,c)
                __fill(r+1,c)
                __fill(r,c-1)
                __fill(r,c+1)
            return
        #与初始点 的 数值相同的才算相邻 其他的不算
        start = image[sr][sc]
        m,n = len(image), len(image[0])

        if start == color:
            return image

        __fill(sr,sc)

        return image

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0

s = Solution()
print(s.floodFill(image,sr,sc,color))