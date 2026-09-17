class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)
        for i in range(0, len(nums) - k):
            heapq.heappop(heap)
        
        return heap[0]