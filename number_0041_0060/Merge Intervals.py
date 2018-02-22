# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda interval:interval.start)

        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1].end >= interval.start:
                if result[-1].end < interval.end:
                    result[-1].end = interval.end
            else:
                result.append(interval)

        return result

if __name__ == '__main__':
    intervals = [[1,2],[2,6],[8,10],[15,18]]
    solution = Solution()

    print solution.merge(intervals)

