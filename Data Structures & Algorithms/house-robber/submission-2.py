class Solution:
    def rob(self, nums: List[int]) -> int:
        total = 0
        index = 0
        memo = {}

        def doRob(index):
            if index >= len(nums):
                return total

            if index in memo:
                return memo[index]


            ans1 = nums[index] + doRob(index + 2)
            ans2 = doRob(index + 1)


            memo[index] = max(ans1, ans2)
            return memo[index]

        return doRob(0)