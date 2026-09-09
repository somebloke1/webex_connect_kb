# Mobile Wallet API

Source: https://help.webexconnect.io/docs/mobile-wallet-api
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:38+00:00

## API Overview

The Mobile Wallet API provides the ability to create and update mobile wallet passes/objects for Apple iOS and Google Android Pay.

### Base URL

The base URL for all API calls is: <https://api.imimobilewallet.com/api/>

The Mobile Wallet implementation might be deployed in more than one geographical region.

Check with the IMImobile staff to verify which base URL is most compatible with your requirements.

### Authentication

All requests to the API require a use of the authentication key as an HTTP header for all requests.

- Name of the header:  `x-api-key`
- Value can be looked up on the Integration Page when you are logged into the Wallet UI. 

### Create and Update Notes

#### Apple notes

Preferably, list all fields in the API that are included in a pass by UI, for create and update.

It is possible that if you add a new field into the Update request and not include existing fields into the call, it is possible that the existing fields might be deleted.

#### Google notes

There is a list of fields that are included  in a template and they cannot be updated via API. They can be updated with the UI.  
There is another list  of fields that are only updated via API and not UI. There is yet another set of fields  
that are updated via the UI or the API. If there is a new field added in the UI, it is static and cannot be changed via API.  
If a field is added via the API, it can be updated via API again.



![Screenshot displaying the interface for designing a mobile wallet pass for Google Android Pay](https://files.readme.io/7c7da52-15598ce0-8448-4ddb-8d66-9bc77f070077.png)




## Create a wallet landing page

A landing page will display installation buttons for Android or Apple, which will allow  the end user to install a wallet pass on a device.

> 📘 Note
> 
> Creation of a landing pages and sending links to such a pages to consumers does not guarantee installation of a passes on consumers' devices.  
> Ultimately, it up to consumers to install passes with the help of landing pages.

### Request

- Method: `POST`
- URI:  `/wallet/[Wallet ID]/landing`

### Headers

| Name         | Value              | Required |
| :----------- | :----------------- | :------- |
| Content-Type | `application/json` | yes      |
| x-api-key    | api key            | yes      |

### Body

The body of the request is in JSON format and may contain the following fields:

| Name                   | Description                                                                                                                                                                          | Required |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
| `data`                 | A nested object that contains the data elements and values of the wallet object/pass.                                                                                                | yes      |
| `data.barcode.type`    | Format of the barcode. Possible values are: `AZTEC`, `CODABAR`, `CODE128`, `CODE39`, `DATAMATRIX`, `EAN13`, `EAN8`, `ITF14`, `PDF417` `,PDF417COMPACT`, `QRCODE`, `TEXTONLY`, `UPCA` | yes      |
| `data.barcode.value`   | Value that is encoded in the barcode                                                                                                                                                 | yes      |
| `data.barcode.altText` | Value that is encoded in the barcode                                                                                                                                                 | yes      |

### Apple-Only Fields

> 📘 
> 
> These custom fields only apply to Apple. N starts at 0. All values must be specified for a given field.

- `key` - Identifier for the field
- `label` - Label of the field that is displayed on the pass.
- `value` - Value of the field that is displayed on the pass.
- `alignment` - Alignment of the field value and label.  Possible values are:
  - `PKTextAlignmentLeft`
  - `PKTextAlignmentCenter`
  - `PKTextAlignmentRight` 



| Name | Description | Required |
| --- | --- | --- |
| `data.customHeaderFields[N].key` `data.customHeaderFields[N].label`  `data.customHeaderFields[N].value`  `data.customHeaderFields[N].align` | Header fields are displayed at the top of the pass. | no |
| `data.customPrimaryFields[N].key`  <br>`data.customPrimaryFields[N].label`  `data.customPrimaryFields[N].value`  `data.customPrimaryFields[N].align` | Primary fields are displayed on the strip image of the pass | no |
| `data.customSecondaryFields[N].key`  `data.customSecondaryFields[N].label`  <br>`data.customSecondaryFields[N].value`  <br>`data.customSecondaryFields[N].align` | Secondary fields are located below the strip image. | no |
| `data.customAuxiliaryFields[N].key` `data.customAuxiliaryFields[N].label`  <br>`data.customAuxiliaryFields[N].value` `data.customAuxiliaryFields[N].align` | Auxiliary fields are located below the secondary fields. | no |
| `data.customBackFields[N].key`  `data.customBackFields[N].label`  `data.customBackFields[N].value`  `data.customBackFields[N].align` | Back fields are located on the back of the pass. | no |




## Google-Only Fields

> 📘 
> 
> The texts field only applies to Google. Both header and body must be specified. N starts at 0.

| Name                            | Description                             | Required |
| :------------------------------ | :-------------------------------------- | :------- |
| `texts[N].header texts[N].body` | Adds a text field to the wallet object. | no       |

```json Example Request
{
  "data":{
    "type":"offer",
    "state":"active",
    "expirationDate":"2017-12-31T23:59:59-0400",
    "validTimeInterval.end":"2017-12-31T23:59:59-0400",
    "barcode.type":"CODE128",
    "barcode.value":"CPN12345678",
    "barcode.altText":"CPN12345678",
    "customHeaderFields[0].key":"headerField1",
    "customHeaderFields[0].label":"Expires",
    "customHeaderFields[0].value":"12/31/17",
    "customHeaderFields[0].align":"PKTextAlignmentLeft",
    "customSecondaryFields[0].key":"secondaryField1",
    "customSecondaryFields[0].label":"SPEED PERKS DOUBLE REWARDS",
    "customSecondaryFields[0].value":"$10 off $50 purchase",
    "customSecondaryFields[0].align":"PKTextAlignmentLeft",
    "texts[0].header":"SPEED PERKS DOUBLE REWARDS",
    "texts[0].body":"$10 off $50 purchase"
  }
}
```

### Request

Status Code:  `200` - The mobile wallet pass/object was successfully created

### Response body

The body of the response is in JSON format. Most of the response fields are the same as

in the request. In addition, the response returns a `passId` and a URL link to the landing page

for installation of this pass on a device.

```json
{
  "content": {
    "passId": "XXXXXX",
    "walletId": "XXXXXXX",
    "accountId": "accountId",
    "appleTemplateId": "e3tgewokrnfrdkc2kudmzu3zxe",
    "googleTemplateId": "AdvanceAutoPartsOctober2017",
    "data": {
      "state": "active",
      "expirationDate": "2017-12-31T23:59:59-0400",
      "validTimeInterval.end": "2017-12-31T23:59:59-0400",
      "barcode.type": "CODE128",
      "barcode.value": "CPN12345678",
      "barcode.altText": "CPN12345678",
      "customHeaderFields[0].key": "headerField1",
      "customHeaderFields[0].label": "Expires",
      "customHeaderFields[0].value": "12/31/17",
      "customHeaderFields[0].align": "PKTextAlignmentLeft",
      "customSecondaryFields[0].key": "secondaryField1",
      "customSecondaryFields[0].label": "SPEED PERKS DOUBLE REWARDS",
      "customSecondaryFields[0].value": "$20 off $50 purchase",
      "customSecondaryFields[0].align": "PKTextAlignmentLeft",
      "texts[0].header": "SPEED PERKS DOUBLE REWARDS",
      "texts[0].body": "$20 off $50 purchase"
    },
    "distributionType": "ONE-TO-ONE",
    "landingPageStrategy": "GOOGLE",
    "customLayout": {
      "mainImage": "<https://-> link to an image",
      "mainImagePosition": "BELOW",
      "logoImagePosition": "CENTER",
      "titleText": "SAVE NOW!",
      "mainText": "any text here, including HTML markup",
      "installConfirmationPage": {
        "text": "<b>Your reward can be found in your Apple Wallet or Google Android Pay app.</b><br><br><b>Visit shop.acmeshop.com for the latest deals.</b>",
        "fontColor": "#ffffff",
        "backgroundColor": "#000000"
      }
    },
    "redirect": true,
    "passName": "SpeedPerksDiscount10"
  },
  "_links": {
    "self": {
      "href": "<https://imimobilewallet.com/passes/[PASS> ID HERE]/landing.html"
    }
  }
}
```

## Update a single wallet pass

### Pass Update

Apple allows updating (also adding or removing) almost all fields through API calls.

Google allows updating only fields used in API call when issuing a pass. Some fields could be added: `texts`, `messageList`. 

## Wallet Template Update

Updating a published wallet template has no effect on the apple passes, only future passes will include the changes

On the other hand updating a published wallet template will change all installed google passes

Wallet passes/objects may be updated using this API. The `passId` and `data`

Objects are required for the update requests. Only data for fields that are changing need to be specified, however, all fields may be specified if desired.

> 📘 Note
> 
> If a field is present in a template, but omitted from the request, its value from the template will be displayed.

Fields may be modified or added using this API. A lock screen notification message may be triggered on Apple IOS devices to inform the consumer that the pass has been updated.

### Request

- Method: `PATCH`
- URI: `/pass` 

### Headers

| Name         | Value              | Required |
| :----------- | :----------------- | :------- |
| Content-Type | `application/json` | yes      |

### Body

The body of the request is a JSON object and may contain the following fields:



| Name | Description | Required |
| --- | --- | --- |
| passId | The ID of the wallet pass/object to update. | yes |
| customLayout | Must be included but the value portion can be left blank | Yes |
| data | A nested object that contains the data elements and values of the wallet object/pass. All data fields (except for type) must be specified including values that are not changing. Additional data fields may be included. | yes |
| data.trackProgress | Pass this as "true" in order to track the progress of a pass upade on the Status report page in wallet builder ui | no |
| `data.<field>.changeMessage` (Apple only) | A lock screen notification may be triggered on Apple devices to notify the consumer about the update by including a `changeMessage` value. The lock screen notification only displays when a field value is modified.  <br>Notes about using `changeMessage`:  <br>  <br>1. Use %@ in the changeMessage to display the new value of the field within the lock screen notification message.<br>2. If `%@` is omitted from the `changeMessage`, the notification message will say "Store card changed" or "Coupon changed" (depending on the pass type) regardless of any other text in the `changeMessage`.<br>3. `%@` only applies to the field value (for example, an updated label will not trigger a lock screen notification).<br>4. Multiple fields may be updated, but the lock screen notification is only capable of displaying information about one of the fields. | no |




#### Example 1: Update an existing field

```json
{
  "passId": "XXXXXXXXX",
  "customLayout": {},
  "data": {
    "expirationDate": "2021-01-15T23:59:59-0400",
    "validTimeInterval.end": "2021-01-15T23:59:59-0400",
    "customHeaderFields[0].key": "headerField1",
    "customHeaderFields[0].label": "Expires",
    "customHeaderFields[0].value": "01/15/21",
    "customHeaderFields[0].align": "PKTextAlignmentLeft",
    "customHeaderFields[0].changeMessage": "Your offer expiration has been extended until %@",
    "trackProgress":"true"
  }
}
```

#### Example 2: Add New Field

```json
{
  "passId": "XXXXXXX",
  "customLayout": {},
  "data": {
    "customBackFields[0].key": "BackField1",
    "customBackFields[0].label": "Reminder",
    "customBackFields[0].value": "Don't forget to use your Volume Perks reward before it expires!",
    "customBackFields[0].align": "PKTextAlignmentLeft",
    "customBackFields[0].changeMessage": "%@"
  }
}
```

## Response

Status Code: 200 - The mobile wallet pass/object was successfully updated

## Response Body

The body of the response is a JSON document. Most of the response fields are the same as in the  
response for the issue method. Any new field values or `changeMessage` fields will be included as well.

**Example**:

```json
{
  "content": {
    "passId": "XXXXXXX",
    "appleTemplateId": "e3tgewokrnfrdkc2kudmzu3zxe",
    "googleTemplateId": "AcmeToolsOctober2020",
    "data": {
      "type": "offer",
      "state": "active",
      "expirationDate": "2021-01-15T23:59:59-0400",
      "validTimeInterval.end": "2021-01-15T23:59:59-0400",
      "barcode.type": "CODE128",
      "barcode.value": "CPN12345678",
      "barcode.altText": "CPN12345678",
      "customHeaderFields[0].key": "headerField1",
      "customHeaderFields[0].label": "Expires",
      "customHeaderFields[0].value": "01/15/21",
      "customHeaderFields[0].align": "PKTextAlignmentLeft",
      "customHeaderFields[0].changeMessage": "Your offer expiration has been extended until %@",
      "customSecondaryFields[0].key": "secondaryField1",
      "customSecondaryFields[0].label": "SPEED PERKS DOUBLE REWARDS",
      "customSecondaryFields[0].value": "$20 off $50 purchase",
      "customSecondaryFields[0].align": "PKTextAlignmentLeft",
      "texts[0].header": "SPEED PERKS DOUBLE REWARDS",
      "texts[0].body": "$20 off $50 purchase"
    },
    "distributionType": "ONE-TO-ONE",
    "landingPageStrategy": "GOOGLE",
    "customLayout": {
      "mainImage": "https:[url to image here]",
      "mainImagePosition": "BELOW",
      "logoImagePosition": "CENTER",
      "titleText": "SAVE NOW!",
      "mainText": "<b>Volume Perks reward: Save $20 today!</b>",
      "installConfirmationPage": {
        "text": "<b>Your reward can be found in your Apple Wallet or Google Android Pay app.</b><br><b>Visit acmetools.com for latest deals.</b>",
        "fontColor": "#ffffff",
        "backgroundColor": "#000000"
      }
    },
    "redirect": true,
    "passName": "SpeedPerksDiscount10"
  },
  "_links": {
    "self": {
      "href": "<https://api.imimobilewallet.com/passes/XXXXXXXX/landing.html">
    }
  }
}
```

## Retrieve a single wallet pass

An issued wallet pass/object may be retrieved using its passId.

### Request

- Method: `GET`
- URI: `/pass/{passId}`

### Headers

| Name         | Value              | Required |
| :----------- | :----------------- | :------- |
| Content-Type | `application/json` | yes      |

### Body

The body of the response is in JSON format. Most of the response fields are the same as a response for the issue method. Any new field values or `changeMessage` fields will be included as well.

**Example Curl request:** 

```json
curl -X GET -H "Content-type: application/json" -H \
  "x-api-key: [API AUTH KEY]" <https://api.imimobilewallet.com/api/pass/[PASS> ID]
```

**Response:**

```json
{
    "content": {
        "passId": "[PASS ID]",
            "walletId": "[WALLET ID]",
            "googleTemplateId": "[GOOGLE TEMPLATE ID]",
            "data": {
            "texts[0].body": "update body",
                "barcode.type": "PDF417",
                "walletName": "amazon",
                "barcode.value": "123",
                "texts[0].header": "Update",
                "trackProgress": "true",
                "state": "active",
                "type": "offer"
        },
        "distributionType": "ONE-TO-ONE",
            "landingPageStrategy": "CUSTOM",
            "customLayout": {
            "type": "STACKED",
                "useOriginalImages": true,
                "hideBarcode": false,
                "googleTheme": "dark",
                "image1": {
                "name": "URL",
                    "url": "<https://google-wallet-assets.s3.amazonaws.com/e9187e90-4139-11eb-8c86-d770cac81bbd-image1.png">
            },
            "barcodePosition": "top"
        },
        "redirect": false,
            "passName": "amazon"
    },
    "_links": {
        "self": {
            "href": "<https://imimobilewallet.com/passes/[PASS> ID]/landing.html"
        }
    }
}
```

> 📘 Note
> 
> The 'data' field will contain only fields used when issuing and updating a pass.

## Request a list of pass ids by wallet name

### Request

- Method: `GET`
- URI: `/api/wallet/[wallet_name]/passes` 

### Request headers

| Name         | Value              | Required | Description                                                                                              |
| :----------- | :----------------- | :------- | :------------------------------------------------------------------------------------------------------- |
| Content-Type | `application/json` | yes      |                                                                                                          |
| Accept       | text/csv           | no       | If omitted, the response will be in the JSON format. If provided, the response will be in a  CSV format. |

## Response

A list of pass IDs associated with a provided wallet name in a CSV format with a single column.

### Response headers

| Name                | Value                                             |
| :------------------ | :------------------------------------------------ |
| Content-Disposition | `attachment; filename="[wallet-name]-passes.csv"` |

## Loyalty

| UI field name (which are part of TEMPLATE)      | UI field name (Which are part of PASS) | Key for API JSON Body (issue/update)           | Included in template | Included in pass |
| :---------------------------------------------- | :------------------------------------- | :--------------------------------------------- | :------------------- | :--------------- |
|                                                 | ACCOUNT ID                             | loyaltyAccountId                               |                      | YES              |
|                                                 | ACCOUNT NAME                           | loyaltyAccountName                             |                      | YES              |
|                                                 |                                        | loyaltyPointsLabel                             |                      | YES              |
|                                                 |                                        | loyaltyPointsBalanceString                     |                      | YES              |
|                                                 |                                        | loyaltyPointsBalanceInt                        |                      | YES              |
|                                                 |                                        | loyaltyPointsBalanceDouble                     |                      | YES              |
|                                                 |                                        | loyaltyPointsBalanceMoneyValue                 |                      | YES              |
|                                                 |                                        | loyaltyPointsBalanceMoneyCurrencyCode          |                      | YES              |
|                                                 |                                        | linkedOfferIds[%index%]                        |                      | YES              |
|                                                 |                                        | secondaryLoyaltyPointsLabel                    |                      | YES              |
|                                                 |                                        | secondaryLoyaltyPointsBalanceString            |                      | YES              |
|                                                 |                                        | secondaryLoyaltyPointsBalanceInt               |                      | YES              |
|                                                 |                                        | secondaryLoyaltyPointsBalanceDouble            |                      | YES              |
|                                                 |                                        | secondaryLoyaltyPointsBalanceMoneyValue        |                      | YES              |
|                                                 |                                        | secondaryLoyaltyPointsBalanceMoneyCurrencyCode |                      | YES              |
|                                                 |                                        | barcode.value                                  |                      | YES              |
| BARCODE TYPE (BARCODE)                          | BARCODE TYPE                           | barcode.type                                   | YES                  | YES              |
| BARCODE ENCODING (BARCODE)                      |                                        |                                                | YES                  |                  |
| PROGRAM NAME (ANDROID)                          |                                        |                                                | YES                  |                  |
| ACCOUNT NAME LABEL (ANDROID)                    |                                        |                                                | YES                  |                  |
| ACCOUNT ID LABEL (ANDROID)                      |                                        |                                                | YES                  |                  |
| REWARDS TIER LABEL (ANDROID)                    |                                        |                                                | YES                  |                  |
| REWARDS TIER (ANDROID)                          |                                        |                                                | YES                  |                  |
| HOME PAGE URI (ANDROID)                         |                                        |                                                | YES                  |                  |
| ISSUER NAME (ANDROID)                           |                                        |                                                | YES                  |                  |
| ANDROID CARD BACKGROUND COLOR (GRAPHICS COLORS) |                                        |                                                | YES                  |                  |
| PASS TYPE (SETUP/PASS INFORMATION)              |                                        |                                                | YES                  |                  |
| PASS TYPE (SETUP/PASS INFORMATION)              |                                        | messageList\[].header                          | YES                  | YES              |
| ITEM BODY (ANDROID/MESSAGE)                     |                                        | messageList\[].body                            | YES                  | YES              |
| ITEM LABEL (ANDROID/URLS)                       |                                        | linkList\[].description                        | YES                  | YES              |
| ITEM URI (ANDROID/URLS)                         |                                        | linkList\[].url                                | YES                  | YES              |
| ITEM HEADER (ANDROID/TEXT MODULE)               |                                        | textList\[].header                             | YES                  | YES              |
| ITEM BODY (ANDROID/TEXT MODULE)                 |                                        | textList\[].body                               | YES                  | YES              |
| HERO IMAGE (GRAPHICS/ANDROID/ANDROID IMAGES)    |                                        | heroImage.url                                  | YES                  | YES              |

## Boarding

![](https://files.readme.io/965bf9e-Boarding.jpg "Boarding.jpg")

## Offer

![](https://files.readme.io/cbf61c7-Offer.jpg "Offer.jpg")

## Gift

![](https://files.readme.io/32109b6-Gift.jpg "Gift.jpg")

## Event

![](https://files.readme.io/e07cd56-Event.jpg "Event.jpg")