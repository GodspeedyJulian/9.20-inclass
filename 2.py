Char=input("input a symbol: ")
while True:
    a=int(input("input an odd number: "))
    if a%2==1:
        break
Space=int((a-1)/2)
NumberOfChar=1
while NumberOfChar<=a:
    for i in range (Space):
        print(" ",end='')
    if NumberOfChar !=a and NumberOfChar>1:
        print(Char,end='')
        for i in range(NumberOfChar-2):
            print(" ",end='')
        print(Char)
    if  NumberOfChar==a:
        for i in range (NumberOfChar):
            print(Char,end="")
    if NumberOfChar==1:
        print(Char)
    NumberOfChar+=2
    Space-=1
