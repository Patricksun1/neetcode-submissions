class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        index = 0
        for num in nums:
            if num in remainder:
                return [remainder[num], index]
            else:
                rem = target - num
                remainder[rem] = index
            
            index += 1
            

        return []