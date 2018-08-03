class Solution:

    def integerBreak(self, n):
        max = 0
        for x in range(2, n - (n - 1) // 2 + 1):
            product = 1
            intList = self.getIntList(n, x)
            for i in intList:
                product *= i
            if product > max:
                max = product
        return max

    def getIntList(self, n, length):
        base = math.ceil(n / length)
        intList = []
        numBase = n + length - length * base
        for x in range(0, length):
            if x < numBase:
                intList.append(base)
            else:
                intList.append(base - 1)
        return intList


solution = Solution()
print(solution.integerBreak(30))
