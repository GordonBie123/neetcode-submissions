class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the # separating the length from the string
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            result.append(s[start:end])
            i = end

        return result