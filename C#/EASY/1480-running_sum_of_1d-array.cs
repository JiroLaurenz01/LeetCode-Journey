public class Solution {
    public int[] RunningSum(int[] nums) {
        // Initialize a variable to store the running sum
        int sum = 0;
        
        // Iterate through the array using a for loop
        for (int i = 0; i < nums.Length; i++) {
            // Add the current element to the running sum
            sum += nums[i];
            
            // Update the current element in the array to be the running sum
            nums[i] = sum;
        }
        
        // Return the modified array with running sums
        return nums;
    }
}
