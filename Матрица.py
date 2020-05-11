#Сформувати функцію для обчислення індексу максимального елемента масиву
#n*n, де 1<=n<=5.
#Павлюк Владислав
import random
import numpy as np
N=int(input("Введите размер матрицы:"))
while N>=5 or N<=1:# проверка на размерность
    N=int(input("Введите размер матрицы:"))
matrix=np.array([[random.randint(1,25) for i in range(N)] for j in range(N)])#инициализируем матрицу
print(matrix)
def matr_iter(matrix):#Решим с помощью итерации
  radok=0
  stolb=0
  max = matrix[0][0]
  for i in range(N):#Проходимся по рядам и столбцам
    for j in range(N):
        if(matrix[i][j]>max):#Если значение больше нашей пустой переменной,мы запишем его в нашу переменную
            max=matrix[i][j]#Будет выполняться до тех пор,пока не найдется первое максимальное значение
            radok=[i]#В одну переменную запишем индекс ряда
            stolb=[j]#В другую индекс столбца
  print((radok),(stolb))
matr_iter(matrix)#Решим рекурсивно
def matr_rec(matrix,count=0,count1=0,i=0,j=0):
    if count1==len(matrix[count]):# Будем присваивать значению count(что является рядом)+1 до тех пор,пока он не будет соответсвовать длинне матрице
            count+=1
            count1=0
    if count==len(matrix):#Когда условие выполниться вернем наши i и j,которые равны нулю
            return i, j
    if matrix[count][count1]>matrix[i][j]:#Тут мы ищем индекс максимального элемента,и наше i приймет значение ряда(count),а j значение столбца(count1)
            i=count
            j=count1
    count1+=1
    return matr_rec(matrix,count,count1,i)
print(matr_rec(matrix))
#В данной задаче намного удобнее будет использовать циклы,код намного читабельнее и компактней.
#Так же решение через рекурсию сильно усложняет задачу и ее решение.
