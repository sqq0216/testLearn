#判断是否为回文数

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        else:
            new_x = str(x)
            length = len(new_x)
            res = ""
            for i in range(0, length):
                print(i)
                if(new_x[i] == new_x[length-i-1]):
                    print(new_x[i], new_x[length-1-i])
                    continue
                else:
                    return False
                    break
            return True
                

    
if __name__ == "__main__":           
    mm = Solution()
    ss = mm.isPalindrome(1231)
    if(ss):
        print("是回文数")
    else:
        print('不是回文数')