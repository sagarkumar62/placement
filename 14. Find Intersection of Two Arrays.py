# 14. Find Intersection of Two Arrays: Find the common elements between two arrays.

# def intersection_of_two_array(arr1, arr2):
#     d = []
#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 d.append(i)
#     return list(set(d))

# arr1 = [1,2,2,1]
# arr2 = [2,2,1]

# inter = intersection_of_two_array(arr1,arr2)

# print(inter)


# def intersection_of_two_array(arr1, arr2):
#     set1 = set(arr1)
#     result = set()

#     for num in arr2:
#         if num in set1:
#             result.add(num)

#     return list(result)


# arr1 = [1,2,2,1]
# arr2 = [2,2,1]

# inter = intersection_of_two_array(arr1, arr2)

# print(inter)


def intersection_of_two_array(arr1, arr2):
    arr1.sort()
    arr2.sort()

    i =0
    j = 0

    result = []

    while i< len(arr1) and j<len(arr2):
        if arr1[i] == arr2[j]:

            if arr1[i] not in result:
                result.append(arr1[i])

            i+=1
            j+=1

        else:
            i+=1
            j+=1

    return result

arr1 = [1,2,2,1]
arr2 = [2,2,1]

inter = intersection_of_two_array(arr1, arr2)

print(inter)