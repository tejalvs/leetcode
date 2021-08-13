class Solution:
    def breakPalindrome(self, p):
        for s in re.sub('[^a]', 'a', p, 1), p[:-1] + 'b':
            if s < s[::-1]:
                return s
        return ''  
