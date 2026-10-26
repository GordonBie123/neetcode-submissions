class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            string_sorted = "".join(sorted(string))
            groups[string_sorted].append(string)
                
        return list(groups.values())