class Solution:
    m = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n in self.m:
            return self.m[n]
        
        self.m[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.m[n]
    