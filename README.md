# daily_leetcode [![Generate Active Daily Every Day at 00:00 UTC](https://github.com/MinHyeong-Lee/daily_leetcode/actions/workflows/generate_active_daily.yml/badge.svg)](https://github.com/MinHyeong-Lee/daily_leetcode/actions/workflows/generate_active_daily.yml)

This repository is copied from yyolk's [leetcode_dailies](https://github.com/yyolk/leetcode_dailies)

My daily leetcode problem submissions


## Generate today's boilerplate

Calls the 'undocumented' leetcode graphQL API to query for `activeDailyChallengeQuestion`.

It includes everything we want to generate our answer boilerplate.

```
python -m generate_active_daily
```

### Backfill missing permalinks in the solutions

This is an abnormal operation, it could be run during the daily upkeep, but all new boilerplate solutions include it already[^1].

```
python -m generate_active_daily.backfill_solution_links --no-debug --overwrite
```

## Generate the Solution Directories TOC

Each solution dir has a README.md with a table of contents that is a calendar with the days completed, hyperlinked to that solution file.

```
python -m generate_calendar_toc
```