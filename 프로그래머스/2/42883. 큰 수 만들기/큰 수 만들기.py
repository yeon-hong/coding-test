def solution(number, k):
    stack = []
    del_count = 0
    
    for i in number:
        while stack and del_count < k and stack[-1] < i:
            stack.pop()
            del_count += 1
        stack.append(i)
    
    # '987654321' <- 이런 경우  
    if del_count < k:
        stack = stack[:-(k - del_count)]
        
    return ''.join(stack)