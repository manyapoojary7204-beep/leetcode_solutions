class Solution(object):
    def differenceOfSums(self, n, m):
        numbers = list(range(1, n+1))
        not_divide = [num for num in numbers if num % m != 0]
        divide = [num for num in numbers if num % m == 0]
        return sum(not_divide) - sum(divide)
