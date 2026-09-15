class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        def listSum(nums):
            res = 0
            for num in nums:
                res += num

            return res


        def dfs(i, currSum):

            if currSum == target:
                ans.append(curr.copy())
                return

            if i >= len(nums) or currSum > target:
                return
            

            curr.append(nums[i])
            dfs(i, currSum + nums[i])

            
            curr.pop()
            dfs(i + 1, currSum)
        
        dfs(0, 0)
        return ans



    