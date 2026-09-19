print("task 1: ")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print("task 2: ")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

print("task 3: ")
#duplicates are overwrite
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print("task 4: ")

this_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(this_dict))
print("task 5: ")
this_dict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

print("task 6: ")
dicti = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dicti["model"]
print(x)

print("task 7: ")
dict2 ={
    "name" : "aiza",
    "age" :20,
    "year" : 2005
}
x= dict2.keys()
print(x)

print("task 8: ")
dict2 ={
    "name" : "aiza",
    "age" :20,
    "year" : 2005
}
x= dict2.values()
print(x)
print("task 9: ")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["name"]= "suzuki"
print(x) #after the change

print("task 10: ")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

