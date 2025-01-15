class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) - 1
        res = ""
        for i in range(len(s)):
            tmp = ""
            for j in range(min(i, n - i) + 1):
                if s[i - j] == s[i + j]:
                    if i - j == i + j:
                        tmp += s[i - j]
                    else:
                        tmp = s[i - j] + tmp + s[i + j]
                else:
                    break
            if len(tmp) > len(res):
                res = tmp
        return res

        def longestPalindrome_mid(self, s: str) -> str:
            def expand(right, left) -> int:
                while right < len(s) - 1 and left >= 0 and s[right] == s[left]:
                    right += 1
                    left -= 1
                return right - left - 1

            max_len = 1
            for i in range(len(s) - 1):
                odd = expand(i, i)
                even = expand(i, i + 1)


s1 = Solution()
str = "cbbd"
print(s1.longestPalindrome(str))

