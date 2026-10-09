int minStartValue(int* nums, int numsSize) {
    int min = nums[0] ; 
    for (int i = 1 ; i < numsSize ; i++) {
        nums[i] += nums[i -1 ] ; 
        min = (min > nums[i] ) ? nums[i] : min ; 
    }
    if (min > 0) {
        return 1 ; 
    }
    return -1 * min + 1 ; 
}