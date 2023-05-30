#leetcode #2
# complete

def addtwonums(l1, l2):
    retList = []
    carry = 0
    if(len(l1) > len(l2)):
        while(len(l1) > len(l2)):
            l2.append(0)
    if(len(l2) > len(l1)):
        while(len(l2) > len(l1)):
            l1.append(0)

    # print(l1)
    # print(l2)

    for i in range(len(l1)):
        retList.append(l1[i] + l2[i] + carry)
        if carry == 1:
            carry = 0
        if retList[i] >= 10:
            retList[i] = retList[i] % 10
            carry = 1
    if carry == 1:
        retList.append(1)
    return retList

def main():
    print(addtwonums([2,4,3],[5,6,4]))
    print(addtwonums([0],[0]))
    print(addtwonums([9,9,9,9,9,9,9],[9,9,9,9]))


if __name__ == '__main__':
    main()