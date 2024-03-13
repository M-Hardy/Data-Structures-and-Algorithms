class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res_l = 0
        res_r = 0
        res_len = 0

        for i in range(len(s)):           
            #odd length palindromes
            odd_l, odd_r = self.getLongestPalindrome(i, i, s)
            if odd_r - odd_l + 1 > res_len:
                res_r = odd_r
                res_l = odd_l
                res_len = odd_r-odd_l + 1
            
            #even length palindromes
            even_l, even_r = self.getLongestPalindrome(i, i+1, s)
            if even_r - even_l + 1 > res_len:
                res_r = even_r
                res_l = even_l
                res_len = even_r - even_l + 1

        return s[res_l:res_r+1]
    

    def getLongestPalindrome(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            r += 1
            l -= 1
        return (l+1, r-1)