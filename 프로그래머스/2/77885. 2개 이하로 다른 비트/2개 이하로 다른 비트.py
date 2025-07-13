def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            bin_num = list('0' + bin(num)[2:])
            
            for i in range(len(bin_num) - 1, 0, -1):
                if bin_num[i] == '0':
                    bin_num[i] = '1'
                    bin_num[i + 1] = '0'
                    break
            else:
                # 모든 비트가 1인 경우, 맨 앞의 0을 1로 바꾸고 다음 비트는 0으로 교체
                bin_num[0] = '1'
                bin_num[1] = '0'
            
            answer.append(int(''.join(bin_num), 2))
    return answer

