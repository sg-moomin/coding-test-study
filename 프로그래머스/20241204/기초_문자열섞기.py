# https://school.programmers.co.kr/learn/courses/30/lessons/181942
def solution(str1, str2):
    a, b = len(str1), len(str2)
    result = ""
    for i in range(0, a):
        result += str1[i] + str2[i]
    
    return result


# 다른 풀이 
def solution(str1, str2):
    res=''
    for s1,s2 in zip(str1,str2):
        res+=s1+s2
    return res