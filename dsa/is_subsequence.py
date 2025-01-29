"""
check whether given string is a subsequence of other string or not
"""
def is_subsequence(str1, str2):
    i,j = 0, 0
    while i<len(str1) and j<len(str2):
        if str1[i] == str2[j]:
            i+=1
        j+=1
    return i == len(str1)


str1 = "abc"
str2 = "ahbdcw"
print(is_subsequence(str1, str2))
