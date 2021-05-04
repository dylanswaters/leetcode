# leetcode 1816
# complete

def truncateSentence(s, k):
    words = s.split()
    retS = ""
    for i in range(0, k):
        if(i > 0 and i < k):
            retS = retS + " "
        retS = retS + words[i]
    return retS

def main():
    print(truncateSentence("Hello how are you Contestant", 4))
    print(truncateSentence("What is the solution to this problem", 4))
    print(truncateSentence("chopper is not a tanuki", 5))

if __name__ == '__main__':
    main()
