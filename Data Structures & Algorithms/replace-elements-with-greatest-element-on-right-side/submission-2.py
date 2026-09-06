class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largestSeen = arr[-1]
        for i in range(1, len(arr)):
            currVal = arr[-1 - i]
            arr[-1 - i] = largestSeen

            if  currVal > largestSeen:
                largestSeen = currVal
   
        arr[-1] = -1

        return arr