# leetcode # 1
# complete

def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return([i,j])


def main():
    print(twosum([2,7,11,15], 9))
    print(twosum([3,2,4], 6))
    print(twosum([3,3], 6))


if __name__ == '__main__':
    main()