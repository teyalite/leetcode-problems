class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []

        m = {}

        for i in range(len(s) - 9):
            if s[i:i+10] in m:
                m[s[i:i+10]] += 1
            else:
                m[s[i:i+10]] = 1

        return list(map(lambda x: x[0], filter(lambda x: x[1] > 1, m.items())))