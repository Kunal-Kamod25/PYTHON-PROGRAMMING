class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            ans = ans * 10 + digit

        ans *= sign

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(1534236469))
