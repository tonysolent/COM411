print("What is your name human? : ")
name=input()
print()
print("how old are you (in years)")
age=int(input())
print()
print("how tall are you (in meters)")
height=float(input())
print()
print("how much do you weigh (in kilograms)")
weight=float(input())
print()
bmi=weight/height**2
print()
print(f"{name} you are {age} years old and your bmi is {bmi}")