class Solution {
    public int returnToBoundaryCount(int[] nums) {
        int res = 0 ; 
        int curr_position = 0 ; 

        for (int num : nums) 
        {
            curr_position += num ; 
            
            if (curr_position == 0 ) res++ ; 
        }

        return res ; 
    }
}