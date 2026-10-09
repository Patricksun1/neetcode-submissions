class Solution:
    def maxDifference(self, s: str) -> int:
        chars = {}

        for c in s:
            if chars.get(c):
                chars[c] += 1
            else:
                chars[c] = 1

        minEven = float("inf")
        maxOdd = float("-inf")

        for count in chars.values():
            oddFlag = count % 2

            if oddFlag and count > maxOdd:
                maxOdd = count
            
            if not oddFlag and count < minEven:
                minEven = count
            

        return maxOdd - minEven