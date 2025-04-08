def solution(wallet, bill):
    answer = 0

    wallet.sort()

    short_side = min(bill)
    long_side = max(bill)

    while short_side > wallet[0] or long_side > wallet[1]:

        long_side //= 2

        answer += 1


        if short_side > long_side:
            short_side, long_side = long_side, short_side
            
    return answer