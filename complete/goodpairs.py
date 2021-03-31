# leetcode 1512
# complete

def numGoodPairs(nums):
    goodPairs = 0
    for i in range(0,len(nums)):
        for j in range(0, len(nums)):
            # print(i, j)
            if nums[i] == nums[j] and i < j:
                goodPairs += 1
    return goodPairs

def main():
    print(numGoodPairs([1,2,3,1,1,3]))
    print(numGoodPairs([1,1,1,1]))
    print(numGoodPairs([1,2,3]))

if __name__ == '__main__':
    main()
