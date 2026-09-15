class Solution {
    public int countPartitions(int[] nums) {
        int res = 0 , totalSum = 0 , prefixSum = 0 ; 

        for (int num : nums) 
        {
            totalSum += num ; 
        }

        for (int i = 0  ; i <  nums.length - 1 ; i++ ) 
        {
            prefixSum += nums[i] ; 
            totalSum -= nums[i] ; 

            if ( (prefixSum - totalSum) % 2 == 0 ) res++ ; 
        }

        return res ; 
    }
}