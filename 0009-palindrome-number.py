class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]

if __name__ == '__main__':
    x = 123
    ret = Solution().isPalindrome(x)
    print(ret)