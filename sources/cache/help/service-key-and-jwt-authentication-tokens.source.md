## Understanding the role of Service Key and JWT Auth Credentials

Every Service in <<prodname>> provides authentication credentials (a unique service key and JWT auth credentials) that can be used to authenticate and authorize all external requests to invoke [Messaging APIs](https://developers.imiconnect.io/reference/messagesv2), [Custom Event API](https://developers.imiconnect.io/reference#messagesv2) and [Inbound Webhooks](doc:inbound-webhooks). These credentials are accessible under the API tab within a Service.

Further, you can configure [Outbound Webhooks](doc:outbound-webhooks) to receive delivery receipts for the messages and/or voice calls associated with a Service.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9dd3ccf-Serivce_Key_n_JWT.jpg",
        "Service Key & JWT Authentication Tokens Accessing Service Keys, JWT Authentication Credentials, and Configuring Outbound Webhooks.png",
        "Screenshot of Webex Connect Service Key and JWT Auth Credentials"
      ],
      "align": "center",
      "border": true,
      "caption": "Accessing Service Keys, JWT Authentication Credentials, and Configuring Outbound Webhooks"
    }
  ]
}
[/block]


> 📘 Service Key and JWT Authentication Tokens
> 
> If you pass both JWT Authentication and Service Key in an API request, the JWT Authentication takes priority.
> 
> By default, the Service Key and JWT Authentication Tokens are masked. Only tenant Owners, Full Access Users, and Limited Access Users can see the Service Key and JWT Authentication Tokens by clicking the Show Icon (eye icon) next to these.

## Generating JWT Tokens

> 👍 Generating the JWT Token
> 
> Webex Connect uses a subset of the JWT fields, described here:
> 
> **alg**  
> A string used in the header, identifying the algorithm used to encode the payload. The alg value is always HS256 when exchanging messages with Business Chat.
> 
> **iss**  
> A claim that is a string identifying the principal that issued the JWT. The value is always the Service ID when exchanging messages with API V2.
> 
> **iat**  
> A claim that is a numeric date—that is, an integer—identifying the time at which the JWT was issued. The value is the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date and time, ignoring leap seconds. For more information, see the Terminology section in RFC 7519.
> 
> **exp** (optional)  
> A claim that is a numeric date—that is, an integer—identifying the time at which the JWT will expire. The value is the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date and time, ignoring leap seconds. For more information, see the Terminology section in RFC 7519. The expiry time should be greater than the issued at timestamp.
> 
> A Service Secret is a Base64-encoded string. Decode the string before using the key to sign the JWT. You must include the service secret as a Base-64-encoded string.

> 🚧 JWT Token Expiry
> 
> The JWT token expires after 60 minutes from the time that you have generated the token.

Use any third-party tool like jwt.io to generate the JWT key. Here is a sample payload for JWT authorization:

```objectivec Sample Payload
{
  "alg": "HS256",
  "typ": "JWT"
}

{
  "iss": "<your service key>",
  "iat": 16112812000, //issued at epoch timestamp
  "exp": 16112813000  // expires at epoch timestamp 
}

HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  
<your-256-bit-secret>

) // select the secret base64 encoded checkbox and click ShareJWT
```

After you have generated the JWT token, you can use it in your API request as a header parameter in the following format:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8075f16-jwt-token-in-api-header.png",
        "jwt-token-in-api-header.png",
        "Screenshot displaying How to pass the JWT token when invoking Webex Connect APIs and Webhooks"
      ],
      "align": "center",
      "border": true,
      "caption": "Header Parameters in API"
    }
  ]
}
[/block]


## Rotating authentication credentials periodically

Apart from the service key and the JWT Authentication token automatically generated when a service is created, the <<prodname>> platform provides the ability to generate a second service key/JWT token in addition to the one(s) currently in use. This allows you to have an extra key/JWT auth credentials allowing you to rotate the keys periodically as per security best practices.

> ❗️ Service Key and JWT Tokens Security
> 
> The service key and JWT Authentication tokens must be stored in a secure environment and must not be shared with unauthorized users. If you suspect that a service key or JWT authentication tokens have been compromised, you can regenerate the service key/JWT auth credentials for the concerned Service.

### Creating an Extra Service Key

To create another Service Key:

1. Go to the **API **tab within the service for which you want to create another service key.
2. Select **Service Key** in the **Auth Type** drop-down list.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0fc2c31-Serivce_Key_n_JWT2.jpg",
        "Service Key & JWT Authentication Tokens Create Authentication Credentials.png",
        "Screenshot of Create Authentication Credentials."
      ],
      "align": "center",
      "border": true,
      "caption": "Create Authentication Credentials"
    }
  ]
}
[/block]


3. Click **Create Authentication Credential(s)**. The <<prodname>> platform generates a service key.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/12b2404-Serivce_Key_n_JWT1.jpg",
        "Service Key & JWT Authentication Tokens Creating a Service Key.png",
        "Screenshot of Creating a Service Key."
      ],
      "align": "center",
      "border": true,
      "caption": "Creating a Service Key"
    }
  ]
}
[/block]


### Discarding an existing Service Key

If you no longer require a service key, you can discard it. When you discard a service key, its status changes to \_Inactive \_and you can \_Reactivate \_it at any point.

An inactive service key leads to the failure of any API calls and/or existing event scheduler configurations that use this service key. After you discard a service key, make sure that you save (again) the event scheduler configurations that use this service key to avoid any interruptions in the event scheduler triggers.

To discard a Service Key:

1. Click **Discard **against the required service key.
2. Click **Yes, Discard** in the confirmation message that appears to discard and move the service key to \_Inactive \_status.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2311759-Serivce_Key_n_JWT3.jpg",
        "Service Key & JWT Authentication Tokens Discarding Service Key Credentials.png",
        "Screenshot of Discarding Webex Connect Service Key"
      ],
      "align": "center",
      "sizing": "480px",
      "border": true,
      "caption": "Discarding Service Key Credentials"
    }
  ]
}
[/block]


> 📘 Note
> 
> At any point, you can have only one service key in _Inactive \_status. The <<prodname>> platform mandates that at any point there is at least one service key that is \_Active_. When you discard a service key, the **Discard **action for the other \_Active \_service key is automatically disabled.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ac89ec7-Serivce_Key_n_JWT4.jpg",
        "Service Key & JWT Authentication Tokens Discarding a Service Key.png",
        "Screenshot of Discarding existing JWT Auth Credentials"
      ],
      "align": "center",
      "border": true,
      "caption": "Discarding a JWT Auth credentials"
    }
  ]
}
[/block]


### Reactivating a Service Key

You can only reactivate a service key that is in \_Inactive \_status. To reactivate an \_Inactive \_service key:

1. Click **Reactivate **for the Inactive service key.  
   The service key is reactivated and moves to \_Active \_status.

### Deleting a Service Key

You can only delete a service key that is in \_Inactive \_status. To delete an \_Inactive \_service key:

1. Click the **Delete **icon against the Inactive service key.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4947c26-Serivce_Key_n_JWT5.jpg",
        "Service Key & JWT Authentication Tokens Deleting a Service Key.png",
        "Screenshot of Deleting a Service Key"
      ],
      "align": "center",
      "border": true,
      "caption": "Deleting a Service Key"
    }
  ]
}
[/block]


2. Enter the password and click **Yes, Delete** in the confirmation dialog. The service key gets deleted.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/43d6341-Serivce_Key_n_JWT6.jpg",
        "Service Key & JWT Authentication Tokens Deleting Service Key Credentials.png",
        "Screenshot of the Deleting Service Key Credentials window"
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Deleting Service Key Credentials"
    }
  ]
}
[/block]


### Creating an Extra Pair of JWT Tokens

To create another JWT Token:

1. Go to the **API **tab within the service for which you want to create another JWT Authentication token.
2. Select **JWT Token** in the **Auth Type** drop-down list.
3. Click **Create Authentication Credential(s)**. The <<prodname>> platform generates a JWT Authentication token.

### Discarding a JWT Token

If you no longer require a JWT Token, you can discard it. When you discard a JWT Token, its status changes to \_Inactive \_and you can \_Reactivate \_it at any point.

An inactive JWT Token leads to the failure of any API calls and/or existing event scheduler configurations that use this JWT Token. After you discard a JWT Token, make sure that you save (again) the event scheduler configurations that use this service key to avoid any interruptions in the event scheduler triggers.

To discard a JWT Token:

1. Click **Discard **against the required JWT Token.
2. Click **Yes, Discard** in the confirmation message that appears to discard and move the JWT Token to \_Inactive \_status.

> 📘 Note:
> 
> At any point, you can have only one JWT Token in _Inactive \_status. The <<prodname>> platform mandates that at any point there is at least one JWT Token that is \_Active_. When you discard a JWT Token, the **Discard **action for the other \_Active \_JWT Token is automatically disabled.

### Reactivating a JWT Token

You can only reactivate a JWT Token that is in Inactive status. To reactivate an Inactive JWT Token:

1. Click **Reactivate **for the Inactive JWT Token.  
   The JWT Token is reactivated and moves to \_Active \_status.

### Deleting a JWT Token

You can only delete a JWT Token that is in \_Inactive \_status. To delete an \_Inactive \_JWT Token:

1. Click the **Delete **icon against the \_Inactive \_JWT Token.
2. Enter the password and click **Yes, Delete** in the confirmation dialog. The JWT Token gets deleted.