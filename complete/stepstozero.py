# leetcode 1342
# complete

def numSteps(num):
    n = num
    steps = 0
    while(n != 0):
        if(n % 2 == 0):
            n = n / 2
            steps += 1
        else:
            n = n - 1
            steps += 1
    return steps

def main():
    print(numSteps(14))
    print(numSteps(8))
    print(numSteps(123))


if __name__ == '__main__':
    main()
