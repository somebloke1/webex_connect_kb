> 📘 Note:
> 
> New Sandbox API endpoint: <https://api.us.webexconnect.io/v1/voice/calls>

> 📘 Note:
> 
> Once call is anwered by the end user ,<<prodname>> will send "answered event" to the URL configured in the API request.The client's application should send one of the following actions as response to the event.

## Actions

| Action Name | Description                                                                                                                                                                          |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Answered    | Answered action is sent from developer application to <<prodname>>, to inform <<prodname>> to answer the call                                                                        |
| Hangup      | Hangup action is sent from developer application to <<prodname>>, to inform <<prodname>> to hangup or reject  the call                                                               |
| Play        | Play action is sent from developer application to <<prodname>>, to play the provided content file or to use TTS to play the audio corresponding to the TTS text which was specified. |
| Patch       | Patch action is sent from developer application to <<prodname>>, to inform <<prodname>> to perform call patch operation.                                                             |
| Record      | Record action is sent from developer application to <<prodname>>, to inform <<prodname>>t to perform record operation.                                                               |

_All these actions have to include 200 OK as the response header._