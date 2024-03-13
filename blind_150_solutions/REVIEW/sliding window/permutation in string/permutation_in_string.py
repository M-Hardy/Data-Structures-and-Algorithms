class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        s1_count = [0] * 26
        s2_count = [0] * 26
        perm_chars = 0

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
            if s1_count[ord(c) - ord('a')] == 1:
                perm_chars += 1
        
        for i,c in enumerate(s2):
            if i >= len(s1):
                first_char_index = ord(s2[i-len(s1)]) - ord('a')
                if s2_count[first_char_index] == s1_count[first_char_index]:
                    perm_chars += 1
                s2_count[first_char_index] -= 1
            
            s2_count[ord(c) - ord('a')] += 1
            if s2_count[ord(c) - ord('a')] == s1_count[ord(c) - ord('a')]:
                perm_chars -= 1                

            if perm_chars == 0:
                return True
            
        return False
    
    
    def checkInclusion2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        s1_count = {}
        s2_count = {}
        permutation_chars = 0
        l = 0      
        
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
            if s1_count[c] == 1:
                permutation_chars += 1

        for r,c in enumerate(s2):

            if r-l == len(s1):
                if permutation_chars == 0:
                    return True
                else:
                    if s2[l] in s1_count and s2_count[s2[l]] == s1_count[s2[l]]:
                        permutation_chars += 1
                    s2_count[s2[l]] -= 1
                    l += 1
            
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            if s2[r] in s1_count and s2_count[s2[r]] == s1_count[s2[r]]:
                permutation_chars -= 1

        return permutation_chars == 0
    
    
    def checkInclusion3(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        s1_count = {}
        s2_count = {}
        l = 0        

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        while l < len(s2) and s2[l] not in s1_count:
            l += 1
        
        r = l
        while r < len(s2) and l <= len(s2) - len(s1):        

            while s2[r] in s1_count:
                s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1

                if r-l+1 == len(s1):
                    if s2_count == s1_count:
                        return True
                    else:
                        break
        
                if s2_count[s2[r]] > s1_count[s2[r]]:
                    break

                r += 1
            
            l += 1
            r = l
            s2_count = {}
        
        return False