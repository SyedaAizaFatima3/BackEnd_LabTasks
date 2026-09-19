print("Task 1: ")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print("Task 2: ")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print("Task 3: ")

thistuple = ("apple",)
print(type(thistuple))

print("Task 4: ")

#A tuple can contain different data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print("Task 5: ")

tuple1 = ("abc", 34, True, 40, "male")

print("Task 6: ")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print("Task 7: ")

#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print("Task 8: ")
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print("Task 9: ")

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print("Task 10: ")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

print("Task 11: ")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

print("Task 12: ")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

print("Task 13: ")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

print("Task 14: ")
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
print("Task 15: ")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print("Task 16: ")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print("Task 17: ")

thistuple = ("apple", "banana", "cherry")
tuple2 = ("orange",)
thistuple += tuple2
print(thistuple)

print("Task 18: ")

thistuple = ("apple", "banana", "cherry")
del thistuple

print("Task 19: ")

#unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

print("Task 20: ")

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

print("Task 21: ")
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

print("Task 22: ")

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

print("Task 23: ")

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print("Task 24: ")
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

print("Task 25: ")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

print("Task 26: ")
thistuple = (1,1,2,4,5,5,5,6,9,9,7,8)
x= thistuple.index(5)
print(x)
