def remove_given_element(arr, element):
    return [x for x in arr if x != element]

# Example usage:
arr = [3, 1, 2, 3, 4, 3]
element_to_remove = 3
result = remove_given_element(arr, element_to_remove)
print(result)  # Output: [1, 2, 4]

