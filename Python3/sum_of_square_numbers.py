class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c))
        
        for a in range(n+1):
            b = sqrt(c - a*a)
            if b - int(b) == 0: return True
        
        return False
