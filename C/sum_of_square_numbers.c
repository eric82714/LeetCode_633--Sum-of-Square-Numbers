bool judgeSquareSum(int c){
    for(long a = 0; a*a <= c; a++) {
        double b = sqrt(c - a*a);
        if(b - (int)b == 0) return true;
    }
        
    return false;
}
