length = int(input("Введите колво элементов списка: "))
numb =[0]*length
for i in range (0,length ):
    numb [i] = int(input("Введите число: "))
numbers_2=[0]*length

for i in range(0,length):
    numbers_2[i] = pow(numb [i],2)
print(numbers_2)

