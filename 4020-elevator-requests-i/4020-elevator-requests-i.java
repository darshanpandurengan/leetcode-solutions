class Solution {
    public int elevatorRequests(int n, int[] requests) {
        int time = requests[0]  , prefix = requests[0] ; 

        for (int i = 1 ; i < requests.length ; i++) 
        {
            time += Math.abs(prefix - requests[i]) ; 
            prefix = requests[i] ; 
        }

        return time ; 
    }
}