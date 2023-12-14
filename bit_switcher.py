def bit_operation(n: int, bit_n: list, operation='^') -> int:
    """
    Выполняет операции включения, выключения или переключения битов числа n
    с использованием заданной операции (по умолчанию - переключение '^')

    Параметры:
        n (int): Исходное число
        bit_n (list): Список позиций битов для взаимодействия
        operation (str): Операция: '&' (выключение), '|' (включение) или '^' (переключение)

    Возвращает:
        int: Результат операции
    """
    mask = sum(2 ** n for n in bit_n)
    match operation:
        case '&': return n & ~mask
        case '|': return n | mask
        case _: return n ^ mask


def get_user_choice() -> str:
    """
    Получает выбор пользователя: "bit" (взаимодействие с битами) или "exit" (выход)
    """
    return input('''Выберите действие и введите его:
    Взаимодействие с бит: bit
    Выход из программы: exit\n''').lower()


def get_bit_interact_data() -> tuple:
    """
    Получает данные для взаимодействия с битами от пользователя:
    число, позиции битов, операция
    """
    num = int(input('Введите число: '))
    bit_positions = [int(x) for x in input(
        'Введите биты для взаимодействия (через пробел): ').split() if x.isdigit()]
    operation = input('''Выберите операцию (по умолчанию "^"):
    Выкл: &
    Вкл: |
    Переключение: ^\n''')
    return num, bit_positions, operation


def main():
    calculate = True
    while calculate:
        ans = get_user_choice()
        match ans:
            case 'bit':
                print(
                    f'Результат: {bit_operation(*get_bit_interact_data())}\n')
            case 'exit':
                print('Завершение работы программы...')
                exit()
            case _:
                print('Неправильно введеное действие.\n')
                continue


if __name__ == '__main__':
    main()
