# https://school.programmers.co.kr/learn/courses/30/lessons/181939
a = 9
b = 91
print(max(str(a) + str(b), str(b) + str(a)))

def solution(a, b):
    return int(max(str(a) + str(b), str(b) + str(a)))