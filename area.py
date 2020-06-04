# Two Tasks are there in this file

# Task-1 --> Accept radius of circle and find area

radius = float(input('Enter radious of the circle: '))

print('The area of the circle with radius', radius, 'is:',3.14*radius*radius)

'''
OUtput

Enter radious of the circle: 1.1
The area of the circle with radius 1.1 is: 3.7994000000000008

'''

# Task-2 --> Input filename and display extension

file_name = input('Enter file name: ')

if '.' in file_name:              # Check if dot (.) exists in the file name
    index = file_name.find('.')   # Find out index of dot (.)
    print('Extension:', file_name[index+1:])  # Display extension using slicing from index + 1 onwards
else:
    print('Extension not found')   # Error message if dot (.) not found

'''
Output

Case-1
======
Enter file name: abc.py
Extension: py

Case=2
======
Enter file name: abc
Extension not found

'''
