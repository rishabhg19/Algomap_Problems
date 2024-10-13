class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = defaultdict(int)
        for character in magazine:
            available[character] += 1
        
        for character in ransomNote:
            available[character] -= 1
        if min(available.values()) < 0:
            return False
        return True