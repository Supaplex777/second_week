#Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt,
#  писала пользователю "Пока!" и завершала работу при помощи оператора break
def hello_user():
    try:
        while True:
            message = input('Привет как дела?\n')
            if message == 'Хорошо':
                print('программа закрыта')
                break
            else:
                print('программа работает')
    except KeyboardInterrupt:
        print('Пока')
hello_user()



