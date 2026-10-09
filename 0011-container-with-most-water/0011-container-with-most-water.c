int getMin(int x , int y ) {
    return (x > y) ? y : x ; 
}
int getMax(int x , int y) {
    return (x > y) ? x : y ; 
}
int maxArea(int* height, int heightSize) {
    int left = 0 , right = heightSize - 1  ; 
    int ans = 0 ; 
    while (left <= right) {
        int length = getMin(height[left] , height[right]) ; 
        int area = (right - left) * length ;
        ans = getMax(ans , area) ; 
        if (length == height[left]) {
            left++ ;
        }
        else{ 
            right--;
        }
    } 
    return ans ;  
}