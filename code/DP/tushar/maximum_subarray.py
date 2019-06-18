class Solution:
    def __init__(self):
        self.roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        self.final = 0
        
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        for index in range(0, len(s)-1):
            if s[index] == 'I' and (s[index+1] == 'V' or s[index+1] == 'X'):
                self.final -= self.roman[s[index]]                
            elif s[index] == 'X' and (s[index+1] == 'L' or s[index+1] == 'C'):
            	self.final -= self.roman[s[index]]
            elif s[index] == 'C' and (s[index+1] == 'D' or s[index+1] == 'M'):
                self.final -= self.roman[s[index]]
            else:
                self.final += self.roman[s[index]]
                                         
        return self.final + self.roman[s[-1]]
