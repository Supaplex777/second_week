import random
def name(a):
    try:
        p = 1/a 
        print(p)
    except ArithmeticError:
        print('не надо делить на ноль')
    except TypeError:
        print('Программа принимает число')
name(0)  

while True:
    name(random.randint(0,1))
    








    