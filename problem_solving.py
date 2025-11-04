from functools import total_ordering
from os import sendfile

print('nishat')

def reverse_string(s):
    return s[:: -1]
print(reverse_string('nishat'))


def reverse_string(s):
    return s[: : -1]
print(reverse_string('abhi'))


def even_num(nums):
    total = 0
    for n in nums:
        if n % 2 ==0:
            total +=n
            return total
print(even_num([2,5,8,90]))



def even_num(nums):
    total =0
    for n in nums:
        if n % 2 == 0:
            total += n
            return total
print(even_num([3,5,6,7,8,9,122]))

def ood_number(nums):
    total =0
    for n in nums:
        if n % 2 !=0:
            total +=n
    return total
print(ood_number([3,4,5,6,7,22]))

def word_frequency(sentance):
    words=sentance.split()
    freq ={}
    for w in words:
        freq[w] = freq.get(w,0) +1
    return freq
print(word_frequency("nishat is a , good boy boy"))


def word_count(sentance):
    word=sentance.split()
    ferq={}
    for w in word:
        ferq[w] = ferq.get(w,0) +1
    return ferq
print(word_count('nishat nishat '))


def even_num(num):
    total =0
    for n in num:
        if n % 2 ==0:
            total +=n
    return total
print(even_num([2,3,4,5,6,7,8,9]))


def ood_num(num):
    total =0
    for n in num:
        if n % 2 !=0:
            total +=n
    return total
print(ood_num([3,4,5,6,7,8,9]))


def revesre_string(s):
    return s[:: -1]
print(revesre_string('nishat'))

def word_counter(sentence):
    word = sentence .split()
    freq ={}
    for w in word:
        freq[w] = freq.get(w ,0) + 1
    return freq
print(word_counter("nishat nisaht bangladesh bangladesh nishat nishat "))


def word_counter(sentance):
    word = sentance.split()
    freq={}
    for w in word:
        freq[w] =freq.get(w,0) + 1
    return freq
print(word_counter("nishat nishat nishat bangladesh "))