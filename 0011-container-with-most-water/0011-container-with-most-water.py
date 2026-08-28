class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left

            if height[left] < height[right]:
                current_height = height[left]
                left += 1
            else:
                current_height = height[right]
                right -= 1

            area = width * current_height

            if area > max_water:
                max_water = area

        return max_water

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna