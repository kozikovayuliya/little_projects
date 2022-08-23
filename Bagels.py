# Description of the game
# В дедуктивной логической игре «Бейглз» необходимо по
# подсказкам угадать секретное число из трех цифр. В ответ на ваши попытки угадать игра выдает одну из трех
# подсказок: Pico, если вы угадали правильную цифру на
# неправильном месте, Fermi, если в вашей догадке есть правильная цифра на правильном месте, и Bagels, если в догадке
# не содержится правильных цифр. На угадывание секретного
# числа у вас десять попыток.

import random


def main():
    print('Bagels, a deductive logic game.\n'
          'By Al Sweigart al@inventwithpython.com\n'
          'I am thinking of a 3-digit number. Try to guess what it is.\n'
          'Here are some clues:\n'
          'When I say: That means:\n'
          ' Pico One digit is correct but in the wrong position.\n'
          ' Fermi One digit is correct and in the right position.\n'
          ' Bagels No digit is correct.')


def get_secret_num():
    numbers = list('0123456789')  # формирование списка цифр
    random.shuffle(numbers)  # перемешивание списка
    secret_num = numbers[0:3]  # первые 3 символа перемешанного списка сформируют загаданное число
    secret_num = ''.join(secret_num)
    return secret_num


def user_input_validation(guess):  #валидация инпута пользователя
    validation_flag = False  #вернет True, если не встретит проблем при обработке, иначе False
    if len(guess) != 3:
        print('Please, write three-digit number')

    elif not guess.isdigit():
        print('Please, write number. Like "123".')

    else:
        validation_flag = True

    return validation_flag


def checking_numbers(guess, secret_number):  #проверка введенного пользователем числа и возвращение подсказок

    clues = []
    for i in range(3):
        if guess[i] == secret_number[i]:  #если верная цифра на своем месте - Fermi
            clues.append('Fermi')
        elif guess[i] in secret_number:  #если цифра есть в загаданном числе, но не на своем месте - Pico
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  #если в списке нет ни Pico, ни Fermi, вернем Bagels (=ни одного из введенных цифр нет в загаданном числе
    else:
        clues.sort()  #отсортируем список, чтобы не подсказывать позиции угаданных цифр
        return ' '.join(clues)


while True:  #основной цикл игры
    secret_num = get_secret_num()  #загадывание числа
    print('Number was choosen. Try to guess it. You have 10 attempts.')

    try_counter = 1
    while try_counter <= 10:  #цикл с попытками прервется, когда превысит 10

        while True:  #цикл с валидацией введенного числа прервется, когда валидация пройдет
            guess = input()
            if user_input_validation(guess) is True:
                break

        if guess == secret_num:  #когда введенное число совпадет с загаданным, цикл (с попытками) прервется
            print(f'Thats right! It was {int(secret_num)}')
            break
        else:
            print(checking_numbers(guess, secret_num))  #иначе выводятся подсказки

        try_counter += 1

        if try_counter > 10:
            print(f'You ran out of guesses. The answer was {int(secret_num)}')

    print('Do you want to play again? (yes or no)')  #основной цикл игры прервется, если пользователь не захочет больше играть
    if not input().lower().startswith('y'):
        break

print('Thanks for playing!')

if __name__ == '__main__':
    main()

