# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.forward_queue = []
        self.backward_queue = []
        

    def push(self, x: int) -> None:
        self.forward_queue.append(x)
        

    def pop(self) -> int:
        return self.forward_queue.pop()
        

    def top(self) -> int:
        l = len(self.forward_queue) - 1
        return self.forward_queue[l]
        

    def empty(self) -> bool:
        if len(self.forward_queue) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()