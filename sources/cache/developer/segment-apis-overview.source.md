Segments like Topics are used on the <<prodname>> platform for broadcasting messages to app users on in-app and push messaging channels. Segments are equivalent to a target group that is identified prior to attempting the delivery of a message. Segments like topics are defined for a particular appid on <<prodname>>. 

A segment can be of two types:

- A list of user ids of your app users. You should pass the app userids to create such segments.
- A combination of multiple topics. These segments are created by passing a conditional expression (AND - & and OR - |) on involved topic ids.

> 📘 JWT Authentication
> 
> <<prodname>> allows using JWT Authentication for the [Thread APIs](https://developers.imiconnect.io/reference#overview-of-thread-apis), Segment APIs, and [Topic APIs](https://developers.imiconnect.io/reference#overview-3). Please reach out to the support team to enable the JWT Authentication.

## Postman Collection

Here is a Postman collection to test our APIs. Make sure you change the key in the header to your service key.

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download Postman from here](https://www.getpostman.com/)

The following are the APIs in this section:

- [Create Segment](ref:create) 
- [Delete Segment](ref:delete-1)
- [Delete Users from Segment](ref:delete-users-from-segment)  
- [List](ref:list-1) 
- [Update](ref:update)
- [Add Users](ref:add-users)
- [Get All Users](ref:get-all-users).