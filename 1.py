symbol=input("input a symbol: ")
MaxNumberOfSymbols=int(input("input max number of symbols(an odd number): "))
while MaxNumberOfSymbols %2!=1:
    MaxNumberOfSymbols=int(input("input max number of symbols(an odd number!!!): "))
NumberOfSpaces= int((MaxNumberOfSymbols-1)/2)
NumberOfSymbols=1
while NumberOfSymbols <= MaxNumberOfSymbols:
    for i in range (NumberOfSpaces):
        print(" " ,end="")
    for i in range (NumberOfSymbols):
        print(symbol,end="")
    print(" ")
    NumberOfSpaces -=1
    NumberOfSymbols +=2
