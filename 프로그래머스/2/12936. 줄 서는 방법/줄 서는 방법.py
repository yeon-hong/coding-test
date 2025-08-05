import math

def solution(n, k):
    numbers = list(range(1, n + 1))     
    k -= 1                              # 인덱스가 0부터 시작하므로 1 빼줌 (k = 4)
    answer = []

    for i in range(n, 0, -1):           # n자리 수의 순열을 차례대로 결정
        fact = math.factorial(i - 1)    # 현재 자리수에서 하나를 고정했을 때 만들 수 있는 경우 (fact개 마다 앞자리수가 바뀜)
        idx = k // fact                 # k번째 순열은 현재 자리에서 몇 번째 숫자인지를 결정 (k번째 큰수는 idx 번째에 속해있음)
        k %= fact                       # 남은 순열에서의 순서 갱신 (숫자를 고정하고 나머지 수 조합중 몇번째인지 갱신)
        answer.append(numbers.pop(idx)) # 그 숫자를 결과에 추가하고, 리스트에서 제거

        
    return answer