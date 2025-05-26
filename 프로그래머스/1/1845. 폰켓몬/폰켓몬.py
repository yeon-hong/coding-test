def solution(nums):
    answer = 0
    arr = []

    for i in nums:
        if i not in arr:
            arr.append(i)
            answer += 1
        if len(nums)/2 == len(arr):
            break
        
    return answer