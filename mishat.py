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


def lengthofSubstrig(s):
    char_set=set()
    left=0
    max_len=0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        char_set.add(s[right])

        max_len=max(max_len,right - left +1)

    return max_len
print(lengthofSubstrig('nuri'))



def lengthofSubstring(s):
    char_set=set()
    left=0
    max_len=0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        char_set.add(s[right])

        max_len=max(max_len,right - left +1)
    return max_len
print(lengthofSubstrig('nishat'))




def lenght(s):
    char_set=set()
    left=0
    max_len=0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1
        char_set.add(s[right])
        max_len=max(max_len,right -left +1)
    return max_len
print(lengthofSubstrig('nishat'))





def findMedianSortedArrays(nums1, nums2):
    merged = []
    i = j = 0
    m, n = len(nums1), len(nums2)

    # Merge two sorted arrays
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Append remaining elements
    while i < m:
        merged.append(nums1[i])
        i += 1

    while j < n:
        merged.append(nums2[j])
        j += 1

    # Find median
    total = len(merged)
    mid = total // 2

    if total % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]


# Test
num1 = [2, 2]
num2 = [4, 5]
print(findMedianSortedArrays(num1, num2))


def findMedianSortedArrays(nums1, nums2):
    merged = []
    i = j = 0
    m, n = len(nums1), len(nums2)

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < m:
        merged.append(nums1[i])
        i += 1

    while j < n:
        merged.append(nums2[j])
        j += 1

    total = len(merged)
    mid = total // 2

    if total % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]


# Test
num1 = [2, 2]
num2 = [4, 5]
print(findMedianSortedArrays(num1, num2))  # Output: 3.0

def findmedian(num1,num2):
    merged=[]
    i=j=0
    m,n=len(num1),len(num2)
    while i < m and j < n:
        if num1[i] < num2[j]:
            merged.append(num1[i])
            i+=1
        else:
            merged.append(num2[j])
            j+=1
    while i < m:
        merged.append(num1[i])
        i+=1
    while j < n:
        merged.append(num2[j])
        j+=1

    total=len(merged)
    mid = total //2
    if total % 2==0:
        return (merged[mid -1] + merged[mid]) / 2
    else:
        return merged[mid]
num1=[1,2]
num2=[3,4]
print(findmedian(num1,num2))




def longestPalindrom(s):
    if len(s) > 2:
        return s

    start=0
    max_len=1

    def expend(left,right):
        while left >=0 and right <len(s) and s[left] ==s[right]:
            left -=1
            right +=1
            return  right - left -1,left +1,right -1

    for i in range(len(s)):
        len1,l1,r2=expend(i,i)
        len2,l2,r2=expend(i,i+1)

        if len1 > max_len:
            max_len=len1
            start=l1
        if len2 >max_len:
            max_len=len2
            start=l2
    return s[start:start + max_len]



def longestPalindrom(s):
    if len(s) > 2:
        return s

    start=0
    max_len=1

    def expend(left,right):
        while left >=0 and right <len(s) and s[left] ==s[right]:
            left -=1
            right +=1
            return  right - left -1,left +1,right -1

    for i in range(len(s)):
        len1,l1,r2=expend(i,i)
        len2,l2,r2=expend(i,i+1)

        if len1 > max_len:
            max_len=len1
            start=l1
        if len2 >max_len:
            max_len=len2
            start=l2
    return s[start:start + max_len]
def longestpaldrom(s):
    if len(s) < 2:
        return s

    start = 0
    max_len = 1

    def extend(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left + 1, right - 1

    for i in range(len(s)):
        len1, l1, r1 = extend(i, i)        # odd palindrome
        len2, l2, r2 = extend(i, i + 1)    # even palindrome

        if len1 > max_len:
            max_len = len1
            start = l1
        if len2 > max_len:
            max_len = len2
            start = l2

    return s[start:start + max_len]


print(longestpaldrom("babad"))  # "bab" or "aba"
print(longestpaldrom("cbbd"))   # "bb"



def longestpaldrom(s):
    if len(s) < 2:
        return s

    start=0
    max_len=1

    def extend(left,right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return right-left -1,left +1 ,right -1

    for i in range(len(s)):
        len1,l1,r1=extend(i,i)
        len2,l2,r2=extend(i,i+1)

        if len1 > max_len:
            max_len=len1
            start=l1

        if len2 > max_len:
            max_len=len2
            start=l2

    return s[start:start+max_len]
print(longestpaldrom("babad"))  # "bab" or "aba"
print(longestpaldrom("cbbd"))   # "bb"





def convert(s,numRows):
    if numRows ==1 or numRows>=len(s):
        return s
    rows=[''] *numRows
    curRow=0
    goingDwon=False
    for char in s:
        rows[curRow] +=char
        if curRow==0 or curRow==numRows-1:
            goingDwon=not goingDwon
        curRow+=1 if goingDwon else -1

    return ''.join(rows)
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"



def convert(s,numRow):
    if numRows ==1 or numRow > len(s):
        return s
    rows=[''] * numRows

    curRow=0
    goingDwon=False
    for char in s:
        rows[curRow] +=char
        if curRow ==0 or curRow ==numRows -1:
            goingDwon=not goingDwon
        curRow +=1 if goingDwon else  -1

    return '' .join(rows)
s = "PAYPALISHIRING"
numRows =3
print(convert(s,numRows))


def findmedian(num1,num2):
    merged=[]
    i=j=0
    n,m=len(num1) ,len(num2)

    while i < n and j <m:
        if num1[i] < num2[j]:
            merged.append(num1[i])
            i+=1
        else:
            merged.append(num2[j])
            j+=1
    while i < m:
        merged.append(num1[i])
        i+=1
    while j <n:
        merged.append(num2[j])
        j+=1
    total = len(merged)
    mid = total //2
    if total % 2==0:
        return (merged[mid-1] + merged[mid]) /2
    else:
        return merged[mid]
num1=[3,4]
num2=[3,4]
print(findmedian(num1,num2))


def isvalid(s):
    st=[]
    mp = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in mp:
            if not st or st[-1] !=mp[ch]:
                return False
        else:
            st.append(ch)

    return len(s) ==0
print(isValida("()[]{}"))   # Example test


def findmedian(num1,num2):
    merged=[]
    i = j =0

    m,n = len(num1),len(num2)

    while i < n  and j < m:
        if num1[i] < num2[j]:
            merged.append(num1[i])
            i+=1
        else:
            merged.append(num2[j])
            j+=1
    while i < n :
        merged.append(num1[i])
        i+=1
    while j < m:
        merged.append(num2[j])
        j+=1
    total=len(merged)
    mid= total //2

    if total % 2==0:
        return (merged[mid -1] + merged[mid]) /2
    else:
        return merged[mid]
num1 = [2, 2]
num2 = [4, 5]
print(findMedianSortedArrays(num1, num2))


def mergeTwoList(list1,list2):
    result=[]
    i,j =0,0
    while i <len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j +=1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result
print(mergeTwoList([1,2,3],[2,3,4]))

