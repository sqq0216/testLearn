from typing import List 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None:
            return 0
        elif target in nums:
            return nums.index(target)
        else:
            i = 0
            while i < len(nums) :
                if target > nums[i]:
                    i += 1
                    continue
                else:
                    return i
            return i
            


if __name__ == "__main__":
    list = [1,3,5,6]
    tar = 5
    sol = Solution()
    res = sol.searchInsert(list, tar)
    print(res)