def two_sum(nums,terget):
    seen={}
    for i ,n in enumerate(nums):
        rem=terget - n
        if rem in seen:
            return [seen[rem],i]

        seen[n] =i
print(two_sum([2,3,4,5,7],9))


def maxprofite(prices):
    buy=prices[0]
    profit=0
    for p in prices:
        buy=min(buy,p)
        profit=max(profit,p-buy)
    return profit
print(maxprofite([2,3,4,5,6,7]))

def maxProfit(prices):
    buy=prices[0]
    profit=0
    for p in prices:
        buy=min(buy,p)
        profit=max(profit,p-buy)
    return profit
print(maxProfit([2,3,4,5,6,7,8,9,0]))


def isValid(s):
    st=[]
    mp = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in mp:
            if not st or st.pop() !=mp[ch]:
                return False
        else:
            st.append(ch)
    return not st
print(isValid("()[]{}"))   # Example test

def findMedianSortedArray(num1, num2):
    merged = []
    i = j = 0
    m, n = len(num1), len(num2)

    # Merge two sorted arrays
    while i < m and j < n:
        if num1[i] < num2[j]:
            merged.append(num1[i])
            i += 1
        else:
            merged.append(num2[j])
            j += 1

    # Remaining elements
    while i < m:
        merged.append(num1[i])
        i += 1

    while j < n:
        merged.append(num2[j])
        j += 1

    # Find median
    total = len(merged)
    mid = total // 2

    if total % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]


num1 = [1, 2]
num2 = [2, 3]
print(findMedianSortedArray(num1, num2))
