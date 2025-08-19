def solution(numbers, target):
    def dfs(idx, current_sum):
        # numbers 끝까지 다 사용했을 때
        if idx == len(numbers):
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 + 또는 -로 사용한 결과 합산
        plus = dfs(idx + 1, current_sum + numbers[idx])
        minus = dfs(idx + 1, current_sum - numbers[idx])
        
        return plus + minus
    
    answer = dfs(0, 0)
    return answer

