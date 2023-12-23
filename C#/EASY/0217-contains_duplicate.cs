public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        // Create a HashSet from the array 'nums'
        // A HashSet automatically removes duplicates, so the count will be less than the original array's length if there are duplicates
        return new HashSet<int>(nums).Count() != nums.Count();
    }
}
