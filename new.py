#
#
# s ='education'
# vowels =0
# for ch in s:
#     if ch .lower() in 'aeiou':
#         vowels +=1
#
# print(vowels)
#
# s ='education'
# vowels = 0
# for ch in s:
#     if ch .lower()in 'aeiou':
#         vowels +=1
# print(vowels)
#
# test = 'madam'
# if test==test[::-1]:
#     print('palindrome')
# else:
#     print(" not palindrome")
#
# s ='ppppp'
# vowels =0
# for ch in s:
#     if ch.lower() in 'aeiou':
#         vowels+=1
# print(vowels)
#
#
#
# test ='madam'
# if test == test[::-1]:
#     print('palindrome')
# else:
#     print("not palindrome")
from typing import reveal_type

# nums = [12, 7, 19, 4, 19, 15]
# lergest= nums[0]
# for num in nums:
#     if num > lergest:
#         lergest= num
#
# secound = None
# if num !=lergest:
#     if secound is  None or num > lergest:
#         secound = num
# print(secound)
#
#
#


nums = [2,3,4,5,6,7,8,9]
lergest = None
secound =None
for num in nums:
    if lergest is None or num > lergest:
        secound = lergest
        lergest = num
    elif num !=lergest:
        if secound is None or num > lergest:
            secound = num
print(secound)

#
# s = "I am learning python programming".strip()
# count = 0
# is_word = False
#
# for ch in s:
#     if ch != " ":          # single space check
#         if not is_word:    # new word start
#             count += 1
#             is_word = True
#     else:
#         is_word = False    # space → word sesh
#
# print("Total words =", count)

s = "I am learning python programming".strip()
count =0
is_word =False

for ch in s:
     if ch !=" ":
         if not is_word:
             count +=1
             is_word =True
     else:
         is_word=False
print(count)




digit=2345
sum =0
while digit > 0:
    num = digit %10
    sum +=num
    digit = digit // 10
print(sum)


num = 234556

sum =0
while num > 0:
    digit = num % 10
    sum +=digit
    num = num // 10
print(sum)


s = 'nishat'
count = {}
for ch in s:
    if ch in count:
        count[ch] +=1
    else:
        count[ch] =1
for ch, count in count.items():
    print(f"{ch} : {count}")

n = 'bangladesh'

count ={}
for ch in n:
    if ch in count:
        count[ch] +=1
    else:
        count[ch] =1
print(count)

