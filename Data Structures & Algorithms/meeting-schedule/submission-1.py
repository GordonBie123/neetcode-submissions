"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if we get to the end of the array and no conflict then we return true
        intervals.sort(key=lambda x: x.start)
        slow, fast = 0, 1
        while fast < len(intervals):
            if intervals[slow].end > intervals[fast].start:
                return False
            slow +=1 
            fast += 1
        return True