length = int(input("Введите колво элементов списка: ")) #запрос от пользователя
numb =[0]*length #задание длины массива
for i in range (0,length ):#составление цикла 
    numb [i] = int(input("Введите число: "))#задание значений элемента
numbers_2=[0]*length#задание длины массива
for i in range(0,length):#созданеи цикла
    numbers_2[i] = pow(numb [i],2)# возведение в степень 
print(numbers_2)#вывод на экран

