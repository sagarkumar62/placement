# 12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

def find_the_missing_number(arr,n):
    expected_sum = n*(n+1)//2
    sum_of_arr = 0
    for i in arr:
        sum_of_arr+=i
    missing_number = expected_sum - sum_of_arr
    return missing_number


arr = [1, 2, 4, 5]
n = 5
print(find_the_missing_number(arr, n))  # Output: 3