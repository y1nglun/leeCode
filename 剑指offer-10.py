"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, (a + b) % 1000000007
        return b
