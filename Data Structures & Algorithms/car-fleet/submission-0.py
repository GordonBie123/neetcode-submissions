class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []

        for pos, speed in cars:
            time = (target - pos) / speed
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)        

            