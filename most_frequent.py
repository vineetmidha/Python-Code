# Input a string and print the letters in decreasing order of their frequencies in the string.

def most_frequent(s):
    freq = {}

    for x in s:
        if x not in freq:
            freq[x] = s.count(x)

    a = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for x, y in a:
        print(x, "=", y)
    
s = input('Enter a string: ')

most_frequent(s)

'''
OUTPUT:

Enter a string: mississippi
i = 4
s = 4
p = 2
m = 1

'''
