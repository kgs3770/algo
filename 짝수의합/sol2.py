def solution(n):
    answer = 0

    for i in range(1, n+1, 2):
            answer += 1
            # answer += i
    
    return answer


print(solution(10))
print(solution(4))