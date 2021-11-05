def main():
    res = 0
    for num in range(3,1000):
        if ((num % 3) == 0 or (num % 5) == 0):
            res += num
    return res
if __name__ == "__main__":
    res = main()
    print(res)