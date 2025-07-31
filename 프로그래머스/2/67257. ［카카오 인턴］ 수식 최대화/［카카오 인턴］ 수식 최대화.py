from itertools import permutations

def solution(expression):

    nums = []
    ops = []
    tmp = ''
    for ch in expression:
        if ch.isdigit():
            tmp += ch
        else:
            nums.append(int(tmp))
            ops.append(ch)
            tmp = ''
    nums.append(int(tmp)) 


    op_set = set(ops)
    op_orders = list(permutations(op_set))

    answer = 0

    for order in op_orders:
        n = nums[:]
        o = ops[:]
        for op in order:
            while op in o:
                idx = o.index(op)

                if op == '+':
                    res = n[idx] + n[idx + 1]
                elif op == '-':
                    res = n[idx] - n[idx + 1]
                elif op == '*':
                    res = n[idx] * n[idx + 1]

                n[idx] = res
                del n[idx + 1]
                del o[idx]

        answer = max(answer, abs(n[0]))

    return answer
