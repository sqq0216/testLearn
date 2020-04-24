#罗马数字转整数

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         #print(s)
#         if len(s):
#             li=['I','V','X','L','C','D','M']
#             attr = [1,5,10,50,100,500,1000]
#             res = 0
#             i = 0
#             while i < len(s):
#                 if res < 4000:
#                     index = li.index(s[i])
#                     if i < len(s)-1:
#                         next = s[i+1] 
#                         #print(next)
#                         if s[i] == 'I' :
#                             if next == 'V':
#                                 res += 4
#                                 i += 2
#                                 continue
#                             elif next == 'X':
#                                 res += 9
#                                 i += 2
#                                 continue
#                         elif s[i] == 'X':
#                             if next == 'L':
#                                 res += 40
#                                 i += 2
#                                 continue
#                             elif next == 'C':
#                                 res += 90 
#                                 i += 2
#                                 continue              
#                         elif i == 'C':
#                             if next == 'D':
#                                 res += 400
#                                 i += 2
#                                 continue
#                             elif next == 'M':
#                                 res += 900
#                                 i += 2
#                                 continue
#                         #print(i)
#                     res += attr[index]
#                 else:
#                     break
#                     print('请输入1到3999内的数字：')                    
#         else:
#             print('请输入非0 数字：')
#         return res
       
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        i = 0
        res = 0
        while i < len(s)-1:
            if dict[s[i]] < dict[s[i+1]]:
                res += dict[s[i+1]] - dict[s[i]]
                i += 2
            else:
                res += dict[s[i]]
                #print(dict[s[i]])
                i += 1
        if i < len(s):
            res += dict[s[len(s)-1]]
        if 0 < res < 4000:
            return res
        else:
            print('请输入0-4000内的数字：')
            return None

if __name__ == "__main__":
    test = Solution()
    print(test.romanToInt('DCXXI'))
    #print(test)
    