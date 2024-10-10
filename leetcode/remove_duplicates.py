class Solution(object):
    def removeDuplicates(self, nums):
        candidate = nums[0]
        count = 0
        i = 0

        while i < len(nums):
            if candidate != nums[i]:
                candidate = nums[i]
                count = 1
                i+=1
            else:
                count +=1
                i+=1
                if count > 2:
                    i-=1
                    nums.pop(i)
        return len(nums)

        
nums = [1,1,1,2,2,3]
solution = Solution()
print(solution.removeDuplicates(nums))

#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150