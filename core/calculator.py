from decorators import cache_decorator


def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)

    def _sum(a, b):
        return a + b

    def diff(a, b):
        return a - b

    def divide(a, b):
        if not b:
            return 'Нельзя делить на 0'
        return a / b

    def mul(a, b):
        return a * b

    def exp(a, b):
        return a**b

    operators = {'+': _sum, '-': diff, '/': divide, '*': mul, '**': exp}

    func = operators.get(operation)
    return func(a, b)


def checkOperator(oper):
    # проверяет, поддерживается ли введенный мат. оператор
    operators = {'+', '-', '/', '*', '**'}
    if not oper in operators:
        print('Вы ввели некорретную операцию!')
        return False
    return True


if __name__ == '__main__':
    # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов

    try:
        a = int(input('Введите целое число: '))
    except:
        print('Вы ввели не целое число!')
        exit(0)

    try:
        b = int(input('Введите целое число: '))
    except:
        print('Вы ввели не целое число!')
        exit(0)

    operation = input('Введите операцию из списка: + | - | / | * | ** \n')
    operation = operation.strip()

    if not checkOperator(operation):
        exit(0)

    print('Результат: ', calculator(a, b, operation))
