class Solution(object):
    def isSubsequence(self, s, t):
        index = 0
        for i in range(len(s)):
            uvjet = False
            for j in range(index, len(t)):
                if s[i] == t[j]:
                    uvjet = True
                    index = j+1
                    break
            if not uvjet:
                break
        return uvjet

s = "aaaaaa"
t = "bbaaaa"
solution = Solution()
print(solution.isSubsequence(s, t))

#https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150