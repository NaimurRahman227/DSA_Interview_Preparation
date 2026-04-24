class Solution(object):
    def longestPalindrome(self , s):
        res = ""

        for i in range(len(s)):
            temp = self.expand(s , i , i)
            if len(temp) > len(res):
                res = temp


            temp = self.expand(s , i , i+1)
            if len(temp) > len(res):
                res = temp

        return res
    def expand(self , s , left , right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1 : right]
    
if __name__ == "__main__":
    LPS = Solution()
    userString = input('')

    print(LPS.longestPalindrome(userString))
