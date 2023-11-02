# This is a sample Python script.
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from math import sqrt

squares = [4, 9, 16, 25]
for i in squares :
    print(int(math.sqrt(i)))

squares.append(36)
squares.append(49)
squares.extend([64,81,100])
squares.insert(0,2)
print(squares)
squares.remove(49)
print(squares)

list = [1,2,3,2,1]
list.remove(2)
print(list)

squares.pop()
print(squares)

some_list = [1,2,3,4]
some_list.clear()
print(some_list)

numlist = [3,5,1,9,2,0]
print(numlist)
numlist.sort(reverse=True)
print(numlist)

names = ["Ruby", "Sam", "James", "Lily"]
names.sort(key=lambda n : len(n))
print(names)

names2 = [ "Eric", "anna", "Sophie", "sam" ]
names2.sort(key=lambda n: str.upper(n))
print(names2)

list2 = [4,7,1,8,3,10]
print(list2)
sortedlist = sorted(list2)
print(sortedlist)

squares.reverse()
print(squares)
squares[:] = squares[::-1]
print(squares)

colours = ["red", "green", "yellow", "blue", "red"]
print(colours.index("yellow"))
print(colours.index("red",3))
print(colours.index("blue"))
print(colours.count("red"))

for x in range(10):
    squares.append(x*x)
print (squares)

cubes = []
for x in range(10):
    cubes.append(x*x*x)
print(cubes)

even_nums = [num for num in range(100,201) if num % 2 == 0]

