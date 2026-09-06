class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distIndexTable = {}
        distances = []
        index = 0
        currkthSmallest = 0
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            distances.append(dist)
        
        distances.sort()
        kthClosest = distances[k - 1]

        result = []
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            if dist <= kthClosest:
                result.append(point)
        
        return result
                


