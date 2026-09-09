You need to configure the callback URL from the Numbers sections, so that an incoming call to you asset will be notified to your application. 

Here is the [link](https://help.imiconnect.io/docs/phone-numbers#handle-incoming-calls-via-callback-url)

**Sample Incoming Payload**:

```json
{
  "event": "ACCEPTED",
  "callerId": "+4475XXXXXXXX",
  "dialedNumber": "+4474XXXXXXXX",
  "offeredTime": "2023-04-25T05:14:50.178Z",
  "eventTime": "2023-04-25T05:14:52.031Z",
  "sessionId": "c51e56af-0c71-4917-98dd-53d299012e46"
}
```

To answer the call, you must respond to the above mentioned event with the following action:

```json
{
  "action": "ANSWER"
}
```

> 📘 Note:
> 
> Once answered, you can send the actions (Play, Record, Call patch and Hangup) based on your use-case or flow.