class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

        # {"alice": {1:"happy", 2:"sad"}}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        arr = self.time_map[key]
        left, right = 0, len(arr) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res
