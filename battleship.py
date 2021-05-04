# leetcode 419
# complete

def battleships(board):
    checkedSpaces = []
    count = 0
    for row in range(0, len(board)):
        for item in range(0, len(board[0])):
            if board[row][item] == "x":
                if [row, item] not in checkedSpaces:
                    # print("found new at " + str(row) + "," + str(item))
                    checkedSpaces.append([row, item])
                    count += 1
                    crow, citem = row, item+1
                    while citem < len(board[0]):
                        # print("checking v " + str(crow) + "," + str(citem))
                        # print(" " + board[crow][citem])
                        if board[crow][citem] == "x":
                            checkedSpaces.append([crow,citem])
                            citem += 1
                        else:
                            break
                    crow, citem = row+1, item
                    while crow < len(board):
                        # print("checking h " + str(crow) + "," + str(citem))
                        # print(" " + board[crow][citem])
                        if board[crow][citem] == "x":
                            checkedSpaces.append([crow,citem])
                            crow += 1
                        else:
                            break
                    # print(checkedSpaces)
    return count

def main():
    print(battleships([["x",".",".","x"],[".",".",".","x"],[".",".",".","x"]]))

if __name__ == '__main__':
    main()
