#leetcode #14
#complete

def longestCommonPrefix(strs):
    strs.sort()
    # print(strs)
    answer = ""
    for i in range(min(len(strs[0]), len(strs[-1]))):
        if strs[0][i] != strs[-1][i]:
            return answer
        answer += strs[0][i]


def main():
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))

if __name__ == "__main__":
    main()