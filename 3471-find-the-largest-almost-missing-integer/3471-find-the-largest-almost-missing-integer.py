import collections

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        
        count = collections.Counter(nums)
        
        if k == 1:
            return max([num for num in nums if count[num] == 1], default=-1)
        
        ans = -1
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])
        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna