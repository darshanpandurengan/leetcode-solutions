int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int res = 0 , countor = 0 ; 
    for(int i = 0 ; i < numsSize ; i++) {
        if(nums[i]) countor++ ; 
        else countor = 0 ; 
        if(countor > res) res = countor ; 
    }
    return res ; 
}