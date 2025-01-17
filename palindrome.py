word = str(input('Enter any word : '))
i = 0
j= len(str(word)) -1
while (i <= j):
    if(word[i] == word[j]):
        i += 1
        j -= 1
        if(i == j or j-i ==1):
            print("This word is palindrome")
        continue
    else:
        print("This word is not palindrome")
        break
        
    



