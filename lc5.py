class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(right, left) -> int:
            while right < len(s) - 1 and left >= 0 and s[right] == s[left]:
                right += 1
                left -= 1
            return right - left - 1

        start = 0
        end = 0
        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)
            l1 = i - odd // 2
            r1 = i + odd // 2
            if r1 - l1 > start - end:
                start = l1
                end = r1
            l2 = i - even // 2
            r2 = i - even // 2
            if r2 - l2 > start - end:
                start = l2
                end = r2
        return s[start:end]


s1 = Solution()
str = "cbbd"
print(s1.longestPalindrome(str))
