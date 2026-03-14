# 17. Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

def leaders(arr):
        n = len(arr)
        result = []

        for i in range(n):
            isLeader = True

            for j in range(i+1, n):
                if arr[j] > arr[i]:
                    isLeader = False
                    break

            if isLeader:
                result.append(arr[i])

        return result