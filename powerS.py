def printPowerC(word):
    n = len(word)
    
    for m in range(1, 1 << n):  
        ListOC = []
        for i in range(n):
            if m & (1 << i):  
                ListOC.append(word[i])
        print("".join(ListOC))


try:
    w = input("Enter a word: ")
    if not w.isalpha():
        raise ValueError
    
    print("\nCombinations of letters:")
    printPowerC(w)

except ValueError:
    print("Enter valid string")



