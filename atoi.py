# leetcode 8

def myAtoi(a):
    fStr = a.strip()
    space = fStr.find(' ')
    # print(space)
    if(space != -1):
        fStr = fStr[0:fStr.find(' ')]
    print("strip: " + fStr)
    if(fStr.isdigit()):
        return int(fStr)

def main():
    print(myAtoi("42"))
    print(myAtoi("   -42"))
    print(myAtoi("4193 with words"))
    print(myAtoi("words and 987"))
    print(myAtoi("-91283472332"))

if __name__ == "__main__":
    main()
