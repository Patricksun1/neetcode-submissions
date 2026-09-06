# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        result = ListNode(0)
        curr = result
        if len(lists) == 0:
            return None
            
        for lst in lists:
            if lst is None:
                continue
            heapq.heappush(min_heap, NodeWrapper(lst))

        while min_heap:
            ret = heapq.heappop(min_heap)
 
            curr.next = ret.node
            curr = curr.next

            if ret.node.next:
                heapq.heappush(min_heap, NodeWrapper(ret.node.next))

        return result.next
