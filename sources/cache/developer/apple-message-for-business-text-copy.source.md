[block:html]
{
  "html": "<div></div>\n\n<style>\n  .rm-ReferenceMain .rm-Article {\n    display: flex;\n    flex-direction: column;\n}\n \n.rm-ParamContainer {\n    order: 1;\n}\n \n.field-description, .markdown-body {\n    order: 2;\n}\n \n.rm-ReferenceMain .markdown-body {\n  margin-top: 10px\n}\n \n.rm-ReferenceMain .rm-Article .rm-APISectionHeader {\n    order: 3;\n}\n \n[class^=\"APIResponseSchemaPicker\"] {\n    order: 4;\n}\n \n[class^=\"Footer-desktop\"] {\n  order: 5\n}\n\n</style>"
}
[/block]


<br />

> 📘 Note:
> 
> - It is recommended to use a valid authorization ID; the failure of notification won’t be logged in Debug Logs.
> - The notify URL should be filled with the proper URL format; otherwise, it would be considered an invalid URL.
> - The notify URL should be provided with proper spacing of the URL; when space is provided in front of the URL or at the end of the URL, it would be considered an invalid URL.

## Responses

### 200

The request is accepted for processing. Webex Connect returns a transaction identifier for the request. Submission status is available through outbound webhooks, Notify URL, and Debug Console.

### 400

The request is invalid. This response is returned for synchronous Messaging API request validation failures, such as missing mandatory parameters or invalid request values.

## Error Codes

Refer to the [Apple Messages for Business section in Channel Specific Status Codes](https://developers.webexconnect.io/reference/channel-specific-status-codes).

## Important Considerations

- Invitation messages are addressed to customer mobile numbers.
- Standard Apple Messages for Business message types continue to use the AMB opaque user ID.
- Subsequent standard Apple Messages for Business messages must use the resolved AMB opaque user ID.
- Invitation messages do not support free-form text.
- To send an Invitation Message with a brand logo, configure the business logo on the Apple Messages for Business app asset and set `withImage` to `true`. Webex Connect uses the image-enabled invitation template.
- If `withImage` is set to `true` and the selected Apple Messages for Business app asset does not have a business logo configured, the invitation message transaction fails.
- To send an Invitation Message without a brand logo, set `withImage` to `false`. Webex Connect uses the no-image invitation template.
- If the customer selects **No** on the invitation, opts out of invitation messages, or closes the Apple Messages for Business conversation, Webex Connect suppresses subsequent invitation messages to that customer. If another invitation message is attempted for the same customer, the invitation message may fail with the following error: `The user you are trying to communicate with, has opted not to receive messages from you.` Send another invitation only after customer consent is re-established.
- Apple does not provide delivery or read status events for invitation messages. Webex Connect provides submission success or failure notifications.