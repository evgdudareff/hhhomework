import random

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100


def gen(N):
    i = 0
    while i < N:
        yield random.randint(1, 100)
        i += 1


generatorFunc = gen(3)
while True:
    try:
        print(next(generatorFunc))
    except StopIteration:
        break

print('\n\n')

# написать генераторное выражение, которое делает то же самое
N = 4
generator = (random.randint(1, 100) for i in range(0, N))
while True:
    try:
        print(next(generator))
    except StopIteration:
        break
