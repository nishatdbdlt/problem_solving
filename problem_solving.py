from functools import total_ordering
from os import sendfile
from pydoc import replace
from unittest import removeResult

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

def most_frequent(lst):
    freq ={}
    for i in lst:
        freq[i] = freq.get(i ,0) + 1
    return max(freq, key=freq.get)
print(most_frequent([2,3,4,5,6,7,8,]))


def most_letter(lst):
    freq= {}
    for i in lst:
        freq[i] = freq.get(i,0) + 1
    return max(freq,key=freq.get)
print(most_letter([3,4,5,6,7,8,9,33,33,33]))
#palindrome
def is_palindrome(s):
    s = s.lower() .replace( " ", "")
    return  s == s[:: -1]
print(is_palindrome('madaM'))
print(is_palindrome('nishat'))


def is_palindrome(s):
    s = s.lower() .replace("" , " ")
    return s == s[: : -1]
print(is_palindrome("Nishat"))

def is_palindrome(s):
    s =s.lower(). replace(" ","")
    return s ==s[: : -1]
print(is_palindrome('nishaT'))
print(is_palindrome("madam"))

def is_palindrome(s):
    s = s.lower(). replace("" ,"")
    return  s ==s[:: -1]
print(is_palindrome("NishaT"))
print(is_palindrome("madaM"))


def is_palindrome(s):
    s = s.lower(). replace(" ","")
    return s==s[: : -1]
print(is_palindrome("Nishat"))

def remove_duplicate(lst):
    resutl =[]
    for i in lst:
        if i not in resutl:
            resutl.append(i)
    return resutl
print(remove_duplicate([3,4,5,6,6,7,4,3]))


def remove_duplicate(lst):
    list=[]
    for i in lst:
        if i not in list:
            list.append(i)
    return list
print(remove_duplicate([33,33,3,2,]))

def remove_dupicate(s):
    word=s.split(' ,')
    qnique=[]
    for w in word:
        if w not in qnique:
            qnique.append(w)
    return ", " .join(qnique)
print(remove_dupicate("nishat,nishat,"))


def remove_duplicate(s):
    word = s.split(',')
    unique = []
    for w in word:
        w = w.strip()
        if w not in unique:
            unique.append(w)
    return ",".join(unique)

print(remove_duplicate("nishat,nishat ,n,m,m,n"))


def marge_and_sort(a,b):
    return sorted( a + b)
print(marge_and_sort([3,4,5],[4,5,6]))


def marge_and_sort(a,b):
    return sorted(a+ b)
print(marge_and_sort([2,3,4,5,6],[0,9,8,87,]))


def marge_sort(a,b):
    return sorted(a+b)
print(marge_sort([2,3,4],[4,5,6]))

def fibonacci(n):
    a,b = 0,1
    result =[]
    for _ in range(n):
        result.append(a)
        a,b = b,a +b
    return result
print(fibonacci(6))


def fibonacci(s):
    a,b = 0,1
    result =[]
    for _ in range(s):
        result.append(a)
        a,b = b,a+b
    return result
print(fibonacci(7))


def fabinocci(s):
    a,b = 0,1
    result =[]
    for _ in range(s):
        result.append(a)
        a,b = b ,a +b
    return result
print(fibonacci(10))