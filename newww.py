from codecs import replace_errors
from zoneinfo import reset_tzpath


def isPalindreom(n:int) ->bool:
    s=str(n)
    return s==s[:: -1]
print(isPalindreom(123))

#romar to integer


def romartotal(s:str) ->int:
    roman={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,

    }
    total=0
    for i in range(len(s)):
        if i+1 <len(s) and roman[s[i]] < roman[s[i+1]]:
            total -=roman[s[i]]
        else:
            total+=roman[s[i]]
    return total

print(romartotal("MCMXCIV"))

#longest comon prefix

def longestcommonPrefix(strs: list[str])  -> str:


    if not strs:
        return ""

    prefix=strs[0]

    for i in strs[1:]:
        while not i.startswith(prefix):
            prefix=prefix[:-1]
            if prefix =='':
                return ''

    return prefix



print(longestcommonPrefix(["nishat", "nishu", "ni"]))







def isvalid(s:str) ->bool:
    stack=[]

    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping:
            top_element=stack.pop() if stack else '#'
            if mapping[char] !=top_element:
                return False

        else:
            stack.append(char)
    return not stack
print(isvalid("()[]{}"))    # True
print(isvalid("(]"))        # False


def isValid(s:str) ->bool:
    stack=[]
    map= {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in map:
            top_element=stack.pop() if stack else  '#'
            if map[char] !=top_element:
                return False
        else:
            stack.append(char)
    return not stack
print(isvalid("()[]{}"))    # True
print(isvalid("(]"))


def isvalid(s:str) ->bool:
    stack=[]
    map = {")": "(", "]": "[", "}": "{"}


    for char in s:
        if char in map:
            top_element=stack.pop() if stack else '#'
            if map[char] !=top_element:
                return False
        else:
            stack.append(char)
    return not stack
print(isvalid("()[]{}"))    # True
print(isvalid("(]"))

def isvalid(s:str) ->bool:
    stack =[]
    map= {")": "(", "]": "[", "}": "{"}

    for i in s:
        if i in map:
            top_element=stack.pop() if stack else '#'
            if map[i] !=top_element:
                return False
        else:
            stack.append(i)
    return not stack
print(isvalid("()[]{}"))

print(isvalid("(]"))


def isvalid(s:str) ->bool:
    stack=[]
    map= {")": "(", "]": "[", "}": "{"}
    for i in s:
        if i in map:
            top_element=stack.pop() if stack else '#'
            if map[i] !=top_element:
                return False
        else:
            stack.append(i)
    return not stack
print(isvalid("()[]{}"))





def longestcommonprefix(strs:list[str]) ->str:

 if not strs:
     return ''

 prefix=strs[0]
 for i in strs[1:]:
     while not i.startswith(prefix):
         prefix=prefix[:-1]
         if prefix == '':
             return ''



 return prefix
print(longestcommonprefix(["nishat", "nishu", "ni"]))

def longestcommonprefix(strs:list[str]) -> str:
    if not strs:
        return ''
    prefix=strs[0]
    for i in strs[1:]:
        while not i.startswith(prefix):
            prefix=prefix[ :-1]
            if prefix =='':
                return ''
    return prefix
print(longestcommonprefix(["nishat", "nishu", "ni"]))





