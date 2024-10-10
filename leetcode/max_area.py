class Solution(object):
    def maxArea(self, height):
        right = len(height) - 1
        left = 0
        maxArea = 0

        while True:
            if left == right:
                break

            area = min(height[left], height[right]) * (right - left) 
            if area > maxArea:
                maxArea = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return maxArea


height = [1,8,6,2,5,4,8,3,7]
solution = Solution()

print(solution.maxArea(height))