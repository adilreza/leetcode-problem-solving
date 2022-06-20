class Solution {
public:
    bool isPalindrome(int x) {
    long int temp, revers=0, rem;
    temp = x;
    if(x < 0 || (x != 0 && x % 10 == 0))
        return false;
    else {
        while (1) {
            if (x == 0) {
                break;
            } else {
                rem = x%10;
                revers = revers*10 + rem;
                x = x/10;
            }
        }
        if (temp==revers){
            return true;
        }
        else{
            return false;
        }
    }
}
};