# leetcode # 9
# complete

def ispalindrome(x):
    # print(str(x)[::-1])
    if(str(x)[::-1] == str(x)):
        return True
    else:
        return False
    
def ispalindromenostring(x):
    reversedNum = 0
    xcopy = x
    while xcopy != 0 or xcopy != -1:
        # print(xcopy)
        if xcopy == 0 or xcopy == -1:
            break
        digit = xcopy % 10
        reversedNum = reversedNum * 10 + digit
        xcopy //= 10
        # print(reversedNum)
    if(x == reversedNum):
        return True
    else:
        return False
    

def main():
    print(ispalindrome(121))
    print(ispalindrome(-121))
    print(ispalindrome(10))
    print(ispalindromenostring(121))
    print(ispalindromenostring(-121))
    print(ispalindromenostring(10))

if __name__ == '__main__':
    main()