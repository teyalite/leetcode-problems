from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")": "(", "]": "[", "}": "{"}
        
        stack = LifoQueue(maxsize=len(s))

        for symbol in s:
            if symbol in closing:
                if stack.empty():
                    return False
                
                current = stack.get()
                
                if closing[symbol] == current:
                    continue
                else:
                    stack.put(current)
                    stack.put(symbol)
            else:
                stack.put(symbol)
    
        return stack.empty()