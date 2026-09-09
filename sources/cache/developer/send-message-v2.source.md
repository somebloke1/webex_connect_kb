> 🚧 API Endpoint and Authentication
> 
> - Your API endpoint varies based on where your <<prodname>> account is hosted. Visit [Know Your API Endpoint](https://developers.imiconnect.io/reference/endpoints) section to know more. 
> 
> - You can use either Service Key or JSON Web Tokens (JWT) for authentication. If you use both JWT authentication and Service Key in an API request, JWT authentication takes priority, and the Service Key is ignored.

The messaging API supports batching. You can send personalized messages to a maximum of 1000 destinations at once (subject to your TPS limits). E.g., if your messaging API TPS configuration is 10 you can send messages to up to 10 destinations at once.

## Prerequisites

[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Prerequisite",
    "0-0": "[SMS](https://developers.webexconnect.io/reference/sms-apis)",
    "0-1": "Sender ID - A Sender ID is a name or number that an SMS appears to come from (‘from address’) when you receive a message on your phone.  \n  \nA sender ID can be alpha-numeric or a short-code or a long-code depending on demographical restrictions",
    "1-0": "[Email](https://developers.webexconnect.io/reference/email-api)",
    "1-1": "You will need to set up an Email app within <<prodname>>and verify your domain before you are able to send emails.  \n  \nPlease contact the Support team for any assistance in setting up Email app",
    "2-0": "[RCS](https://developers.webexconnect.io/reference/rcs-apis)",
    "2-1": "RCS chatbot needs to be created on all operators in geography before RCS messages can be sent.  \n  \nThis setup takes at least 7 days after submission on the UI under the apps section of <<prodname>>",
    "3-0": "",
    "3-1": "",
    "4-0": "[MMS](https://developers.webexconnect.io/reference/mms-api) ",
    "4-1": ""
  },
  "cols": 2,
  "rows": 5,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Messaging API v2 - Samples

```json API Definition
{
    "appid": "<channel asset specific App ID available in Assets page>", //This is required only for Push, In-App, Messenger, WhatsApp, and Apple Messages for Business
    "channel": "<channel name - v2 API currently supports sms, email and rcs",
    "from": "<from address for the message, for SMS this will be a senderID, for email the sender address and for all OTT channels it will be appId available on the UI>",
    "to": [
        {
            "msisdn/email": [
                "single/multiple destination objects of the same type" //MSISDN i.e., phone numbers in E.164 format
            ],
            "correlationId": "<correlationId for this array of destination objects>",
            "substitutions": {
                "parameter1": "<substitutions for this array of destination objects> ",
                "parametern": "<substitutions for this array of destination objects> "
            }
        },
        // Pass multiple objects in a single destination array for bulk messaging
        // Pass one object in each destination array for personalized messaging		
        {
            "msisdn/email": [
                "single/multiple destination objects of the same type"
            ],
            "correlationId": "<correlationId for this array of destination objects>",
            "substitutions": {
                "parameter1": "<substitutions for this array of destination objects> ",
                "parametern": "<substitutions for this array of destination objects> "
            }
        }
    ],
    // Global substitutions
    "substitutions": {
        "parameterx": "<global replaceable parameters, destination level parameters take precendence",
    },
    // Message scheduling
    "sendAt": "{{TimeinUTC}}",
    //max 7 days from current time
    "expireAt": "{{TimeinUTC}}", //Either(expireAt/validity)one can be passed.If both are provided then you will receive a 400 Bad request.
    "validity": "time period in seconds", //For e.g., 60 for 60 seconds
    // Channel specific message options
    "options": {
		object(smsOptions)||object(emailOptions)||Object(rcsOptions)
    },
    // Call-backs
    "callbackData": "<notify data>",
  "notifyUrl": "https://notify.example.com",
  "notifyUrlAuthId":"TNPXXXT09U", //Optional.
    "requestedReceipts": [
        "DELIVERED",
        "READ"
    ],
    // Union field message can be only one of content or template
    "content": {
    object(smsMessage)||object(emailMessage)||object(rcsMessage)
    },
    "template": {
        "id": "<unique template ID fom the UI"
    }
    //Optional object if you want to use Contact Policy 
    "contactPolicy": {
             “contactPolicyGroup” : "xKa4xfM3S_a9bP98ryCw8w", //the GroupID to be applied. Required if any of the following options are included and set to true

             “channelCheckConsent” : true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 

            “channelApplyFrequencyCap” : true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    }
}
```

## Postman Collection

Here is a Postman collection to test our APIs. Make sure you change the key in the header to your service key.

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection:Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download](https://www.getpostman.com/) Postman from official site.

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

## Body Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "channel",
    "0-1": "enum",
    "0-2": "yes",
    "0-3": "email  \n\\* rcs",
    "1-0": "from",
    "1-1": "string",
    "1-2": "yes",
    "1-3": "\\_ email - [fromaddress@domain.com](mailto:fromaddress@domain.com) (domain needs to be registered in apps)  \n \\* rcs - app ID generated on the UI",
    "2-0": "to",
    "2-1": "JSONArray",
    "2-2": "yes",
    "2-3": "array of destination JSON objects that contain the channel specific destination and personalized substitutions for each destination object. MSISDN i.e., phone numbers should be in E.164 format.  \n  \n**Channel wise destinations** -  \n\\_ email - email  \n\\* rcs - msisdn",
    "3-0": "substitutions",
    "3-1": "JSONObject",
    "3-2": "no",
    "3-3": "a JSON object with global substitutions. If a variable exists both in personalized substitutions and global substitutions, the personalized substitution takes preference",
    "4-0": "sendAt",
    "4-1": "date/time",
    "4-2": "yes",
    "4-3": "The timestamp of the message to be delivered (maximum 7 days)  \n  \nFor example,  \n  \\_ 2021-06-26T13:47:18.000Z - UTC",
    "5-0": "expireAt",
    "5-1": "date/time",
    "5-2": "yes",
    "5-3": "The time format for when the message has to be expired and failed if not delivered  \n  \nFor example,  \n  \\_ 2021-06-26T13:47:18.000Z - UTC",
    "6-0": "validity",
    "6-1": "string",
    "6-2": "yes",
    "6-3": "Time period in seconds. E.g., 60 for sixty seconds.  \n  \nOnly one of expireAt or validity should be sent in the request. The request will not be accepted if both values are present in the payload.  \n  \nIf both sendAt and validity parameters are present in the same request, the validity time period will be added to the sendAt time to decide the expiry time.",
    "7-0": "options",
    "7-1": "JSONObject",
    "7-2": "no",
    "7-3": "a JSON object that contains additional channel specific options in API. More information under each channel below",
    "8-0": "callbackData",
    "8-1": "string",
    "8-2": "no",
    "8-3": "A string that is returned with each outbound web-hook for the message (delivery, failed etc). Maximum number of characters allowed in callbackData including any spaces is 2000.",
    "9-0": "notifyUrl",
    "9-1": "string",
    "9-2": "no",
    "9-3": "a HTTPS endpoint for message delivery web-hooks",
    "10-0": "notifyUrlAuthId",
    "10-1": "string",
    "10-2": "no",
    "10-3": "Unique Authentication ID.",
    "11-0": "requestedReceipts",
    "11-1": "JSONArray",
    "11-2": "no",
    "11-3": "a JSON array that can filter message delivery web-hooks to the notifyURL.  \n  \nCan contain one or more of the following for each channel  \n\\_ email -  \"Parameter\",  \n    \"h-1\": \"Type\",  \n    \"h-2\": \"Mandatory\",  \n    \"h-3\": \"Descriptio  \n\\* rcs - \": \"Type\",  \n    \"h-2\": \"Mandatory\",  \n  \nCheck [Outbound Webhooks](https://developers.imiconnect.io/reference#outbound-webhooks) for more information on receipts",
    "12-0": "content",
    "12-1": "JSONObject",
    "12-2": "yes, if template is not provided",
    "12-3": "contains the content of the message for each channel. see below for more examples",
    "13-0": "template",
    "13-1": "JSONObject",
    "13-2": "yes, if content is not provided",
    "13-3": "contains the template id for each channel that's configured on the UI"
  },
  "cols": 4,
  "rows": 14,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]