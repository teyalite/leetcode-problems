class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
    
        is_negative = n < 0
        n = abs(n)
        val = 1

        while n > 0:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                val *= x
                n -= 1
    
        return 1.0/val if is_negative else val 