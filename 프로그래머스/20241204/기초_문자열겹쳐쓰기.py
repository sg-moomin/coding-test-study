# https://school.programmers.co.kr/learn/courses/30/lessons/181943
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    # return my_string.replace(my_string[s:s+len(overwrite_string)], overwrite_string)

# test 
str = 'Program29b8UYP'
str2 = 'merS123'
print(str.replace(str[7:7+len(str2)], str2))


# 다른 풀이 
def solution(m, o, s):
    return m[:s]+o+m[len(o)+s:]