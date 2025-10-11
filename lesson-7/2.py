print("2 choises are given. choose your pick !!!")
print("a. car")
print("b. scooter")
x = input("choose from the above options")
if x == 'a':
    print("Choose an car from the following")
    print("i. toyota")
    print("ii. nissan")
    y = input("choose any car from the above options")
    if y == 'i':
        print("nice choice. You chose toyota")
    else:
        print("nice choice. you chose nissan")
elif x == 'b':
    print("choose a scooter from the following")        
    print("I. honda")
    print('II. hyundai')
    z = input("choose any scooter from the above options")
    if z == 'I':
        print("nice choice. You chose honda")
    else:
        print("nice choice. You chose hyundai")
else:
    print("the choice is invalid")        