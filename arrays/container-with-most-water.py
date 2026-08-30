class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            width = right - left
            if height[left] < height[right]:
                area = height[left] * width
                left += 1
            else:
                area = height[right] * width
                right -= 1

            if area > best:
                best = area

        return best
