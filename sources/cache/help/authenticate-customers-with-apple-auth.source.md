Enterprises can send an _authentication_ type message on <<AMB>> to prompt the user to login with their credentials right within the message window. This level of authentication opens up a whole new set of sensitive customer support use-cases seamlessly possible.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b2dd215-apple_business_register.png",
        "apple_business_register.png",
        "Screenshot of configuring OAuth2 Authentication."
      ],
      "align": "center",
      "sizing": "smart",
      "caption": "Screenshot of configuring OAuth2 Authentication."
    }
  ]
}
[/block]


## Prerequisites

- [<<AMB>> account](https://developers.imiconnect.io/reference/apple-business-chat-faqs#registration-for-apple-messages-for-business)

- **OAuth authorization endpoint, OAuth token endpoint, OAuth client ID -** These details need to be entered on your <<AMB>> account within Apple Business Register. These details will be provided by you OAuth provider. Below is an example that we setup using LinkedIn’s OAuth service.

- **OAuth client secret -** This needs to be entered on the ‘manage app’ section of <<AMB>> app on <<prodname>> UI.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/873a5dc-1.jpeg",
        "manage_app_ABP.png",
        "Screenshot of Managing Apple Messages for Business App."
      ],
      "align": "center",
      "sizing": "smart",
      "border": true,
      "caption": "Screenshot of Managing Apple Messages for Business App."
    }
  ]
}
[/block]


## Using Authentication in a flow

Once your authentication configuration is setup on both Apple Business Register and <<prodname>>, you can start using it in a flow.

Each type of interactive message on <<AMB>> usually have two styles that need to be defined -

1. Received Message - This configuration defines how the initial authentication message is displayed to the customer including title, subtitle, image and size of the bubble
2. Reply Message - This configuration defines the message presented to the user after the interaction is complete
3. Within the flow node, you can configure how the message is displayed to the user and also other OAuth properties such as ‘Scopes’ and ‘Response Types’

Below is an example of a user journey using LinkedIn OAuth APIs as an example -

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2dff2d3-2.png",
        "linkedin_OAuth.png",
        "Screenshot of a user journey using LinkedIn OAuth APIs."
      ],
      "align": "center",
      "sizing": "smart",
      "caption": "Screenshot of a user journey using LinkedIn OAuth APIs."
    }
  ]
}
[/block]


Once an authentication request is sent, you can use the receive node to wait for user response and take the subsequent action.

### Sample API Request

Apple Auth is also supported through Connect's messaging API. Below is a sample request.

Here is the sample request, to use it in API.

```json Sample Code
{
   "appid":"a_636914165400010000",
   "correlationid":"ABCText123",
   "callbackData":"ABCRegAutomationstg",
   "notifyurl":"https://requestinspector.com/p/01dephvmctpzw12mrrgvrykg83",
   "deliverychannel":"AppleBusinessChat",
   "channels":{
      "AppleBusinessChat":{
         "type":"interactive",
         "interactiveData":{
            "data":{
               "version":"1.0",
               "requestIdentifier":"21d4a1c4-327c-ba35-45b1-36a050b15ad212-711",
               "images":[
                  {
                     "identifier":"6de6a59c-846f-45d8-a1d7-24382d9919d1",
                     "url":"http://drohnemieten.dein-betrieb.com/wp-content/uploads/2017/05/maxresdefault.jpg"
                  },
                  {
                     "identifier":"b70de3eb-a412-4fdd-a4b1-cb4eef853ded",
                     "url":"http://www.tompetty.com/sites/g/files/g2000007521/f/sample1_1.jpg"
                  }
               ],
               "authenticate":{
                  "oauth2":{
                     "responseType":"code",
                     "scope":[
                        "r_liteprofile"
                     ]
                  }
               }
            },
            "receivedMessage":{
               "subtitle":"hhh1!",
               "title":"Sign In to LinkedIn",
               "imageIdentifier":"6de6a59c-846f-45d8-a1d7-24382d9919d1"
            },
            "replyMessage":{
               "subtitle":"this is sub!",
               "title":"You Signed In",
               "imageIdentifier":"b70de3eb-a412-4fdd-a4b1-cb4eef853ded"
            }
         }
      }
   },
   "destination":[
      {
         "abcUserId":[
            "urn:mbid:AQAAY3cnOb7D+iCja4lzroWImGAC2QzKl1EnKaWl+XD/Mf52YjdOgSnTnb0HLontidf8PKkzEB0sNjco/S3Nmwc8Bp3iPZcxh/TeOMcqUFF2Kl1O5JxcJpVLwOemJRYwp+RhHqR33hzCQ+Z+9FYL4/tdCxtyEbxxxxxxxx"
         ]
      }
   ]
}
```

Once the message is received Apple Auth will send the client info as token to the OAuth provider for authentication. The OAuth provider will then validate the token against the OAuth provider details and sends the notification in cases of Successful or Failed authentication.

Once the customer is authenticated, you will receive the following JSON back.   

### Webhook Payload

```json Success
{
   "abcUserId":"urn:mbid:AQAAY3cnOb7D+iCja4lzroWImGAC2QzKl1EnKaWl+XD/Mf52YjdOgSnTnb0HLontidf8PKkzEB0sNjco/S3Nmwc8Bp3iPZcxh/TeOMcqUFF2Kl1O5JxcJpVLwOemJRYwp+RhHqR33hzCQ+Z+9FYL4/tdCxtyEbw=",
   "channel":"AppleBusinessChat",
   "abcAccountId":"2d15f71d-b227-4a10-95ae-6c6a2eff1991",
   "appId":"a_636914165400010000",
   "event":"AuthenticationResponse",
   "ts":"2020-06-18T12:01:28.406+01:00",
   "tid":"bcf815fa-13e3-e0c6-22a3-acf3e4115371",
   "authenticateStatus":"authenticated",
   "authenticateToken":"AQWw-4bU6Hw_A1xkFVhlYzLpcVWBjM-bvgswFMHyfghvcfOOKs5QLNyI09yEMnAPl2dvVEIY1n_jxsYd6Pl4-4UA6SvPPOv23Jk86WWiB18boPZlPVqBAXHZ11JpMGmLrARd7XvgnsBCE9h9Q3RHma64Tq_nFcMMapEbVT59-EymVASCDLPhYEQKXf3q9GPINw9FpWtl2aTHA73rKUb3Wt8b7vNOOAeYMxQezpS8MlKbk6jQ3enUYoRBzGajiQjbEzeJuh0mnYu8vwIknd0SRU7dmHRzHwd7tK52GVGsPPUQ-TetIcNpcHhu3XNVqHhFIZqQ2f2Ctxh_Xjpq9j4uROCI1VNMLA",
   "requestIdentifier":"21d4a1c4-327c-ba35-45b1-36a050b15ad212-711",
   "capabilities":"AUTH%2C0.91",
   "timezone":"2020-06-18T12:01:28.406+01:00",
   "deviceAgent":"iPhone+OS"
}
```

```json Failed
{
   "abcUserId":"urn:mbid:AQAAY3cnOb7D+iCja4lzroWImGAC2QzKl1EnKaWl+XD/Mf52YjdOgSnTnb0HLontidf8PKkzEB0sNjco/S3Nmwc8Bp3iPZcxh/TeOMcqUFF2Kl1O5JxcJpVLwOemJRYwp+RhHqR33hzCQ+Z+9FYL4/tdCxtyEbw=",
   "channel":"AppleBusinessChat",
   "abcAccountId":"2d15f71d-b227-4a10-95ae-6c6a2eff1991",
   "appId":"a_636914165400010000",
   "event":"AuthenticationResponse",
   "ts":"2020-06-18T12:02:32.649+01:00",
   "tid":"5958f185-c912-7363-cbb2-dbe3bb5e2e92",
   "authenticateStatus":"failed",
   "authenticateToken":{
      "status":"Failure",
      "code":1,
      "description":"Unsupported elliptic curve point type"
   },
   "requestIdentifier":"21d4a1c4-327c-ba35-45b1-36a050b15ad212-711",
   "capabilities":"AUTH%2C0.91",
   "timezone":"2020-06-18T12:02:32.649+01:00",
   "deviceAgent":"iPhone+OS"
}
```