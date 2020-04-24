#最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = []
        len_list = len(strs)
        if len_list == 0:
            return "".join(res)
        elif len_list == 1:
            return "".join(strs)
        else:
            list_len = []
            for i in range(0, len(strs)):
                list_len.append(len(strs[i]))
            #print(list_len)
            minNum = min(list_len)
            for j in range(0, minNum):
                for k in range(0, len(strs)-1):
                    if strs[k][j] == strs[k+1][j]:
                        continue
                    else:
                        break
                if strs[k][j] == strs[k+1][j]:
                    res.append(strs[0][j])
                else:
                    break
            #print(res)
            res_str = "".join(res)
            return str(res_str)
if __name__ == "__main__":

    sol = Solution()
    list1 = ["a"]
    print(sol.longestCommonPrefix(list1))