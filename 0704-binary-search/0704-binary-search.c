int binary(int *nums , int l , int r , int t) {
    int mid = (l +r) / 2 ; 
    if(nums[mid] == t) return mid ; 
    if(l >= r) return -1 ; 
    if(nums[mid] < t) return binary(nums , mid + 1 , r , t) ; 
    return binary(nums , l , mid - 1 , t) ;
}
int search(int* nums, int numsSize, int target) {
    return binary(nums , 0 , numsSize - 1, target) ; 
}