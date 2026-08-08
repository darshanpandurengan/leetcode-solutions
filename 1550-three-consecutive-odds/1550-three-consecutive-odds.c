bool threeConsecutiveOdds(int* arr, int arrSize) {
    int countor = 0 ;
    for(int i = 0 ; i < arrSize ; i++) 
    {
        if(arr[i] % 2 == 1) countor++ ; 
        else countor = 0 ; 
        if (countor == 3) return true ; 
    }
    return false ; 
}