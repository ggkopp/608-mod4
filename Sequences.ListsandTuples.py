#specify slicing with starting and ending indecies
from http.client import responses
from socket import NI_NUMERICHOST


numbers = [2, 3, 5, 7, 11, 13, 17, 19]

print(numbers[2:6])

#specifying a slice with only an ending index
print(numbers[:6])
print(numbers[0:6])

#specifying slice with only a starting index
print(numbers[6:])
print(numbers[6:len(numbers)])

#specifying slice with no indices
print(numbers[:])

#slicing with steps
print(numbers[::2])

#slicing with negative indices and steps
print(numbers[::-1])

#modifying lists via slices
numbers[0:3] = ['two', 'three', 'five']

print(numbers)

numbers[0:3] = []

print(numbers)

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers[::2] = [100, 100, 100, 100]
print(numbers)

print(id(numbers))

#self check select numbers even integers 5.5
numbers = list(range(1, 16))
print(numbers)
print(numbers[1:len(numbers):2])
#replace the elements at indices 5 - 9 with 0's
numbers[5:10] = [0] * len(numbers[5:10])
print(numbers)
#keep only the five elements
numbers[5:] = []
print(numbers)
#delete all the remaining elements
numbers[:] = []
print(numbers)

#deleting element at a specific list
numbers = list(range(0, 10))
print(numbers)
del numbers[-1]
print(numbers)

#deleting slice from a list
del numbers[0:2]

print(numbers)

#delete every other element
del numbers[::2]
print(numbers)

#deleting a slice representing the entire list
del numbers[:]
print(numbers)

#self check 5.6 delete slice containing first four elements
numbers = list(range(1, 16))
del numbers[0:4]
print(numbers)
#starting with the first element, delete every other element
del numbers[::2]
print(numbers)

#5.7 Passing lists into functions
def modify_elements(items):
    """Multiplies all element values in items by 2."""
    for i in range(len(items)):
        items[i] *=2

numbers = [10, 3, 7, 1, 9]
modify_elements(numbers)
print(numbers)

#Passing a tuple to a function results in typeError
#numbers_tuple = (10, 20, 30)
#print(numbers_tuple)
#modify_elements(numbers_tuple)

#Sorting
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
numbers.sort()
print(numbers)

# 5.9 list method index
numbers = [3, 7, 1, 4, 2, 8, 5, 6]
print(numbers.index(6))

# in and not in
print(100 in numbers)
print(5 in numbers)
print(1000 not in numbers)

# 5.9 self checks
numbers = [67, 12, 46, 43, 13]
print(numbers.index(43))

if 44 in numbers:
    print(f'Found 44 at index: {numbers.index(44)}')
else:
    print('44 not found')

# more functions
#insert
color_names = ['orange', 'yellow', 'green']
color_names.insert(0, 'red')
print(color_names)
#append
color_names.append('blue')
print(color_names)
#extend
color_names.extend(['indigo', 'violet'])
print(color_names)
#remove
color_names.remove('green')
print(color_names)
#Clear
color_names.clear()
print(color_names)
# Count
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
for i in range(1, 6):
    print(f'{i} appears {responses.count(i)} times in responses')
#reverse
color_names = ['red', 'green', 'yellow', 'orange', 'blue']
color_names.reverse()
print(color_names)
#copied list
copied_list = color_names.copy()
print(copied_list)
#pop
print(copied_list.pop(0))

#5.12 lists 
list1 = []
for item in range(1, 6):
    list1.append(item)

print(list1)

list2 = [item for item in range(1, 6)]
print(list2)

list3 = [item ** 3 for item in range(1, 6)]
print(list3)

list4 = [item for item in range(1, 11) if item % 2 == 0]
print(list4)

# 5.12 self checks
cubes = [(x, x ** 3) for x in range(1, 6)]
print(cubes)

multiples = [x for x in range(3, 30, 3)]
print(multiples)

#5.14 
#filter
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
def is_odd(x):
    """returns true only if x is odd"""
    return x % 2 != 0
print(list(filter(is_odd, numbers)))

#map and lambda
print(list(map(lambda x: x ** 2, numbers)))

#5.16 two-dimensional lists
a = [[77, 68, 86, 73], #first students grades
    [96, 87, 89, 81], #second students grades
    [70, 90, 86, 81]] #thrid students grades

for row in a:
    for item in row:
        print(item, end=' ')
    print()

print('Garrett Kopp')