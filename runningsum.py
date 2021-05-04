# leetcode 1480
# complete

def runningSum(nums):
    newNums = []
    curSum = 0
    for i in nums:
        curSum += i
        newNums.append(curSum)
    return newNums

def main():
    print(runningSum([1,2,3,4]))
    print(runningSum([1,1,1,1,1]))
    print(runningSum([3,1,2,10,1]))

if __name__ == '__main__':
    main()
