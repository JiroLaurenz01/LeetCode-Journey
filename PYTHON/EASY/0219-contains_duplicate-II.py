class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a hashtable to store the last seen index of each element
        hashtable = {}

        # Iterate through the list using both the index (i) and the element (num)
        for i, num in enumerate(nums):
            # Check if the current element has been seen before within the specified window (k)
            if num in hashtable and i - hashtable[num] <= k:
                # If yes, return True as duplicates are found within the window
                return True

            # Update the last seen index for the current element
            hashtable[num] = i

        # Return False if no duplicates are found within the specified window
        return False
