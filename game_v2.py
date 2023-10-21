
""" алгоритм угадывания числа наиболее быстрым методом: методом деления отрезка пополам
    сходимость этого метода 1/2**n
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """ алгоритм угадывания числа: метод деления отрезка пополам.
        нам заранее известно по условиям, что загаданное число
        лежит в диапазоне от 1 до 100. Середина этого промежутка равна 
        100/2=50, поэтому начинаем с predict_number = 50.
        Далее, если загаданное число больше, чем predict_number,
        то ищем в диапазоне от predict_number до верхнего предела отрезка.
        иначе до нижнего, каждый раз меняя верхний и нижний пределы
    """
   
    count = 0
    predict_number = 50
    numb_min, numb_max = 1,101      # границы отрезка в начале алгоритма

    while True:
        count += 1

        if number == predict_number: break          # выход из цикла если угадали
        elif number > predict_number :              # если наше число больше, чем загаданное, то
            numb_min = predict_number               # нижняя граница отрезка становится серединой        
        else :
            numb_max = predict_number
        predict_number = int((numb_min+numb_max)/2) # а число для угадывания на середине нового отрезка
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
        формируется сначала список из 1000 случайных чисел от 1 до 100, и совершается 
        1000 попыток угадать каждое из этих случайных чисел
    Args:
        random_predict ([type]): функция угадывания

    Returns:
        возвращает среднее количество попыток, за которые удалось угадать число
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)                                      # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
       count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
