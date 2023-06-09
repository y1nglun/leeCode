"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, n):
                dp[i] = max(dp[i], j * max(dp[i - j], i - j))

        return dp[n]


"""
动态规划
转移方程:
剪了第一段后，剩下(i - j)长度可以剪也可以不剪。
如果不剪的话长度乘积即为j * (i - j)；
如果剪的话长度乘积即为j * dp[i - j]。
取两者最大值max(j * (i - j), j * dp[i - j])
"""
