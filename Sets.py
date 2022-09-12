# 6.2.8 dictionary method update
country_codes = {}
country_codes.update({'South Africa': 'za'})
print(country_codes)

country_codes.update(Austrailia='ar')
print(country_codes)

country_codes.update(Austrailia='au')
print(country_codes)

#6.2.9. Dictionary Comprehensions
months = {'January': 1, 'February': 2, 'March': 3}
months2 = {number: name for name, number in months.items()}
print(months2)

#6.3 Sets
colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
print(colors)
print(len(colors))

#checking for value in set
print('red' in colors)
print('purple' not in colors)

#iterating through a set
for color in colors:
    print(color.upper(), end=' ')

#creating a set with the built in set function
numbers = list(range(10)) + (list(range(5)))
print(numbers)
print(set(numbers))

#comparing sets
print({1, 3, 5} == {3, 5, 1})
print({1, 3, 5} != {3, 5, 1})
print({1, 3, 5} > {3, 5, 1})
print({1, 3, 5}.issuperset({3, 5, 1}))

#6.3.2 Union
print({1, 3, 5} | {2, 3, 4})

#intersection
print({1, 3, 5} & {2, 3, 4})
print({1, 3, 5, 7}.intersection([1, 2, 2, 3, 3, 4, 4]))

#difference
print({1, 3, 5} - {2, 3, 4})
print({1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4]))

#disjoint if they do not have any common elements.
print({1, 3, 5}.isdisjoint({2, 3, 4}))

#mutable mathmatical set operations
numbers = {1, 3, 5}
numbers |= {2, 3, 4}
print(numbers)

#methods for adding and removing numbers
numbers.add(17)
numbers.add(3)
print(numbers)

numbers.remove(3)
print(numbers)

#6.3.4
numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
evens = {item for item in numbers if item % 2 == 0}
print(evens)
print('Garrett Kopp')