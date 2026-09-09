[block:html]
{
  "html": "<div></div>\n\n<style>\n  .rm-ReferenceMain .rm-Article {\n    display: flex;\n    flex-direction: column;\n}\n \n.rm-ParamContainer {\n    order: 1;\n}\n \n.field-description, .markdown-body {\n    order: 2;\n}\n \n.rm-ReferenceMain .markdown-body {\n  margin-top: 10px\n}\n \n.rm-ReferenceMain .rm-Article .rm-APISectionHeader {\n    order: 3;\n}\n \n[class^=\"APIResponseSchemaPicker\"] {\n    order: 4;\n}\n \n[class^=\"Footer-desktop\"] {\n  order: 5\n}\n\n</style>"
}
[/block]


> 🚧 Template API usage
> 
> The template should be registered and approved from **Tools -> Templates** section within imiconnect platform, before it can be used to send notification messages.

## Other Template Types

```json Template with Image Header
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
            ]
        }
    ],
    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "image": {
                "link": ""
            },
            "{{variable1}}": "", //Simple text variable. Configured parameter key is the name of the variable specified during template creation
            "{{variable2}}": ""
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
  "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Template with Video Header
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
            ]
        }
    ],
    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "video": {
                "link": ""
            },
            "{{variable1}}": "", //Simple text variable. Configured parameter key is the name of the variable specified during template creation
            "{{variable2}}": ""
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
  "notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Template with Document
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
            ]
        }
    ],
    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "document": {
                "link": "", //Mandatory.
                "filename": "" //Optional.
            },
            "{{variable1}}": "", //Simple text variable. Configured parameter key is the name of the variable specified during template creation
            "{{variable2}}": ""
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Template with CTA Button
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
            ]
        }
    ],
    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "{{ctaVariable}}": {
                "type": "url", //Mandatory.
                "payload": "URL_EXTENSION" //Mandatory.
            }
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Template with Quick Replies
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
            ]
        }
    ],
    "message": {
        "template": "<Template-ID>", //Mandatory.
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "quickReply": [
                {
                    "button_text": "{{buttonText1}}", //Mandatory. Configure the value of the <buttontext> as the name of the button specified during template creation here.
                    "payload": "BUTTON 1 PAYLOAD" //Mandatory. Configure unique button payload. This will be returned back as part of Postback event in Webex Connect incoming components.
                },
                {
                    "button_text": "{{buttonText2}}",
                    "payload": "BUTTON 2 PAYLOAD"
                },
                {
                    "button_text": "{{buttonText3}}",
                    "payload": "BUTTON 3 PAYLOAD"
                }
            ]
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Template with Localizable Parameters
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
            ]
        }
    ],
    "message": {
        "template": "<Template-ID>", //Configure Template Id. Template Id can be fetched from the Tools - Template listing page.//
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "{{dateTimeVariable}}": {
                "type": "date_time", //Mandatory. 
                "fallback_value": "Feb 20th, 2023 8:45pm", //Mandatory. 
                "timestamp": "1782231500" //Optional. 
            }, //Localisable time variable. Configured parameter key is the name of the variable specified during template creation
            "{{currencyVariable}}": {
                "type": "currency", //Mandatory. 
                "currency_code": "USD", //Mandatory. 
                "amount_1000": "150000", //Mandatory. 
                "fallback_value": "EUR 300" //Mandatory. 
            },
            //Body configuration - Configure from simple text variables or localisable variables i.e. Time or Currency.
            "{{variable1}}": "", //Simple text variable. Configured parameter key is the name of the variable specified during template creation
            "{{variable2}}": ""
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "", //Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```
```json Authentication Template
{
    "deliverychannel": "whatsapp", //Mandatory. Channel used to send the message i.e., whatsapp in this case.
    "appid": "{{WAAppid}}", //Mandatory. Contains the applicationid
    "destination": [
        {
            "waid": [
                "{{waid}}" //Mandatory. WhatsApp ID or phone number for the person you want to send a message to.
            ]
        }
    ],
    "message": {
        "template": "<Template-ID>",
        "parameters": { //Configuration of all parameters is mandatory. Specify the dynamic value of parameters configured at the time of template creation. The variables created at the time of template creation are highlighted using the following format {{variable}}
            "otp": {
                "type": "otp", //Mandatory.
                "value": "12xxxx" //Mandatory.
            }
        }
    },
    "channels": {
        "OTT-Messaging": {
            "wa": {
                "identity_key_hash": "njbYlYcxxxxx" //Optional. Pass this value to validate the identity of your customer.
            }
        }
    },
    "correlationid": "", //Optional. The correlationid is a unique identifier that you can attach to every request as a reference a particular transaction or event. This is configured as a part of the request.
    "callbackData": "", //Optional. Data that you have configured to receive on the notify Url. This is configured as a part of the request.
  "notifyurl": "" ,//Optional. Configure a URL to get notifications on delivery reports for a WhatsApp message. This field accepts only a valid URL or a variable. If an invalid URL is passed in API request or via a variable, then such request will not be considered eligible for retries.
"notifyurlAuthId": "TNPBXKT09U" //Optional.
}
```

> 📘 Note
> 
> It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> 
> The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> 
> The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

## Error Codes

Refer to the [Apple Messages for Business](https://developers.imiconnect.io/reference/channel-specific-status-codes-1#apple-messages-for-business) section.