score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is:", grade)
John Carlo Nuqui
11:28 PM
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")  
else:
    factorial = 1
    for i in range(1, n + 1):  
        factorial *= i

    print(f"The factorial of {n} is: {factorial}")
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")
