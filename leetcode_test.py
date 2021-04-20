# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         if len(nums) >= 1:  # 判断数组长度是否符合计算要求
#             if isinstance(nums[0], int): # 判断数组类型是否符合计算要求
#                 rtype = [nums[0]]
#                 for i in range(1, len(nums)):
#                     if isinstance(nums[i], int):
#                         total = rtype[i-1] + nums[i]
#                         rtype.append(total)
#                     else:
#                         return '数据类型错误'
#                 return rtype
#             else:
#                 return '数据类型错误'
#         else:
#             return 'nums数组长度为0'
#     main
#     nums = [1]
#     a = Solution()
#     b = a.runningSum(nums)
#     print(b)

# class Solution:
#     def reverseLeftWords(self, s: str, n: int) -> str:
#         if 1 <= n < len(s):
#             return s[n:] + s[:n]
#         else:
#             return 'n值不符合要求'
#     main
#     a = Solution()
#     b = a.reverseLeftWords(s='abcdefgh', n=5)
#     print(b)

# a = '   -123  '
# b = a.split()
# c = 2 ** 31 % 10
# d = '9'
# e = int(d)
# summation = []
# i = 2
# for j in range(i, 6*i+1):
#     summation.append(j)

# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         product = 1
#         summation = 0
#         while n > 0:
#             value = n % 10
#             n //= 10
#             product *= value
#             summation += value
#         return product-summation
#     a = Solution()
#     n = 234
#     b = a.subtractProductAndSum(n)
#     print(b)

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         b = 0
#         for i in nums:
#             b += i
#         a = int((n * (n-1) / 2)-b
#         if not 0 in nums:
#             return 0
#         if a in nums:
#             return n
#         return a
#
# l = Solution()
#     m = [0,1,2,3,4,6]
#     n = l.missingNumber(m)
#     print(n)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(i in jewels for i in stones)

if __name__ == '__main__':
    a = Solution()
    j = "aA"
    s = "aAAbbbb"
    b = a.numJewelsInStones(jewels=j, stones=s)
    print(b)