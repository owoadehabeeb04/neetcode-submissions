class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3 opeen parentheseis and 3 close parenthesis
        # begining musr bbe open parentheses while end must be close parenhtesir
        #make sure the noof close parenthesis more than the open parenthesis
        # dont add a close parenthesis if no of open parenthesis is the same as no of close parenthesis 


        stack = []
        res = []
        def backTrack(openN, closedN):
            if openN == closedN == n:
                return res.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backTrack(openN, closedN + 1)
                stack.pop()

        backTrack(0, 0)
        return res
            

        