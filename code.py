class Solution:
    def isPalindrome(self, s):
        s = ''.join(c for c in s.lower() if c.isalnum()) 
#method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9)
        return s[::-1] == s


