# 16. Check if Two Arrays Are Equal: if two arrays contain the same elements

def equal_arrays(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    if len1 != len2:
        return False
    
    freq = {}

    for num in arr1:
        freq[num] = freq.get(num, 0)+1

    for num in arr2:
        if num not in freq:
            return False
        freq[num]-=1
        if freq[num] < 0:
            return False
    return True


