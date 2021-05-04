# leetcode 1672
# complete
def maxWealth(accounts):
    highest = 0
    for i in accounts:
        nv = sum(i)
        if(nv > highest):
            highest = nv
    return highest

def main():
    print(maxWealth([[1,2,3],[3,2,1]]))
    print(maxWealth([[1,5],[7,3],[3,5]]))
    print(maxWealth([[2,8,7],[7,1,3],[1,9,5]]))

if __name__ == '__main__':
    main()
