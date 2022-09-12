#Creating a list of C integers
c = [-45, 6, 0, 72, 1543]
print(c)

#Getting the value of the first and last item
print(c[0])
print(c[4])
print(len(c))
print(c[-1])

#attempt to access an index longer than the list "index list out of range"
# print(c[100])

#using list variables in expressions
print(c[0] + c[1] + c[2])

#append new items
b_list = []

for number in range (0,5):
    b_list += [number]

print(b_list)

#concatinate c and b_list
concatenate_list = c + b_list
print(concatenate_list)

#for i in range()
for i in range(len(concatenate_list)):
    print(f'{i}: {concatenate_list[i]}')

#create 3 lists, use comparison operators to compare the lists
list_1 = [1, 3, 5]
list_2 = [1, 3, 5]
list_3 = [1, 3, 5, 7]

print(list_1 == list_2)
print(list_1 == list_3)
print(list_2 == list_3)
print(list_1 >= list_2)

#create a function cube list to cube every item in a list. 
def cube_list(values):
    for i in range(len(values)):
        values[i] **=3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cube_list(numbers)

print(numbers)
print('Garrett Kopp. Lists')
