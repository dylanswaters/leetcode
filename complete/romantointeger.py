#leetcode #13
#complete

def romanToInt(s):
    romanVals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sum = 0
    for i in range(len(s)-1):
        # print(str(s[i]) + " " + str(romanVals[s[i]]))
        if romanVals[s[i]] < romanVals[s[i+1]]:
            sum -= romanVals[s[i]]
        else:
            sum += romanVals[s[i]]
    return sum

def main():
    print(romanToInt("III"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))

if __name__ == '__main__':
    main()