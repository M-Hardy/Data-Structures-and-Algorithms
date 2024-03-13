class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        char_freq = {}
        l = 0
        max_len = 0
        
        for r,c in enumerate(s):
            char_freq[c] = char_freq.get(c, 0) + 1             
            
            # (r-l) + 1 is current window size (len of substring)
            while (r-l+1) - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, r-l+1)

        return max_len


    def characterReplacement2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        char_freq = {}
        l = 0
        max_len = 0
        max_freq = 0

        for r,c in enumerate(s):
            char_freq[c] = char_freq.get(c, 0) + 1 
            max_freq = max(max_freq, char_freq[c])
            
            # r-l+1 = current window size/substring len
            # we don't need to decrement max_freq ever
            # because it's essentially a marker of longest
            # string, so only need to update when longest
            # substring w/ replacements gets LONGER, not
            # shorter
            while (r-l+1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, r-l+1)

        return max_len