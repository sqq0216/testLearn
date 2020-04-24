def getCommonStrLength(s1,s2):
    len1 = len(s1)
    res = []
    i = 0
    while i < len1:
        if s1[i] in s2:
            count = s2.count(s1[i])
            s2_sol = s2
            while count > 0 :
                j = len1-i
                while j > 0:
                    if s2[s2_sol.index(s1[i]):s2_sol.index(s1[i])+j] == s1[i:i+j]:
                        res.append(j)
                        break
                    j -= 1
                count -= 1
                s2_sol = s2_sol[s2_sol.index(s1[i])+1:]
        i += 1
    if len(res) == 0:
        return 0
    return max(res)

s1 = 'bacefaebcdfabfaadebdaacabbdabcfffbdcebaabecefddfaceeebaeabebbad'
s2 = 'dedcecfbbbecaffedcedbadadbbfaafcafdd'
print(getCommonStrLength(s2,s1))