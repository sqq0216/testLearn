#在一个字符串中寻找另一个字符串出现的位置

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        
        if ln == 0:
            return 0
        if lh == 0 or lh < ln:
            return -1
        i = 0
        while(i<=lh-ln):
            if haystack[i] == needle[0]:
                if haystack[i:i+ln] == needle:
                    return i
                else:
                    i = i+1
            else:
                i += 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    result = sol.strStr('helo', 'll')
    print(result)

           