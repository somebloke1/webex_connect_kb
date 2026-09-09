# Character Sets Supported for Messaging

Source: https://help.webexconnect.io/docs/references-character-sets-supported-for-messaging
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:40+00:00

Webex Connect supports sending and receiving messages in all international language characters. In fact, through Webex Connect, you can send or receive messages that contain any character specified in UTF-8 encoding standard, across all available channels.  

In case of SMS, if your text contains only GSM-7 characters, you must send the message through GSM encoding. If it contains Unicode characters (i.e., characters outside GSM set), it should be sent as Unicode text. Please refer to the chapter  [SMS Length and Encoding](https://developers.webexconnect.io/reference/sms-length-and-encoding-copy1)  for more information on Text (GSM) vs Unicode implications and supported characters. 

> 📘 Sending emojis
> 
> While sending emojis through Send Message API v2, you can paste either the emoji as-is or the UTF8-encoded string of the emoji. Whereas while sending through Send Node, you are expected to paste the emoji as-is, i.e., UTF8-encoded string will not be converted to emoji when sent through Send Node.