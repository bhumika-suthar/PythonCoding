def notSame(alpha, arr):
    for i in arr:
        if(alpha == i):
            return False
        else:
            return True

def checkAnalog(word1,word2):
    arr = []
    for alpha in word1:
        if (alpha in word2):
            if(notSame(alpha, arr)):
                print(f"{arr}")
                arr.append(alpha)
    if(len(word2 )== len(arr)):
        print(f"The words {word1} and {word2} are anagram")
    else:
        print(f"The words {word1} and {word2} are not anagram")


word1 = str(input("Enter word 1 : "))
word2 = str(input("Enter word 2 : "))

checkAnalog(word1,word2)
