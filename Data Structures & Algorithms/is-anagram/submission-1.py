class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_chars = {} 
        s_chars = {}
        for char in s:
            if char in s_chars:
                s_chars[char] += 1
            elif char not in s_chars:
                s_chars[char] = 1
        for char in t:
            if char in t_chars:
                t_chars[char] += 1
            elif char not in t_chars:
                t_chars[char] = 1
        if t_chars == s_chars:
            return True
        return False
        