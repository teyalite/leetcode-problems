class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        remainder = 1
        index = len(digits) - 1

        while index >= 0:
            digits[index] = digits[index] + remainder
            remainder = 0

            if digits[index] >= 10:
                digits[index] = digits[index] % 10
                remainder = 1
            
            index -= 1

        if remainder != 0:
            digits.insert(0, remainder)

        return digits
    