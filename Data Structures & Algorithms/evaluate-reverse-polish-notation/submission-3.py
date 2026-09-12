class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        number_stack = []
        for token in tokens:
            if token in operators:
                second = number_stack.pop()
                first = number_stack.pop()
                if token == "+":
                    number_stack.append(first + second)
                elif token == "-":
                    number_stack.append(first - second)
                elif token == "*":
                    number_stack.append(first * second)
                elif token == "/":
                    number_stack.append(int(first / second))
            else:
                number_stack.append(int(token))
        return number_stack[0]
        
                
