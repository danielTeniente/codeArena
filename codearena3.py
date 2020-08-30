# Write your code here
T = int(input())
for i in range(T):
    N = int(input())
    lista = input().split()
    suma = 0
    for j,num in enumerate(lista):
        lista[j]=int(num)
        suma += lista[j]
        
    print('{0:.8f}'.format(suma/N))