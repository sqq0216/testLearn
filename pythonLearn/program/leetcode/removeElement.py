#移除元素
#关键：从列表元素最后开始遍历，判断并处理列表

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums))[::-1]:
            if i != -1:
                if nums[i] == val:
                    del nums[i]
        return len(nums)