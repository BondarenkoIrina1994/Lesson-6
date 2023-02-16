# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n=int(input('Введите количество элементов в массиве N= '))
while n<=0:
    n=float(input('Некорректное значение! Введите число больше 0:'))
my_list=[]
for i in range(n):
        a=float(input(f'Введите {i+1}-й элемент масссива:'))
        my_list.append(a)
min_number=float(input('Введите минимум:'))
max_number=float(input('Введите максимум:'))
while max_number<=min_number:
   max_number=float(input('Некорректное значение! Введите число превыщающее {min_number}:'))
print(f'Индексы элементов массива, значения которых лежат в диапазоне [{min_number},{max_number}]:')
cost=0
for i in range(len(my_list)):
      if (my_list[i]>=min_number) and ((my_list[i]<=max_number)):
            print(i)
            cost+=1
if cost==0:
     print('Таких элементов нет!!!')