class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        start = 1
        end = x

        while start < end - 1:
            median = start + int((end - start) / 2)

            if median * median > x:
                end = median
            else:
                start = median

        return start
