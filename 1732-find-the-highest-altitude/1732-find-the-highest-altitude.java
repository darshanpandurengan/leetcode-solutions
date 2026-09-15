class Solution {
    public int largestAltitude(int[] gain) {
        int res = 0 , prefix = 0 ; 
        for (int g : gain)
        {
            prefix += g ; 
            res = (prefix > res) ? prefix : res ; 
        }
        return res ; 
    }
}