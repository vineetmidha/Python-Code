# Student Administration System - My Captain

import csv

# User Defined Function to manage menu

def menu():
    while True:
        print("Student Administration Tool")
        print("===========================")
        print('1. Register New Student')
        print('2. Display All Students')
        print('3. Exit')
        
        choice=input('Enter choice [1-3]: ')

        if choice == '1':
            add_new()
        elif choice == '2':
            display_all()
        elif choice == '3':
            break
        else:
            print('Invalid choice')

# User Defined Function to write/add new record in the CSV file

def add_new():

    print('New Student Registration')
    print('========================')
    
    name = input('Enter Name: ')
    name = name.upper()

    age = input('Enter Age: ')

    address = input('Enter Address: ')
    address = address.upper()
   
    record = [name, age, address]   # pack data in a list

    ans = input("Want to save (y/n): ")

    # Write data onto file
    
    if ans == 'y' or ans == 'Y':
        with open('student.csv', 'a', newline='') as f:     # file opened in "append" mode
            writer = csv.writer(f)                          # create writer object

            if f.tell() == 0:                               # Check if the file is empty
                writer.writerow(['Name','Age','Address'])   # Write header row in the file

            writer.writerow(record)                         # Write record in the file

        print("Record saved successfully.")
        input("Press any key to continue...")

# User Defined Function to display all the records from the CSV file

def display_all():
    print('Display All Records')
    print('===================')

    with open('student.csv', 'r') as f:         # File opened in "read" mode
        reader = csv.reader(f)                  # Create reader object
        
        for row in reader:                      # Loop to read each row/line of the file
            for element in row:                 # Nested loop to read each element of the line
                print(element, end=' ')
            print()

    input("Press any to continue...")    

menu()

'''

OUTPUT:


Student Administration Tool
===========================
1. Register New Student
2. Display All Students
3. Exit
Enter choice [1-3]: 1

New Student Registration
========================
Enter Name: vineet
Enter Age: 46
Enter Address: delhi
Want to save (y/n): y
Record saved successfully.
Press any key to continue...

Student Administration Tool
===========================
1. Register New Student
2. Display All Students
3. Exit
Enter choice [1-3]: 1

New Student Registration
========================
Enter Name: aashish
Enter Age: 23
Enter Address: kerala
Want to save (y/n): y
Record saved successfully.
Press any key to continue...

Student Administration Tool
===========================
1. Register New Student
2. Display All Students
3. Exit
Enter choice [1-3]: 1

New Student Registration
========================
Enter Name: arav
Enter Age: 12
Enter Address: delhi
Want to save (y/n): y
Record saved successfully.
Press any key to continue...

Student Administration Tool
===========================
1. Register New Student
2. Display All Students
3. Exit
Enter choice [1-3]: 2

Display All Records
===================
Name Age Address 
VINEET 46 DELHI 
AASHISH 23 KERALA 
ARAV 12 DELHI 
Press any to continue...

Student Administration Tool
===========================
1. Register New Student
2. Display All Students
3. Exit
Enter choice [1-3]: 4
Invalid choice

Student Administration Tool
===========================
1. Register New Student
2. Display All Students
3. Exit
Enter choice [1-3]: 3

'''
