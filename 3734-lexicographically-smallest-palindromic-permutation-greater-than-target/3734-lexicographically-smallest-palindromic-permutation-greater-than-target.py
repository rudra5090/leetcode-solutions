class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one character with odd frequency
        odd_chars = []

        for i in range(26):
            if count[i] % 2 == 1:
                odd_chars.append(i)

        if len(odd_chars) > 1:
            return ""

        # Build counts for the left half
        half_count = [0] * 26

        for i in range(26):
            half_count[i] = count[i] // 2

        half_len = n // 2
        target_left = target[:half_len]

        middle = ""

        if n % 2 == 1 and odd_chars:
            middle = chr(ord('a') + odd_chars[0])

        # --------------------------------------------------
        # CASE 1:
        # Try using exactly target_left as the left half.
        # --------------------------------------------------

        remaining = half_count[:]
        possible = True

        for ch in target_left:
            idx = ord(ch) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        if possible:
            left = target_left

            if n % 2 == 1:
                palindrome = left + middle + left[::-1]
            else:
                palindrome = left + left[::-1]

            if palindrome > target:
                return palindrome

        # --------------------------------------------------
        # CASE 2:
        # Find the smallest left half greater than target_left.
        # --------------------------------------------------

        for i in range(half_len - 1, -1, -1):

            remaining = half_count[:]
            possible = True

            # Keep prefix equal to target
            for j in range(i):
                idx = ord(target_left[j]) - ord('a')

                if remaining[idx] == 0:
                    possible = False
                    break

                remaining[idx] -= 1

            if not possible:
                continue

            current = ord(target_left[i]) - ord('a')

            # Pick the smallest character greater than target[i]
            for next_char in range(current + 1, 26):

                if remaining[next_char] > 0:

                    remaining[next_char] -= 1

                    left = target_left[:i]
                    left += chr(ord('a') + next_char)

                    # Fill remaining characters in sorted order
                    for c in range(26):
                        left += chr(ord('a') + c) * remaining[c]

                    # Construct palindrome
                    if n % 2 == 1:
                        palindrome = left + middle + left[::-1]
                    else:
                        palindrome = left + left[::-1]

                    return palindrome

        return ""

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna