def solution(s):
    answer = 0
    n = len(s)
    for i in range(0, n):
        c = s[i:] + s[:i]  # 문자열 회전
        if f(c):
            answer += 1
    return answer

def f(c):
    stack = []
    for i in c:
        if i == '[' or i == '{' or i == '(':
            stack.append(i)
        elif i == ']':
            if not stack or stack[-1] != '[':  # 스택이 비어있거나 매칭되지 않으면
                return False
            stack.pop()  # 괄호 추가!
        elif i == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()  # 괄호 추가!
        elif i == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()  # 괄호 추가!
    
    return len(stack) == 0  # 스택이 비어있으면 True