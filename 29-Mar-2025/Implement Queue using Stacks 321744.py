# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.forward_stack = []
        self.backward_stack = []
        

    def push(self, x: int) -> None:
        self.forward_stack.append(x)
        self.backward_stack.insert(0, x)

    def pop(self) -> int:
        self.forward_stack.pop(0)
        return self.backward_stack.pop()

        

    def peek(self) -> int:
        return self.forward_stack[0]

        

    def empty(self) -> bool:
        if len(self.forward_stack) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()