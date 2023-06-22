# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


def dec_to_n():
    system: int = 16
    tmp_num: int = number
    new_num: str = ''
    while tmp_num != 0:
        mod: str = str(tmp_num % system)
        new_num = mod + new_num
        tmp_num //= system
    return new_num

if __name__ == '__main__':
    number = int(input("Введите число: "))
    print(dec_to_n())
    print(f'Это число в шестнадцатиричном представлении - {hex(number)}')
