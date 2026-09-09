# Using JWT for API Authentication

Source: https://developers.webexconnect.io/reference/using-jwt-for-api-authentication
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:39+00:00

JSON Web Tokens are an [open, industry standard RFC 7519 method](https://jwt.io/) for representing claims securely between two parties.

Webex Connect allows you to use JWT tokens for API authentication as an alternative in addition to the 'Service Key'-based authentication.

A JWT is composed of a header, a payload, and a signature. The payload contains information called claims, which describe the subject to whom the token was issued. 

Here's a quick sample:

## Header

**alg **: a string used in the header, identifying the algorithm used to encode the payload. The alg value is always HS256.

```json Header
{
  "alg": "HS256",
  "typ": "JWT"
}
```

## Payload

**iss ** : a claim that is a string identifying the principal that issued the JWT. This value is always the Service ID (this is available on the API tab within a Service in Webex Connect when you select JWT Token as the Auth Type) when exchanging messages.

**iat**: a claim that is a numeric date—that is, an integer—identifying the time at which the JWT was issued. The value is the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date and time, ignoring leap seconds. For more information, see the Terminology section in RFC 7519.

```json Payload
{
  "iss": "<SERVICE ID available on the API tab within a Service in Webex Connect when you select JWT Token as the Auth Type >",
  "iat": 1516239022
}
```

## Verify Signature

Decode the base64 encoded 'SERVICE SECRET' which is accessible within the API tab when you select JWT Auth type and use it to generate the signed bearer token (that is to be passed to Webex Connect for API authentication as a header parameter) using the HS256 algorithm.

```javascript Verify Signature
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  <Decode the base64 encoded SERVICE SECRET and use it here>
)
```

> 🚧 JWT Tokens Expiry
> 
> - Token Expiry: The JWT token expires after 60 minutes from the time that you have generated the token.
> - Token Regeneration: Please note that JSON Web Tokens generated using above approach have limited expiry time. You will need to implement the business logic for regeneration of JWTs in your system/application if you want to use it.

A decoded JWT token should contain the following:

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

### Steps for Setting Up JWT Bearer Authentication in Postman:

Open Postman, and in your request window, click on the **Authorization** tab.

1. Select **JWT Bearer** as the **Auth Type** from the dropdown menu.

   

![JWT Bearer](https://files.readme.io/5753634d67292ec9cf12f942ebdd8ca0c4582d4d760a07ae0f17df3017dc19b0-Screenshot_2024-12-15_052647.png)


2. Select **HS256** as the **Algorithm** from the dropdown menu.
3. Enter the **Service Secret** in the **Secret **. `Service secret is available on the API tab within a service in Webex Connect when you select JWT Token as the Auth type`.

   

![ServiceID and Service Secret](https://files.readme.io/4056482eeb183dc24ecb55a7b21f4e4473dc87ce7025974d3712036b3f1d69b1-Screenshot_2024-12-15_051321.png)


4. Ensure that the **Secret Base64 encoded **option is checked if your secret is _Base64_ encoded.
5. In the Payload section, enter the following JSON:

   ```json
   {
       "iss": "Service ID", // Service ID available on the API tab within a Service in Webex Connect when you select JWT Token as the Auth Type
       "iat": 1734006610 //Numeric date—that is, an integer—identifying the time at which the JWT was issued. The value is the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date and time, ignoring leap seconds.
   }
   ```
6. Ensure all other necessary request details (such as the endpoint URL, headers, and body) are correctly configured and complete the Request Setup.
7. Click **Send ** to execute the request and verify that the JWT Bearer token is being used correctly.

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
