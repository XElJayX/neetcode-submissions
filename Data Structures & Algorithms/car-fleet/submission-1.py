class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse = True)
        time = [(target-pos)/s for pos, s in cars]
        stack = []

        for t in time:
            stack.append(t)
            if len(stack)>=2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        return len(stack)
