#Сформувати функцію, що буде обчислювати факторіал заданого користувачем
#натурального числа n.
#Павлюк Владислав
import sys
x=int(input('Введите число'))
def fact_rec(x):# Найдем наш факториал с помощью рекурсии,будем вызывать нашу функцию до тех пор,пока х не приймет значение 1
    if x==1: 
        return 1
    else:
       return fact_rec(x-1)*x 
sys.setrecursionlimit(x+100)#Увеличим количество вызовов рекурсии
print(fact_rec(x))
def fact_iter(x):#Найдем наш факториал с помощью итерации
    count=1
    for i in range(1,x+1):#Cоздадим обычный цикл,и перемножим все цифры от 1 до х+1 и запишем это в наш счетчик
        count*=i
    print(count)
fact_iter(x)
#В данной задаче проще и удобнее будет использовать рекурсию,код более читабелен в отличие от варианта с итерацией.
#И его проще реализовать.
