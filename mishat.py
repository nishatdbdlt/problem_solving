from pkgutil import resolve_name, iter_modules
from pydoc import replace
from sqlite3 import SQLITE_CONSTRAINT_UNIQUE
from zoneinfo import reset_tzpath

from prectice import finonacii


def even_num(num):
    total=0
    for i in num:
        if i % 2 ==0:
            total += i
    return total
print(even_num([3,4,5,6,7,8]))

def ood_number(num):
    total =0
    for i in num:
        if i % 2 !=0:
            total +=i
    return total
print(ood_number([1,2,3,4,5,6,7,8,9,10]))


def is_palnidrome(s):
    s = s. lower().replace('','')
    return s == s[: : -1]
print(is_palnidrome('nishat'))
print(is_palnidrome('madam'))

def is_plandrome(s):
    s = s . lower() . replace('','')
    return s==s[: : -1]
print(is_plandrome('madam'))
print(is_palnidrome('bangladesh'))


def is_plandrome(s):
    s =s.lower().replace('b','a')
    return s ==s[: : -1]
print(is_palnidrome('maddam'))
print((is_palnidrome("nuri")))


def most_frequent(lst):
    freq={}
    for i in lst:
        freq[i] =freq.get(0, 1) +1
    return max(freq,key=freq.get)
print(most_frequent([1,2,4,5,6,7,8]))






def fibonacci(s):
    a, b = 0, 1
    result = []
    for _ in range(s):
        result.append(a)
        a , b = b , a+b
    return result
print(fibonacci(9))

#
# def remove_duplicate(s):
#     items=s.split()
#     unique=[]
#     for item in items:
#         item= item.strip()
#         if item not in unique:
#             unique.append(item)
#     return ', ' .join(unique)
# text = 'naim nishat oenk'
# print(remove_duplicate(text)



def remove_duplicte(s):
    items=s.split()
    unique=[]
    for item in items:
        item= item.strip()
        if item not in unique:
          unique.append(item)
    return ',' .join(unique)
text='nishat, nuiii,mm'
print(remove_duplicte(text))
