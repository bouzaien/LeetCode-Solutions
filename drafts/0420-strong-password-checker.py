class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        b_charNumber, l = self.charNumber(s)
        b_hasLowerAndUpper, low, upp = self.hasLowerAndUpper(s)
        b_threeRepeating = self.threeRepeating(s)
        
        changes = 0
        
        if not b_charNumber:
            if l<6:
                changes = 6-l
            else:
                changes = l-20
        if not self.hasLowerAndUpper(s):
            changes = max(changes, 1)
        if not self.threeRepeating(s):
            changes = max(changes, 1)
        return changes
    
    def charNumber(self, s):
        l = len(s)
        return l>=6 and l<=20, l
    
    def hasLowerAndUpper(self, s):
        lower_count = 0
        upper_count = 0
        for c in s:
            if c.islower():
                lower_count += 1
            if c.isupper():
                upper_count += 1
            if bool(lower_count * upper_count):
                return True, lower_count, upper_count
        return False, lower_count, upper_count
    
    def threeRepeating(self, s):
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == 1:
                return False
            else:
                return True
            
if __name__ == '__main__':
    s = '123456'
    sol = Solution()
    ret = sol.strongPasswordChecker(s)
    print(sol.charNumber(s))
    print(sol.hasLowerAndUpper(s))
    print(sol.threeRepeating(s))
    print(ret)