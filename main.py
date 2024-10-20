spisok = input("Введите список ") # Получение списка от пользователя
a = [int(i)*int(i) for i in spisok.split()] # Создание генератора списка 
print(a) # Вывод списка
