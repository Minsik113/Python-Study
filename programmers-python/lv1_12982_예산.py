'''
d가 10만까지니까 정렬 O(nlon) = 10만 x 약17 => 1초에 200만연산이니 정렬가능

그리드 문제임
작은애들부터 주면됨

'''
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget - i >= 0: # 예산줄 수 있으면 
            answer += 1 # 줄 수 있으니 1증가
            budget -= i  # 예산을 준 만큼 뺌
        else:
            break
    return answer