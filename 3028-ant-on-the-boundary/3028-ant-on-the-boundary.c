int returnToBoundaryCount(int* nums, int numsSize) {
    int curr = 0 , res = 0 ;
    for(int i = 0 ; i < numsSize ; i++) 
    {
        curr += nums[i] ; 
        if (curr == 0) res++ ; 
    }
    return res ; 
}