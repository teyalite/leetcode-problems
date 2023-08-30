class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        
        i = 0
        num = 0
        
        while i < len(s):
            if i == len(s) - 1 or ref[s[i]] >= ref[s[i + 1]]:
                num += ref[s[i]]
                i += 1
            else:
                num += ref[s[i] + s[i + 1]]
                i += 2
                
        return num
