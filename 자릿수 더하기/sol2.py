def solution(n):
    answer = 0

    for i in str(n):
        answer = answer + int(i)
    
    return answer

print(solution(1234))
pritn(solution(930211))