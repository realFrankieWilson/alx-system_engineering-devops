## 0x16. API advanced
---

The advanced part of the api

This projects aim at using queries to make a get request to some api endpoint and working with them in order to get some certain information according to the need
---

#### General
*	How to read API documentation to find the endpoints you’re looking for
*	How to use an API with pagination
*	How to parse JSON results from an API
*	How to make a recursive API call
*	How to sort a dictionary by value
---

#### Tasks:
---

##### 0. How Many subs?
---
This deals with function that querries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and returns the number of subscribers (not activer users, total subscribers) for a given subreddit.
The function returns 0 if an invalid subreddit is given.
---

##### 1. Top Ten
---
This function queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and prints the titles of the first 10 hot posts listed for a given subreddit.
---

##### 2. Recurse it!
---
The function is a recursive one that querries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA) and returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function returns None.
---

#### Advanced Task:
---
##### Count it!
---
This function is also a recursive function that queries the [Reddit API](https://intranet.alxswe.com/rltoken/b-4nD6hwEeNYTwYl5yWNwA), parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript counst as javascript, although, java is not).
---

#### Author:
__Frank Williams Ugwu__
