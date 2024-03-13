class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        closed_brackets = {')':'(', ']':'[', '}': '{'}

        for bracket in s:
            if not bracket in closed_brackets:
                stack.append(bracket)

            elif not stack or closed_brackets[bracket] != stack.pop():
                return False

        return not stack