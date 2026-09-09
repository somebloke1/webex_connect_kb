> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

> ❗️ API Access
> 
> This API is currently in beta and only available to select clients. Please reach out to your account manager for access.

## Prerequisites

- messageId - Generated when you send message using API v2

## Postman Collection

Here is a Postman collection to test our APIs. 

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download](https://www.getpostman.com/) Postman from official site.

## Headers

> 🚧 Authentication
> 
> Messaging API v2 supports both "key" and JWT based authentication. The method of authentication can be selected under the API settings tab in a service.
> 
> If you are passing both JWT authentication and Service Key in an API request, the JWT authentication takes priority.

> 👍 Generating the JWT Token
> 
> Connect uses a subset of the JWT fields, described here:
> 
> alg  
> A string used in the header, identifying the algorithm used to encode the payload. The alg value is always HS256 when exchanging messages with Business Chat.
> 
> iss  
> A claim that is a string identifying the principal that issued the JWT. The value is always the Service ID when exchanging messages with API V2.
> 
> iat  
> A claim that is a numeric date—that is, an integer—identifying the time at which the JWT was issued. The value is the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date and time, ignoring leap seconds. For more information, see the Terminology section in RFC 7519.
> 
> A Service Secret that is a Base64-encoded string. Decode the string before using the key to sign the JWT

A decoded JWT token should contain the following -

```json Decoded JWT Token
header
{
  "alg": HS256,
}
claims
{
  "iss": <Service ID>,
  "iat": <issued at unix-timestamp (in seconds)>
}
```