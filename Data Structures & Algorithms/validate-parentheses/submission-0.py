class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"}":"{","]":"[",")":"("}
        stack = []
        for char in s:
            if char in parentheses:
                if not stack or stack[-1] != parentheses[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0