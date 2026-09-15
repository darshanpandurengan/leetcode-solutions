class Solution {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer , Integer> freq  = new HashMap<>() ; 
        int sum = 0 ; 

        for (int num : nums) 
        {
            if (freq.containsKey(num)) 
            {
                freq.put(num , freq.get(num) + 1 ) ; 
            }
            else {
                freq.put(num , 1) ; 
            }
        }

        for(Map.Entry<Integer , Integer > entry : freq.entrySet()) 
        {
            if (entry.getValue() == 1) 
            sum += entry.getKey() ; 
        }
        return sum ; 
    }
}