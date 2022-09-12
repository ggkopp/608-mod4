#Create a Tuple(s)
student_tuple = ('John', 'Green', 3.3)
another_student_tuple = ('Kyle', 'Orange', 3.4)

print(student_tuple)

#access tuple elements by index
print(student_tuple[-2], another_student_tuple[1])

#add more items to tuple
student_tuple += ('Mathmatics', 3.9)
another_student_tuple += ('Science', 3.7)

#self checks
single = (123.45,)

print(single)

#self checks list + Tuple = error
# print[1, 2, 3] + (4, 5, 6)

print(student_tuple)
print(another_student_tuple)

#create student tuples
student_tuple1 = ('John', 'Travolta', [9, 3, 8, 7, 7, 10])

#Unpacking the tuple
first_name, last_name, grades = student_tuple1

print(student_tuple1)
print(first_name)
print(grades)

# creating a primitive bar chart
"""Displaying a bar chart"""
numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')
print('Garrett Kopp')
  
