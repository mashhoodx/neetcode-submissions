class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for i in tokens:
            if i=="+":
                x=stack.pop()
                y=stack.pop()
                stack.append(y+x)
            elif i=="-":
                x=stack.pop()
                y=stack.pop()
                stack.append(y-x)
            elif i=="*":
                x=stack.pop()
                y=stack.pop()
                stack.append(y*x)
            elif i=="/":
                x=stack.pop()
                y=stack.pop()
                z=abs(y)//abs(x)
                if (x<0) != (y<0):
                    z=-z
                stack.append(z)
            else:
                stack.append(int(i))
        return stack[-1]
            
        