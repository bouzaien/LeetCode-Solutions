class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))