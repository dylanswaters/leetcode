# leetcode 771
# complete

def numJewels(jewels, stones):
    count = 0
    for s in stones:
        if s in jewels:
            count += 1
    return count

def main():
    print(numJewels("aA","aAAbbbb"))
    print(numJewels("z","ZZ"))

if __name__ == '__main__':
    main()
