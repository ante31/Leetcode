class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while True:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
                
            elif numbers[left] + numbers[right] < target:
                left += 1

            elif numbers[left] + numbers[right] > target:
                right -= 1
        
numbers = [2,7,11,15]
target = 9

solution = Solution()
print(solution.twoSum(numbers, target))
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150