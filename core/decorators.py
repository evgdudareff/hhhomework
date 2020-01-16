def cache_decorator(func, *args):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает

    cach = {}

    def wrapperFunction(*args):
        if args not in cach:
            cach[args] = func(*args)
            return cach[args]
        else:
            return cach[args]
    return wrapperFunction
