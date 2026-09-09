[block:html]
{
  "html": "<div></div>\n\n<style>\n  .rm-ReferenceMain .rm-Article {\n    display: flex;\n    flex-direction: column;\n}\n \n.rm-ParamContainer {\n    order: 1;\n}\n \n.field-description, .markdown-body {\n    order: 2;\n}\n \n.rm-ReferenceMain .markdown-body {\n  margin-top: 10px\n}\n \n.rm-ReferenceMain .rm-Article .rm-APISectionHeader {\n    order: 3;\n}\n \n[class^=\"APIResponseSchemaPicker\"] {\n    order: 4;\n}\n \n[class^=\"Footer-desktop\"] {\n  order: 5\n}\n\n</style>"
}
[/block]


> ❗️ HSM Message Deprecation Alert
> 
> WhatsApp has announced that they will be deprecating the HSM message type sometime in early 2022. We recommend you to use Template message type instead of HSM messages, and migrate any existing HSMs to Template Message type. Unlike HSM which was meant to be used only for text messages, Template message type can be used to configure template messages of multiple components including text.

> 🚧 Some of the below values such as namespace, element_name, etc. are not available on imiconnect platform UI and need to be taken from WhatsApp Business Manager by reaching out to your regional support team. However, you wouldn't need it as we now recommend you to use Template message type instead of HSM.

> ❗️ WhatsApp Language Policy Change
> 
> Please note that the fallback language policy has been deprecated and the deterministic language policy is now the default policy. Do not use 'fallback' language policy while sending HSMs as it may lead to message delivery failures.

**_Localizable Parameters_**

When sending a Message Template, the hsm object is required. To define Message Templates, you specify a namespace and an element_name pair that identify a template. Templates have parameters that will be dynamically incorporated into the message. For the example used in this document, the Message Template looks like this:

| Parameters | Type             | Mandatory | Description                                                                                    |
| :--------- | :--------------- | :-------- | :--------------------------------------------------------------------------------------------- |
| default    | String           | Yes       | Default text if localization fails                                                             |
| currency   | currency object  | No        | If the currency object is used, it contains required parameters currency_code and amount_1000. |
| date_time  | date_time object | No        | If the date_time object is used, further definition of the date and time is required.          |

## Error Codes

Refer to the [Apple Messages for Business](https://developers.imiconnect.io/reference/channel-specific-status-codes-1#apple-messages-for-business) section.