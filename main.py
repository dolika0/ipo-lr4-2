print("Введите список")#вывод инф-ции на экран
spisok=list(map(int,input().split()))#создание списка
print(spisok)#вывод списка
i=0#присвивание значения 
for n in spisok :#создание списка
   spisok[i]=n**2#возведение элементов списка в квадрат
   i=i+1#увеличение i на один
print(spisok)#вывод списка

    

#length = int(input("Введите колво элементов списка: "))
#numb =[0]*length
#for i in range (0,length ):
  #  numb [i] = int(input("Введите число: "))
#numbers_2=[0]*length

#for i in range(0,length):
#    numbers_2[i] = pow(numb [i],2)
#print(numbers_2)




