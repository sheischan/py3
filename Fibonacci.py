'''
Fibonacci series.
0 1 1 2 3 5 8 13 21 34 
'''
def fibonacci(a,b):
    return a + b
print("How many fibonacci numbers you want to see?")
f = int(input())

j = 0
k=1
for i in range(0,f,2):
    j = fibonacci(j,k)
    k=k+j
    print(j,end=" ")
    print(k,end=" ")
    
