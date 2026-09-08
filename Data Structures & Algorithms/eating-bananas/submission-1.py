class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxVal = piles[0]

        for pile in piles:
            if pile > maxVal:
                maxVal = pile
            
        if h == len(piles):
            return maxVal
        
        l = 1
        r = maxVal
        res = maxVal
        while l <= r:
            mid = l + (r - l)//2
            time = self.timeTaken(piles, h, mid)
            if time > h:

                l = mid + 1
            elif time <= h:
                res = mid
                r = mid - 1

        return res

    def timeTaken(self, piles, h, k):
        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(pile/k) 

        return totalTime


