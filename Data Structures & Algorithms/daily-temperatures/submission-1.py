class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        num = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                pos, t = stack.pop()
                num[pos] = i - pos
            stack.append([i,temp])
        return num