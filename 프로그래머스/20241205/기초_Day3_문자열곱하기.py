# https://school.programmers.co.kr/learn/courses/30/lessons/181940

def solution(my_string, k):
    answer = ''
    for i in range(0, k):
        answer += my_string
    
    return answer

# 다른 풀이
def solution(my_string, k):
    return my_string*k