def find_second_largest_element(arr):
    largest = arr[0]
    second_largest = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest
    

# Example usage:
input_array = [3, 5, 1, 8, 2]
second_largest_element = find_second_largest_element(input_array)
print(f"Second largest element: {second_largest_element}")