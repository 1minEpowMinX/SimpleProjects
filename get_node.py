def get_gcf(a: int, b: int) -> int:
    ''' Finds the gcf of two numbers using Euclid's fast algorithm
        var a: int
        var b: int
        return: gcf a & b '''
    while b != 0:
        a, b = b, a % b
    return a


def main():
    while True:
        a, b = map(int, input(
            'Введите число a и b для нахождения НОД: ').split())
        print(f'НОД для чисел {a} и {b} равен {get_gcf(a, b)}')


if __name__ == '__main__':
    main()
