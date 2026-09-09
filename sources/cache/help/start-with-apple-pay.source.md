<<AMB>> enables you to provide customers with the option to buy products and services using Apple Pay without leaving the conversation. Consumers can respond to the payment request using their preferred Apple Pay payment methods.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/77ec436-apple_business_chat.png",
        "apple_business_chat.png",
        "Flow diagram for Apple pay through Messages for Business"
      ],
      "align": "center",
      "sizing": "smart",
      "border": true,
      "caption": "Use of Apple Pay through Messages for Business"
    }
  ]
}
[/block]


```json Sample Code
openssl pkcs12 -in <CERT_FROM_KEYCHAIN_EXPORT.p12> -out OUTPUT.pem / -nodes -clcerts
```

## Prerequisites

1. [<<AMB>> account](https://developers.imiconnect.io/reference/apple-business-chat-faqs)
2. You must have an Apple Developer account in order to create an Apple Pay Merchant account. If you do not have an Apple Developer account, please set one up at [Apple Developers](https://developer.apple.com/). The approval time may take several days. You will need to get your Merchant ID and Certificate from here.
3. Payment processing endpoint.

## Register your Merchant ID on Apple Business Register

Use the following steps to verify that your Merchant ID is registered with Apple Business Register: 

1. Go to [register.apple.com](http://register.apple.com/) and sign in with your Apple ID as the administrator or technical contact for the business that owns your Apple Pay credentials. 
2. Go to your company’s Business Chat Accounts and find the appropriate business account. If your company has multiple accounts, ensure that you enter the merchant information into the Business Chat account corresponding to your company’s Apple Pay capability. 
3. Edit the Apple Pay section of your Business Chat Account and update your merchant ID. 

## Generate the PEM File required by the payment session

Use the following steps to generate the PEM file required by the payment session: 

1. Download the Merchant Identity Certificate from your Apple Pay developer account to your local file system. 
2. In the Applications folder on Mac, open the Utilities folder and launch Keychain Access. 
3. Add the Merchant Identity Certificate to Keychain Access by opening the certificate file. 
4. In the Keychain Access, find the certificate, and then expand it. You should see a private key. 
5. Hold down the command key and select both the certificate and the private key. 

From Menu select File > Export Items…. 

1. Select “Personal Information Exchange (.p12)” as File Format and save the .p12 file. 
2. Convert the .p12 file to a .pem file using the following command: 

## Configure the App on Webex Connect Platform

Use the following steps to configure the App on <<prodname>> Platform: 

1. Go to the Apps page. 
2. Scroll down to the required app and click Manage App. 
3. Enable Payment and provide the following details that you have obtained here -Merchant ID, Merchant Name, Domain Name 
4. Choose the payment networks allowed by the business in Supported Networks. Selection of at least one network is mandatory. 
5. Upload the PEM File that you downloaded. This is the certificate for your business. 
6. The Payment Gateway URL directs the money to your account.  

Optionally, provide values for the following Endpoints. These are a set of URLs used the payment process. 

1. Shipping Contact Update URL - URL for the customer to update any changes in the shipping address 
2. Payment Method Update URL – URL to change the payment method 
3. Fallback URL – a URL to complete the purchase transaction in case of a failed payment  
4. Order Tracking URL – URL to update the order information after completing the order 
5. Shipping Method Update URL – URL to change or update the shipping method 

## Use Apple Pay option within a flow

Once the above steps are configured, you can start using flow nodes to send Apple Pay requests and wait for payment response to configure your customer journeys.

### Sample API Request

Apple Pay is also supported through Connect's messaging API. Below is a sample request.

```json Sample Code
curl --location --request POST 'http://api.imiconnect.io/resources/v1/messaging' \ 
--header 'Content-Type: application/json' \ 
--header 'key: e7705d87-4e48-11ea-87fa-00505f944c2b' \ 
--header 'Content-Type: text/plain' \ 
--data-raw '{ 
    "appid": "a_636893638318070000", 
    "correlationid": "ABCText123", 
    "callbackData": "ApplePaytest-QA", 
    "notifyurl": "https://requestinspector.com/inspect/01e194dd7rgrsrs4ra1zk9mr5x", 
    "deliverychannel": "AppleBusinessChat", 
    "channels": { 
        "AppleBusinessChat": { 
            "type": "interactive", 
            "interactiveData": { 
                "data": { 
                    "version": "1.0", 
                    "requestIdentifier": "21d4a1c4-327c-ba35-45b1-36a050b15ad2", 
                    "images": [ 
                        { 
                            "identifier": "6de6a59c-846f-45d8-a1d7-24382d9919db", 
                            "url": "http://drohnemieten.dein-betrieb.com/wp-content/uploads/2017/05/maxresdefault.jpg" 
                        } 
  
                    ], 
                    "payment": { 
                        "paymentRequest": { 
                            "lineItems": [ 
                                { 
                                    "amount": "45", 
                                    "type": "final", 
                                    "label": "The Alchemist" 
                                } 
                            ], 
   "lineItems": [ 
                                { 
                                    "amount": "100", 
                                    "type": "final", 
                                    "label": "The Clifton Chronicles" 
                                } 
                            ], 
 
                            "shippingMethods": [ 
                                { 
                                    "label": "Same day shipping (Optional)", 
                                    "amount": "20", 
                                    "detail": " Order placed before 10 AM is delivered on the same day before 10 PM (Optional)", 
                                    "identifier": "SDS" 
                                } 
                            ], 
                            "requiredShippingContactFields": [ 
                                "postalAddress", 
                                "name", 
                                "phone" 
                       “email” 
                            ], 
                            "countryCode": "US", 
                            "requiredBillingContactFields": [ 
                                "postalAddress", 
                                "name", 
                                "phone" 
                       “email” 
                            ], 
                            "currencyCode": "USD", 
                            "total": { 
                                "amount": "145", 
                                "type": "final", 
                                "label": " Your total order value today is" 
                            } 
                        } 
                    } 
                }, 
                "useLiveLayout": true, 
                "receivedMessage": { 
                    "title": "Order for Books 
                }, 
                "replyMessage": { 
                    "title": "Your order for books" 
                } 
            } 
        } 
    }, 
    "destination": [ 
        { 
            "abcUserId": [ 
                "urn:mbid:AQAAY2wXvkqhE0m1GvEzOA6kyZmr5KjyyPDkEYhD4hGjbH5LzOclqRKnpOJb62GRu395zKyda06SneUVy4TN1Palrvnm5HLqcGyAQdhNkGVqFpanbWl4mMigOSYqF4J26WpCW4iTBYSrZmei3+eFa+QoCkTt8Dw=" 
            ] 
        } 
    ] 
}
```

## Receiving Payment Updates

Given below is a sample webhook payload for Apple Pay request with a success response -  
Webhooks can be configured under Integrations > Outbound webhooks

```json Sample Code
{  
   "sourceId":"urn:mbid:AQAAYyBG2mFWYJKsTDLmTItbWN39j+kMBhc9jK3nacozBM57YJ6lpPGkOMatOHjPg68h5FS+4IcQd5knINWzFVc55rIlYxeZHS3zwzVOKsIt5GK9/2DwyaWshEH47L1NM2V+1ACesTobhHJq+hiJiK1mFaI6q94=", 
   "v":1, 
   "interactiveData":{  
      "data":{  
         "receivedMessage":{  
            "imageIdentifier":"1", 
            "subtitle":"We'll see you there!", 
            "style":"large", 
            "title":"IMIChat bill pay" 
         }, 
         "replyMessage":{  
            "imageIdentifier":"1", 
            "subtitle":"$3 \u2013 Payment Not Completed", 
            "style":"large", 
            "title":"IMIChat bill pay" 
         }, 
         "requestIdentifier":"a8c6a56e-4f33-4d78-a36c-737cbc94ce10", 
         "payment":{  
            "merchantSession":{  
               "merchantSessionIdentifier":"PSHAEE6A74CB76B439CA227EA05B52E8967_0002B0D80068F71D5887F2726CFD997A28E0ED57ABDACDA64934730A24A31583", 
               "merchantIdentifier":"E21457C93EF89B9F301E948B8095EAB5380F5D1A3F5A07D4066FBBEB99350BD9", 
               "epochTimestamp":1573466611985, 
               "initiative":"messaging", 
               "signature":"308006092a864886f70d010702a0803080020101310f300d06096086480165030402010500308006092a864886f70d0107010000a080308203e330820388a00302010202084c304149519d5436300a06082a8648ce3d040302307a312e302c06035504030c254170706c65204170706c69636174696f6e20496e746567726174696f6e204341202d20473331263024060355040b0c1d4170706c652043657274696669636174696f6e20417574686f7269747931133011060355040a0c0a4170706c6520496e632e310b3009060355040613025553301e170d3139303531383031333235375a170d3234303531363031333235375a305f3125302306035504030c1c6563632d736d702d62726f6b65722d7369676e5f5543342d50524f4431143012060355040b0c0b694f532053797374656d7331133011060355040a0c0a4170706c6520496e632e310b30090603550406130255533059301306072a8648ce3d020106082a8648ce3d03010703420004c21577edebd6c7b2218f68dd7090a1218dc7b0bd6f2c283d846095d94af4a5411b83420ed811f3407e83331f1c54c3f7eb3220d6bad5d4eff49289893e7c0f13a38202113082020d300c0603551d130101ff04023000301f0603551d2304183016801423f249c44f93e4ef27e6c4f6286c3fa2bbfd2e4b304506082b0601050507010104393037303506082b060105050730018629687474703a2f2f6f6373702e6170706c652e636f6d2f6f63737030342d6170706c65616963613330323082011d0603551d2004820114308201103082010c06092a864886f7636405013081fe3081c306082b060105050702023081b60c81b352656c69616e6365206f6e207468697320636572746966696361746520627920616e7920706172747920617373756d657320616363657074616e6365206f6620746865207468656e206170706c696361626c65207374616e64617264207465726d7320616e6420636f6e646974696f6e73206f66207573652c20636572746966696361746520706f6c69637920616e642063657274696669636174696f6e2070726163746963652073746174656d656e74732e303606082b06010505070201162a687474703a2f2f7777772e6170706c652e636f6d2f6365727469666963617465617574686f726974792f30340603551d1f042d302b3029a027a0258623687474703a2f2f63726c2e6170706c652e636f6d2f6170706c6561696361332e63726c301d0603551d0e041604149457db6fd57481868989762f7e578507e79b5824300e0603551d0f0101ff040403020780300f06092a864886f76364061d04020500300a06082a8648ce3d0403020349003046022100be09571fe71e1e735b55e5afacb4c72feb445f30185222c7251002b61ebd6f55022100d18b350a5dd6dd6eb1746035b11eb2ce87cfa3e6af6cbd8380890dc82cddaa63308202ee30820275a0030201020208496d2fbf3a98da97300a06082a8648ce3d0403023067311b301906035504030c124170706c6520526f6f74204341202d20473331263024060355040b0c1d4170706c652043657274696669636174696f6e20417574686f7269747931133011060355040a0c0a4170706c6520496e632e310b3009060355040613025553301e170d3134303530363233343633305a170d3239303530363233343633305a307a312e302c06035504030c254170706c65204170706c69636174696f6e20496e746567726174696f6e204341202d20473331263024060355040b0c1d4170706c652043657274696669636174696f6e20417574686f7269747931133011060355040a0c0a4170706c6520496e632e310b30090603550406130255533059301306072a8648ce3d020106082a8648ce3d03010703420004f017118419d76485d51a5e25810776e880a2efde7bae4de08dfc4b93e13356d5665b35ae22d097760d224e7bba08fd7617ce88cb76bb6670bec8e82984ff5445a381f73081f4304606082b06010505070101043a3038303606082b06010505073001862a687474703a2f2f6f6373702e6170706c652e636f6d2f6f63737030342d6170706c65726f6f7463616733301d0603551d0e0416041423f249c44f93e4ef27e6c4f6286c3fa2bbfd2e4b300f0603551d130101ff040530030101ff301f0603551d23041830168014bbb0dea15833889aa48a99debebdebafdacb24ab30370603551d1f0430302e302ca02aa0288626687474703a2f2f63726c2e6170706c652e636f6d2f6170706c65726f6f74636167332e63726c300e0603551d0f0101ff0404030201063010060a2a864886f7636406020e04020500300a06082a8648ce3d040302036700306402303acf7283511699b186fb35c356ca62bff417edd90f754da28ebef19c815e42b789f898f79b599f98d5410d8f9de9c2fe0230322dd54421b0a305776c5df3383b9067fd177c2c216d964fc6726982126f54f87a7d1b99cb9b0989216106990f09921d00003182018c30820188020101308186307a312e302c06035504030c254170706c65204170706c69636174696f6e20496e746567726174696f6e204341202d20473331263024060355040b0c1d4170706c652043657274696669636174696f6e20417574686f7269747931133011060355040a0c0a4170706c6520496e632e310b300906035504061302555302084c304149519d5436300d06096086480165030402010500a08195301806092a864886f70d010903310b06092a864886f70d010701301c06092a864886f70d010905310f170d3139313131313130303333315a302a06092a864886f70d010934311d301b300d06096086480165030402010500a10a06082a8648ce3d040302302f06092a864886f70d0109043122042028817adbd7737a77b831dae2cc526c36836089748c170ca41f6a837e065d9a46300a06082a8648ce3d04030204473045022008e907661fd17bf5b7ed875a645e1b8309024afa09e2790f3792c339fffadfd9022100a9641cd02298fab047415c68ae824e1c0cc032b6f083abef33ea7111e24680b0000000000000", 
               "initiativeContext":"https://qa-abctestpgw.imiconnect.com/paymentGateway", 
               "displayName":"ApplePayPOC", 
               "signedFields":[  
                  "merchantIdentifier", 
                  "merchantSessionIdentifier", 
                  "initiative", 
                  "initiativeContext", 
                  "displayName", 
                  "nonce" 
               ], 
               "nonce":"2c58a676", 
               "expiresAt":1573473811985 
            }, 
            "endpoints":{  
               "orderTrackingUrl":"qa-abctestpgw.imiconnect.com/orderTracking", 
               "fallbackUrl":"qa-abctestpgw.imiconnect.com/orderTracking", 
               "paymentMethodUpdateUrl":"qa-abctestpgw.imiconnect.com/orderTracking", 
               "shippingContactUpdateUrl":"qa-abctestpgw.imiconnect.com/orderTracking", 
               "shippingMethodUpdateUrl":"qa-abctestpgw.imiconnect.com/orderTracking" 
            }, 
            "state":"paymentNotCompleted", 
            "paymentRequest":{  
               "lineItems":[  
                  {  
                     "amount":"1.5", 
                     "label":"Adoption fee", 
                     "type":"Final" 
                  }, 
                  {  
                     "amount":"3", 
                     "label":"Your Total", 
                     "type":"Final" 
                  } 
               ], 
               "total":{  
                  "amount":"3", 
                  "label":"Your Total", 
                  "type":"Final" 
               }, 
               "applePay":{  
                  "merchantIdentifier":"merchant.com.imiconnectSDK.imimobile", 
                  "supportedNetworks":[  
                     "amex", 
                     "visa", 
                     "discover", 
                     "masterCard" 
                  ], 
                  "merchantCapabilities":[  
                     "supportsDebit", 
                     "supportsCredit", 
                     "supports3DS" 
                  ] 
               }, 
               "countryCode":"US", 
               "currencyCode":"USD", 
               "requiredBillingContactFields":[  
                  "name", 
                  "phone" 
               ], 
               "shippingMethods":[  
 
               ] 
            } 
         }, 
         "version":"1.0" 
      }, 
      "bid":"com.apple.messages.MSMessageExtensionBalloonPlugin:0000000000:com.apple.icloud.apps.messages.business.extension", 
      "sessionIdentifier":"5a86d8a1-2a71-61f0-8d2c-39ff46626244" 
   }, 
   "id":"2f834884-b0ed-4bc4-9c93-514e5c781728", 
   "type":"interactive", 
   "destinationId":"542bf1e0-ca58-43f2-941a-fe8c45da69f1", 
   "tid":"2cdf1a0e-2d6f-1332-261d-7ef5eebd1211", 
   "ts":"2019-11-11T10:03:47.949Z" 
}
```