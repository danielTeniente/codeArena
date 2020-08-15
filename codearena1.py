'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

T = int(input() )
for i in range(T):
    input_sample = input().split()
    N = int(input_sample[0] )
    D = int(input_sample[1] )
    
    numeros = input().split()
    for i,num in enumerate(numeros):
        numeros[i] = int(num)
    bandera = False
    for i in range(1,len(numeros)):
        diferencia = (numeros[i]-numeros[i-1])
        if(diferencia<0):
            diferencia = -1*diferencia
        if(diferencia<=D):
            print("YES")
            bandera = True
            break
    if(not bandera):
        print("NO")
        

            


