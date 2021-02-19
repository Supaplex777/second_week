list_1 =['Петя','Вася','Костя','Игорь','Жека']

while list_1:
    if 'Костя' == list_1.pop():
        print('Привет Костя')
        break
    else:
        print('Работаю дальше')
    