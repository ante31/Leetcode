class Solution(object):
    def threeSum(self, nums):
        solution = []
        nums.sort()
        for index in range(len(nums)):
            left = index + 1
            right = len(nums)-1

            while True:
                if right == left:
                    break

                if nums[index] + nums[left] + nums[right] == 0 and index != left and index != right:
                    candidate = [nums[index], nums[left], nums[right]]
                    if candidate not in solution:
                        solution.append(candidate)
                        left += 1
                        
                
                if nums[left] + nums[right] + nums[index] < 0:
                    left += 1
                    if left == index:
                        left += 1

                elif nums[left] + nums[right] + nums[index] > 0:
                    right -= 1
                    if right == index:
                        right -= 1

        return solution

            
nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))