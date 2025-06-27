class Solution:
   
    def maxArea(self, height: List[int]) -> int:
        i, ii = 0, len(height) - 1
        maxArea = 0

        while i < ii:
            lowestIndex = min(height[i], height[ii])
            area = lowestIndex * (ii - i)

            if area > maxArea: maxArea = area

            if height[i] < height[ii]: i += 1 
            else: ii -= 1

        return maxArea