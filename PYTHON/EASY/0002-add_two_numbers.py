# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbersV1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
    
    def addTwoNumbersV2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node for the result linked list with a value of 0
        result = ListNode(0)
        # Set the current pointer to the dummy node
        curPt = result

        # Initialize a carry variable to handle addition overflow
        carry = 0
        
        # Iterate through the linked lists or continue until there's no carry
        while l1 or l2 or carry:
            # Initialize v1 and v2 to 0 for cases where l1 or l2 is None
            v1 = v2 = 0
            
            # If l1 is not None, update v1 and move to the next node in l1
            if l1:
                v1 = l1.val
                l1 = l1.next
            # If l2 is not None, update v2 and move to the next node in l2
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            # Calculate the sum of values and the carry for the next iteration
            value = v1 + v2 + carry

            # Determine the carry for the next iteration
            carry = value // 10
            # Extract the digit for the current node
            value = value % 10

            # Create a new node in the result linked list with the calculated value
            curPt.next = ListNode(value)
            # Move the current pointer to the new node
            curPt = curPt.next

        # Return the result linked list, excluding the dummy node
        return result.next
