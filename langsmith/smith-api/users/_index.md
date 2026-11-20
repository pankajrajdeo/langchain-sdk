---
title: "langsmith/smith-api/users"
description: "Index of 4 pages and 0 subdirectories under langsmith/smith-api/users."
category: "index"
tags: [index, langsmith, smith-api, users]
---

# langsmith/smith-api/users

4 pages here.

## Files

- [Create a user](create-a-user.md) - Stores a user of your application and its traits, such as name and email, for one tracing project. user_id is the ID your runs send in metadata.user_id: 1 to 512 characters. traits is an optional...
- [Get a user](get-a-user.md) - Returns one user of your application and its traits in a tracing project. URL-encode user_id in the path, so that a / in it is sent as %2F.
- [List users](list-users.md) - Returns one page of the users of your application in a tracing project, most recently updated first. page_size sets the number of users per page. To get the next page, pass the response's next_cursor...
- [Update a user's traits](update-a-users-traits.md) - Merges traits into the stored traits of an existing user of your application in a tracing project: keys you send overwrite stored values, keys you do not send are kept, and a key sent as null is...
