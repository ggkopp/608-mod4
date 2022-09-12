#6.2.1
from itertools import count


country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}

# determining if a dictionary is empty 
print(len(country_codes))

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

country_codes.clear()

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

#6.2.2 iterating through a dictionary 
days_per_month = {'January': 31, 'February': 28, 'March': 31}
print(days_per_month)

for month, days in days_per_month.items():
    print(f'{month} has {days} days')

#6.2.3. Basic Dictionary Operations
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'X': 100}
print(roman_numerals)

print(roman_numerals['V'])

#updating the value of existing key-value pair
roman_numerals['X'] = 10
print(roman_numerals)

#removing a key-value pair
roman_numerals['L'] = 50
print(roman_numerals)
print(roman_numerals.pop('X'))

#6.2.4
months = {'January': 1, 'February': 2, 'March': 3}

for month_name in months.keys():
    print(month_name, end=' ')

for month_name in months.values():
    print(month_name, end=' ')

# 6.2.5. Dictionary Comparisons
country_capitals1 = {'Belgium': 'Brussles', 'Haiti': 'Port-au-Prince'}
country_capitals2 = {'Nepal': 'Kathmandu', 'Uruguay': 'Montevideo'}
country_capitals3 = {'Haiti': 'Port-au-Prince', 'Belgium': 'Brussles'}

print(country_capitals1 == country_capitals2)
print(country_capitals1 == country_capitals3)
print(country_capitals1 != country_capitals2)

#6.2.7. Word Count
"""Tokenizing a string and counting unique words."""

text = ('this is sample text with several words with words other than the example included ' 
        'this is more sample text with some different words that include even more text that before')

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))
print('Garrett Kopp')



