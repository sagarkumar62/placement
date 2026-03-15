# 18. Move Zeroes to End: Move all zeroes in an array to the end while maintaining the order of non-zero elements.


def moveZeroes(nums):

        temp = []

        for num in nums:
            if num != 0:
                temp.append(num)

        zero_count = len(nums) - len(temp)

        for i in range(zero_count):
            temp.append(0)

        return temp


nums = [0,1,0,3,12]

a = moveZeroes(nums)
print(a)