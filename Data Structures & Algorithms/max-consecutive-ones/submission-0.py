class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        currCount = 0
        
        for num in nums:
            if num == 1:
                currCount += 1
                if currCount > max:
                    max = currCount
            else:
                currCount = 0
        return max