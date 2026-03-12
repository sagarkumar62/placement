def find_sum_of_elements(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

# Example usage:
input_array = [1, 2, 3, 4, 5]
sum_of_elements = find_sum_of_elements(input_array)
print(f"Sum of elements: {sum_of_elements}")