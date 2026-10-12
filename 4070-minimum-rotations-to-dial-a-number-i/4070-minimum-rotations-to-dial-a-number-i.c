int minRotations(char* s) {
    int res = 0 ; 
    int prev = '0' ; 
    while (*(s) != '\0')
    {
        int temp =abs(*(s) - prev) ; 
        res += (temp < 10 - temp) ? temp : 10 - temp ; 
        prev = *(s) ; 
        *(s++) ; 
    }
    return res ; 
}