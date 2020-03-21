class Solution(object):
    def lengthOfLongestSubstring(self, s):

        """
        :type s: str
        :rtype: int
        """
        max_ = 0
        n = len(s)
        if n == 1:
            return n
        if n == 2:
            return int(s[0] != s[1]) + 1
        for i in range(n-1):
            for j in range(i+1,n):
                if s[j] not in s[i:j]:
                    if j + 1 == n:
                        if j-i+1 > max_:
                            max_ = j-i+1
                    continue
                else:
                    if j-i > max_:
                        max_ = j-i
                    break
        return max_

if __name__ == '__main__':
    s = "abcabcbb"
    ret = Solution().lengthOfLongestSubstring(s)
    print(ret)