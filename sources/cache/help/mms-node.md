# MMS Node

Source: https://help.webexconnect.io/docs/mms-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:52+00:00

The MMS node enables you to send messages to customers through the MMS channel that are configured within a service. You can send multimedia messages up to 4096 characters with a 80 char limit for Message Subjects using a combination of pictures, video, and audio files.



![MMS Node](https://files.readme.io/85b6204-image.png)




## Node Configuration

Drag and drop the MMS node on the flow canvas. Double-click the node to configure it.



![MMS Node](https://files.readme.io/70ab795-1.png)




## Node Configuration - Common fields for all message types

To configure the MMS node:

1. Select one of the following for **Destination Type**. 
   1. **Customer Id** - is a master ID that is linked to all different channel-specific user IDs of a user. It is useful in cross channel communication. For example, you want to send an exclusive promo code to a user’s app because of previous positive feedback that they have given via Messenger. In that case, you can use the Customer Id of the user since it remains constant across the channels.
   2. **msisdn** - Mobile Station International Subscriber Directory Number (MSISDN) is a number used to identify a mobile phone number internationally.
2. Enter the **Destination** value. This field contains the destination value corresponding to the selected Destination Type. The value can be static or dynamic. For example, if the destination type is CustomerID, the destination can be dynamic by declaring it as $(customerID). Likewise, if the destination type is msisdn, the destination can be dynamic by declaring it as $(phoneNumber).
3. Select number or sender ID that is used to send the MMS from the **From Number** field. The node supports short codes, long codes, and AlphaSender IDs. The only restrictions are the ones placed by the country network operators, which can vary.
4. Enter the text in the MMS Message field to be sent to the customer. It supports up to 80 characters, including unicode.
5. Select one of the following from the Media Type dropdown. You can add up to 9 Media types.
   - Audio
   - Video
   - Image
   - Text
   - PDF
   - Calendar
   - Contact
6. Enter the **MMS Slide Media URL**. The URL can be public.
7. Enter the text in the **Message** field. The message should not be longer than 4096 characters.
8. (Optional) In the **Correlation ID** field, enter the unique reference ID to be passed back to you in delivery receipts for this transaction.
9. (Optional) In the **Notify URL** field, enter the URL where you can receive delivery receipts for this transaction. 
10. (Optional) In the **Callback Data** field, enter any additional data that needs to be posted to the Notify URL. 
11. (Optional) **Advanced Options**
    1. **Wait For**: Select the event to wait for on this node. The available options are None, Gateway Submit, Delivery Report, and Read. In case of timeout, the node will exit regardless of the configured Wait For option.
       - **None**: The default option, exits the node immediately after executing the Send action.
       - **Gateway Submit**: Exits the node upon submitting the message.
       - **Delivery Report**: Waits until receiving the delivery receipt for the message sent.
       - **Read**: Waits until the customer has read the message.
    2. **Time Out**: Maximum time in seconds until which the node should wait for one of the 'Wait for' conditions to be met. The node exits via the 'onDeliveryReportFail' node outcome edge when the set time elapses.
    3. **Expiry**: Select the message expiry format. The available options are UTC and Seconds.
       - **Expiry Date And Time**: If you selected UTC, enter the message expiry date and time in YYYY-MM-DDTHH:MM:SS format. For example, if the value is set to 2019-23-04T03:06:48, the message is terminated if a send attempt is made beyond the set time.
       - **Expiry Time**: If you selected Seconds, enter the maximum time in seconds within which the message must be submitted.
12. Click **Save**.

## Notify URL

You can choose to notify a URL with the delivery report for your preferred channel. This field accepts only a valid URL or a variable. If an invalid URL is passed in an API request or via a variable, then such a request will not be considered eligible for retries.

**Validations for Notify URL field:**

- It is an optional field for all the channels. Send node can be executed without including these values.
- The notify URL should be updated with the proper URL format. The system returns the error message when the Notify URL field is not updated correctly as ‘Invalid URL: field accepts only valid URL or variable.’
- When you provide a space in front of the URL, the system displays the 'Invalid URL: field accepts only valid URLs or variables' error message.
- When you provide space at the end of the URL, the system trims and ignores the space, and the URL receives delivery receipts (DRs).
- Select the **Enable Notify URL Auth** checkbox to activate the authentication of the notify URL.
- There is no maximum length validation defined for this field.
- Variables can be added to this field.

> 📘 Note:
> 
> Notify URLs track the status of delivery receipts (DRs) for sent messages.
> 
> If Enable Notify URL Auth is enabled for your node and an Auth ID that is random, invalid, or deleted is used, the payload will be parked in Webex Connect and not forwarded to the receiver's server. However, this does not impact the delivery of the message.
> 
> If Enable Notify URL Auth is not enabled, the payload is forwarded to the receiver's server regardless of any invalid Auth ID used.