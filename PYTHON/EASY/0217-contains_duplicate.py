class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert the input list 'nums' to a set, eliminating duplicates
        hashset = set(nums)

        # Check if the length of the set is different from the length of the original list
        # If there are duplicates, the set will have fewer elements than the list
        return len(hashset) != len(nums)
