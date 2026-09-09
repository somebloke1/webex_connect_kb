This document details the channel-specific status codes and the associated reasons for message delivery failure. 

> 📘 Columns
> 
> Please note that the 'Details' column is added in tables when there is additional information to be provided about the information in the 'Description' column.

## Common Error Codes across Channels

| Error Code | Description                                       |
| :--------- | :------------------------------------------------ |
| 7000       | Invalid JSON                                      |
| 7001       | Authentication failed                             |
| 7002       | Service Key Missing                               |
| 7003       | Mandatory parameters missing                      |
| 7004       | Invalid parameters/Values                         |
| 7005       | Request expired                                   |
| 7006       | Internal error occurred                           |
| 7007       | Service inactive                                  |
| 7009       | Max number of destination address limited to 1000 |
| 7020       | You have reached the maximum transaction limit    |
| 7104       | Invalid app id                                    |
| 7108       | Invalid template ID                               |
| 7200       | Unknown Status                                    |

## Apple Messages for Business

| Status Code | Description                             |
| :---------- | :-------------------------------------- |
| 7000        | Invalid input details(JSON not correct) |
| 7006        | Internal server error                   |
| 7010        | Service provider exception              |
| 7011        | Unknown Exception                       |
| 7301        | Message expired                         |
| 7307        | Endpoint not reachable                  |
| 7316        | Invalid application details             |
| 7317        | Merchant API session failed             |
| 7501        | Submitted                               |
| 7738        | Failed to upload media                  |
| 1001        | Queued                                  |
| 7000        | Invalid JSON                            |
| 7001        | Authentication failed                   |
| 7002        | Service key missing                     |
| 7003        | Mandatory parameters missing            |
| 7004        | Invalid parameters                      |
| 7007        | Service inactive                        |
| 7009        | Max number of destinations              |
| 7722        | Parameter value is invalid              |

## Email

[block:parameters]
{
  "data": {
    "h-0": "Status Code",
    "h-1": "Description",
    "h-2": "Details",
    "0-0": "7500",
    "0-1": "Delivered",
    "0-2": "Returned when e-mail is delivered",
    "1-0": "7501",
    "1-1": "Submitted",
    "1-2": "Returned when e-mail sent to the gateway",
    "2-0": "7502",
    "2-1": "Read",
    "2-2": "Returned when e-mail is read",
    "3-0": "7520",
    "3-1": "Bounce",
    "3-2": "The following bounce types are possible:  \n  \n- Undetermined: Indicates Amazon SES was unable to determine a specific bounce reason.\n- Permanent (general): Indicates Amazon SES received a general hard bounce and recommends that you remove the recipient's email address from your mailing list.\n- Permanent (no email): Indicates Amazon SES received a permanent hard bounce because the target email address does not exist. It is recommended that you remove that recipient from your mailing list.\n- Permanent (suppressed): Indicates Amazon SES has suppressed sending to this address because it has a recent history of bouncing as an invalid address.\n- Transient (general): Indicates Amazon SES received a general bounce. You may be able to successfully retry sending to that recipient in the future.\n- Transient (mail box full): Indicates Amazon SES received a mailbox full bounce. You may be able to successfully retry sending to that recipient in the future.\n- Transient (message too large): Indicates Amazon SES received a message too large bounce. You may be able to successfully retry sending to that recipient if you reduce the message size.\n- Transient (content rejected): Indicates Amazon SES received a content rejected bounce. You may be able to successfully retry sending to that recipient if you change the message content.\n- Transient (attachment rejected): \t  \n  Indicates Amazon SES received an attachment rejected bounce. You may be able to successfully retry sending to that recipient if you remove or change the attachment.\n- Emails that failed to deliver due to soft bounces, such as Transient (Mailbox full) might still get Delivered notification, since the email clients first acknowledge the delivery of email before establishing issues such as recipient mailbox being full.\n- In case of soft bounces, Amazon SES retries sending email multiple times for 14 hours and notifies soft bounce only if delivery is still unsuccessful.",
    "4-0": "7521",
    "4-1": "Complaint",
    "4-2": "The following complaint types are possible:  \n  \n- Abuse: Indicates unsolicited email or some other kind of email abuse.\n- Auth-failure: Email authentication failure report.\n- Fraud: Indicates some kind of fraud or phishing activity.\n- Not-spam: Indicates that the entity providing the report does not consider the message to be spam. This may be used to correct a message that was incorrectly tagged or categorized as spam.\n- Other: Indicates any other feedback that does not fit into other registered types.\n- Virus: Reports that a virus is found in the originating message.",
    "5-0": "7522",
    "5-1": "Email address is not verified",
    "5-2": "This occurs when the account is in sandbox mode. Returned when destination email address is not verified.",
    "6-0": "7523",
    "6-1": "Invalid email address",
    "6-2": "Returned when destination email address is invalid. The email ID should be in the format: [abc@xyz.com](mailto:abc@xyz.com) where “abc” is the unique combination of string and numerics or one of the two, while “xyz” is the domain or server to be linked to. As part of the syntax, “@” and “.” are mandatory to ensure the validity of the email address.",
    "7-0": "7524",
    "7-1": "Email address max length reached",
    "7-2": "Returned when the maximum email length has been reached. According to the example above - “[abc@xyz.com](mailto:abc@xyz.com)”, the maximum length of “abc” should be less than or equal to 64 characters and the maximum length of “xyz.com” should be less than or equal to 255 characters. The total character length of the email address should not exceed 320 (inclusive of “@”).",
    "8-0": "7528",
    "8-1": "Clicked",
    "8-2": "Returned when the email is clicked.",
    "9-0": "7535",
    "9-1": "attachment length exceeded",
    "9-2": "Returned when overall email size including attachment exceeds the limit. For clients post version 5.63, the limit is 40MB.",
    "10-0": "7536",
    "10-1": "Exception while parsing the EMAIL Template, unable to fetch template",
    "10-2": "",
    "11-0": "7240",
    "11-1": "already bounced: [abc@domain.tld](mailto:abc@domain.tld) ",
    "11-2": "Returned when there is an attempt to send email again to the same email address after a bounce.",
    "12-0": "7241",
    "12-1": "EmailId in unsubscribe blocked list",
    "12-2": "\\* Returned when the destination  email is found in **<<prodname>>**  unsubscribe list.",
    "13-0": "7553",
    "13-1": "SMTP Authentication Failed",
    "13-2": "",
    "14-0": "7554",
    "14-1": "SMTP Failures",
    "14-2": ""
  },
  "cols": 3,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Google Business Messages **(Deprecated)**

| Error Code | Description                                                                                                                                                                                                                                                         |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 7900       | No error                                                                                                                                                                                                                                                            |
| 7904       | Request not authenticated due to missing, invalid, or expired OAuth token.                                                                                                                                                                                          |
| 7905       | Client does not have sufficient permission. This can happen because the OAuth token does not have the right scopes, the client doesn't have permission, or the API has not been enabled.                                                                            |
| 7906       | A specified resource is not found.                                                                                                                                                                                                                                  |
| 7909       | Either out of resource quota or reaching rate limiting. The client should look for google.rpc.QuotaFailure error detail for more information.                                                                                                                       |
| 7910       | Request cancelled by the client.                                                                                                                                                                                                                                    |
| 7913       | API method not implemented by the server.                                                                                                                                                                                                                           |
| 7914       | Network error occurred before reaching the server. Typically a network outage or misconfiguration.                                                                                                                                                                  |
| 7915       | Service unavailable. Typically the server is down.                                                                                                                                                                                                                  |
| 7916       | Request deadline exceeded. This will happen only if the caller sets a deadline that is shorter than the method's default deadline (i.e. requested deadline is not enough for the server to process the request) and the request did not finish within the deadline. |
| 7901       | Client specified an invalid argument. Check error message and error details for more information.                                                                                                                                                                   |
| 7902       | Request can not be executed in the current system state, such as deleting a non-empty directory.                                                                                                                                                                    |
| 7903       | Client specified an invalid range.                                                                                                                                                                                                                                  |
| 7907       | Concurrency conflict, such as read-modify-write conflict.                                                                                                                                                                                                           |
| 7908       | The resource that a client tried to create already exists.                                                                                                                                                                                                          |
| 7911       | Unrecoverable data loss or data corruption. The client should report the error to the user.                                                                                                                                                                         |
| 7917       | Unknown server error. Typically a server bug.                                                                                                                                                                                                                       |
| 7912       | Internal server error. Typically a server bug.                                                                                                                                                                                                                      |
| 7501       | Submitted                                                                                                                                                                                                                                                           |
| 7500       | Delivered                                                                                                                                                                                                                                                           |
| 7502       | Read                                                                                                                                                                                                                                                                |
| 7307       |                                                                                                                                                                                                                                                                     |

## In-App Messaging and Live Chat

| Status Code | Description                                                                                                              |
| :---------- | :----------------------------------------------------------------------------------------------------------------------- |
| 7500        | Delivered                                                                                                                |
| 7501        | Submitted                                                                                                                |
| 7502        | Read                                                                                                                     |
| 7000        | Invalid input details                                                                                                    |
| 7006        | Internal server error                                                                                                    |
| 7010        | Service provider exception                                                                                               |
| 7011        | Unknown Exception                                                                                                        |
| 7301        | Message expired                                                                                                          |
| 7304        | Invalid app credentials(Invalid OAuth)                                                                                   |
| 7305        | Invalid user credentials                                                                                                 |
| 7307        | End point not reachable                                                                                                  |
| 7308        | Invalid topic                                                                                                            |
| 7309        | No topic subscribers found                                                                                               |
| 7310        | No segment found                                                                                                         |
| 7311        | Thread or streamname required                                                                                            |
| 7312        | Invalid thread id                                                                                                        |
| 7000        | Invalid JSON (Generic Template)                                                                                          |
| 7003        | param 'mediaid' or type based attachment is required (Generic Template)                                                  |
| 7004        | param 'title' in notification, is missed or empty (Generic Template)                                                     |
| 7034        | Max allowed elements reached - Upto 8 elements are allowed in attachments (Generic Template)                             |
| 7703        | Max allowed buttons in a section reached  - Upto 3 buttons allowed in element (Generic Template)                         |
| 7704        | Duplicate identifiers not allowed (Generic Template)                                                                     |
| 7708        | Max allowed image urls reached - Upto 5 allowed URLs in element (Generic Template)                                       |
| 7004        | invalid value for param 'type' in rt attachment, only image, location, file, video and audio are allowed (Quick Replies) |
| 7003        | param 'mediaid' or type based attachment is required (Quick Replies)                                                     |
| 7704        | Duplicate identifiers not allowed (Quick Replies)                                                                        |
| 7706        | Max allowed quick replies reached -  max  5 quick replies will be allowed (Quick Replies)                                |
| 7026        | Request Json parameter size exceeded 4 KB (Quick Replies)                                                                |

## Instagram **(Deprecated)**

| Error Code | Description                                                                               |
| :--------- | :---------------------------------------------------------------------------------------- |
| 7000       | Invalid input details(JSON not correct)                                                   |
| 7307       | End point not reachable                                                                   |
| 7302       | Rate limit exceeded                                                                       |
| 7301       | Message expired                                                                           |
| 7303       | Delivery notification of a message expired                                                |
| 7006       | Internal server error                                                                     |
| 7304       | Invalid app credentials(Invalid OAuth)                                                    |
| 7305       | Invalid user credentials                                                                  |
| 7306       | Duplicate message                                                                         |
| 7011       | Unknown Exception                                                                         |
| 7501       | Submitted                                                                                 |
| 7500       | Delivered                                                                                 |
| 7502       | Read                                                                                      |
| 7010       | Service provider exception                                                                |
| 7526       | Either subscription messaging permission not enabled or invalid tag received from request |
| 7313       | Inbound message not received from user                                                    |

## MMS

| Status Code | Description                                                                                                          |
| :---------- | :------------------------------------------------------------------------------------------------------------------- |
| 7010        | Service provider exception                                                                                           |
| 7144        | Delivery to the country code not supported                                                                           |
| 7145        | Slide message max text size exceeded                                                                                 |
| 7146        | Max slides exceeded                                                                                                  |
| 7147        | Quota exceeded at route level                                                                                        |
| 7148        | Invalid attachment type                                                                                              |
| 7212        | Invalid request. Make a valid request via GET/POST/XML with all the required variables                               |
| 7213        | User Authentication Failed                                                                                           |
| 7214        | This account has no API rights                                                                                       |
| 7215        | You can call API every X seconds                                                                                     |
| 7216        | This account has no rights to use this action                                                                        |
| 7217        | XML Parse error: $error                                                                                              |
| 7218        | API not activated                                                                                                    |
| 7219        | Invalid receiver number                                                                                              |
| 7220        | Invalid short code                                                                                                   |
| 7221        | IP was not allowlisted. API call rejected                                                                            |
| 7222        | Set throughput exceeded for this API action. API call rejected                                                       |
| 7223        | Phone number is in blocked list. API call rejected                                                                   |
| 7224        | Account has reached the API request limit                                                                            |
| 7225        | More than one object is not allowed in the same slide                                                                |
| 7226        | MMS audio/video/image are not allowed with object in the same slide                                                  |
| 7227        | Too many Slides                                                                                                      |
| 7228        | Audio and Video not allowed in same slide                                                                            |
| 7229        | Video and Image not allowed in same slide                                                                            |
| 7230        | Text more than X characters                                                                                          |
| 7231        | Content not allowed                                                                                                  |
| 7232        | Bad X slide duration                                                                                                 |
| 7233        | This content does not exist                                                                                          |
| 7234        | The name is required                                                                                                 |
| 7235        | No slides                                                                                                            |
| 7236        | Slide X is empty                                                                                                     |
| 7237        | Image in slide X is too big                                                                                          |
| 7238        | Audio in slide X is too big                                                                                          |
| 7239        | Video in slide X is too big                                                                                          |
| 7242        | Text in slide X is too long                                                                                          |
| 7243        | vCard in slide X is too big                                                                                          |
| 7244        | iCal in slide X is too big                                                                                           |
| 7245        | PDF in slide X is too big                                                                                            |
| 7246        | Passbook file in slide X is too big                                                                                  |
| 7247        | Image file in slide X is corrupted                                                                                   |
| 7248        | Could not copy Image in slide X                                                                                      |
| 7249        | Could not copy Audio in slide X                                                                                      |
| 7250        | Could not copy Video in slide X                                                                                      |
| 7251        | Could not copy vCard in slide X                                                                                      |
| 7252        | Could not copy iCal in slide X                                                                                       |
| 7253        | Could not copy PDF in slide X                                                                                        |
| 7254        | Could not copy Passbook file in slide X                                                                              |
| 7255        | Internal error                                                                                                       |
| 7256        | mmslink_expiration_date is invalid                                                                                   |
| 7257        | Carrier lookup failed. Please retry                                                                                  |
| 7258        | Carrier not provisioned                                                                                              |
| 7259        | The fallbacksmstext is required                                                                                      |
| 7260        | Invalid serviceid / serviceid is required                                                                            |
| 7261        | Operator Not supported                                                                                               |
| 7262        | Unrecognized content type                                                                                            |
| 7263        | The ‘operator id’ is required                                                                                        |
| 7264        | Number is not subscribed in this campaign                                                                            |
| 7265        | The campaignref is required                                                                                          |
| 7266        | Invalid campaignref                                                                                                  |
| 7267        | Message failed at vendor                                                                                             |
| 7268        | Message rejected or not supported at vendor                                                                          |
| 7269        | API access is blocked for this account. Please check the status of this account or its primary account if applicable |
| 7270        | Message delivery expired by operator                                                                                 |
| 7271        | Message delivery expired by application                                                                              |
| 7272        | Invalid VASID/VASPID                                                                                                 |

## Messenger

| Status Code | Description                                                                                                                                                                                       |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 7000        | Invalid input details(JSON not correct)                                                                                                                                                           |
| 7006        | Internal server error                                                                                                                                                                             |
| 7010        | Service provider exception                                                                                                                                                                        |
| 7011        | Unknown Exception                                                                                                                                                                                 |
| 7301        | Message expired                                                                                                                                                                                   |
| 7303        | Endpoint not reachable                                                                                                                                                                            |
| 7313        | Inbound message not received from the user                                                                                                                                                        |
| 7500        | Delivered                                                                                                                                                                                         |
| 7501        | Submitted                                                                                                                                                                                         |
| 7502        | Read                                                                                                                                                                                              |
| 7526        | Either subscription messaging permission not enabled or invalid tag received from the request                                                                                                     |
| 2018336     | The action is not submitted due to new privacy rules in Europe. See [developer documentation](https://developers.facebook.com/docs/messenger-platform/europe-updates#%3E) for more information.98 |
| 2018047     | The action is not submitted due to new privacy rules in Europe. See [developer documentation](https://developers.facebook.com/docs/messenger-platform/europe-updates#%3E) for more information.   |

## Push

[block:parameters]
{
  "data": {
    "h-0": "Status Code",
    "h-1": "Description",
    "h-2": "Details",
    "0-0": "7500",
    "0-1": "Delivered",
    "0-2": "The push was successfully delivered to the device.",
    "1-0": "7501",
    "1-1": "Submitted",
    "1-2": "The push was successfully submitted to the push service (APNS/FCM/HMS) for delivery",
    "2-0": "7502",
    "2-1": "Read",
    "2-2": "Generated when the user interacts with the push on the device. Note that this status does not occur if the user dismisses the push.",
    "3-0": "7503",
    "3-1": "Message expired before delivery attempt",
    "3-2": "Returned when the message is expired before attempting a delivery. The expiry value is configured in the request body.",
    "4-0": "7504",
    "4-1": "Authentication error",
    "4-2": "Returned when an authentication error occurs.",
    "5-0": "7505",
    "5-1": "Too large payload ( >4kb)",
    "5-2": "Returned when the payload is more than 4kb for Android.",
    "6-0": "7506",
    "6-1": "Invalid time to live value",
    "6-2": "Returned when an invalid value is passed for time to live parameter for Android",
    "7-0": "7507",
    "7-1": "Too many requests for the App",
    "7-2": "This error occurs when an Firebase receives too many requests for the same app, overloading the server. Firebase doesn't specify limits, but suggests using exponential back-off to mitigate this issue.",
    "8-0": "7508",
    "8-1": "GCM server error",
    "8-2": "Returned when an error occurs in Google Cloud Messaging server",
    "9-0": "7509",
    "9-1": "Too many concurrent requests for same customer",
    "9-2": "This error indicates messaging to a device exceeds the allowed rate. To address this, use exponential back-off. Note that FCM's limit for Android is 240 messages per minute or 5,000 per hour per device.",
    "10-0": "7510",
    "10-1": "Too big payload",
    "10-2": "Returned when the payload is more than 4kb for iOS.",
    "11-0": "7511",
    "11-1": "Invalid time to live value",
    "11-2": "Returned when an invalid value is passed for time to live parameter for iOS.",
    "12-0": "7512",
    "12-1": "Invalid push id",
    "12-2": "Returned when the push id is invalid.",
    "13-0": "7513",
    "13-1": "Unregistered Device",
    "13-2": "Returned when a device is not registered.",
    "14-0": "7514",
    "14-1": "Wrong apns certificate gateway",
    "14-2": "Returned when a wrong APNS certificate is provided.",
    "15-0": "7515",
    "15-1": "Bad apns certificate",
    "15-2": "Returned when an APNS certificate is invalid.",
    "16-0": "7516",
    "16-1": "Too many request for the same device",
    "16-2": "This error indicates the APNs server received too many requests for the same device token. Implement exponential back-off to mitigate this issue.",
    "17-0": "7517",
    "17-1": "APNS server error",
    "17-2": "Returned when an APNS server error occurs.",
    "18-0": "7518",
    "18-1": "Unknown",
    "18-2": "Returned when an unknown error occurs.",
    "19-0": "7537",
    "19-1": "Some tokens are successfully sent. Tokens identified by illegal_token are those failed to be sent",
    "19-2": "",
    "20-0": "7538",
    "20-1": "Some token parameters are incorrect",
    "20-2": "",
    "21-0": "7539",
    "21-1": "The number of tokens must be 1 when a synchronization message is sent",
    "21-2": "",
    "22-0": "7540",
    "22-1": "Incorrect message structure",
    "22-2": "",
    "23-0": "7541",
    "23-1": "The message expiration time is earlier than the current time",
    "23-2": "",
    "24-0": "7542",
    "24-1": "The collapse_key message field is invalid",
    "24-2": "",
    "25-0": "7543",
    "25-1": "The message contains sensitive information",
    "25-2": "",
    "26-0": "7544",
    "26-1": "OAuth authentication error",
    "26-2": "",
    "27-0": "7545",
    "27-1": "OAuth token expired",
    "27-2": "",
    "28-0": "7546",
    "28-1": "The current app does not have the permission to send push messages",
    "28-2": "",
    "29-0": "7547",
    "29-1": "All tokens are invalid",
    "29-2": "",
    "30-0": "7548",
    "30-1": "The message body size exceeds the default value",
    "30-2": "",
    "31-0": "7549",
    "31-1": "The number of tokens in the message body exceeds the default value",
    "31-2": "",
    "32-0": "7550",
    "32-1": "You are not authorized to send high-priority notification messages",
    "32-2": "",
    "33-0": "7551",
    "33-1": "System internal error",
    "33-2": "",
    "34-0": "7560",
    "34-1": "Request parameters were invalid.",
    "34-2": "Returns when any invalid value is given for any parameter in request body.",
    "35-0": "7562",
    "35-1": "The authenticated sender ID is different from the sender ID for the registration token.",
    "35-2": "Returned when push token of one app is used to send push notification for another app.",
    "36-0": "7563",
    "36-1": "Sending limit exceeded for the message target.",
    "36-2": "This error may result from exceeding either the overall message rate limit for an App asset or the device-specific limit. FCM has not documented these limits, however it recomends to employ an exponential back-off to resolve this error.",
    "37-0": "7564",
    "37-1": "The server is overloaded.",
    "37-2": "Returned when FCM server is overloaded. FCM has not documented any rate limits, however it recomends to employ an exponential back-off to resolve this error.",
    "38-0": "7565",
    "38-1": "An unknown internal error occurred.",
    "38-2": "Returned when the FCM server encounters an error while trying to process the request.",
    "39-0": "7566",
    "39-1": "APNs certificate or web push auth key was invalid or missing.",
    "39-2": "Returned by FCM when APNS certificate or web push auth key is either missing or invalid in your FCM project. To resolve this issue, please update your APNs certificate in your FCM project.",
    "40-0": "7569",
    "40-1": "Request not authenticated due to missing, invalid, or expired OAuth token.",
    "40-2": "The authentication token passed by 'Webex Connect' while submitting a push notification request to FCM was either invalid or expired.",
    "41-0": "7570",
    "41-1": "Client does not have sufficient permission. This can happen because the OAuth token does not have the right scopes, the client does not have permission, or the API has not been enabled.",
    "41-2": "Please be aware that any modification or deletion of scopes in the Google Cloud Service account can lead to this error. By default, Webex Connect adds the required scopes when generating an OAuth token.  \n  \nAdditionally, users must verify that the HTTP v1 API is enabled within their Firebase project settings.",
    "42-0": "7571",
    "42-1": "Unregistered error returned from the FCM.",
    "42-2": "Returned by FCM when the token used is no longer valid and a new one must be used.",
    "43-0": "7577",
    "43-1": "Unknown server error. Typically a server bug.",
    "43-2": "Returned when an unknown server error occurs in the FCM server.",
    "44-0": "7578",
    "44-1": "API method not implemented by the server.",
    "44-2": "This occurs when a particular method is not working on the Google servers.",
    "45-0": "7880",
    "45-1": "Check the format of the registration token you pass to the server. Make sure it matches the registration token the client app receives from registering with FCM. Do not truncate the token or add additional characters.",
    "45-2": "",
    "46-0": "7881",
    "46-1": "Check that the request contains a registration token (in the registration_id in a plain text message, or in the to or registration_ids field in JSON).",
    "46-2": "",
    "47-0": "7882",
    "47-1": "Make sure the message was addressed to a registration token whose package name matches the value passed in the request.",
    "47-2": "",
    "48-0": "7883",
    "48-1": "A registration token is tied to a certain group of senders. When a client app registers for FCM, it must specify which senders are allowed to send messages. You should use one of those sender IDs when sending messages to the client app. If you switch to a different sender, the existing registration tokens won't work.",
    "48-2": "",
    "49-0": "7884",
    "49-1": "Check that the payload data does not contain a key (such as from, or gcm, or any value prefixed by google) that is used internally by FCM. Note that some words (such as collapse_key) are also used by FCM but are allowed in the payload, in which case the payload value will be overridden by the FCM value.",
    "49-2": "",
    "50-0": "7885",
    "50-1": "The rate of messages to subscribers to a particular topic is too high. Reduce the number of messages sent for this topic, and do not immediately retry sending.",
    "50-2": "",
    "51-0": "7886",
    "51-1": "The apns-topic was invalid.",
    "51-2": "",
    "52-0": "7887",
    "52-1": "Pushing to this topic is not allowed.",
    "52-2": "",
    "53-0": "7889",
    "53-1": "The apns-id value is bad.",
    "53-2": "",
    "54-0": "7890",
    "54-1": "The device token is not specified in the request :path. Verify that the :path header contains the device token.",
    "54-2": "",
    "55-0": "7891",
    "55-1": "The device token does not match the specified topic.",
    "55-2": "",
    "56-0": "7892",
    "56-1": "The apns-topic header of the request was not specified and was required. The apns-topic header is mandatory when the client is connected using a certificate that supports multiple topics.",
    "56-2": ""
  },
  "cols": 3,
  "rows": 57,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## RCS

| Status Code | Description                                                                     |
| :---------- | :------------------------------------------------------------------------------ |
| 7000        | Invalid input details - JSON                                                    |
| 7006        | Internal server error                                                           |
| 7010        | Service provider exception                                                      |
| 7011        | Unknown Exception                                                               |
| 7301        | Message expired                                                                 |
| 7307        | Endpoint not reachable                                                          |
| 7500        | Delivered                                                                       |
| 7501        | Submitted                                                                       |
| 7502        | Read                                                                            |
| 7740        | Invalid media details                                                           |
| 7318        | General Bad Request error for everything not caught in the specific error below |
| 7319        | Not Found                                                                       |
| 7320        | Invalid JSON                                                                    |
| 7321        | Invalid JSON Content (bad field, invalid phone number)                          |
| 7322        | Provider not configured for chatbot                                             |
| 7323        | Unable to locate carrier for the recipient                                      |
| 7324        | Max TPS reached                                                                 |
| 7325        | Unauthorized access                                                             |
| 7326        | Internal System Error                                                           |
| 7327        | External System error                                                           |
| 7328        | Pass the error detail we have as error                                          |
| 7329        | Carrier lookup process failure                                                  |
| 7330        | Includes: details from MaaP                                                     |
| 7331        | Rate limited at MaaP and retries expired                                        |
| 7334        | MaaP returned a Failure IMDN                                                    |

## SMS

For SMS Status codes, also refer to [SMS - API](https://developers.webexconnect.io/reference/sms-1) article.

[block:parameters]
{
  "data": {
    "h-0": "Status Code",
    "h-1": "Description",
    "h-2": "Details",
    "h-3": "Delivery Status",
    "0-0": "7500",
    "0-1": "Delivered",
    "0-2": "Returned when the message is transmitted to the destination network and confirmation of delivery is provided from the mobile handset.  \n  \nIf the recipient did not receive the message, it may be due to spam, sender ID filters, or a corrupt or malformed message payload the handset was unable to process.",
    "0-3": "Delivered",
    "1-0": "7501",
    "1-1": "Submitted",
    "1-2": "Returned when the message has is in an interim status indicating submission to network provider, prior to it being actually delivered to the handset",
    "1-3": "Submitted",
    "2-0": "7004",
    "2-1": "Invalid parameters/Values",
    "2-2": "Returned when an invalid value or parameters are provided",
    "2-3": "Failed",
    "3-0": "7006",
    "3-1": "Internal server error",
    "3-2": "Returned when the message failed at the gateway and was not transmitted to the destination operator.  This is may be an intermittent temporary error",
    "3-3": "Failed",
    "4-0": "7101",
    "4-1": "Invalid Sender ID",
    "4-2": "Failed - The wrong sender Id is being used for this request  \nUn-Delivered - Returned when the sender is not authorized or configured at the destination operator",
    "4-3": "Failed/Un-Delivered",
    "5-0": "7102",
    "5-1": "Invalid address",
    "5-2": "Returned when the address is invalid",
    "5-3": "Failed",
    "6-0": "7107",
    "6-1": "Message Length Exceeded",
    "6-2": "Returned when the message length exceeded 4000 characters. ",
    "6-3": "Un-Delivered",
    "7-0": "7109",
    "7-1": "User in DnD",
    "7-2": "Returned when the user is registered on Do Not Disturb list",
    "7-3": "Un-Delivered",
    "8-0": "7201",
    "8-1": "Delivery failed at Operator",
    "8-2": "Returned when the message was routed to the operator but was rejected for various network-specific reasons (temp. failure or other network related issue)",
    "8-3": "Un-Delivered",
    "9-0": "7202",
    "9-1": "Delivery failed at platform",
    "9-2": "Returned when the delivery failed at platform",
    "9-3": "Un-Delivered",
    "10-0": "7203",
    "10-1": "Unknown Subscriber address",
    "10-2": "Failed - An invalid number used for this request  \nUn-Delivered - Returned when the number is an invalid mobile number on the destination network. This may indicate the subscriber is no longer valid, the number has ported away, or may have service blocks preventing message delivery",
    "10-3": "Failed/Un-Delivered",
    "11-0": "7204",
    "11-1": "Insufficient Credits in subscriber account",
    "11-2": "Returned when a message is sent to a prepaid mobile subscriber who no longer has a credit balance on their SIM card and can no longer receive messages",
    "11-3": "Un-Delivered",
    "12-0": "7205",
    "12-1": "Error in Binary message",
    "12-2": "Returned when there is an error in binary message.",
    "12-3": "Un-Delivered",
    "13-0": "7206",
    "13-1": "Can't deliver. Subscriber SIM Full",
    "13-2": "Returned when the subscribers SIM is full",
    "13-3": "Un-Delivered",
    "14-0": "7207",
    "14-1": "Subscriber out of coverage area or not reachable",
    "14-2": "Returned when the subscriber is out of coverage area",
    "14-3": "Un-Delivered",
    "15-0": "7208",
    "15-1": "Message expired",
    "15-2": "Returned when the message could not be delivered to the handset and exceeded its delivery time limit.  This occurs when a subscriber has their handset turned off, or handset has no more memory to accept messages",
    "15-3": "Un-Delivered",
    "16-0": "7209",
    "16-1": "Unable to deliver multipart message",
    "16-2": "Returned when the message was sent as a multi-part message (either a long text message more than 160 chars which is split into multiple parts, or a message with specific character encoding) to the network destination and one or more of the parts was returned undeliverable. The specific error for the non-delivery is not disclosed and all parts of the message will be flagged with this error code",
    "16-3": "Un-Delivered",
    "17-0": "7210",
    "17-1": "Billing Configuration error",
    "17-2": "Returned when there is an error in billing configuration.This may be caused by an unexpected network destination, or due to a provisioning error.",
    "17-3": "Un-Delivered",
    "18-0": "7211",
    "18-1": "Billing error at operator",
    "18-2": "Returned when message could not be delivered as network operator has indicated there was a billing related error",
    "18-3": "Un-Delivered"
  },
  "cols": 4,
  "rows": 19,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


In addition to the existing SMS error codes, client tenants hosted in the United States and Canada regions have these additional error codes for SMS:

[block:parameters]
{
  "data": {
    "h-0": "Status Code",
    "h-1": "Description",
    "h-2": "Details",
    "h-3": "Delivery Status",
    "0-0": "7111",
    "0-1": "Spam content detected",
    "0-2": "Returned when the network operator has rejected this message as spam. Subsequent messages to the recipient may or may not be delivered depending on the underlying cause:  \n-The sender ID has exceeded or violated carrier rules on message velocity (too many messages to the same recipient, too many messages from the same sender ID with sender ID restrictions).  \n-The message content was marked as spam due to detected keywords.  \n-The message was flagged for linking to websites suspected of spam or fraud.  \n-The message content contained URL-shortening services that the network operator may have banned",
    "0-3": "Un-Delivered",
    "1-0": "7280",
    "1-1": "Message deleted",
    "1-2": "Returned when a network operator deletes the message for technical reasons related to network performance.",
    "1-3": "Un-Delivered",
    "2-0": "7281",
    "2-1": "Campaign error",
    "2-2": "Returned when the Sender ID (phone number) is not registered with an approved 10 DLC brand and campaign ID with the campaign registry and is blocked from transmitting messages to the operator.  \n  \nThis could be caused by a missing configuration for the sender ID, the sender ID has changed or some other campaign-related error has occurred during submission.",
    "2-3": "Un-Delivered",
    "3-0": "7282",
    "3-1": "Invalid route",
    "3-2": "Returned when no valid route could be determined. The operator might not be supported or the number flagged as non-wireless (landline).",
    "3-3": "Un-Delivered",
    "4-0": "7283",
    "4-1": "Invalid operator or landline",
    "4-2": "Returned when the operator is not valid or the number is flagged as non-wireless (landline).",
    "4-3": "Un-Delivered",
    "5-0": "7284",
    "5-1": "Duplicate MT (caught by Duplication Guard)",
    "5-2": "Returned when message caught by duplicate guard",
    "5-3": "Un-Delivered",
    "6-0": "7302",
    "6-1": "Rate limit exceeded",
    "6-2": "Returned when the sender ID used to send traffic has exceeded its authorized TPS limit.  10 DLC registered numbers which are subject to rate limits will return such errors when exceeding the limits associated with their approved campaign IDs. The limits may be network operator, campaign or sender ID related. There could also be other throughput restrictions.  \n  \nPlease note that campaign and brand limits apply across service providers and are shared by the brand and/or campaign – ensure that when using multiple service providers, you are not exceeding the limits across those providers.",
    "6-3": "Un-Delivered",
    "7-0": "7513",
    "7-1": "Unregistered device",
    "7-2": "Returned when the device is unregistered  \n-The device inbox may be full at the device or network operator.  \n-The device has been marked as busy by the network operator.  \n-The device may have been flooded with messages and further submission to the device is not possible.",
    "7-3": "Un-Delivered",
    "8-0": "7518",
    "8-1": "Unknown",
    "8-2": "Returned when an unknown error occurs.  \nThe message may or may not have been delivered, but no additional information is available from the network operator.",
    "8-3": "Un-Delivered",
    "9-0": "7607",
    "9-1": "Invalid message type",
    "9-2": "Returned when the  Message type is not accepted by the operator (like Binary messages, or unicode)",
    "9-3": "Un-Delivered",
    "10-0": "7720",
    "10-1": "Recipient blocked to receive messae",
    "10-2": "Returned when the recipient subscriber or operator is blocked to receive messages.",
    "10-3": "Un-Delivered"
  },
  "cols": 4,
  "rows": 11,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


## Voice

| Code | Description                                                   |
| :--- | :------------------------------------------------------------ |
| 7000 | Invalid JSON                                                  |
| 7003 | Dynamic Format - “Mandatory parameter missing: {{parameter}}” |
| 7004 | Dynamic Format - “Invalid parameter: {{parameter}}”           |
| 7127 | Source IP not in the allowed list                             |
| 7016 | Unknown exception                                             |
| 7020 | You have reached maximum transaction limit                    |
| 7101 | Invalid sender ID                                             |
| 7102 | Invalid destination address                                   |
| 7104 | Invalid app ID                                                |
| 8009 | The profile doesn’t exist for this tenant                     |
| 7107 | Message length exceeded                                       |
| 7108 | Invalid template ID                                           |
| 7126 | Invalid content type                                          |
| 7009 | Maximum number of destinations reached                        |
| 7022 | JSON size exceeded                                            |
| 7005 | Request expired                                               |
| 7401 | No Answer.                                                    |
| 7402 | Customer busy.                                                |
| 7404 | Others.                                                       |
| 7406 | Rejected.                                                     |
| 7407 | Call Offered.                                                 |
| 7408 | Call Accepted.                                                |
| 7409 | Call Dropped.                                                 |
| 7410 | Disconnected.                                                 |
| 7411 | Trombone Connected.                                           |
| 7412 | Trombone Released.                                            |
| 7208 | Message Expired.                                              |
| 7519 | Call answered                                                 |

## Voice - Logbook Error Codes

| Error Code                    | Description                                                             | Details                                                                   |
| :---------------------------- | :---------------------------------------------------------------------- | :------------------------------------------------------------------------ |
| 1001                          | Address Incomplete(Request-URI incomplete)                              | Call was rejected by User as the phone was  busy                          |
| 1003                          | User doest not exist                                                    | Call was rejected by User as the phone was  busy                          |
| 1005                          | User switched off                                                       | Call was not answered by User as the phone was switched off               |
| 1007                          | OBD-Timeout                                                             | Call was not answered by User as the phone was switched off               |
| 2001                          | No Service Configured for shortcode                                     | Call was not answered by User as the shortcode service was not configured |
| 2002                          | No answer from end user                                                 | Call was not answered by the user                                         |
| 2003                          | Subscriber Busy / Line is Busy                                          | Call was not asnwered by User as the phone was  busy                      |
| 2005                          | End user Call dropped by Platform                                       | Call dropped by the platform                                              |
| 2006                          | End user Call Rejected by Platform                                      | Others, Call dropped due to internal error                                |
| 3000                          | End user call dropped with unknown Error                                | Users' call was dropped due to unknown reason                             |
| 3002                          | No response from Network / SIP Server Timeout                           | Timedout due to no reponse from the network                               |
| 3003                          |                                                                         |                                                                           |
| 1010                          | Number not in service/ Invalid Number                                   | Customers number is not valid or not in service                           |
| 1002                          | Call has been rejected by the receiver                                  | Call was rejected by User as the user was  busy                           |
| 2008                          | Call Dropped by Network/End user                                        | Call disconnected                                                         |
| 1011                          | Call media capabilities Not Acceptable                                  | Others, Call dropped due to internal error                                |
| 1009                          | Malformed Request                                                       | Others, Call dropped due to internal error                                |
| 1012                          | Number not supported / Invalid End User Number                          | Customers number is not valid or not in service                           |
| 1013                          | Server received a request that does not match any dialog or transaction | Others, Call dropped due to internal error                                |
| 1008                          | The server did not understand an event package specified                | Others, Call dropped due to internal error                                |
| Other 1000, 2000, 3000 series | Call dropped due to internal error                                      | Call dropped due to internal error                                        |

## WhatsApp

Error descriptions for each state are sent in additional info in the webhook

[block:parameters]
{
  "data": {
    "h-0": "Status Code",
    "h-1": "Description",
    "h-2": "Details",
    "0-0": "7500",
    "0-1": "Delivered",
    "0-2": "Returned when the message is delivered to the destination WhatsApp number.",
    "1-0": "7501",
    "1-1": "Submitted",
    "1-2": "Message submitted to WhatsApp for delivery.",
    "2-0": "7502",
    "2-1": "Read",
    "2-2": "Message read by the recipient.",
    "3-0": "7200",
    "3-1": "Unknown Status",
    "3-2": "Please refer to additional info object, part of the failed DR payload for more details. The error codes scenarios are captured in the following Meta documentations: [Cloud API error codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/)  \n  \nFor e.g.,  \n{  \n  \"deliveryInfoNotification\": {  \n    \"deliveryInfo\": {  \n      \"timeStamp\": \"2025-02-21T11:25:48.539Z\",  \n      \"Description\": \"Unknown Status\",  \n      \"code\": \"7200\",  \n      \"deliveryChannel\": \"whatsapp\",  \n      \"additionalInfo\": \"(#131049)  | In order to maintain a healthy ecosystem engagement, the message failed to be delivered.\",  \n      \"destination\": \"918096xxxxxx\",  \n      \"destinationType\": \"waid\",  \n      \"identityKeyHash\": \"\",  \n      \"deliveryStatus\": \"Failed\"  \n    },  \n    \"subtid\": \"\",  \n    \"transid\": \"b0b4a89e-7f5f-431a-a5f6-a22ab5f9bfd0\",  \n    \"callbackData\": \"\",  \n    \"correlationid\": \"\"  \n  }  \n}  \n  \nThis indicates that Marketing template message user limit has reached, refer [template](https://help.imiconnect.io/docs/templates-whatsapp#configuring-marketing-and-utility-templates)  page for more details on the above error. ",
    "4-0": "7010",
    "4-1": "Service provider exception",
    "4-2": "Please refer to additional info object, part of the failed DR payload for more details. The error codes scenarios are captured in the following Meta documentations: [Cloud API error codes](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/) ",
    "5-0": "7011",
    "5-1": "Unknown Exception",
    "5-2": "",
    "6-0": "7701",
    "6-1": "Media download error",
    "6-2": "Failed to download the media from the sender.",
    "7-0": "7703",
    "7-1": "Business eligibility - Payment issue",
    "7-2": "",
    "8-0": "7704",
    "8-1": "Message is not valid",
    "8-2": "Message failed to send because it was pending for too long.",
    "9-0": "7705",
    "9-1": "Message expired",
    "9-2": "Message failed to send during its Time To Live (TTL) duration.",
    "10-0": "7706",
    "10-1": "Rate limit hit",
    "10-2": "Message failed to send because there were too many messages sent from this phone number in a short period of time.  \nResend the failed messages.",
    "11-0": "7707\t",
    "11-1": "Unsigned certificate",
    "11-2": "Incorrect certificate. Message failed to send due to a phone number registration error.",
    "12-0": "7710",
    "12-1": "Re-engagement message",
    "12-2": "Message failed to send because more than 24 hours have passed since the customer last replied to this number. Use a message template to respond.",
    "13-0": "7711",
    "13-1": "Spam Rate limit hit",
    "13-2": "Message failed to send because there are restrictions on how many messages can be sent from this phone number. This may be because too many previous messages were blocked or flagged as spam. Check your quality status in the WhatsApp Manager.",
    "14-0": "7712",
    "14-1": "User's number is part of an experiment",
    "14-2": "Failed to send a message because this user's phone number is part of an [experiment](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments).  \n  \nSkip sending messages to this user.",
    "15-0": "7713\t",
    "15-1": "Generic error",
    "15-2": "Message failed to send due to an unknown error. Try again. If the error persists reach out to your support contact to raise a ticket with WhatsApp.",
    "16-0": "7714",
    "16-1": "Message too long",
    "16-2": "Length of the message exceeds 4096 characters.",
    "17-0": "7715",
    "17-1": "Invalid recipient type",
    "17-2": "The recipient type is not valid.",
    "18-0": "7717",
    "18-1": "Resource already exists",
    "18-2": "Possible UUID conflict for media upload request or media with that UUID already exists.",
    "19-0": "7721",
    "19-1": "Required parameter is missing",
    "19-2": "",
    "20-0": "7722",
    "20-1": "Parameter value is not valid. The namespace does not correspond to the WABA id.",
    "20-2": "Value entered for a parameter is of the wrong type or other problem.",
    "21-0": "7723",
    "21-1": "Parameter is not required",
    "21-2": "Contains a parameter that is not required.",
    "22-0": "7726",
    "22-1": "User is not valid",
    "22-2": "",
    "23-0": "7727",
    "23-1": "Internal error",
    "23-2": "Media upload failed due to bad image (image not uploaded correctly) or endpoint containing media was not found",
    "24-0": "7729",
    "24-1": "System overloaded",
    "24-2": "On-Premises system is under heavy load, wait for some time before trying again to allow the system to recover from the load.",
    "25-0": "7730",
    "25-1": "Not Primary Master",
    "25-2": "Retrying the request should resolve this error. If this does not resolve the error, reach out to your support contact.",
    "26-0": "7731",
    "26-1": "Not Primary Coreapp",
    "26-2": "Retrying the request should resolve this error. If this does not resolve the error, reach out to your support contact.",
    "27-0": "7733",
    "27-1": "Bad User",
    "27-2": "Sender and recipient phone number is the same. Send a message to a phone number different from the sender.",
    "28-0": "7736",
    "28-1": "Generic error",
    "28-2": "",
    "29-0": "7802",
    "29-1": "A user_identity_changedsystem notification requires acknowledgement",
    "29-2": "You sent a message to a WhatsApp user who has potentially changed, please re-authenticate the customer and reach out to your support contact to initiate acknowledgement with WhatsApp.",
    "30-0": "7803",
    "30-1": "Sender account has been locked",
    "30-2": "Your account has been locked to send any messages due to an integrity policy violation. See [WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp/overview/policy-enforcement) Policy Enforcement for information.",
    "31-0": "7804",
    "31-1": "Template Param Count Mismatch",
    "31-2": "The number of variable parameter values included in the request did not match the number of variable parameters defined in the template. See [Message Template Guidelines](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) and make sure the request includes all of the variable parameter values that have been defined in the template.",
    "32-0": "7805",
    "32-1": "Template Missing",
    "32-2": "Template status is not active, or template does not exist for a language and locale.",
    "33-0": "7808",
    "33-1": "Template Param Length Too Long",
    "33-2": "Parameter length too long",
    "34-0": "7809\t",
    "34-1": "Template Hydrated Text Too Long",
    "34-2": "Translated text too long",
    "35-0": "7811",
    "35-1": "Template Format Character Policy Violated",
    "35-2": "Template content violates a WhatsApp policy. See [Rejection Reasons](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#common-rejection-reasons) to determine possible reasons for violation.",
    "36-0": "7812\t",
    "36-1": "Template Required Component Missing",
    "36-2": "Required component in the Template is missing",
    "37-0": "7813\t",
    "37-1": "Template Invalid Hydrated URL",
    "37-2": "URL in button component of a Template is invalid",
    "38-0": "7814",
    "38-1": "Template Media Format Unsupported",
    "38-2": "Media format used in a Template is unsupported.",
    "39-0": "7815",
    "39-1": "Template Invalid Phone Number",
    "39-2": "Phone Number in Template button component is invalid",
    "40-0": "7816",
    "40-1": "Template Parameter Format Mismatch",
    "40-2": "Variable parameter values are formatted incorrectly. The variable parameter values included in the request are not using the format specified in the template. See [Message Template Guidelines](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/).",
    "41-0": "7819",
    "41-1": "Invalid number of sections",
    "41-2": "List Message request contains below minimum or above the maximum number of sections. You need to have at least 1 section object and you can have up to 10.",
    "42-0": "7820",
    "42-1": "Invalid number of rows",
    "42-2": "There is an invalid number of rows. For List Messages, there must be at least one rows object per section.",
    "43-0": "7820",
    "43-1": "Invalid number of rows",
    "43-2": "There is an invalid number of rows. For List Messages, there must be at least one rows object per section.",
    "44-0": "7821",
    "44-1": "Character Policy Violated",
    "44-2": "Format character policy has been violated.",
    "45-0": "7830",
    "45-1": "Invalid Header Structure",
    "45-2": "Returned when the header object structure is invalid.",
    "46-0": "7832",
    "46-1": "AuthException. We were unable to authenticate the app user.",
    "46-2": "Typically this means the Connect app access token has expired, been invalidated, or the user has changed a setting to prevent people from accessing their data. Reach out to you support contact for re-establishing the app.",
    "47-0": "7833",
    "47-1": "API Unknown. Invalid request or possible server error.",
    "47-2": "Reach out to your support contact and request to check the WhatsApp Business Platform Status page and check API status information before trying again.",
    "48-0": "7834",
    "48-1": "API Service. Temporary due to downtime or due to being overloaded.",
    "48-2": "Reach out to your support contact and request to check the WhatsApp Business Platform Status page and check API status information before trying again.",
    "49-0": "7835",
    "49-1": "API Method. Capability or permissions issue.",
    "49-2": "Reach out to your support contact to resolve the issue.",
    "50-0": "7836",
    "50-1": "API Too Many Calls",
    "50-2": "Try again later or reduce the frequency or amount of messages being sent",
    "51-0": "7837",
    "51-1": "API Permission Denied. Permission is either not granted or has been removed.",
    "51-2": "Reach out to your support contact to resolve the issue.",
    "52-0": "7838",
    "52-1": "Parameter is invalid. The request included one or more unsupported or misspelled parameters.",
    "52-2": "The request included one or more unsupported or misspelled parameters.",
    "53-0": "7839",
    "53-1": "Access token has expired",
    "53-2": "Reach out to you support contact for re-establishing the WhatsApp app",
    "54-0": "7840",
    "54-1": "Permission is either not granted or has been removed.",
    "54-2": "Reach out to your support contact for resolve the issue.",
    "55-0": "7842",
    "55-1": "Temporarily blocked for policies violations",
    "55-2": "The WhatsApp Business Account associated with the app has been restricted or disabled for violating a platform policy. See the [Policy Enforcement](https://developers.facebook.com/docs/whatsapp/overview/policy-enforcement/) document to learn about policy violations and how to resolve them.",
    "56-0": "7845",
    "56-1": "Rate limit hit. Cloud API message throughput has been reached.",
    "56-2": "The app has reached the API's [throughput limit](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput). See Throughput. Try again later or reduce the frequency with which the app sends messages.",
    "57-0": "7846\t",
    "57-1": "Service Overloaded",
    "57-2": "Reach out to your support contact and request to check the WhatsApp Business Platform Status page and check API status information before trying again.",
    "58-0": "7849",
    "58-1": "Template does not exist",
    "58-2": "The template does not exist in the specified language or the template has not been approved. Make sure your template has been approved and the template name and language locale are correct.",
    "59-0": "7854",
    "59-1": "Server Temporarily Unavailable",
    "59-2": "Reach out to your support contact and request to check the WhatsApp Business Platform Status page and check API status information before trying again.",
    "60-0": "7860",
    "60-1": "Account has been locked",
    "60-2": "The WhatsApp Business Account associated with the app has been restricted or disabled for violating a WhatsApp platform policy. See the [Policy Enforcement](https://developers.facebook.com/docs/whatsapp/overview/policy-enforcement/) document to learn about policy violations and how to resolve them.",
    "61-0": "7861",
    "61-1": "Unsupported mime type",
    "61-2": "WhatsApp was unable to upload the media used in the message. Please check if its MIME type is correct and is supported.",
    "62-0": "7862",
    "62-1": "Hash mismatch",
    "62-2": "Returned when there is a mismatch in the customer’s hash key due to potential identity change.",
    "63-0": "7863",
    "63-1": "Generic user error",
    "63-2": "Message delivery failed because of an unknown error with your request parameters. Contact the Support team if you continue receiving this error code in the response.",
    "64-0": "7865",
    "64-1": "Phone number Not Registered",
    "64-2": "Phone number is not registered on the WhatsApp Business Platform.",
    "65-0": "7868",
    "65-1": "Template is Disabled",
    "65-2": "Template has been paused too many times due to [low quality](https://imimobile.atlassian.net/wiki/spaces/IT/pages/14810513412/WhatsApp+6.6.2+Error+Code+Related+Updates#:~:text=times%20due%20to-,low%20quality,-and%20is%20now) , and is now permanently disabled.",
    "66-0": "7869",
    "66-1": "Template is Paused",
    "66-2": "Template is paused due to [low quality](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines#quality-rating)  so it cannot be sent in a template message.",
    "67-0": "7870",
    "67-1": "Business Account in maintenance mode",
    "67-2": "The WhatsApp Business Account is in maintenance mode. One reason for this could be that the account is undergoing a [throughput](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput)  upgrade.",
    "68-0": "7871",
    "68-1": "Message Undeliverable",
    "68-2": "Unable to deliver message. Reasons can include:  \n  \n- The recipient phone number is not a WhatsApp phone number.\n\n- Sending an [authentication template](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates)   to a WhatsApp user who has a +91 country calling code (India). Authentication templates currently cannot be sent to WhatsApp users in India.\n\n- Recipient has not accepted our new Terms of Service and Privacy Policy.\n\n- Recipient is using an old WhatsApp version; must use the following WhatsApp version or greater:\n\n- Android: 2.21.15.15\n\n- SMBA: 2.21.15.15\n\n- iOS: 2.21.170.4\n\n- SMBI: 2.21.170.4\n\n- KaiOS: 2.2130.10\n\n- Web: 2.2132.6\n\n- The message was not delivered to create a high quality user experience. See [Per-User Marketing Template Message Limits](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits) .",
    "69-0": "7872",
    "69-1": "User's number is part of an experiment",
    "69-2": "Message was not sent as it is part of WhatsApp [experiment](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/experiments) .",
    "70-0": "7874",
    "70-1": "(Business Account, Consumer Account) pair rate limit hit",
    "70-2": "Too many messages sent from the sender phone number to the same recipient phone number in a short period of time"
  },
  "cols": 3,
  "rows": 71,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Contact Policy-integrated Error Codes

The error codes listed below are common across all Contact Policy-integrated channels. They are applicable only when Contact Policy block has been used when sending outbound messages or calls.

| Status Code | Message                                                        | Description                                                                                                                                                                                                                          |
| :---------- | :------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 9000        | Contact policy not enabled                                     | Contact policy is not enabled.                                                                                                                                                                                                       |
| 9001        | Contact policy inputs required                                 | When the client is enabled with Contact Policy and the request doesn’t have all the required parameters to serve. For example, when a request sent does not have the Contact Policy Group parameter, this error message is returned. |
| 9002        | Recipient has not consented to message                         | The recipient has not provided consent to the received message.                                                                                                                                                                      |
| 9003        | Requested consumer was not found in group                      | The requested consumer was not found in the group.                                                                                                                                                                                   |
| 9004        | Unable to reach Contact Policy Service, please try again later | Contact Policy Service is not reachable.                                                                                                                                                                                             |
| 9005        | Invalid or unknown group ID or channel                         | The Group ID or Channel referred to, is invalid or unknown.                                                                                                                                                                          |
| 9006        | Frequency cap: Recipient has exceeded frequency cap            | You have exceeded the configured contact frequency cap/limit.                                                                                                                                                                        |
| 9007        | Frequency cap: The group was not found                         | The referred group was not found.                                                                                                                                                                                                    |
| 9010        | Consent check failed, customer consent expired                 | The consent check has failed as the customer consent has expired.                                                                                                                                                                    |