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
