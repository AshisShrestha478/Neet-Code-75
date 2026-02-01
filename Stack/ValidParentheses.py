class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for cha in s:
            if cha in "({[":
                stack.append(cha)
            else:
                if not stack:
                    return False

                if stack[-1] != match[cha]:
                    return False
                
                stack.pop()
        
        return len(stack) == 0