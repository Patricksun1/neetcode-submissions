class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, num in enumerate(nums):
            if res.get(target - num) != None:
                return [res.get(target - num), i]
            
            res[num] = i
        
        return []
