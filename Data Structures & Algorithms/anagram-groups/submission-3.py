class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            keyed = "".join(sorted(string))
            groups[keyed].append(string)
        
        return list(groups.values())