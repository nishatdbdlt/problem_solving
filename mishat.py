from functools import total_ordering


def isValida(s):
    st = []
    mp = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in mp:
            # closing bracket
            if not st or st[-1] != mp[ch]:
                return False
            st.pop()
        else:
            # opening bracket
            st.append(ch)

    return len(st) == 0

print(isValida("()[]{}"))   # Example test



def isValid(s):
    st=[]
    mp = {")": "(", "]": "[", "}": "{"}


    for ch in s:
        if ch in mp:
            if not st or st[-1] !=mp[ch]:
                return False
            st.pop()
        else:
                st.append(ch)

    return len(st) ==0
print(isValida("()[]{}"))   # Example test

def addTWonum(l1,l2):
    result = []
    carry=0
    i =0
    while i < len(l1) or i < len(l2) or carry:
        val1=l1[i] if i < len(l1) else 0
        val2=l2[i] if i < len(l2) else 0
        total= val1 + val2 + carry
        result.append(total % 10)
        carry = total // 10
        i +=1
    return result
l1 = [2, 4, 3]   # 342
l2 = [5, 6, 4]   # 465
print(addTWonum(l1,l2))




def Twonum(l1,l2):
    result=[]
    carry=0
    i =0
    while i < len(l1) or i <len(l2) or carry:
        val1=l1[i] if i <len(l1) else 0
        val2 = l2[i] if i < len(l2) else 0
        total = val1 + val2 + carry
        result.append(total % 10)
        carry = total //10
        i +=1
    return result
l1=[2,3,4]
l2=[3,4,5]

print(Twonum(l1,l2))
