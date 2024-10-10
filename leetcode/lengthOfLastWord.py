class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split(" ")
        return len(words[-1])
        

solution = Solution()
s = "Hello  World w   w  ww    wwww  "
print(solution.lengthOfLastWord(s))

#https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150