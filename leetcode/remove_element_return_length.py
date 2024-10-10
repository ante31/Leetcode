
class Solution(object):
    def removeElement(self, nums, val):
        i=0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)    
    
        
nums = [0,1,2,2,3,0,4,2]
val = 2
solution = Solution()
print(solution.removeElement(nums, val))

#https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150