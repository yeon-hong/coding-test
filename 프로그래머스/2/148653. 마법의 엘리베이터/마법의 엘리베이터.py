def solution(storey):
    answer = 0
    digits = list(map(int, str(storey)))
    n = len(digits)
    carry = 0

    for i in range(n - 1, -1, -1):
        curr = digits[i] + carry

        if curr > 5:
            answer += 10 - curr
            carry = 1
        elif curr < 5:
            answer += curr
            carry = 0
        else:  

            if i > 0 and digits[i - 1] >= 5:
                answer += 5
                carry = 1
            else:
                answer += 5
                carry = 0

    if carry == 1:
        answer += 1

    return answer

