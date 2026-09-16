class Solution {
    public int findLucky(int[] arr) {
        int res = -1 ; 
        int[] freq = new int[501] ; 

        for (int num : arr) 
        {
            freq[num]++ ; 
        }

        for (int i = 1 ; i < 501 ; i++)
        {
            if (i == freq[i]) 
            {
                res = Math.max(res , i ) ; 
            }
        }

        return res ; 
    }
}