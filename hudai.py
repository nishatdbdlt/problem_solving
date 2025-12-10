# def lengthoflongsubstirg(s :str)  ->int:
#     seen =set()
#     left =0
#     max_length = 0
#     for right in range(len(s)):
#         while s[right] in seen:
#             seen.remove(s[left])
#             left+=1
#         max_length=max(max_length,right - left + 1)
#
#
#     return max_length
# print(lengthoflongsubstirg('sbdbcbdbd')
#
def lengthoflongsubstring(s: str) ->int:
    seen =set()
    left= 0
    max_length =0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1
        seen.add(s[right])
        max_length=max(max_length,right - left + 1)
    return max_length
print(lengthoflongsubstring('nishat'))



def lenghtofongsubstring(s: str) ->int:
    seen = set()
    left =0
    max_lenght=0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1
        seen.add(s[right])
        max_lenght=max(max_lenght,right - left + 1)
    return max_lenght
print(lenghtofongsubstring("sbddcdbd"))


def lenghtofsubstring(s :str) ->int:
    seen=set()
    left=0
    max_length=0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_length=max(
                      max_length,right - left +1
        )
    return max_length
print(lenghtofsubstring("SBDSADSS"))




def findMedianSortedArray(num1,num2):
    marged = sorted(num1 + num2)
    n = len(marged)
    mid = n //2
    if n % 2 ==0:
        return marged[mid - 1] + marged[mid] /2
    else:
        return marged[mid]

print(findMedianSortedArray([1,2],[2.4]))



def findmedinasortedArray(num1, num2):
    marged = sorted(num1 + num2)
    n =len(marged)
    mid = n // 2

    if n % 2 ==0:
        return marged[mid - 1] + marged[mid] /2
    else:
        return marged[mid]
print(findmedinasortedArray([1,3],[3,4]))






def findmediansortedarrat(num1,num2):
    marged=sorted(num1 + num2)
    n = len(marged)
    mid = n //2

    if n % 2 == 0:
        return marged[mid -1] + marged[mid] /2
    else:
        return marged [mid]
print(findmedinasortedArray([2,3],[4,9]))



def finding(num1,num2):
    marged =sorted(num1 + num2)
    n =len(marged)
    mid = n // 2

    if n % 2 ==0:
        return marged[mid -1 ] + marged[mid] / 2
    else:
        return marged[mid]
print(finding([2,3],[4,9]))



def longestpalindrom(s: str) -> str:
    def expandAroundcenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # return palindrome substring after expanding
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        odd = expandAroundcenter(i, i)
        # Even length palindrome
        even = expandAroundcenter(i, i + 1)

        # Update the longest
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even

    return longest

print(longestpalindrom('babad'))
