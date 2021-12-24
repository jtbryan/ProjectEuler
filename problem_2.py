def fibonacci_sequence():
    '''
    Find the sum of even valued terms where the sequence does not exceed four million
    '''
    cur = 1
    res = 0
    prev1 = 0
    prev2 = 0
    while cur <= 4000000:
        if prev1 == 0 and prev2 == 0:
            prev1 = cur
            cur = cur + prev1
        elif prev1 != 0 and prev2 == 0:
            prev2 = cur 
            cur = cur + prev1
        else:
            prev1 = prev2 
            prev2 = cur
            cur = prev1 + prev2
        if cur % 2 == 0:
            res += cur
    return res
if __name__ == "__main__":
    res = fibonacci_sequence()
    print(res)