# Есть список not_even_list, реализовать логику в функции even: создать новый список с четными элементами из списка not_even_list
not_even_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def even(some_not_even_list):
    evenList = [num for num in some_not_even_list if num % 2 == 0]
    return evenList


# Следующий код с циклом, переписать с использованием спискового включения (list comprehension)
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]


def get_ages(some_years_of_birth):
    ages = [2014 - year for year in some_years_of_birth]
    return ages


# Есть список numbers, реализовать логику в функции get_first_n_last: вернуть новый список состоящий из первого и последнего элемента переданного списка
numbers = [5, 10, 15, 20, 25]


def get_first_n_last(some_list):
    return [some_list[0], some_list[-1]]


# Написать функцию, которая принимает список и возвращает новый список, состоящий из элементов принятого, но без повторений
list_with_repetition = [1, 1, 3, 4, 2, 2, 2, 6]


def get_list_without_repetition(some_list):
    return list(set(some_list))


# Написать функцию, которая возвращает словарь, ключи которого из списка keys, а значения из списка values
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#00FF00', '#0000FF']


def map_keys_and_values(some_keys, some_values):
    return dict(zip(some_keys, some_values))


# Написать функцию, которая принимает строку и возвращает словарь состоящий из ключей - символов из строки, значений - количество повторений этих символов в строке
s = 'some string'


def count_symbols(some_string):
    dictOut = {char: some_string.count(char) for char in some_string}
    return dictOut


# Применение функций
print(even(not_even_list))  # [4, 16, 36, 64, 100]

print(get_ages(years_of_birth))  # [24, 23, 24, 24, 22, 23]

print(get_first_n_last(numbers))  # [5, 25]

print(get_list_without_repetition(list_with_repetition))  # [1, 2, 3, 4, 6]

print(map_keys_and_values(keys, values))
# {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}

print(count_symbols(s))
#{'s': 2, 'o': 1, 'm': 1, 'e': 1, ' ': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1}
