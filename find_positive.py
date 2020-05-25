a = []

while True:
    n = int(input('Enter a number [0 to exit]: '))
    
    if n == 0:
        break
        
    a.append(n)
    
for x in a:
    if x > 0:
        print(x, end=',')

'''
OUTPUT:

Enter a number [0 to exit]: 12
Enter a number [0 to exit]: -7
Enter a number [0 to exit]: 5
Enter a number [0 to exit]: 64
Enter a number [0 to exit]: -14
Enter a number [0 to exit]: 0
12,5,64,

'''
