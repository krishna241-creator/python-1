x = int(input("attendence count"))
y = input("medical cause: yes or no")
if y == 'yes':
    print("allowed")
else:
    if x >= 75:
        print("allowed")
    else:
        print("not allowed")
              