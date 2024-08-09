#question 3 task 1 

year = int(input("Put in a year: "))

if year / 4:
    print("True")
elif year / 100:
    print("False")
elif year / 400:
    print("True")
else:
    print("False")