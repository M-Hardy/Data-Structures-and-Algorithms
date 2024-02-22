class Solution(object):
    
    #O(n) space & time complexity
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_len = 0
        start = 0
        char_index_map = {}

        for i,c in enumerate(s):
            if c in char_index_map and char_index_map[c] >= start:
                max_len = max(max_len, i - start)
                start = char_index_map[c] + 1                
            char_index_map[c] = i
        max_len = max(max_len, len(s) - start)
        return max_len

    #NC solution - same time & space complexity
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[r])
                l += 1
            char_set.add(s[r])
            res = max(res, (r - l) + 1) #include right char as part of current string length
        return res

