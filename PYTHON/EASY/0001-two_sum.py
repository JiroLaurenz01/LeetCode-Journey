class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the difference and index pairs
        hashtable = {}

        # Iterate through the list using both the index (i) and the element (num)
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current element
            diff = target - num

            # Check if the current element is already in the hashtable
            if num in hashtable:
                # If yes, return the indices of the two elements that sum up to the target
                return [hashtable[num], i]

            # If not, store the difference and its corresponding index in the hashtable
            hashtable[diff] = i

        # Return an empty list if no solution is found
        return []
