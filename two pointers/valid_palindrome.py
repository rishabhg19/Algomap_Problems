class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s = s.lower()
        build_string = [character for character in s if ord('z') - ord(character) >= 0 and ord('z') - ord(character) <= 25 or ord(character) >= 48 and ord(character) <= 57]
        right = len(build_string) - 1
        print(ord('9'))
        while left < right:
            if build_string[left] != build_string[right]:
                return False
            left += 1
            right -= 1
        return True