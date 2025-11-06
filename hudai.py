def two_Sum(nums,terget):

    seen = {}
    pairs=[]

    for i , num in enumerate(nums):
        rem = terget - num
        if rem in seen:
            for index in seen[rem]:
                pairs.append([index,i])

        if num in seen:
            seen[num].append(i)
        else:
            seen[num]= [i]
    return pairs
print(two_Sum([2,3,4,5,6,7,8,9],9))