#!/usr/bin/env python3 
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7, 10, 2]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']


#elemtype=input('Enter type:')
elem=input('Enter elem:')


num_list.reverse()
x=len(num_list) - num_list.index(int(elem)) - 1
num_list.reverse()

word_list.reverse()
textelem=input('Enter text:')
y=len(word_list) - word_list.index(textelem) - 1
word_list.reverse()

print(num_list)
print(x)
print(word_list)
print(y)
