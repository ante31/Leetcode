class Solution(object):
    def majorityElement(self, nums):
        candidate = 0
        count = 0

        for i in nums:
            if count == 0:
                candidate = i
                count=1
                continue
            if i == candidate:
                count+=1
            else:
                count-=1
        
        return candidate
    
nums = [2,2,1,1,1,2,2]

solution = Solution()
print(solution.majorityElement(nums))
            
#https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150