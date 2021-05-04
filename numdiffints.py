# leetcode 1805
# complete

def numdiffints(word):
    intList = []
    ci = 0
    while ci < len(word):
        # print(ci)
        if word[ci].isdigit():
            newint = ""
            while word[ci].isdigit():
                newint += word[ci]
                ci += 1
                if ci >= len(word):
                    break
            if int(newint) not in intList:
                intList.append(int(newint))
                # print(intList)
        ci += 1
    return(len(intList))

def main():
    print(numdiffints("a123bc34d8ef34"))
    print(numdiffints("leet1234code234"))
    print(numdiffints("a1b01c001"))

if __name__ == '__main__':
    main()
