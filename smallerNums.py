# leetcode 1365
# complete

def smallerNums(nums):
    retList = []
    for i in nums:
        count = 0
        for j in nums:
            if j < i:
                count += 1
        retList.append(count)
    return retList

def main():
    print(smallerNums([8,1,2,2,3]))
    print(smallerNums([6,5,4,8]))
    print(smallerNums([7,7,7,7]))


if __name__ == '__main__':
    main()
