## WhatsApp Templates

Templates need to be registered and approved before they can be utilised by leveraging template messages to open marketing, utility, and authentication conversations with customers. Unlike free-form messages, template messages are the only type of message that can be sent to customers who are yet to message you, or who have not sent you a message in the last 24 hours.

In addition, templates may be disabled automatically based on customer feedback and engagement. Once disabled, a template cannot be sent in a template message until its quality rating has improved or it no longer violates WhatsApp business or commerce policies.

> 👍 WhatsApp Template registration Best Practices
> 
> - It is important to follow WhatsApp's guidelines when submitting requests for template message approvals to avoid unintended rejections. Please [follow registration guidelines](https://help.webexconnect.io/docs/whatsapp-templates) when registering templates for WhatsApp. Refer to [Template categorization](https://developers.facebook.com/docs/whatsapp/updates-to-pricing/new-template-guidelines/) for understanding different template category use-cases.
> - You don't need to manually refresh WhatsApp template registration status. The status will be refreshed automatically on the UI as soon as WhatsApp provides an update. You can view the reason for rejection in case a WhatsApp template is rejected.
> - Any edits made to the content of a message template from the WhatsApp Manager will not be synced within the platform. Please create a new template from within the platform to make use of template update requirement.
> - Name of a template that was deleted in the past 30 days cannot be re-used for registering new template.
> - Adding a sample to your template submission increases the chances for approval substantially.
> - Meta has announced a [policy change for WhatsApp message templates](<#Valid and Verifiable URLs in WhatsApp Templates (Effective January 1, 2026)>) . Effective January 1, 2026, all businesses must include valid and verifiable HTTPS URLs in the message body or Call-To-Action (CTA) buttons when submitting WhatsApp templates.

## Configuring Marketing and Utility Templates

To configure a Marketing and Utility template:

1. Go to **Tools** > **Templates**.
2. Click **Add New Template**.
3. Enter a **Name** for the template. Only lower case letters and underscores are allowed in this field. Do not use spaces in the template name.
4. Select the **Channel** as _WhatsApp_.
5. Select the one of the two template options below for **Category**:
   - **Marketing**: Send promotions or information about your products, services, or business.
   - **Utility**: Send messages about an existing order or account.
6. Select the required **Language**. The drop-down list contains all the languages that Facebook/WhatsApp supports.
7. Select the **WABA ID** of the WhatsApp Business Account that you want to associate this template with from the drop-down list.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d36f6eb-4.jpeg",
        "template_video.png",
        "Screenshot of Configuring the WhatsApp Template"
      ],
      "align": "center",
      "sizing": "smart",
      "border": true,
      "caption": "Screenshot of Configure WhatsApp Template"
    }
  ]
}
[/block]


8. Select the **Header** type. This is an optional step.  
   Provide the header text if you select **Text** as the type for **Header**. You can use at most one variable in the header text.  
   Select _Image_, _Video_ or _Document_ if you select **Media** as the **Header** type. In the template, you just indicate if it is an image, video or document that you would like to send in the template. The actual image, video or document is to be configured in the WhatsApp send node. 

> ❗️ Input Parameters
> 
> Input parameters (dynamic content or variables) in templates cannot include newline characters or more than 4 consecutive spaces.

A template with a text header appears as shown below:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8c933f7-template-textheader-footer.png",
        "template-textheader-footer.png",
        "Screenshot of Text Header Preview"
      ],
      "align": "center",
      "sizing": "300to",
      "border": true,
      "caption": "Screenshot of Text Header Preview"
    }
  ]
}
[/block]


Here is a preview of the template that contains an image in the header, variables in the message body, and a footer:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63c6d23-template-imageheader-footer.png",
        "template-imageheader-footer.png",
        "Screenshot of Image Header Preview"
      ],
      "align": "center",
      "sizing": "400to",
      "border": true,
      "caption": "Screenshot of Image Header Preview"
    }
  ]
}
[/block]


This is a preview of the template that contains a document in the header, variables in the message body, and a footer:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c5e376e-template-docheader-footer.png",
        "template-docheader-footer.png",
        "Screenshot of Document Header Preview"
      ],
      "align": "center",
      "sizing": "400to",
      "border": true,
      "caption": "Screenshot of Document Header Preview"
    }
  ]
}
[/block]


9. Enter the appropriate message in the **Message Body**. Use the formatting icons to format the text within the message. Currently, you can format the text as follows:
   - **Bold**
   - _Italics_
   - Strikethrough
   - `Monospace`.  
     You can also add variables in the message body. You will need to provide values for the configured variables while using the WhatsApp send node within the flow builder.

> 📘 Variable name and its usage
> 
> You can click **+ Add Variable** to include a variable to Header (text type), Message Body or Call-to-Action Button. By default the name of the variable will be $(variable1) however it can be customised as needed. Make sure to specify all the variable names as keys within the 'parameters' object of templates Messaging API JSON payload.

10. Provide the **Footer** text. This is an optional step.
11. In the **Buttons** section, select the required type of button. This is an optional step.  
    The buttons enable interactivity in WhatsApp messages. 

- **Call-To-Action** (CTA) - use this button to configure a CTA button to direct user to their default dialer app to contact business number or to redirect them to website. You must configure the phone number to which the direct call is placed or the URL of the website you want to direct the users. You can only configure a maximum of two CTA buttons.  
  The type of action can be either **Visit Website** or **Call Phone Number**. For the Visit Website option, you need to specify the button text and the URL of the website. The URL can be dynamic or static. A placeholder is added as an extension of the URL in the case of a dynamic URL. You can add variables to the URL for a dynamic URL. For the **Call Phone Number** option, specify the button text and then the phone number. For this type of action, you can have a maximum of one button type of each type per message, i.e, one Call Phone Number button and one Visit Website button.<br>
- **Quick Replies** (QR) - use this to configure Button text of quick reply (QR) buttons. You can use a maximum of three QR buttons.

> 🚧 Opt-out quick reply
> 
> We recommend businesses to keep an opt-out button in their templates. Allowing customers to request to opt out of template messages can help reduce blocks from customers and increase phone number quality rating. [Learn more](https://www.facebook.com/business/help/448422200528701).

The following is a preview of a message with CTA buttons:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/78140a3-5.png",
        "cta_buttons_preview.png",
        "Screenshot of Call-to-action (CTA) Buttons Message Preview"
      ],
      "align": "center",
      "sizing": "450px",
      "border": true,
      "caption": "Screenshot of Call-to-action (CTA) Buttons Message Preview"
    }
  ]
}
[/block]


The following is a preview of a message with QR buttons:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8c5ad0b-6.png",
        "quick_replies_buttons_preview.png",
        "Screenshot of Quick Replies Buttons Preview"
      ],
      "align": "center",
      "sizing": "450px",
      "border": true,
      "caption": "Screenshot of Quick Replies Buttons Preview"
    }
  ]
}
[/block]


A message with CTA buttons appears as follows:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b463ede-wa_cta_image.png",
        "wa_cta_image.png",
        "Screenshot of Call-To-Action (CTA) Buttons"
      ],
      "align": "center",
      "sizing": "300to",
      "border": true,
      "caption": "Screenshot of Call-To-Action (CTA) Buttons"
    }
  ]
}
[/block]


A message with QR buttons appears as follows:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/721688d-wa_qr_image.jpg",
        "wa_qr_image.jpg",
        "Screenshot of Quick Replies Buttons"
      ],
      "align": "center",
      "sizing": "300to",
      "border": true,
      "caption": "Screenshot of Quick Replies Buttons"
    }
  ]
}
[/block]


> 🚧 Interactive Buttons
> 
> Within a template, you can configure either CTA buttons or QR buttons, but not a combination of these two types.

```json Sample Payload for CTA Buttons
{
   "appid":"a_160730369477132030",
   "deliverychannel":"whatsapp",
   "message":{
      "template":"1024406451379326",
      "parameters":{
         "variable1":{
            "type":"url",
            "payload":"<<url_extension>>"
         }
      }
   },
   "destination":[
      {
         "waid":[
            "9199xxxxxxxx"
         ]
      }
   ]
}
```
```json Sample Payload for QR Buttons
{
   "appid":"a_161007122569873440",
   "deliverychannel":"whatsapp",
   "message":{
      "template":"244219340449037",
      "parameters":{
         "quickReply":[
            {
               "button_text":"Button 1",
               "payload":"<<button 1 payload>>"
            },
            {
               "button_text":"Button 2",
               "payload":"<<button 2 payload>>"
            },
            {
               "button_text":"Button 3",
               "payload":"<<button 3 payload>>"
            }
         ]
      }
   },
   "destination":[
      {
         "waid":[
            "9199xxxxxxxx"
         ]
      }
   ]
}
```

12. Click **Configure Sample Content**. This button enables you to send sample data to WhatsApp making it easier to identify the type of data being sent using this template. This button is enabled only when you have at least one variable is added in the header text, message body or CTA button or if the header is Media. Using this button you can also preview the sample content.

> 📘 Note
> 
> If you want to include variables or media (optional), you must add a content example for your template by clicking the **Configure Sample Content **button.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/209f9f9-Add_Sample.png",
        "Add Sample.png",
        "Screenshot of Configuring Sample Content"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring Sample Content"
    }
  ]
}
[/block]


13. Click **Save**. When you click the **Save** button, the template is submitted for approval to Facebook/WhatsApp. Only the approved templates appear under the list of available templates on the **Templates** page and also within the WhatsApp send node.

> 🚧 Using WhatsApp Templates in Messaging API v1
> 
> If you have set-up a WhatsApp Template from within Tools ->Templates section, you need to use Template message type when trying to utilise these templates in the messaging API.

> ❗️ Character Limitation for Templates
> 
> The character limitation for a template is 1024 characters, this includes the message content within the header, body, footer and buttons.

### Valid and Verifiable URLs in WhatsApp Templates (Effective January 1, 2026)

Meta has announced a policy change affecting WhatsApp message templates. Starting January 1, 2026, WhatsApp requires all businesses including URLs in the message body or Call-To-Action (CTA) buttons to submit valid and verifiable HTTPS URLs. Templates that do not meet this requirement will result in a template creation error.

**Key Points**

- WhatsApp will only accept complete and working HTTPS URLs.
- Invalid or unreachable URLs will lead to template rejection.
- Destination pages must be publicly accessible (not requiring login or restricted access).

**Impact**

- Applies to all templates submitted via <<prodname>> starting January 1, 2026.
- The "Visit Website" CTA button must contain a valid and verifiable HTTPS URL to avoid template creation errors.
- Meta is likely to reject any existing or new template that includes variables for URL configuration outside the "Visit Website" CTA (e.g., in the body or header).

**Required Actions**

- **For new templates**
  - Create templates requiring URL inclusion using the "Visit Website" CTA option.
  - Verify that the provided URL is valid and publicly accessible before submission.
- **For existing templates**
  - Replace templates that use variables in the header or body to pass URL values with templates that use a verifiable "Visit Website" CTA button.
  - Update templates with invalid or non-verifiable URLs to include valid and verifiable "Visit Website" URLs instead.

  **Example**

| Configuration                                               | Result   |
| :---------------------------------------------------------- | :------- |
| “Visit Website” CTA → <https://www.example.com/product/123> | Accepted |
| “Visit Website” CTA → <https://www.example.com/product/123> | Rejected |
| CTA uses http\:// or invalid domain                         | Rejected |

<br />

### Limitation on Marketing Messages

WhatsApp have enforced following limitations on Marketing messages reduce negative engagements like NFR, archive, mute and block rates.

- WhatsApp are limiting the number of marketing template messages a person can receive from all business in a given period of time, starting with a small number of conversations that are less likely to be read. This limit is based on the number of marketing template messages that a WhatsApp user has already received from businesses and may not be related to your specific business.
- Starting April 1st 2025, WhatsApp is pausing marketing communication being sent to US customers. Businesses should use error code 131049 within additional_info as part of failed delivery receipts, to handle this error.

### Template Category Change

Starting October 14, 2024, Meta will be updating the category of an approved message template if they determine that its current category is not accurate as per the template category guidelines. This was done on a monthly basis historically however the category review and change now happens on a daily basis. 

The category changes will ensure that approved templates are accurately categorised as per the [template category guidelines](https://help.webexconnect.io/docs/whatsapp-category-guidelines).  This will apply to marketing and utility templates, and changes can be in both directions (utility template updated to marketing and vice-versa).

If you think that a template's new category is inconsistent with Meta’s guidelines, reach out to Support Team using the details mentioned in the ‘Contact Support’ section within your <<prodname>> account and raise a request.

### Template Pacing

Template pacing is a mechanism that allows time for your WhatsApp end-customers to provide early feedback on templates. WhatsApp identifies and pauses templates that have received poor feedback or engagement, this will allow you enough time to adjust template content before they are sent to too many customers, thereby reducing the likelihood of negative feedback impacting your business. [Template pacing](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing) is valid for marketing and utility templates.

## Configuring Authentication Templates

If your business mobile app offers users the option to receive one-time passwords or verification codes via WhatsApp, you should use an authentication template. Authentication templates can be configured using two code delivery methods:

1. **One-tap autofill authentication templates**:  allow you to send a one-time password or code along with a one-tap autofill button to your users. When a WhatsApp user taps the autofill button, the WhatsApp client triggers an activity which opens your app and delivers it the password or code.
2. **Copy code authentication templates**: allow you to send a one-time password or code along with a copy code button to your WhatsApp users. When the user taps the copy code button, the WhatsApp copies the password or code to the device's clipboard. The user can then switch to your business app and paste the password or code into your business app.

To configure an Authentication template:

1. Go to **Tools** > **Templates**.
2. Click **Add New Template**.
3. Enter a **Name** for the template. Only lower case letters and underscores are allowed in this field. Do not use spaces in the template name.
4. Select the **Channel** as _WhatsApp_.
5. Select the **Authentication** template for **Category**.
6. Select the **WABA ID** of the WhatsApp Business Account that you want to associate this template with from the drop-down list.
7. Select the required **Language**. The drop-down list contains all the languages that Facebook/WhatsApp supports.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8f5f151-Config_Generic.png",
        "",
        "Screenshot of Configuring the New WhatsApp Template"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the New WhatsApp Template"
    }
  ]
}
[/block]


8. Under **Code Delivery Configuration**, select one of the two options:

     **Auto-fill**: Selecting this option will ensure that the code is sent to your app when a customer taps the button. 

   [block:parameters]{"data":{"h-0":"Field","h-1":"Description","h-2":"Example","0-0":"Button Text for Auto-Fill","0-1":"(Optional) One-tap Auto-Fill button label text. The maximum character limit is 25 characters.  \nIf the values for Button Text are not provided, it will take the values based on the language selected.","0-2":"Autofill","1-0":"Button Text for Copy Code","1-1":"(Optional) Copy Code button label text. The authentication template message will display a Copy Code button with this text, if the message fails the eligibility check. The maximum character limit is 25 characters.  \nIf the values for Button Text are not provided, it will take the values based on the language selected. ","1-2":"Copy Code","2-0":"Package Name","2-1":"(Mandatory) Your Android app's package name. The package name in the message (defined in the package_name property in the components array upon template creation) should match the package name set on the intent. The match is determined through the 'getCreatorPackage' method called in the 'PendingIntent' object provided by your application.","2-2":"com.example.myapplication","3-0":"App Signature Hash","3-1":"(Mandatory) Your app signing key hash. It should match with your installed app's signing key hash.","3-2":"K8a%2FAINcGX7"},"cols":3,"rows":4,"align":["left","left","left"]}[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/62269a0-Config_Autofill.png",
        "",
        "Screenshot of Code Delivery Configuration"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Code Delivery Configuration"
    }
  ]
}
[/block]


**Copy-Code** Selecting this option will allow WhatsApp customer to copy and paste the code into your app.

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description ",
    "h-2": "Example",
    "0-0": "Button Text",
    "0-1": "(Optional) Copy Code button label text. The authentication template message will display a Copy Code button with this text if the message fails the eligibility check. The maximum character limit is 25 characters.  \nIf the values for the Button Text are not provided, it will take the values based on the language selected.",
    "0-2": "Copy Code"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/188d9e5-Config_Copycode.png",
        "",
        "Screenshot of Copy Code"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Copy Code"
    }
  ]
}
[/block]


9. Under **Additional Content**, optionally configure one or more of the following:
   1. **Add security recommendation**: Appends the message body with a security recommendation.
   2. **Add expiry time for the code**: Adds a footer to your message conveying the expiry time.
   3. **Lock this template to prevent other users to make changes**: Adds selective edit rights to the template.
10. Click **Save**.

Please note that you will not be able to Edit a WhatsApp Template after it has been saved (i.e., submitted for approval to WhatsApp). If you want to Lock the template (to stop other users from deleting your template), please use Lock option under the Actions dropdown.

### Eligibility Check for Authentication Templates

WhatsApp  performs the following checks when it receives an authentication template message. If any check fails, the one-tap autofill button will be replaced with a copy code button.

- The handshake was initiated no more than 10 minutes ago (or no more than the number of minutes indicated by the template's code_expiration_minutes property, if present).
- The package name in the message (defined in the package_name property in the components array upon template creation) matches the package name set on the intent. The match is determined through the getCreatorPackage method called in the PendingIntent object provided by your application.
- The app signing key hash in the message (defined in the signature_hash property in the components array upon template creation) matches your installed app's signing key hash.
- The message includes the one-tap autofill button text.
- Your app has defined an activity to receive the password or code.  
  Android Notifications

Android notifications indicating receipt of a WhatsApp authentication template message will only appear on the user's Android device if:

- The user is logged into the WhatsApp app or WhatsApp Business app with the phone number (account) that the message was sent to.
- The user is logged into your app.
- Android OS is KitKat (4.4, API 19) or above.
- Show notifications is enabled (Settings > Notifications) in the WhatsApp app or WhatsApp Business app.
- Device level notification is enabled for the WhatsApp app or WhatsApp Business app.
- Prior message threads in the WhatsApp app or WhatsApp Business app between the user and your business are not muted.

<WhatsAppAuthenticationMessageSecurity />