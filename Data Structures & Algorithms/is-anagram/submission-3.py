class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        if s_map == t_map:
            return True
        else:
            return False
        