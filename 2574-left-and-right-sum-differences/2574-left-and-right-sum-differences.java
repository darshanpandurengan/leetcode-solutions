class Solution {
    public int[] leftRightDifference(int[] nums) {
        int size = nums.length ; 
        int leftSum = 0 ; 
        int totalSum = 0 ; 
        int[] res = new int[size] ; 

        for(int num : nums) 
        {
            totalSum += num ; 
        }

        for (int i = 0 ; i < size ; i++) 
        {
            totalSum -= nums[i] ; 
            res[i] = Math.abs(totalSum - leftSum ) ; 
            leftSum += nums[i] ; 
        }
        
        return res ; 
    }
}