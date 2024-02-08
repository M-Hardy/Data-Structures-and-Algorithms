class Solution(object):    
    
    # original solution using two pointers; O(n)
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            while not s[start].isalnum():
                start += 1
                if start >= end:
                    return True
            
            while not s[end].isalnum():
                end -= 1
                if end <= start:
                    return True
            
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        return True

