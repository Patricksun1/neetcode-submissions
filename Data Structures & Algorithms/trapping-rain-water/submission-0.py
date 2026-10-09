class Solution:
    def trap(self, height: List[int]) -> int:
        maxV = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        while l <= r:

            if maxL < maxR:
                if height[l] <= maxL:
                    minHeight = min(maxR, maxL)
                    maxV += minHeight - height[l]
                
                else:
                    maxL = height[l]

                l += 1

            else:
                if height[r] < maxR:
                    minHeight = min(maxR, maxL)
                    maxV += minHeight - height[r]
                else:
                    maxR = height[r]

                r -= 1
            
        
        return maxV

            
           


        