def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

# Example usage:
input_array = [1, 2, 2, 3, 4, 4, 5]
unique_elements = remove_duplicates(input_array)
print(f"Unique elements: {unique_elements}")