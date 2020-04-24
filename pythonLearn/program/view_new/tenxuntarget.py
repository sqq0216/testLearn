def combinationSum(candidates,target):
        result = []
        def dfs(temp,res):
            nonlocal target
            if temp > target:#剪枝一:当前的总值大于目标值
                return
            if temp == target:#当前值和目标值相等的时候,保存当前结果,并返回
                result.append(res[:])
                return
            for i in candidates:
                if res and res[-1] > i:#防止重复的方法是,不让其找在当前元素以前的元素
                    continue
                dfs(temp + i, res + [i])
        dfs(0, [])
        return result
def solut(l,tar):
    res = []
    def sol(li,target):
    for i in li:
        if target - i in li and li.count(i) == 1:
            print([i,target-i])
        return sol(li[1:],target)
li = [1,2,3,4,5,6,7,8]
print(combinationSum(li,8))