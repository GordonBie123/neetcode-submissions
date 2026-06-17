class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(s)) for s in strs]
        sorted_dict = {}
        for sorted_str in sorted_strs:
            if sorted_str not in sorted_dict:
                sorted_dict[sorted_str] = []
        for s in strs:
            if "".join(sorted(s)) in sorted_dict:
                sorted_dict["".join(sorted(s))].append(s)
        return (list(sorted_dict.values()))
        