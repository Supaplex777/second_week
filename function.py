#Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так, чтобы она 
# перехватывала исключения, когда переданы некорректные аргументы.
#Первые два нужно приводить к вещественному числу при помощи float(), а третий - к целому при помощи int() и 
# перехватывать исключения ValueError и TypeError, если приведение типов не сработало.





def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError,TypeError):
        print('Приведение типов не србаотало')
enter = discounted(10,20,'f')
print(enter)
