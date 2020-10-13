class Solution:
  def climbStairs(self, n):

    l = [1, 2]

    for i in range(2, n):
      l.append(l[i-1] + l[i-2])

    return l[n-1]


result = Solution()
print(result.climbStairs(10))

# f = [1, 2, 3, 5]
# append(f[2] + f[1])

# [2,2],[3,3],[4,5],[5,8],[6,13],[7,21],[8,43]
# 5 11111 2111*4 221*3 = 8
# 6 111111 21111*5 2211*6 222 = 13
# 7 1111111 211111*6 22111*10 2221*4 = 21
# 8 11111111 2111111*7 221111*15 22211*10 2222 = 34