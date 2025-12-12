try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    result = num1/num2
    print("the result is:", result)
    print("the result is:", result1)

except ZeroDivisionError:
    print("division with zero is not allowed")
except ValueError:
    print("please enter numerical value")
except NameError as ex:
    print("the exception is: ", ex)

except:
    print("an error has occurred")
finally:
    print("i will execute no matter what happens")