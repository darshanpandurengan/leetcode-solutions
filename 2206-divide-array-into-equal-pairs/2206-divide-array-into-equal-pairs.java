class Solution {
    public boolean divideArray(int[] nums) {
        HashMap<Integer , Integer > freq = new HashMap<>() ; 

        for (int num : nums) {
            if (freq.containsKey(num)) 
            {
                freq.put(num , freq.get(num) + 1 ) ; 
            }
            else 
            {
                freq.put(num ,  1) ; 
            }
        }
        for (int val : freq.values())
        {
            if (val % 2 == 1) return false ; 
        }
        return true ; 
    }
}