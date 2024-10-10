class Solution(object):
    def rotate(self, nums, k):
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]

nums = [1,2,3]
k = 19
solution = Solution()
solution.rotate(nums, k%len(nums))
print(nums)

#https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150