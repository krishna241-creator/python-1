def cube(x):
    return x*x*x

def multiplication(n):
    if n % 3 == 0:
        return cube(n)
    else:
        return False
    
print("your number is:", multiplication(3))
print("your number is:", multiplication(6))