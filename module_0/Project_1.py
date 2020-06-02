#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def middle_area(search_start, search_finish):
    '''Функция принимает два числа - нижнюю границу поиска и верхнюю границу поиска, и возвращает число, 
    равное середине области поиска'''
    predict = (search_start + search_finish)//2
    return predict

def game_core_v3(number):
    '''Сначала устанавливаем число, равное середине области поиска, и если это не загаданное число - сужаем область поиска вдвое.
       Функция принимает загаданное число и возвращает число попыток'''
    search_start = 1                                              # задаём нижнюю границу поиска
    search_finish = 100                                           # задаём верхнюю границу поиска
    predict = middle_area(search_start, search_finish)            # задаём начало поиска 
    count = 1                                                     # начинаем подсчёт числа попыток
    while number != predict:
        count+=1
        if number > predict: 
            search_start = predict + 1
            predict = middle_area(search_start, search_finish)
        elif number < predict: 
            search_finish = predict - 1
            predict = middle_area(search_start, search_finish)
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v3)


# In[ ]:




