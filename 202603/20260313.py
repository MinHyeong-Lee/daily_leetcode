# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/


class Solution:
    """3296. Minimum Number of Seconds to Make Mountain Height Zero

    You are given an integer `mountain_height` denoting the height of a mountain.

    You are also given an integer array `worker_times` representing the work time of
    workers in **seconds**.

    The workers work **simultaneously** to **reduce** the height of the mountain. For
    worker `i`:

    * To decrease the mountain's height by `x`, it takes `worker_times[i] +
    worker_times[i] * 2 + ... + worker_times[i] * x` seconds. For example:

      + To reduce the height of the mountain by 1, it takes `worker_times[i]` seconds.

      + To reduce the height of the mountain by 2, it takes `worker_times[i] +
    worker_times[i] * 2` seconds, and so on.

    Return an integer representing the **minimum** number of seconds required for the
    workers to make the height of the mountain 0."""

    def min_number_of_seconds(
        self, mountain_height: int, worker_times: list[int]
    ) -> int: ...

    minNumberOfSeconds = min_number_of_seconds
