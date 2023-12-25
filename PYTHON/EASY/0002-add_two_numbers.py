# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node for the result linked list
        result = ListNode()
        # Set the current pointer to the dummy node
        curPt = result

        # Initialize a carry variable to handle addition overflow
        carry = 0

        # Iterate through the linked lists or continue until there's no carry
        while l1 or l2 or carry:
            # Extract values from the current nodes or use 0 if the node is None
            valOne = l1.val if l1 else 0
            valTwo = l2.val if l2 else 0

            # Calculate the sum of values and the carry for the next iteration
            value = valOne + valTwo + carry

            carry = value // 10  # Determine the carry for the next iteration
            value = value % 10   # Extract the digit for the current node

            # Create a new node in the result linked list with the calculated value
            curPt.next = ListNode(value)
            # Move the current pointer to the new node
            curPt = curPt.next
            
            # Move to the next nodes in the input linked lists if available, or set to None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result linked list, excluding the dummy node
        return result.next
