'''
You are given two inputs, first is the number of words, next are words which will be passed seperatly through commands.
Print how many unique whole words are there and how many times they occure.

Hackerrank link: https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
'''
num = int(input())

list_words = []

for i in range(num):
    list_words.append(input())
 
occurance = {}
for word in list_words:
    if word in occurance:
        occurance[word] += 1
    else:
        occurance[word] = 1

print(len(occurance))

for value in occurance.values():
    print(value, end = " ")
