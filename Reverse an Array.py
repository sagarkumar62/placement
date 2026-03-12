def reverse_an_array(arr):
    # return arr[::-1]
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example usage:
input_array = [1, 2, 3, 4, 5]
reversed_array = reverse_an_array(input_array)
print(reversed_array)  # Output: [5, 4, 3, 2, 1]

# print("Hello, World!")
