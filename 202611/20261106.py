# https://leetcode.com/problems/count-zero-request-servers/


class Solution:
    """2747. Count Zero Request Servers

    You are given an integer `n` denoting the total number of servers and a **2D**
    **0-indexed** integer array `logs`, where `logs[i] = [server_id, time]` denotes that
    the server with id `server_id` received a request at time `time`.

    You are also given an integer `x` and a **0-indexed** integer array `queries`.

    Return *a **0-indexed** integer array* `arr` *of length* `queries.length` *where*
    `arr[i]` *represents the number of servers that **did not receive** any requests
    during the time interval* `[queries[i] - x, queries[i]]`.

    Note that the time intervals are inclusive."""

    def count_servers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]: ...

    countServers = count_servers
