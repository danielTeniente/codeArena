lista = input().split() 
count = 0
factorial = 1
suma = 0

for i,num in enumerate(lista):

    if(num != "0"):

        count +=1
    lista[i] = int(num)
    suma += lista[i]

if(suma%2 != 0):
    count -=1

for i in range(1, count+1):

    factorial *= i 
print(factorial)