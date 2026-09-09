# Fetch Team's working hours - WxEngage standalone

Source: https://help.webexconnect.io/docs/fetch-teams-working-hours
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:29+00:00

While configuring flows in Webex Connect, you may use this node to append a message to an ongoing conversation with the end customer. This node utilizes the **Fetch team's working hours** API from Webex Engage.

## Configuration

To configure a Fetch team's working hours conversation node, follow these steps:

1. Drag and drop the **Fetch team working hours** node from the Node palette from the left side of the screen.
2. Double-click the Fetch team working hours node to view the configuration settings.



![Screenshot displaying the Configuration Settings for Fetch team working hours node](https://files.readme.io/0f674d2e2e106e279570d76fc0a772ed8de301edfc4edf6596cc766924f70293-image.png)




3. Choose **Fetch conversation** from the Method Name drop-down list.
4. Choose **Authorization** from the Node Runtime Authorization drop-down list.  
   We recommend you set Authorization to a Default Authentication configured in [WxEngage's Integrations](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration) screen under WxConnect's Integrations. Once you re-authenticate from the Integrations screen, all your nodes across flows will pick up the updated token.
5. Choose the team from the **Team Name** drop-down for which you need to fetch the working hours.
6. Click **Save**.

## Output variables

| Variable          | Description                                                                     |
| :---------------- | :------------------------------------------------------------------------------ |
| `inWorkingHours`  | Whether the team is working or not. Boolean value                               |
| `oooResponse`     | The out-of-office response configured for the team                              |
| `timezone`        | Timezone of the team                                                            |
| `status`          | Status enum - Success / Failed                                                  |
| `apiStatus`       | HTTP status code from the underlying response received from WxEngage's REST API |
| `description`     | Description received from WxEngage's API response                               |
| `responsePayload` | The actual payload of the API response                                          |

## Node outcomes

| Category    | Outcome               | Description                                                                                                                                                                                |
| :---------- | :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Success** | `Success`             | Node execution successful                                                                                                                                                                  |
| **Errors**  | `onTimeout`           | Could not receive an API response from WxEngage within the agreed time-out                                                                                                                 |
|             | `onInvalidData`       | Invalid data configured in WxConnect node                                                                                                                                                  |
|             | `onError`             | Error in WxConnect's middleware services                                                                                                                                                   |
|             | `onInvalidChoice`     | Invalid choice                                                                                                                                                                             |
|             | `onauthorizationfail` | Failed to Authorize successfully. Recommend to recheck Auth details in the [Authorize Integration](https://dash.readme.com/project/imiconnect1/v6.8.0/docs/authorize-integration)  section |
|             | `Failure`             | Any other run time failures                                                                                                                                                                |