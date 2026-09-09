## Supported Channels

[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Prerequisite",
    "0-0": "[SMS](https://developers.webexconnect.io/reference/send-message-api-v1)",
    "0-1": "**Sender ID** - A Sender ID is a name or number that an SMS appears to come from (‘from address’) when you receive a message on your phone.  \n  \nA sender ID can be alpha-numeric or a short-code or a long-code depending on demographical restrictions",
    "1-0": "[Voice](https://developers.imiconnect.io/reference/send-message#voice-message)",
    "1-1": "**CLI** - You will need to buy a voice-enabled long-code under the Numbers section. This will be your caller-ID for the outbound call",
    "2-0": "[Live Chat /In-app Messaging](https://developers.imiconnect.io/reference/in-app-live-chat)",
    "2-1": "**Mobile/Web App** - You will need to integrate our [SDK](https://developers.imiconnect.io/docs) into your Android/iOS apps or on your website",
    "3-0": "[Push Notifications](https://developers.imiconnect.io/reference/push)",
    "3-1": "**Mobile/Web App** - You will need to integrate our [SDK](https://developers.imiconnect.io/docs) into your Android/iOS apps or on your website",
    "4-0": "[Facebook Messenger](https://developers.webexconnect.io/reference/facebook)",
    "4-1": "**Facebook App** - You will need to be an admin of [Facebook page](https://www.facebook.com/pages/creation/) and give Connect permission to access page messages through the Facebook app registration UI on <<prodname>> under the apps section.",
    "5-0": "[Apple Messages for Business](https://developers.imiconnect.io/reference/apple-messages-for-business)",
    "5-1": "**Apple Messages for Business App** - You will need to register your company on [Apple Business Register](https://register.apple.com/) and select <<prodname>> as your CS",
    "6-0": "[WhatsApp](https://developers.imiconnect.io/reference/whatsapp-api-docs)",
    "6-1": "**WhatsApp App** - You will need to [register](https://bit.ly/2F3VGdv)  to get approval from WhatsApp and talk to your account manager for subsequent steps.  \n  \nNote: We have created individual channel pages. We encourage you to refer to this [WhatsApp](https://developers.imiconnect.io/reference/whatsapp) page."
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Error Codes

Refer to this [Channel Specific Status Codes](https://developers.imiconnect.io/reference/channel-specific-status-codes-1) for more information.

## Batching Requests

The messaging API supports batching. You can send personalized messages to a maximum of 1000 destinations at once (subject to the messaging API TPS limit for your account).

> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to <<prodname>>, the endpoint for your API varies. See the [endpoint](doc:endpoints) section to understand which endpoint to use for your domain.

## Messaging API v1 - Samples

```json API Definition
{
    "appid":"", // This is required only for Push, In-App, Messenger, WhatsApp, and Apple Messages for Business
    "correlationid":"SMSMTusingmsisdn", //optional; Unique transaction ID from the client end
    "callbackData":"smstesting", //optional; Identifier sent alongside notifications to the notifyurl
  "notifyurl":"",//If an invalid URL is passed in API request, then such request will not be considered eligible for retries.
  "notifyurlAuthId": "TNPBXKT09U" //Optional.
    "deliverychannel":"sms", //Channels such as sms/voice/push/rt/fb/AppleBusinessChat/whatsapp
   
    "channels":{
		"sms":{ 
				"text":"SMS message content with {{link_linkid}}",
                "senderid":"SENDER", //Phone number, short code, or alphanumeric sender ID for sending the SMS 
                "type":"1",
                "extras":{
					"dlt_templateid":"1107158158796985790" //Required for SMS Comms in India as mandated by TRAI TCCCPR regulations.
						}
					},
            
		//Optional array if you want to use SmartLinks
      "smartlinks":[
        {
            "linkid": 5,
            "validity": 30
        }
      ],
    //Optional object if you want to use Contact Policy 
    "contactPolicy": {
             “contactPolicyGroup” : "xKa4xfM3S_a9bP98ryCw8w", //the GroupID to be applied. Required if any of the following options are included and set to true

             “channelCheckConsent” : true, //optional, assumed false, set to true to require opt-in before sending the message,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 

            “channelApplyFrequencyCap” : true //optional, assumed false, set to true to enforce group frequency cap for that channel,“channelCheckConsent” or “channelApplyFrequencyCap” either of the parameter should be “true” 
    },    
		"voice":{object(voiceMessage)
				},
				
		"appmessaging":{object(appMessage)
				},
				
		"push":{object(pushMessage)
				},
				
		"OTT-Messaging":{
		
			"fb":{object(fbMessage)
					},
					
			"wa":{object(whatsappMessage)
					},
				},
				
			"AppleBusinessChat":{object(appleBusinessChatMessage)
				},
		},
		
	"destination":[
			{
			
			"customerid/msisdn/email/android_pushid/ios_pushid/chrome_pushid/safari_pushid/psid/waid/abcUserId":[ "<value1>","<value2>"],
			"correlationid":"<A unique transaction ID up to 50 bytes used by Client to match requests with responses. Will override correlationid given in request body.>"
			}
   		],
		"gtrId":["rcsgtrid"]
    //"gtrids must match the number of destination objects "
  "icmessage": "true" //imiconnect gateway sends "icmessage=true" by default to indicate that the push or in-app message was sent by imiconnect. This happens only when co-existence of SDKs is enabled.>
  
   }
```

## Postman Collection

Here is a Postman collection to test our APIs. 

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download](https://www.getpostman.com/) Postman from official site.

## Body Parameters

The following are the parameters of the request body:

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "deliverychannel",
    "0-1": "string",
    "0-2": "yes",
    "0-3": "sms  \nvoice  \nappmessaging  \npush  \nfb  \nwhatsapp  \napplebusinesschat ",
    "1-0": "correlationid",
    "1-1": "string",
    "1-2": "no",
    "1-3": "A client-side identifier chosen by the Service Provider to correlate requests and their subsequent responses. The correlation-id can be up to 50 bytes long.",
    "2-0": "notifyurl",
    "2-1": "string",
    "2-2": "no",
    "2-3": "The <<prodname>> platform will send notifications to the URL specified in the notifyurl parameter. The URL is used to retrieve the status of the message sent. The notifyurl can also be configured while creating a service. If the URL is specified in both the service and the messaging API, preference will be given to the messaging API request.",
    "3-0": "callbackData",
    "3-1": "String",
    "3-2": "no",
    "3-3": "An identifier or data that will be sent alongside notifications to the _notifyurl_. This can serve as identifying notifications.",
    "4-0": "expiry",
    "4-1": "string",
    "4-2": "no",
    "4-3": "Expiry time in UTC format, after which messages will not be pushed. For example, 2015-04-12T13:00:19.456Z or 2015-04-12T18:30:19.456+5:30.",
    "5-0": "message",
    "5-1": "JSONObject",
    "5-2": "no",
    "5-3": "The message parameter block references a template via the template ID which is created within the <<prodname>> platform.  \n  \nThe amount of sub-parameters in the parameters block depends on the number of parameters expected in the template. These parameters are supplied to the template for substitution in the final message.  \n  \n`{  \n  \"message\": {  \n    \"template\": \"<Template ID>\",  \n    \"parameters\": {  \n      \"parameter1\": \"<value>\",  \n      \"parameter2\": \"<value>\",  \n      \"parameter3\": \"<value>\"  \n    }  \n  }  \n}`  \n  \n**Note:** If you use message templates, then the parameter name should match with the parameter specified in the template. The parameters in this message block are overridden if a channel specific parameter block is also used.  \nMessage length is limited to 1024 bytes per SMS.",
    "6-0": "destination",
    "6-1": "JSONArray",
    "6-2": "Yes",
    "6-3": "The destination parameter is an array of up to 1,000 entries. Messages can be sent to single or multiple recipients in a single request. Destination/Recipient MSISDN numbers i.e., phone numbers need to be provided in E.164 format. For more details, refer to destination array.",
    "7-0": "[channels](https://developers.imiconnect.io/reference/send-message#section-channels)",
    "7-1": "JSONObject",
    "7-2": "Yes",
    "7-3": "Contains one of the following -  \n[smsMessage](https://developers.imiconnect.io/reference/send-message#sms-message)  \n[voiceMessage](https://developers.imiconnect.io/reference/send-message#voice-message)  \n[appMessage](https://developers.imiconnect.io/reference/send-message#in-app-messaging)  \n[pushMessage](https://developers.imiconnect.io/reference/send-message#push-message)  \n[fbMessage](#https://developers.imiconnect.io/reference/send-message#facebook-messenger)  \n[whatsappMessage](https://developers.imiconnect.io/reference/send-message#whatsapp-message)  \n[applebusinesschat](https://developers.imiconnect.io/reference/send-message#apple-messages-for-business)"
  },
  "cols": 4,
  "rows": 8,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Smart Links Support
> 
> Please note that Smart Links is supported for text message type in SMS, In-App Messaging and Live Chat, Facebook Messenger, and WhatsApp.

## Channels

The **channels** parameter block configures channel communication parameters and will override the service's default values and the parameters in the base request.

### **Voice Message**

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Mandatory",
    "h-3": "Description",
    "0-0": "callflowid",
    "0-1": "String",
    "0-2": "Yes\\*",
    "0-3": "The callflowid created for voice flow using flow builder.  \n  \nIf specified, the IVR flow setup is used for sending the voice message.  \n  \n**Note**: \\*If 'callflowid' is specified, 'media' field must not be used.",
    "1-0": "promptid",
    "1-1": "String",
    "1-2": "Yes\\*",
    "1-3": "Prompt ID of the audio file uploaded in Tools > Voice media.  \n  \nEach file uploaded into the voice media folders on the UI  is assigned a unique prompt id.  \n  \nIf specified, the audio file located in the specified path is used to send the voice message.  \n  \n**Note**: \\*If 'media' is specified, 'callflowid' field must not be used.",
    "2-0": "cli",
    "2-1": "String",
    "2-2": "No",
    "2-3": "Caller Line ID to initiate the call.  \n  \n**Note:** Contact the Support Team using the details mentioned in the ‘Contact Support’ section within your <<prodname>> account, for more info on setting up your own custom CLI."
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


```json voiceMessage-Definition
{
	"callflowid":"voice flow ID",
	"media":"name of media uploaded",
	"cli":"predefined CLI bought under Numebrs section"
}
```
```json voiceMessage-PromptId
{
	"promptid":"354"	//Prompt ID of the uploaded audio file
}
```
```json voiceMessage-Flow
{
	"callflowid":"184",	//the voice flowid assgined by the flow builder
  "cli":"0453745878"
}
```