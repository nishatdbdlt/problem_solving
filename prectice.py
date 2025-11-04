from codecs import replace_errors
from pydoc import replace

print('nishat')



def reverse_stirng(s):
    return  s[: : -1]

print(reverse_stirng('odoo'))


def reverse_sting(b):
    return  b[: : -1]
print(reverse_sting("Bangladesh"))


def even_number(num):
    totol = 0
    for n in num:
        if n % 2 == 0:
            totol += n
    return  totol
print(even_number([4,5,6,7,8,4,3]))


def ood_num(num):
    total =0
    for i in num:
        if i % 2 !=0:
          total +=i
    return total
print(ood_num([2,3,4,5,6,7]))


def word_frequency(sentance):
    word=sentance.split()
    freq={}
    for w in word:
        freq[w]=freq.get(w,0) + 1
    return freq
print(word_frequency("odoo nishat odoo nishat"))


def word_frequency(sentance):
    word=sentance.split()
    freq={}
    for w in word:
        freq[w] =freq.get(w,0) + 1
    return freq
print(word_frequency("odoo nishat odoo nishat developer "))


def word_frequency(nishat):
    word=nishat.split()
    freq={}
    for i in word:
        freq[i] =freq.get(i,0) + 1
    return freq
print(word_frequency('nishat nishat nishat nishat '))


def most_frequency(lst):
    freq={}
    for i in lst:
        freq[i] = freq.get(i,0) + 1
    return  max(freq,key=freq.get)
print(most_frequency([3,4,5,6,7,8,9]))



def most_frquency(list):
    freq ={}
    for i in list:
        freq[i] = freq.get(i,0) + 1
    return max(freq,key=freq.get)
print(most_frquency([5,6,7,8,9]))


def is_palindreome(s):
    s = s.lower().replace(' ' ,' ')
    return  s ==s [:: -1]
print(is_palindreome("nishat"))


def remove_duplicat(lst):
    result = []

    for i in lst:
        if i not in result:
            result.append(i)
    return result
print(remove_duplicat([1,2,3,4,4,5,5,6,]))

def remove_duplicate(list):
    result =[]
    for i in list:
        if i not in result:
            result.append(i)
    return  result
print(remove_duplicate([3,3,4,5,6]))


def mardg_sort(a,b):
    return sorted(a + b)
print(mardg_sort([2,3,4],[5,6,7]))


def marge_sort(a ,b):
    return sorted(a + b )
print(mardg_sort([2,3,4,5],[4,5,6,7]))

def scond_number(nums):
    unique=list(set(nums))
    unique.sort()
    return unique[-2]
print(scond_number([2,3,4,5,6,7]))


def large_number(num):
    unique=list(set(num))
    unique.sort()
    return unique[-2]
print(large_number([3,4,5,6,7,8,]))


def fibonacii(n):
    a,b = 0,1
    result= []
    for _ in range(n):
        result.append(a)
        a,b = b , a+b

    return result
print(fibonacii(8))

def finonacii(n):
    a ,b =0,1
    result =[]
    for _ in range(n):
        result.append(a)
        a,b =b ,a +b
    return result
print(finonacii(6))


def finonacii(n):
    a,b =0,1

    result =[]
    for _ in range(n):
        result.append(a)
        a,b = b , a + b
    return result
print(finonacii(6))