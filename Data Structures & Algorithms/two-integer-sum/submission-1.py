class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, num in enumerate(nums):
            if (target-num) in res:
                return [res.get(target - num), i]
            
            res[num] = i
        
        return []
