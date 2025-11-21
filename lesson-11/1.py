n = int(input("enter number of rows"))
for i in range( n+1 ):
    j = 1
    while j <= i:
        print("*", end="")
        j = j+1
    print()    