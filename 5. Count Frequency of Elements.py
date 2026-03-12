def count_frequency_of_elements(arr):
    frequency = {}
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

# Example usage:
input_array = [1, 2, 3, 4, 5]
frequency_of_elements = count_frequency_of_elements(input_array)
print(f"Frequency of elements: {frequency_of_elements}")