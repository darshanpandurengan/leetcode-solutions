int maximumCount(int* nums, int numsSize) {
    int negativeCount = 0  , positiveCount = 0 ; 
    for(int i = 0 ; i < numsSize ; i++)
    {
        if(nums[i] < 0 )
        {
            negativeCount++ ; 
        }
        else if (nums[i] >  0)
        {
            positiveCount++ ; 
        }
    }
    return (negativeCount > positiveCount) ? negativeCount : positiveCount;
}