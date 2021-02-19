#Задание 2
#Написать функцию, которая принимает на вход две строки
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
#Если строки одинаковые, вернуть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты


def function_two (one_message,two_message):
    if not isinstance(one_message,str)  and not isinstance(two_message,str):        
        return 0
    elif one_message == two_message:
        return 1
    elif len(one_message)>len(two_message) and one_message!=two_message:
        return 2
    elif one_message!=two_message and two_message == 'learn':
        return 3
    

enter = function_two(1,2)
enter_1 = function_two('Привет','Привет')
enter_2 = function_two('здравствуйте','привет')
enter_3 = function_two('ок','learn')
print(enter_3)
    
