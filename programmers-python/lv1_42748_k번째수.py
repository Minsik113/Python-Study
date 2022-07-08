def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        t = array[i-1:j]
        t.sort()
        answer.append(t[k-1])
    return answer