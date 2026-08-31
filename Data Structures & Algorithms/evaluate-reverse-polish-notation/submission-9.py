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
                x=abs(stack[-2])//abs(stack[-1])
                if (stack[-2]<0) != (stack[-1]<0):
                    x=-x
                stack.pop()
                stack.pop()
                stack.append(x)
            else:
                stack.append(int(i))
        return stack[-1]
            
        