# leetcode 29
# complete
def divide(dividend, divisor):
    # div by 0 error
    # if divisor == 0:
    #     print("div by zero")
    #     return
    # check for negatives
    isNegative = False
    if bool(dividend < 0) ^ bool(divisor < 0):
        isNegative = True
    # set vals to absolutes
    dividend = abs(dividend)
    divisor = abs(divisor)
    # compute division
    counter = 0
    current = divisor
    while(current <= dividend):
        counter += 1
        current += divisor
    # negative check
    if isNegative:
        counter = 0 - counter
    return counter

def main():
    print(divide(10,3))
    print(divide(7,-3))
    print(divide(0,1))
    print(divide(1,1))

if __name__ == '__main__':
    main()
