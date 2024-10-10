class Solution(object):
    def romanToInt(self, s):
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        s = s[::-1]
        value = dict[s[0]]

        for i in range (1, len(s)):
            if dict[s[i]] < dict[s[i-1]]:
                value -= dict[s[i]]
            else:
                value += dict[s[i]]

        return value

s = "XIV"
solution = Solution()
print(solution.romanToInt(s))

#https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150