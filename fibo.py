
n = int(input("Enter the number of terms you want to generate: "))

a, b = 0, 1 # initialize two variables 

for i in range(n):  # loop to generate n fibonacci terms
    print(a)
    c = a + b
    a, b = b, c   # exchange of values
    
'''
OUTPUT:

Enter the number of terms you want to generate: 15
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
'''
