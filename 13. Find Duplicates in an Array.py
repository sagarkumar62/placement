def duplicates_in_array(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

    
        
arr = [1, 2, 3, 4, 2, 5, 1]
print(duplicates_in_array(arr))