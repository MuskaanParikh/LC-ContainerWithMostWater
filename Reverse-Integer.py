class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        

        if result < INT_MIN or result > INT_MAX:
            return 0
        if x < 0: return -result
        return result

        