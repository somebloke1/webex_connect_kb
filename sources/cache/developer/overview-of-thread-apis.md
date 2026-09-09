# Overview

Source: https://developers.webexconnect.io/reference/overview-of-thread-apis
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:50+00:00

A thread is used to stitch together all messages sent or received within a particular context into a conversation. Webex Connect offers the ability to create, update, delete, and list threads to enable businesses to make one-way announcements or hold two-way conversations with their mobile/web app users.

> 📘 JWT Authentication
> 
> Webex Connect allows using JWT Authentication for the Thread APIs, [Segment APIs](https://developers.imiconnect.io/reference#overview-4), and [Topic APIs](https://developers.imiconnect.io/reference#overview-3). Please send an email to the support team if you would like to enable JWT Authentication for these APIs.

## Postman Collection

Here is a Postman collection to test our APIs. 

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download Postman from here](https://www.getpostman.com/)

The following are the APIs in this section:

- [User Messages](https://developers.imiconnect.io/reference/user-messages-1) 
- [Create Thread](https://developers.imiconnect.io/reference/create-thread-1) 
- [User Threads](https://developers.imiconnect.io/reference/user-threads-1)
- [User Messages v2](https://developers.imiconnect.io/reference/user-messages-2) 
- [Get Threads](https://developers.imiconnect.io/reference/app-threads-1) 
- [Update Thread](https://developers.imiconnect.io/reference/update-thread)
- [Get Streams - Legacy](https://developers.imiconnect.io/reference/list-streams).

Try our APIs using the [Postman](https://www.getpostman.com/) collection here:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.getpostman.com/collections/5464829fe527f20b349d)

### Rate Thread APIs

| API Name                                                | Default TPS at Tenant Level                                            |
| :------------------------------------------------------ | :--------------------------------------------------------------------- |
| Delete User Messages (all versions)                     | For existing tenants unlimited and default value for new tenants - 100 |
| Get App Threads                                         | For existing tenants unlimited and default value for new tenants - 10  |
| Get User Threads (with and without unread thread count) | For existing tenants unlimited and default value for new tenants -10   |
| Get User Messages all versions                          | For existing tenants unlimited and default value for new tenants -100  |

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "get",
  "url": "",
  "auth": "required",
  "results": {
    "codes": [
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 200
      },
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 400
      }
    ]
  },
  "params": [],
  "examples": {
    "codes": []
  }
}
```
