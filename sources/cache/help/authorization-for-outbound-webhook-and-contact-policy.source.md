## Adding a New Authorization

Adding authorization for outbound webhook allows the notification receiving server to confirm that the notifications are being sent from an authorized system. The receiving server can verify the token received in the header of the request. Successful verification of the token indicates that the notification is received from the authorized system.

To add an authorization for an Outbound Webhook, follow the below steps:

1. Navigate to Assets → Integrations.

2. Click **Add Authorization**.

3. Enter a name for the authorization.

4. For the **Type** option, select one of the following authorization types below. Jump to the respective sections after this procedure for learning more about the configuration details.
   1. No Auth - Select this type when you do not need an authorization.
   2. [Basic Auth](https://help.imiconnect.io/docs/authorization-for-outbound-webhook#basic-auth) - Select this type when you need to authorize using username and password.
   3. [Digest Auth](https://help.imiconnect.io/docs/authorization-for-outbound-webhook#digest-auth) - Select this option when you need to validate the user identity before sending any sensitive information like online banking transactional details.
   4. [AWS Signature](https://help.imiconnect.io/docs/authorization-for-outbound-webhook#aws-signature) - Select this option when you want to use the Amazon Web Services workflow for authorization.
   5. API Key - Enter the Key and Key Value.
   6. [OAuth 2.0](https://help.imiconnect.io/docs/authorization-for-outbound-webhook#oauth-20) - It is a well-adopted delegated authorization framework. Supports two different grant types for OAuth 2.0.

5. Click **Save**.  
   The created authorization will be displayed in the list of authorizations which you can associate with the desired Outbound Webhook configuration.

> 📘 Note
> 
> We are extending the existing capabilities of authorizations supported in <<prodname>> and integrating it within Contact Policy Group Subscription Notification API.

### Basic Auth

The configuration details are mentioned below as follows:

| Field             | Description                                                   |
| :---------------- | :------------------------------------------------------------ |
| Username/Password | Login credentials that you want to use for authentication.    |
| Parameter value   | This is applicable if the parameter is static. Provide value. |

### Digest Auth

In this type of authorization, a network server receives the request from a user and then sends it to a domain controller. The domain controller responds with a special session key.

| Field        | Description                                                                                                                                                                                                                                                                                                    |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Username     | Username to authenticate the request.                                                                                                                                                                                                                                                                          |
| Realm        | String from the server within the **www-Authenticate** response header.                                                                                                                                                                                                                                        |
| Password     | The password to authenticate the request.                                                                                                                                                                                                                                                                      |
| Nonce        | Unique string from the server within the **www-Authenticate** response header.                                                                                                                                                                                                                                 |
| Algorithm    | String that indicates a pair of algorithms used to produce the digest and a checksum.                                                                                                                                                                                                                          |
| QOP          | The quality of protection applied to the message. The value must be one of the alternatives specified by the server in the **www-Authenticate** response header.                                                                                                                                               |
| Nonce Count  | The hexadecimal count of the number of requests (including the current request) that the client has sent with the nonce value in this request. You must specify the count only if a QOP directive is sent in the **www-Authenticate** response header.                                                         |
| Client Nonce | An opaque quoted string value provided by the client. This value is used by both client and server to avoid chosen plaintext attacks, provide mutual authentication, and message integrity protection. You must specify the count only if a QOP directive is sent in the **www-Authenticate** response header. |
| Opaque       | A string specified by the server in the **www-Authenticate** response header. Use this string as is with URLs in the same protection space. <<prodname>> recommends that this string be base-64 encoded data.                                                                                                  |

### AWS Signature

You must use a custom HTTP scheme based on a keyed-HMAC (Hash Message Authentication Code) for authentication.

| Field        | Description                                                    |
| :----------- | :------------------------------------------------------------- |
| Access_Key   | Unique access key for an account used to send the request.     |
| Secret_Key   | The unique secret key for an account used to send the request. |
| Region       | The region that receives the request.                          |
| Service_name | Service that receives the request.                             |

### OAuth 2.0.

Two grant types are supported for OAuth 2.0.

1. Authorization Code - server issues the token in the context of a user.
2. Client Credentials - grant type is used to obtain an access token outside of the context of a user.

The following details are to be added on the Add Authorization page after selecting the Grant Type. Some fields or options are displayed when selecting either of the two types or both.

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Consumer ID",
    "0-1": "Unique identifier of the consumer obtained during the registration process.",
    "1-0": "Grant Type",
    "1-1": "Type of authentication - Authorization Code or Client Credentials. Its selection depends on the grant type offered by the API.",
    "2-0": "Client ID (Client Credentials only)",
    "2-1": "Unique identifier of the client obtained from the platform through which the authorization is done.",
    "3-0": "Client Secret (Client Credentials only)",
    "3-1": "The unique secret of the client obtained from the platform through which the authorization is done.",
    "4-0": "Consumer ID (Authorization Code only)",
    "4-1": "Unique identifier of the consumer obtained during the registration process.",
    "5-0": "Consumer Secret (Authorization Code only)",
    "5-1": "The unique secret of the consumer obtained during the registration process.",
    "6-0": "Call Back URL (Authorization Code only)",
    "6-1": "<<prodname>> callback URL will be used during the registration process at the authorization provider’s end. Note: The [callback URL](https://help.imiconnect.io/docs/custom-nodes#section-callback-url) is not accessible from a web browser. You need to test it using the Custom Node only.",
    "7-0": "Authorization URL (Authorization Code only)",
    "7-1": "Endpoint for authorization server, which retrieves the authorization code must be provided by the authorization provider.",
    "8-0": "Scope",
    "8-1": "Scope of the access request (multiple space-separated values). This is optional.",
    "9-0": "Access Token URL",
    "9-1": "Endpoint for the resource server, which exchanges the authorization code for an access token.",
    "10-0": "Access token has a limited validity",
    "10-1": "Specifies if the token has a limited validity and must be provided by the authorization provider.",
    "11-0": "Validity",
    "11-1": "Validity of the token. This is based on the the OAuth Provider. The value is mostly returned in seconds.",
    "12-0": "Refresh URL Token",
    "12-1": "It should be provided by the authorization provider.  \n  \nIt ensures smooth functioning of authorization in the case provided access token has limited validity.",
    "13-0": "Advance Settings",
    "13-1": "Toggle button that allows you to enable or disable advanced settings.",
    "14-0": "Access Token URL Method",
    "14-1": "An additional method for the access token.",
    "15-0": "Access Token URL Parameter type",
    "15-1": "Type of access token URL parameter – Body or URL.",
    "16-0": "Access Token URL Headers",
    "16-1": "Additional URL header parameters for the access token",
    "17-0": "Get Access Token",
    "17-1": "Button to retrieve the access token.",
    "18-0": "Access Token",
    "18-1": "Displays the refresh token.",
    "19-0": "Refresh Token",
    "19-1": "Displays the refresh token.",
    "20-0": "Client Authentication",
    "20-1": "Value of Client Authentication is defined by the authorization provider’s API.  \n  \nSend client credentials in body is selected by default."
  },
  "cols": 2,
  "rows": 21,
  "align": [
    "left",
    "left"
  ]
}
[/block]