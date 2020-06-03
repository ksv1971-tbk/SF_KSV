#!/usr/bin/env python
# coding: utf-8

# In[7]:


def mean_area(search_start, search_finish):
    '''Функция принимает два числа - нижнюю границу поиска и верхнюю границу поиска, 
    и возвращает число, равное середине области поиска'''
    mean = (search_start + search_finish)//2
    return mean


def game_core_v3(number):
    '''Задаём нижнюю и верхнюю границы поиска.
       Сначала устанавливаем число, равное середине области поиска, 
       и если это не загаданное число - сужаем область поиска вдвое.
       Функция принимает загаданное число и возвращает число попыток'''
    search_start = 1                                              
    search_finish = 100                                           
    predict = mean_area(search_start, search_finish)          
    count = 1                                                     
    while number != predict:
        count+=1
        if number > predict: 
            search_start = predict + 1
            predict = mean_area(search_start, search_finish)
        elif number < predict: 
            search_finish = predict - 1
            predict = mean_area(search_start, search_finish)
    return(count) 


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    import numpy as np
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# запускаем алгоритм угадывания числа
score_game(game_core_v3)


# In[ ]:





# In[ ]:




