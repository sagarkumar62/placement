# def find_pair_with_given_sum(arr, target_sum):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target_sum:
#                 return arr[i], arr[j]
#     return None

def find_pair_with_given_sum(arr, target):
    arr.sort()   # if not already sorted
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None
# Example usage:
input_array = [1, 2, 3, 4, 5]
target_sum = 7
pair = find_pair_with_given_sum(input_array, target_sum)
print(f"Pair with given sum: {pair}")