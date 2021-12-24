def factorization(number):
    i = 2
    while (i * i) <= number:
        if number % i:
            i += 1
        else:
            number //= i # perform integer division
    return number

if __name__ == "__main__":
    number = 600851475143
    res = factorization(number)
    print(res)