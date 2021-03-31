# leetcode 1769
# complete

def minOps(boxStr):
    # currbox is the current box we're checking
    retBoxes = []
    for currbox in range(0,len(boxStr)):
        numMoves = 0
        for i in range(0, len(boxStr)):
            if boxStr[i] == "1":
                numMoves += abs(i - currbox)
        retBoxes.append(numMoves)
    return retBoxes

def main():
    print(minOps("110"))
    print(minOps("001011"))

if __name__ == '__main__':
    main()
