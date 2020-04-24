# 搜索旋转排序数组：假设按照升序排序的数组在预先未知的某个点上进行了旋转。( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。搜索一个给定的目标值 target，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。你可以假设数组中不存在重复的元素。算法时间复杂度要求是 O(log n) 级别。
# 思路：二分法：
def search(li,target):
    if len(li)==0:
        return -1
    left,right = 0,len(li)-1
    while left<right:
        mid = left+(right-left)//2
        if li[mid] == target:
            return mid
        if target == li[left]:
            return left
        if target == li[right]:
            return right
        elif li[left] < li[mid]:
            
            if target > li[left] and target < li[mid]:
                right = mid - 1
                left = left+1
            else:
                left = mid+1   
        
    return -1
li = [5,6,1,2,3,4]
t = 6
print(search(li,t))
