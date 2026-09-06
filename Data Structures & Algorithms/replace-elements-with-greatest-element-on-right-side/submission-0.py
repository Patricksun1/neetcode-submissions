class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            largestOnRight = arr[i + 1]
            j = i + 1
            while j < len(arr):
                if arr[j] > largestOnRight:
                    largestOnRight = arr[j]
                arr[i] = largestOnRight
                j += 1

        arr[-1] = -1

        return arr

        