class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if stack==[]:
                    return False
                if i == ')':
                    if stack.pop()!='(':
                        return False
                if i == ']':
                    if stack.pop()!='[':
                        return False
                if i == '}':
                    if stack.pop()!='{':
                        return False
        if stack:
            return False
        return True
                        