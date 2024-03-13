class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        operand_stack = []
        operators = set(('+', '-', '*', '/'))

        for token in tokens:
            if token not in operators:
                operand_stack.append(int(token))
                                     
            else:
                operand_2 = operand_stack.pop()
                operand_1 = operand_stack.pop()
                
                if token == '+':
                    res = operand_1 + operand_2
                elif token == '-':
                    res = operand_1 - operand_2
                elif token == '*':
                    res = operand_1 * operand_2
                else:
                    # nested float cast was necessary to truncate 
                    # integer division to 0. Note that float 
                    # division should return a float, but it didn't 
                    # here. int casting float division is sufficient 
                    # in Python3:
                    # res = int(operand_1 / operand_2)
                
                    res = int(float(operand_1) / operand_2)
                    
                operand_stack.append(res)
                
        return operand_stack.pop()