class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for num in nums:
            if seen.get(num) != None:
                return True
            
            seen[num] = 1
        
        return False