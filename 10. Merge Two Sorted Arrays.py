def merge_two_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        # Changed < to <= for stability
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements of arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Add remaining elements of arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


# Example
arr1 = [1,1,2,2]
arr2 = [2,3]

print(merge_two_sorted_arrays(arr1, arr2))