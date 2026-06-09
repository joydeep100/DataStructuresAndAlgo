"""933. Number of Recent Calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened 
in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in 
the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
"""

from collections import deque

class RecentCounter1:

    def __init__(self):
        self.ping_times = []
    
    # Used an array O(2n)
    def ping(self, t: int) -> int:
        self.ping_times.append(t)
        valid_time = t - 3000
        count = 0
        for time in self.ping_times[::-1]:
            if valid_time <= time <= t:
                count += 1
            else:
                break
        return count

class RecentCounter2:

    def __init__(self):
        self.ping_times = deque()
    
    ''' I assume that in a queue, insert(0, <item>) would be O(1)
    turns out only pop and popleft are
    ''' 
    def ping(self, t: int) -> int:
        # This itself is O(n)
        self.ping_times.insert(0, t)
        valid_time = t - 3000
        count = 0
        for time in self.ping_times:
            if valid_time <= time <= t:
                count += 1
            else:
                break
        return count
        
class RecentCounter:

    # Better approach, avg case would be better than rest
    def __init__(self):
        self.ping_times = deque()
    
    def ping(self, t: int) -> int:
        self.ping_times.append(t)
        
        valid_time = t - 3000
        while self.ping_times and self.ping_times[0] < valid_time:
            self.ping_times.popleft()
        
        return len(self.ping_times)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)