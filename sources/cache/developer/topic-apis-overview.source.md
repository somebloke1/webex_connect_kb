Topics in <<prodname>> are meant for broadcasting messages to your app users on in-app and push messaging channels. Topics are typically used to categorize and collate the app user preferences and interests. These can be direct customer opt-ins or based on customer behavior over time. The topics are unique for an appid on <<prodname>> and are categorized into multiple groups. The SDK and API endpoints can be used for managing topics of a particular appid and/or a particular app user. 

A topic should be used as the destination in the messaging API request to broadcast messages to all the subscribed app users. The destination can be a single topic id or a conditional expression of multiple topic ids. The available operators are UNION or OR (use ||), INTERSECTION or AND ( use & ), COMPLEMENT or NOT (use ' ) and DIFFERENCE or MINUS (use - ). 

> 📘 JWT Authentication
> 
> <<prodname>> allows using JWT Authentication for the [Thread APIs](https://developers.imiconnect.io/reference#overview-of-thread-apis), [Segment APIs](https://developers.imiconnect.io/reference#overview-4), and Topic APIs. Please reach out to the support team to enable the JWT Authentication.

## Postman Collection

Here is a Postman collection to test our APIs. Make sure you change the key in the header to your service key.

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download Postman from here](https://www.getpostman.com/)

The following are the APIs in this section:

- [Create a topic](https://developers.imiconnect.io/reference/createtopic)
- [Delete a topic](ref:delete)
- [List a topic](ref:list)
- [Get topics per app id](ref:get-2)
- [Subscribe](ref:subscribe)
- [Get All Subscribers of a topic](https://developers.imiconnect.io/reference/get-all-subscribers)
- [Get All Topics](ref:get-all-topics)
- [Unsubscribe User from Topic](ref:unsubscribe-user-from-topics).

## **Error Codes**

| Description                                 | Error code |
| :------------------------------------------ | :--------- |
| Internal error while processing the request | 1          |
| Topic already exists                        | 2          |
| Required attributes missing                 | 3          |
| Invalid request                             | 4          |
| Appid/Topic does not exist                  | 5          |
| UserId does not exist                       | 7          |
| Secret key is missing in header             | 11         |
| AppId is required                           | 14         |
| Secretkey is invalid                        | 26         |
| Stream not found for given appId and userId | 31         |