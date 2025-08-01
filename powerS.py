import math

def printPowerS(S, setSize):
    powerSetSize = int(math.pow(2, setSize))

    outer = 0
    inner = 0

    for outer in range(0,powerSetSize):
        for inner in range(0,setSize):
            if (outer & (1 << inner)) > 0:
                print(S[inner], end = "")
        print("")


try:
    size = int(input("Enter a number(make it under 6 so it doesnt crash):"))
    Set = []
    for i in range(0,size):
        n = input("Enter letters: ")
        if not n.isalpha():  
            raise ValueError
        Set.append(n)
    printPowerS(Set,len(Set))
    

except ValueError:
    print("Enter valid characters")


