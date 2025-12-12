def mergeTwoList(list1,list2):
    result=[]
    i,j = 0,0

    while i <len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1

    result.extend(list1[i:])
    result.extend(list2[j:])
    return result
print(mergeTwoList([1,2,4],[4,5,6]))


def binnarysearch(nums,terget):
    left=0
    right=len(nums) -1

    while left <= right:
        mid = (left + right) //2
        if nums[mid] ==terget:
            return mid
        elif nums[mid] < terget:
            left =mid+1
        else:
            right = mid- 1

    return -1
print(binnarysearch([-1,0,3,5,9,12],9))

def binnarysearch(nums,terget):
    left =0
    right=len(nums) -1
    while left <=right:
         mid=(left + right) //2
         if nums[mid] ==terget:
             return mid
         elif nums[mid] < terget:
             left =mid + 1
         else:
             right=mid -1
    return -1
print(binnarysearch([2,3,4,5,6,7],7))


# def reverse_list(lst):
#     reversed_lst = []
#     for i in range(len(lst)-1, -1, -1):
#         reversed_lst.append(lst[i])
#     return reversed_lst
#
# # Test
# arr = [3, 4, 5, 6, 7]
# print(reverse_list(arr))

#
def reverse_list(lst):
    reverse_list=[]
    for i in range(len(lst)-1,-1,-1):
        reverse_list.append(lst[i])
    return reverse_list
arr=[3,4,5,6,7,8]
print(reverse_list(arr))


def maxSubarray(nums):
    cur=best=nums[0]
    for n in nums[1: ]:
        cur=max(n,cur+n)
        best=max(best,cur)
    return best
print(maxSubarray([2,2,3,4,5,6,7]))


def mmaxSubarray(nums):
    cur=best=nums[0]
    for i in nums[1 :] :
        cur=max(i,cur)
        best=max(best,cur)
    return best
print(maxSubarray([2,2,3,4,5,6,7]))


def maxSubArraay(nums):
    cur=best=nums[0]
    for i in nums[1:]:
        cur=max(i,cur)
        best=max(best,cur)
    return best
print(maxSubArraay([2,3,5,6,7,8]))


# def movezero(nums):
#     i =0
#     for j in range(len(nums)):
#         if nums[j] !=0:
#             nums[i],nums[j]=nums[j],nums[i]
#             i += 1
#     return nums
# arr = [3,4,5,7,9,0,12,0]
# movezero(arr)
# print(movezero(arr))


def movezero(nums):
    i =0
    for j in range(len(nums)):
        if nums[j] !=0:
            nums[i],nums[j] = nums[j],nums[i]
            i +=1
    return nums
arr=[2,3,40,0,0,0,9,5,6,7,8]
movezero(arr)
print(movezero(arr))
