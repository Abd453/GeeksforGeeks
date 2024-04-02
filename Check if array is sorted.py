class Solution:
    def arraySortedOrNot(self, arr, n):
        # Check if the array is sorted in non-decreasing order
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                return False
        return True
