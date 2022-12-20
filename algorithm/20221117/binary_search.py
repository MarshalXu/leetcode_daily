"""
二分查找
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target,如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1


提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。

"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        # mid = 0
        while left < right:
            mid = (right + left) // 2

            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                right = mid
                continue
            if target > nums[mid]:
                left = mid + 1
                continue
        return -1
    
if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = 2
    print(s.search(nums,target))



doubles = [4.8,w1,w2,w3,w4]
double1 = [x1,x2,x3,x4]
res = 0.0
for i in range(0,len(doubles) -1):
    if i == 0:
        res += doubles[i]
    else:
        res += doubles[i] * double1[i-1]