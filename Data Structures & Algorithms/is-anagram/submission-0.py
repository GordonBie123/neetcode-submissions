class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_count = {}
        s_count = {}
        for c in t:
            if c not in t_count:
                t_count[c] = 0
            t_count[c] += 1
        for c in s:
            if c not in s_count:
                s_count[c] = 0
            s_count[c] +=1
        if t_count == s_count:
            return True
        return False