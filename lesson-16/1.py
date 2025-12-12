try:
    num = int(input("enter your number: "))
    print(num)
except ValueError as ex:
    print("exception: ", ex)
print("i am outside try")