class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []

        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user]) - 1

                time, tweetId = self.tweets[user][index]

                heapq.heappush(heap, (-time, tweetId, user, index))
        
        result = []

        while heap and len(result) < 10:
            negative_time, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)
            if index > 0:
                time, olderTweetId = self.tweets[user][index - 1]

                heapq.heappush(heap, (-time, olderTweetId, user, index - 1))
        return result
                

            
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
