class Solution:
    def reverse(self, num: int) -> int:
        # brute force
        sign = -1 if num < 0 else 1
        reversed_str = str(abs(num))[::-1]
        result = int(reversed_str) * sign

        if -2**31 <= result <= 2**31 - 1:
            return result
        else:
            return 0
        