class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur = [0] * 26
        for c in s:
            occur[ord(c) - ord('a')] += 1
        for c in t:
            occur[ord(c) - ord('a')] -= 1
        for num in occur:
            if num != 0:
                return False
        return True