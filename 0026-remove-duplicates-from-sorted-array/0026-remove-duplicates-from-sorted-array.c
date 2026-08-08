int removeDuplicates(int* nums, int numsSize) {
    int left = 1 ; 
    for(int right = 1  ; right < numsSize ; right++) {
        if(nums[left - 1] != nums[right] ) {
            nums[left] = nums[right] ;
            left++ ; 
        }
    }
    return left ;
}