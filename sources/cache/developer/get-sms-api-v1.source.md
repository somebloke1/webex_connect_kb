> 📘 Know Your Endpoint
> 
> SMS channel is supported via Send SMS API v1, Send Message API v2, and Send Message API v1. Refer to the [SMS APIs](https://developers.webexconnect.io/reference/sms) section for information on which API is best suited for your use case.
> 
> The API endpoint for Get SMS API v1 is: 
> 
> [https://api.{YourRegion}.webexconnect.io/v1/sms/messages/{{messageId}].
> 
> Please modify YourRegion in the URL to reflect your tenant’s region. See [Know your endpoint page](https://developers.imiconnect.io/reference/endpoints).
> 
> Refer to [our Postman Collection](https://www.postman.com/ciscodevnet/workspace/webex-connect/collection/26634274-03661a66-48a6-43a4-9a6f-77d6dc84654f) for trying Get SMS API v1.
> 
> **Authentication**
> 
> Refer to the [API Authentication](https://developers.webexconnect.io/reference/authentication-2) section for information on API Authentication.

> 🚧 API Access
> 
> Please note that this API is currently in beta.

## Request Body for Get SMS API v1

Here is a request sample for this API using Service-key-based authentication mechanism.

```curl
curl --location 'https://api.<YourRegion>.webexconnect.io/v1/sms/messages/<messageId>' \
--header 'Authorization: <ServiceKey>'	
```

Here is a request sample for this API using JWT-based authentication mechanism.

```curl
curl --location 'https://api.<YourRegion>.webexconnect.io/v1/sms/messages/<messageId>' \
--header 'Authorization: Bearer <JWT Token>'
```

### Get SMS API v1 Path Parameter

| Parameter | Type   | Mandatory | Description                                                                               |
| :-------- | :----- | :-------- | :---------------------------------------------------------------------------------------- |
| messageId | string | yes       | Specify the message ID that gets generated when you send a message using Send SMS API v1. |

### Get SMS API v1 Header Parameters

| Header        | Type   | Mandatory | Description                                                                              |
| :------------ | :----- | :-------- | :--------------------------------------------------------------------------------------- |
| Authorization | string | yes       | Authorization token (this can be either a JWT signed by a secret key or the service key) |

## Sample Response Body

```json 200 Success
{
    "acceptedTime": "2024-09-04T08:51:47.571-04:00",
    "statusTime": "2024-09-04T08:51:56.000-04:00",
    "messageId": "6deb1c3e-x0x4-XXXX-ad45-aa975403a240",
    "correlationId": "12345676",
    "from": "12345678912",
    "to": "+911XXXX36111",
    "contentType": "text",
    "content": "SMS message content",
    "status": "DELIVERED"
}	
```
```json 403 Authentication Failed
{
    "code": "7001",
    "message": "Authentication failed."
}

```
```text 404 Not Found
<No Response body>
```