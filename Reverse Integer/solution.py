class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)

        if s[0] == '-':
            s = s[1:len(s)]

        s = s[::-1]

        num = int(s)
        num = num if x > 0 else -1 * num

        if num > 2**31 - 1 or num < -2**31:
            return 0
        
        return num