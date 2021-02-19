#Создать список из десяти целых чисел.
#Вывести на экран каждое число, увеличенное на 1.

a =[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
for i in a: 
    b = i + 1
    print(b)

#Ввести с клавиатуры строку.
#Вывести эту же строку вертикально: по одному символу на строку консоли.
message = input('Введи слова:\n')

for a in message:
    print(a)

#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.





school_class = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class2': '4б', 'scores': [2,4,5,3,2]},
{'school_class3': '4в', 'scores': [4,4,4,3,5,]}
]

a = 0 # школа
b = 0 # класс  

for result in school_class:
    b=sum(result['scores'])/len(result['scores'])
    a+=sum(result['scores'])/len(result['scores'])
print(a/len(school_class))