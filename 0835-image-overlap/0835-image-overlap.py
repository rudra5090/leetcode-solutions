from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        # Try every possible translation
        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):

                overlap = 0

                for r in range(n):
                    for c in range(n):

                        r2 = r + dr
                        c2 = c + dc

                        # Check if translated position is inside img2
                        if 0 <= r2 < n and 0 <= c2 < n:
                            if img1[r][c] == 1 and img2[r2][c2] == 1:
                                overlap += 1

                ans = max(ans, overlap)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna