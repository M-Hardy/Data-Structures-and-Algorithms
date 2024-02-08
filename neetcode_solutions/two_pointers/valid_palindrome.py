class Solution(object):    
    
    # 'pythonic' solution, compare reversed string
    #  with non-alphanumeric removed; less efficient
    #  than two pointer method because it uses O(n)
    #  space to create reversed string
    def isPalindrome2(self,s):
        return

    # original solution using two pointers; O(n)
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
                
            while r > l and not s[r].isalnum():
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True