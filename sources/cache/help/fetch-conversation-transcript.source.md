While configuring flows in the Webex Connect, you may use this node to read a conversation history. This node utilizes the **Fetch conversation** API from Webex Engage to read the respective conversation's transcript.

## Configure

To configure a Fetch conversation transcript node, follow these steps:

1. Drag and drop the **Update conversation** node from the Node palette from the left side of the screen.
2. Double-click the Update conversation node to view the configuration settings.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ce61abc786d26a73b89654fdd8775c39f7e7ba8ea11586578c6f2e88c38aa9df-image.png",
        null,
        "Screenshot displaying the Configuration Settings for Fetch conversation transcript node"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the Configuration Settings for Fetch conversation transcript node"
    }
  ]
}
[/block]


3. Choose **Fetch transcript** from the Method Name drop-down list.
4. Choose **Authorization** from the Node Runtime Authorization drop-down list.  
   We recommend you set Authorization to a Default Authentication configured in [WxEngage's Integrations](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration) screen under WxConnect's Integrations. Once you re-authenticate from the Integrations screen, all your nodes across flows will pick up the updated token.
5. In the **Conversation ID** field, enter an appropriate variable that contains WxEngage's conversation ID (e.g.$(n6.conversationId)).

**Pagination**

6. In the Offset field, enter an offset value to skip the configured number of records in the response. This is useful when parsing a paginated response and looping through this node.
7. In the Offset field, enter a limit value to control the number of records in the response. This is especially useful when parsing a paginated response and iterating through this node. The maximum value allowed for this field is 500, while the default value is 10.
8. Click **Save**.

## Output variables

| Variable            | Description                                                                                                                                        |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| `transcriptJsonEsc` | An escaped JSON payload containing array of messages                                                                                               |
| `countOfRecords`    | Refers to the total number of messages currently held against the conversation ID. Use this to fetch all records by calculating Pagination fields. |
| `status`            | Status enum - Success / Failure                                                                                                                    |
| `apiStatus`         | HTTP status code from the underlying response received from WxEngage's REST API                                                                    |
| `code`              | Numeric code received from WxEngage's API response                                                                                                 |
| `description`       | Description received from WxEngage's API response                                                                                                  |
| `responsePayload`   | Raw WxEngage's API response payload (JSON string)                                                                                                  |

## Node outcomes

| Category    | Outcome               | Description                                                                                                                                                                                                                 |
| :---------- | :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Success** | `success`             | Node execution successful                                                                                                                                                                                                   |
| **Errors**  | `onTimeout`           | Could not receive an API response from WxEngage within the agreed time-out                                                                                                                                                  |
|             | `onInvalidData`       | Invalid data configured in WxConnect node                                                                                                                                                                                   |
|             | `onError`             | Error in WxConnect's middleware services                                                                                                                                                                                    |
|             | `onInvalidChoice`     | Invalid choice                                                                                                                                                                                                              |
|             | `onauthorizationfail` | Failed to Authorize successfully. We recommend you to recheck your Node Authorization configurations in the [Authorize Integration](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration)  section |
|             | `Failure`             | Any other run time failures                                                                                                                                                                                                 |