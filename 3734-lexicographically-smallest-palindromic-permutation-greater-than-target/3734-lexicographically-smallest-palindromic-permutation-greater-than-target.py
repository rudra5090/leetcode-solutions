
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        odd = -1

        for i in range(26):
            if count[i] % 2 == 1:
                if odd != -1:
                    return ""
                odd = i

        # Frequency for the first half
        half = [0] * 26

        for i in range(26):
            half[i] = count[i] // 2

        m = n // 2
        target_half = target[:m]

        # Try to make the first half greater
        for pos in range(m - 1, -1, -1):

            remaining = half[:]
            valid = True

            # Match prefix with target
            for i in range(pos):
                c = ord(target_half[i]) - ord('a')

                if remaining[c] == 0:
                    valid = False
                    break

                remaining[c] -= 1

            if not valid:
                continue

            # Choose the smallest character greater than target[pos]
            current = ord(target_half[pos]) - ord('a')
            bigger = -1

            for c in range(current + 1, 26):
                if remaining[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            # Construct first half
            first = []

            for i in range(pos):
                first.append(target_half[i])

            first.append(chr(bigger + ord('a')))
            remaining[bigger] -= 1

            # Fill remaining positions with smallest characters
            for c in range(26):
                while remaining[c] > 0:
                    first.append(chr(c + ord('a')))
                    remaining[c] -= 1

            first = ''.join(first)

            # Middle character for odd length
            middle = ""

            if odd != -1:
                middle = chr(odd + ord('a'))

            # Construct palindrome
            return first + middle + first[::-1]

        return ""

        for i in range(26):
            if count[i] % 2 == 1:
                if odd != -1:
                    return ""
                odd = i

        # Build frequency of the first half
        half = [0] * 26

        for i in range(26):
            half[i] = count[i] // 2

        m = n // 2
        target_half = target[:m]

        # Find the smallest first half greater than target_half
        for pos in range(m - 1, -1, -1):

            remaining = half[:]
            valid = True

            # Match the prefix of target
            for i in range(pos):
                c = ord(target_half[i]) - ord('a')

                if remaining[c] == 0:
                    valid = False
                    break

                remaining[c] -= 1

            if not valid:
                continue

            # Find smallest character greater than target[pos]
            current = ord(target_half[pos]) - ord('a')
            bigger = -1

            for c in range(current + 1, 26):
                if remaining[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            # Build the first half
            first = []

            for i in range(pos):
                first.append(target_half[i])

            first.append(chr(bigger + ord('a')))
            remaining[bigger] -= 1

            # Fill remaining characters in sorted order
            for c in range(26):
                while remaining[c] > 0:
                    first.append(chr(c + ord('a')))
                    remaining[c] -= 1

            first = ''.join(first)

            # Middle character if length is odd
            middle = ""

            if odd != -1:
                middle = chr(odd + ord('a'))

            # Complete palindrome
            return first + middle + first[::-1]

        return ""


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna