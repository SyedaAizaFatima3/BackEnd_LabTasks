print("task 0: ")

def my_function():
    print("Hello from a function")

print("task 1")

def my_function():
    print("Hello from a function")
my_function()

print("task 2:")


def my_function():
    print("Hello from a function")


my_function()
my_function()
my_function()

print("task 3 :")


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

print("task 4:")


def greet():
    return "hello my name is Aiza";


message = greet();
print(message)
print(greet())

print("task 5 :")


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("task 6 :")


# parameter vs args
def my_function(name):  # name is a parameter
    print("Hello", name)


my_function("Emil")  # "Emil" is an argument

print("task 7 :")


def my_function(name="friend"):
    print("Hello", name)


my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

print("task 8 :")


def my_function(country="Norway"):
    print("I am from", country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print("task 9 :")


# keyword args
def my_animal(animal, name):
    print("my " + animal + "'s name is " + name)


my_animal(animal="cat", name="lucy");

print("task 10 :")


# positional args (without keyword)
def my_animal(animal, name):
    print("my " + animal + "'s name is " + name)


my_animal("cat", "lucy");

print("task 11 :")


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])


my_person = {"name": "Emil", "age": 25}
my_function(my_person)

print("task 12 : ")


def my_function():
    return ["apple", "banana", "cherry"]


fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

print("task 13:")


def my_function():
    return (10, 20)


x, y = my_function()
print("x:", x)
print("y:", y)

print("task 14:")


def function2(*kids):
    print("The youngest child is " + kids[2])


function2("Emil", "Tobias", "Linus")

print("task 15:")


def my_function(greeting, *names):
    for name in names:
        print(greeting, name)


my_function("Hello", "Emil", "Tobias", "Linus")

print("task 16:")


def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

print("task 17:")


def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)


my_function(name="Tobias", age=30, city="Bergen")

print("task 18:")


# local variable
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc()

print("task 19:")

# global variable
x = 300


def myfunc():
    x = 200
    print(x)


myfunc()
print(x)

print("task 20:")

x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print("Inner:", x)

    inner()
    print("Outer:", x)


outer()
print("Global:", x)

print("task 21: ")
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

print("task 22: ")


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))

print("task 23: ")


def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)

print(mytripler(11))

print("task 24: ")


# recursive functions
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)


countdown(5)

print("task 25: ")


def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(5))

print("task 26: ")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))

print("task 27: ")


def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)

