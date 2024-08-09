#question 2 task 1

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

if number2 <= number1 >= number3:
    print(number1)
elif number1 <= number2 >= number3:
    print(number2)
else:
    print(number3)


#question 2 task 2

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
number3 = int(input("Third number: "))

if number2 >= number1 <= number3:
    print(number1)
elif number1 >= number2 <= number3:
    print(number2)
else:
    print(number3)