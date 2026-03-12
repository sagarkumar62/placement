# def rotate_array(arr,k):
    # while k > 0:
    #     temp = arr[0]
    #     for i in range(len(arr) - 1):
    #         arr[i] = arr[i + 1]
    #     arr[len(arr) - 1] = temp
    #     k -= 1
    # return arr
    
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    temp = arr[0:k]
    for i in range(n - k):
        arr[i] = arr[i + k]
    arr[n - k:] = temp
    return arr

# Example usage:
input_array = [1, 2, 3, 4, 5]
k = 3
rotated_array = rotate_array(input_array, k)
print(f"Rotated array: {rotated_array}")
    