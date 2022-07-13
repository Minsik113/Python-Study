'''
1~1000이니까 O(n^2)까지 가능
1. 일단 3개의 조합을 다 구하긴해야함 
2. 중복값이 나올 수 있음 -> 튜플에 넣자
3. 1~1000인 애들중 소수인것들 다 저장
4. 2번에서 나온결과가 3에 있는지 카운트
'''
from itertools import combinations
import math

def solution(nums):
    answer = 0
    
    set_arr = []
    for i in list(combinations(nums,3)): # 1
        set_arr.append(sum(i)) # 2
    # print(set_arr)
    
    max_nums = max(set_arr)
    flag = [True for i in range(max_nums+1)] 
    flag[0] = False # 0소수아님
    flag[1] = False # 소수아님
    
    for i in range(2, int(math.sqrt(max_nums)) + 1): # 3
        if flag[i]: #i가 소수면 이 배수는 다 제거
            j = 2
            while i*j <= max_nums:
                flag[i*j] = False
                j+=1
    
    #4 소수인것들 저장
    correct = set()
    for i in range(2, max_nums+1): 
        if flag[i]:
            correct.add(i)
    
    #5 3개의 합이 소수인지 판별
    for i in set_arr:
        if i in correct:
            answer += 1
            print(i)
    # print(correct)
    # print(set_arr)
    return answer