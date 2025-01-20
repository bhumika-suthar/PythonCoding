inputStr = str(input("Enter any String : "))
Vowelarr = ['a', 'e', 'i', 'o', 'u']
i = 0
vowel = 0
conso = 0
while(i < len(inputStr)):  
    if(inputStr[i] == 'a' or inputStr[i] == 'e' or inputStr[i] == 'i' or inputStr[i] == 'o' or inputStr[i] == 'u' ):
        vowel += 1
        i += 1
    
    elif(inputStr[i] != " "):
            conso += 1
            i += 1
    else:
        i += 1
        
print(f"The vowels are {vowel}")
print(f"The vowels are {conso}")
