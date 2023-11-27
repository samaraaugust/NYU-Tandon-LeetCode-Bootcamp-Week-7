class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for start, curr_end in points[1:]:
            if start > end:
                arrows += 1
                end = curr_end

        return arrows
