class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        removedIndex = []

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            else:
                k += 1
            
            i+= 1




        nums = [num for num in nums if num != val]  

        return k