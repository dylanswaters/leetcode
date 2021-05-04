# leetcode 807
# complete
def maxInc(buildHeights):
    yHeight = []
    xHeight = []
    # print(len(buildHeights))
    # add y heights
    rotHeights = []
    for b in buildHeights:
        yHeight.append(max(b))
    # rotate grid
    # create new row for length
    for i in buildHeights[0]:
        rotHeights.append([i])
    # append values to rotate for every item
    for x in range(1, len(buildHeights[0])):
        for y in range(0, len(buildHeights)):
            rotHeights[y].append(buildHeights[x][y])
    # add x heights
    for b in rotHeights:
        xHeight.append(max(b))

    # print("skyline heights")
    # print(xHeight)
    # print(yHeight)
    # create new heights
    newHeights = []
    for b in range(0, len(buildHeights)):
        newRow = []
        for i in range(0, len(buildHeights[0])):
            if(xHeight[i] < yHeight[b]):
                newRow.append(xHeight[i])
            else:
                newRow.append(yHeight[b])
        newHeights.append(newRow)
    return newHeights

def main():
    print(maxInc([ [3, 0, 8, 4],
             [2, 4, 5, 7],
             [9, 2, 6, 3],
             [0, 3, 1, 0] ]))

if __name__ == "__main__":
    main()
