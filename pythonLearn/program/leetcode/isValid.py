#有效括号

#利用栈的特点，对括号匹配是否正确进行判断
#左括号为键，执行进栈，右括号为值，与栈顶的键匹配并弹栈
class Solution:
    def isValid(self, s: str) -> bool:
        # base = {"(":0, ")":0, "[":0, "]":0, "{":0, "}":0}
        # for i in s:
        #     base[i] += 1
        # print(base)
        # if base["("] == base[")"] and base["["] == base["]"] and base["{"] == base["}"]:
        #     return True
        # else:
        #     return False

        #‘？’ 防止栈空无法弹栈
        dic = {'{': '}',  '[': ']', '(': ')', '?':'?'}
        stack = ['?']
        for c in s:
            if c in dic: 
                stack.append(c)
            elif dic[stack.pop()] != c: 
                return False 
        return len(stack) == 1


if __name__ == "__main__":
    sol = Solution()
    res = sol.isValid("(){")
    if(res):
        print("有效")
    else:
        print("无效")
    