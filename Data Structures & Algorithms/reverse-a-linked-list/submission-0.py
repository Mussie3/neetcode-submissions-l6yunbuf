# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            next_node = curr.next  # Step 1: Save the rest of the list
            curr.next = prev       # Step 2: Reverse the arrow (point backward)
            prev = curr            # Step 3: Move prev up to the current node
            curr = next_node       # Step 4: Move curr to the next node
            
        # At the end, curr is None and prev is the new head
        return prev