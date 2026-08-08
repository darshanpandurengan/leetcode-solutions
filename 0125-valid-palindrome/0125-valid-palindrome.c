#include <ctype.h>
#include <string.h>
bool isPalindrome(char* s) {
    int left = 0 , right = strlen(s) - 1 ; 
    while (left < right) {
        if(!(isalnum(s[left]))) {
            left++ ; 
            continue ; 
        }
        if(!(isalnum(s[right]))){ 
            right-- ; 
            continue ;
        } 
        char templ = tolower(s[left]) ; 
        char tempr = tolower(s[right]) ; 
        if(templ != tempr) return false ; 
        left++ ; 
        right--;
    }
    return true; 
}