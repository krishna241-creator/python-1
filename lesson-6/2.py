height = float(input("enter your height"))
weight = float(input("enter your weight"))

bmi = weight / height**2

if bmi <=18.4:
    print("you are underweight")
elif bmi <=24.9:
    print("you are healthy")    
else:
    print("you are overweight")    