# https://leetcode.com/problems/count-mentions-per-user/


class Solution:
    """3433. Count Mentions Per User

    You are given an integer `number_of_users` representing the total number of users
    and an array `events` of size `n x 3`.

    Each `events[i]` can be either of the following two types:

    1. **Message Event:** `["MESSAGE", "timestampi", "mentions_stringi"]`

       * This event indicates that a set of users was mentioned in a message at
    `timestampi`.

       * The `mentions_stringi` string can contain one of the following tokens:

         + `id<number>`: where `<number>` is an integer in range `[0,number_of_users -
    1]`. There can be **multiple** ids separated by a single whitespace and may contain
    duplicates. This can mention even the offline users.

         + `ALL`: mentions **all** users.

         + `HERE`: mentions all **online** users.

    2. **Offline Event:** `["OFFLINE", "timestampi", "idi"]`

       * This event indicates that the user `idi` had become offline at `timestampi` for
    **60 time units**. The user will automatically be online again at time `timestampi +
    60`.

    Return an array `mentions` where `mentions[i]` represents the number of mentions the
    user with id `i` has across all `MESSAGE` events.

    All users are initially online, and if a user goes offline or comes back online,
    their status change is processed *before* handling any message event that occurs at
    the same timestamp.

    **Note** that a user can be mentioned **multiple** times in a **single** message
    event, and each mention should be counted **separately**."""

    def count_mentions(
        self, number_of_users: int, events: list[list[str]]
    ) -> list[int]: ...

    countMentions = count_mentions
