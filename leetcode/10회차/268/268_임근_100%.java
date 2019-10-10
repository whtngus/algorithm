class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        int arraySum = 0;

        for (int i = 1; i < nums.length + 1; i++) {
            sum += i;
            arraySum += nums[i - 1];
        }
        
        return sum - arraySum;
    }
}