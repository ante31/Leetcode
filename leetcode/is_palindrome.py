class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        i = 0
        while i < len(s):
            if not s[i].isalpha() and not s[i].isdigit():
                s = s[:i] + s[i+1:]
                i-=1
            i+=1
        
        reverse = s[::-1]
        return s == reverse
    
s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))

#https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150