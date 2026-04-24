class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculator(right,left,operator):
            print(left,operator,right)
            if operator=="+":
                return left+right
            if operator=="-":
                return left-right           
            if operator=="*":
                return left*right          
            if operator=="/":
                if left//right<0 and left % right !=0:
                    return left//right +1
                return left//right          
            return None
        res=0
        num=[]
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                num.append(calculator(int(num.pop()),int(num.pop()),i))
            else:
                num.append(int(i))
        return num[0]
        