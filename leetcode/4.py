class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        mx=0
        x=0
        for i in gain:
            x+=i
            mx=max(mx,x)
        return mx