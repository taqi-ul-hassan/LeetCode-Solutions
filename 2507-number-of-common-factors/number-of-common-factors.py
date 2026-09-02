class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a,b)
        result = []
        for i in range(1,g+1):
            if g%i == 0:
                result.append(g)
        return len(result)
