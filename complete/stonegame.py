# leetcode 977
# complete

def stoneGame(piles):
    alexStones = 0
    leeStones = 0
    turn = 0
    stones = 0
    while piles:
        if piles[0] > piles[-1]:
            stones = piles[0]
            piles.pop(0)
        else:
            stones = piles[-1]
            piles.pop(-1)
        if turn == 0:
            alexStones += stones
            turn = 1
        else:
            leeStones += stones
            turn = 0
    winner = False
    if(alexStones > leeStones):
        winner = True
    return winner

def main():
    print(stoneGame([5,3,4,5]))

if __name__ == '__main__':
    main()
