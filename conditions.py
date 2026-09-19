age = 20

if age >= 18:
    print("You are an adult")

age = 16

if age >= 18:
    print("You can vote")

else:
    print("You cannot vote")

marks = 75

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")



a = 10
b = 20

if a == b:
    print("a is equal to b")

if a != b:
    print("a is not equal to b")

if a < b:
    print("a is smaller than b")

if b > a:
    print("b is greater than a")

if a <= b:
    print("a is less than or equal to b")

if b >= a:
    print("b is greater than or equal to a")


number = -5

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")


number = 10

# % gives remainder
# If remainder is 0, number is even

if number % 2 == 0:
    print("Even number")

else:
    print("Odd number")


age = 21

if age < 13:
    print("Child")

elif age < 18:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior citizen")

marks = 85

if marks >= 50 and marks <= 100:
    print("Pass")

else:
    print("Fail")


age = 20
has_card = True

# Both conditions must be True

if age >= 18 and has_card:
    print("Entry allowed")

else:
    print("Entry not allowed")


day = "Sunday"

# At least one condition must be True

if day == "Saturday" or day == "Sunday":
    print("Weekend")

else:
    print("Weekday")


is_raining = False

# not changes True to False
# and False to True

if not is_raining:
    print("You can go outside")

else:
    print("Take an umbrella")


age = 22
student = True

if (age < 25 and student) or age < 18:
    print("Eligible")

else:
    print("Not eligible")


age = 20
has_id = True

if age >= 18:

    print("You are an adult")

    if has_id:
        print("You have ID")
        print("Entry allowed")

    else:
        print("You don't have ID")

else:

    print("You are under 18")


marks = 85

if marks >= 50:

    print("You passed")

    if marks >= 80:
        print("Excellent result")

    elif marks >= 70:
        print("Very good result")

    else:
        print("Good result")

else:

    print("You failed")


marks = 78

if marks >= 90:
    grade = "A+"

elif marks >= 80:
    grade = "A"

elif marks >= 70:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 50:
    grade = "D"

else:
    grade = "F"

print("Grade:", grade)


year = 2024

# A year is leap year if:
# 1. Divisible by 400
# OR
# 2. Divisible by 4 but NOT divisible by 100

if year % 400 == 0:

    print("Leap year")

elif year % 100 == 0:

    print("Not a leap year")

elif year % 4 == 0:

    print("Leap year")

else:

    print("Not a leap year")


a = 25
b = 40

if a > b:
    print("a is larger")

elif b > a:
    print("b is larger")

else:
    print("Both are equal")

