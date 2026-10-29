"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort meetings by start time
        intervals.sort(key=lambda interval: interval.start)

        # Min-heap containing the end time of each occupied room
        end_times = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # Reuse the room that becomes available earliest
            if end_times and end_times[0] <= start:
                heapq.heappop(end_times)

            # Occupy a room until this meeting ends
            heapq.heappush(end_times, end)

        return len(end_times)