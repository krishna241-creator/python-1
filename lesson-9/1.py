num = int(input("enter a number: "))
sum = 0  
x = num
while x>0:
    digit = x % 10
    sum = sum + digit**3
    x = x // 10
if num == sum:
    print("your number is an armstrong number")     
else:
    print("your number is not an armstrong number")           