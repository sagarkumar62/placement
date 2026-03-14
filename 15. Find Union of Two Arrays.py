# def union(nums1, nums2):

#         result = []

#         for num in nums1:
#             if num not in result:
#                 result.append(num)

#         for num in nums2:
#             if num not in result:
#                 result.append(num)

#         return result

def union(nums1, nums2):

        s = set(nums1)

        for num in nums2:
            s.add(num)

        return list(s)


arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

union_arr = union(arr1,arr2)
print(union_arr)