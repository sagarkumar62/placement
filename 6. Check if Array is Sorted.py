def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Example usage:
input_array = [1, 2, 3, 4, 5]
is_sorted_array = is_sorted(input_array)
print(f"Is array sorted: {is_sorted_array}")


