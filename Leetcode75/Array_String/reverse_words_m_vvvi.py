''' Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "   a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        length = len(s)
        start = 0
        end = 0
        res = ''

        while(end < length):
            # find start, most important is before checking index check lenght
            # so instead of while(s[start] == ' ' and start < length) do ***while(start < length and s[start] == ' ')***
            while(start < length and s[start] == ' '):
                start += 1
            end = start

            #find end
            while(end < length and s[end] != ' '):
                end += 1
            
            res = s[start:end] + ' ' + res
            start = end
        
        return res.strip()

res = Solution()
print(res.reverseWords('  the  sky is blue'))