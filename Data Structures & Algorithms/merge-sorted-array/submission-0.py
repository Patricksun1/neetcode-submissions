class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(0, n):
            addedFlag = 0
            for j in range(0, m + i):
                if nums2[i] <= nums1[j]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    addedFlag = 1
                    break
            
            if addedFlag == 0:
                nums1.insert(m + i, nums2[i])
                nums1.pop()


            

    # for i in range(0, n):
    #     lo = 0
    #     hi = m + i
        
    #     while lo <= hi:
    #         mid = lo + (lo + hi)/2


        

        