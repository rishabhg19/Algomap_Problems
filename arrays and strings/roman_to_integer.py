# Leetcode 13 Roman to Integer
# Algomap Arrays and Strings 3
class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integerValue = 0
        for i in range(len(s)):
            if s[i:i+2] == "IV" or s[i:i+2] == "IX" or s[i:i+2] == "XL" or s[i:i+2] == "XC" or s[i:i+2] == "CD" or s[i:i+2] == "CM":
                integerValue -= converter[s[i]]
            else:
                integerValue += converter[s[i]]
        return integerValue