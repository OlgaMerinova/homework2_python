# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег




MULT = 50
MIN_CASH = 30
MAX_CASH = 600
PERCENT = 0.015
EXTRA_PERCENT = 0.97
MAX_SCORE = 5_000_000
RICH_CASH = 0.1
MAX_COUNT = 3
count = 0
total_score = 0
commis = 0
system = 0

def menu(system):
    system = int(input("Выберите действие:\n"
                        f'1 - пополнить счет \n'
                        f'2 - снять денежные средства \n'
                        f'3 - выйти из меню \n'))
    return system


def number_time(cash, count):
    if count > MAX_COUNT:
        cash *= EXTRA_PERCENT
    count += 1
    return cash

def add_cash(cash, count):
    if cash % MULT == 0:
        total_score += cash
        print(f'Успешно, Ваш баланс составляет: {total_score}')
    else:
        print(f'Ошибка, внесите сумму, кратную 50. Ваш баланс составляет: {total_score}')
    count += 1
    return total_score


def give_cash(cash, count):
    while cash > total_score:
        if cash % MULT == 0:
            commis = cash * PERCENT
            if MAX_CASH < commis > MIN_CASH:
                total_score = total_score - commis
            elif commis < MIN_CASH:
                total_score = total_score - MIN_CASH
            elif commis > MAX_CASH:
                total_score = total_score - MAX_CASH
        count += 1
    return total_score

def max_cash(cash, count):
    if total_cash > MAX_SCORE:
        commis = cash * RICH_CASH
        total_score -= commis
    count += 1
    return total_score

def quit():
    return f'Ваш остаток на счет {total_score}'


if menu(system) == 1:
    add_cash(cash, count)
    number_time(cash)
elif menu(system) == 2:
    print(give_cash())
    print(number_time())
    print(max_cash())
elif menu(system) == 3:
    print(quit())

