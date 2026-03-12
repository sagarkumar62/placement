def find_max_and_min(arr):
    max_element = arr[0]
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
        if arr[i] < min_element:
            min_element = arr[i]
    return max_element, min_element

# Example usage:
input_array = [3, 5, 1, 8, 2]
max_element, min_element = find_max_and_min(input_array)
print(f"Maximum element: {max_element}")
print(f"Minimum element: {min_element}")