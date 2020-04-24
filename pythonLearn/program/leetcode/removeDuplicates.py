#删除排序数组中的重复元素
#从后面开始判断：如果和前一个元素值一样，则删除后一个（当前元素）
#为什么从后面开始： 删除元素不会影响前面元素的索引
from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums))[::-1]:
            # print(i)
            if i-1 != -1:
                if nums[i-1] == nums[i]:
                    del nums[i] 
            # print(nums)
        # print(nums)
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    ls = [1, 1, 2]
    result = sol.removeDuplicates(ls)
    print(result)