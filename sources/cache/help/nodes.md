# Nodes

Source: https://help.webexconnect.io/docs/nodes
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:51+00:00

Each node contains specific configurable properties, which appear when you double-click that node. You can then configure those properties with appropriate data.

Once a node is configured, you can connect it to other nodes in a logical sequence using connectors and create the flow. If you delete a node in a flow, the immediate connectors attached to the node are also deleted and you need to reconstruct the flow.

## List of Nodes

The following table lists the nodes depending on the type of flow:



| Flow Nodes | Voice Flow Nodes |
| --- | --- |
| [Start](https://help.webexconnect.io/docs/start-node)  <br>[End]  <br>  <br>**Utilities**  <br>   [Evaluate](https://help.webexconnect.io/docs/evaluate-node)  <br>   [Branch](https://help.webexconnect.io/docs/branch-node)  <br>   [HTTP request](https://help.webexconnect.io/docs/http-request-node)  <br>   [Delay](https://help.webexconnect.io/docs/delay-node)  <br>   [DataParser](https://help.webexconnect.io/docs/data-parser-node)  <br>   [Data Transform](https://help.webexconnect.io/docs/data-transform-node)  <br>   [Call Workflow](https://help.webexconnect.io/docs/call-workflow-node)  <br>   [Page connector](https://help.webexconnect.io/docs/page-connector-node)  <br>   [Profile](https://help.webexconnect.io/docs/profile-node)  <br>   [Generate OTP](https://help.webexconnect.io/docs/generate-otp-node)  <br>   [Validate OTP](https://help.webexconnect.io/docs/validate-otp-node)  <br>   [SocialHour](https://help.webexconnect.io/docs/social-hour-check-node)  <br>   [Cryptographic Hash](https://help.webexconnect.io/docs/cryptographic-hash-node-configuration)  <br>   [Decryption](https://help.webexconnect.io/docs/decryption-node)  <br>   [Encryption](https://help.webexconnect.io/docs/encryption-node)  <br>  <br>**Channels**  <br>   [Send SMS](https://help.webexconnect.io/docs/sms-node)  <br>   [Push](https://help.webexconnect.io/docs/push)  <br> [RCS Capability](https://help.webexconnect.io/docs/rcs-capability-node)  <br> [RCS Message](https://help.webexconnect.io/docs/rcs-message-node)  <br>   [In-app messaging](https://help.webexconnect.io/docs/in-app-messaging)  <br>   [Email](https://help.imiconnect.io/docs/email-node)  <br>   [Messenger](https://help.webexconnect.io/docs/messenger)  <br>   [Send Voice](https://help.webexconnect.io/docs/send-voice-node)  <br>   [Apple Messages for Business](https://help.imiconnect.io/docs/apple-messages-for-business)  <br>   [WhatsApp](https://help.imiconnect.io/docs/whatsapp-node)  <br>   [Receive](https://help.webexconnect.io/docs/receive-node)  <br>   **Embedded Voice Nodes**  <br>   [Call User Node](https://help.webexconnect.io/docs/call-user-node)  <br>   [Voice Node Group](https://help.webexconnect.io/docs/voice-node-group)  <br>   [Play Node](https://help.webexconnect.io/docs/play-node)  <br>   [Record Node](https://help.webexconnect.io/docs/record-node)  <br>   [Collect Input Node](https://help.webexconnect.io/docs/collect-input-node)  <br>   [IVR Menu Node](https://help.webexconnect.io/docs/ivr-menu-node)  <br>   [Call Patch Node](https://help.webexconnect.io/docs/call-patch-node)  <br>  <br>**Integrations**  <br>   [Create Chat](https://help.webexconnect.io/docs/create-chat-node)  <br>   [Validate Chat](https://help.webexconnect.io/docs/validate-chat-node)  <br>   [Inbound Webhooks](https://help.webexconnect.io/docs/inbound-webhooks)  <br>   [Outbound Webhooks](https://help.webexconnect.io/docs/outbound-webhooks)  <br>   [Custom Events](https://help.webexconnect.io/docs/custom-events)  <br>   [Generic Bot](https://help.webexconnect.io/docs/third-party-bot)  <br>   [Custom Node](https://help.webexconnect.io/docs/custom-nodes-integration) | The voice flow nodes will be deprecated in one of the upcoming releases. Use the Embedded Voice Nodes instead of these nodes.  <br>  <br>[Start](doc:voice-start) (To be depreceated soon)  <br>[Disconnect](doc:voice-disconnect) (To be depreceated soon)  <br>  <br>**Voice nodes**  <br>   [Play](doc:voice-play) (To be depreceated soon)  <br>   [Collect Input](doc:voice-collect-input) (To be depreceated soon)  <br>   [Call URL](doc:voice-call-url) (To be depreceated soon)  <br>   [Evaluate](doc:voice-evaluate) (To be depreceated soon)  <br>   [Call Transfer](doc:voice-transfer) (To be depreceated soon)  <br>   [Dial DTMF](doc:voice-dial-dtmf) (To be depreceated soon)  <br>   [Send](doc:voice-send) (To be depreceated soon)  <br>   [Record](doc:voice-record) (To be depreceated soon)  <br>   [Call Project](doc:voice-call-project) (To be depreceated soon) |




### Adding a Node to Flow Canvas

Nodes are available in the [Node Palette](https://help.webexconnect.io/docs/flows-introduction#section-2-node-palette). Nodes are classified into different categories for easy identification based on their configurable properties. A few key points about nodes are that:

- You can drag-and-drop a node from the Node Palette onto the Flow Canvas. When dropped, the node snaps to the canvas grid.
- You can click any node on the canvas to select it. 
- You can drag a selected node to an empty position on the canvas grid and re-arrange it. However, you cannot drop it on another node.
- You can double-click any node on the canvas to bring up the Node Configuration dialog box.

## Node Configuration

The Node Configuration dialog box appears with a split-screen view.

- The main area of the dialog box is dedicated to configuration. 
- The split view on the right presents contextual information related to the node configuration.



![Screenshot of Node Configuration Page.](https://files.readme.io/c918dd3-4c5021a-Nodes.jpg)




## Configuration Area

It consists of three tabs:

1. **Configuration**: the main tab (default view) lists all the mandatory and optional fields required for configuring the node.
2. **Transition actions**: this tab lists the node transition actions, that is actions to be performed by the flow while entering/leaving this node. A transition action can be configured to run on entering a node or while exiting a node. For more information, see [Node Transition Actions](https://help.webexconnect.io/docs/transition-actions).
3. **Data Streams**: this tab lists all the data streams configured for the node.

## Contextual Information Sidebar

The sidebar presents contextual node data for use within the main configuration area. The following information is available in the node sidebar:

- **Input variables**: list of all variables available as input to this node. It lists all nodes that are directly connected to this node. You can search for variables by their name. 
- **Output variables**: list of output variables of this node. The list is updated based on the node configuration.
- **Node outcomes**: list of all possible outcomes. The outcomes can be one or more, depending on the node type and the data supplied during run-time. You can connect a node outcome to the next node or configure it to terminate the flow. You can customize the node outcome text for display on the flow canvas as the _Connector Label_.

## Connectors

You can connect any two nodes in a flow using the connectors. You can connect a node outcome to the next target node, establish a connection, and pass the control to the next node.

A node can have multiple incoming connectors. The number of outgoing connectors for a node is defined by the node outcomes.

### Drawing a Connector

1. Hover over a node and select the output edge to start drawing a connector. A connector appears when you point, hold, and drag a node outcome towards a target node. 
2. Drop the connector onto an empty space in the canvas to terminate the flow when that particular outcome is encountered. This brings up the configuration for the End Node. While trying to connect an event to the target node, the target node is highlighted.<br>  
   A dotted line appears until you connect the outcome to the next node. After the outcome is connected to the target node, the dotted line turns into a continuous line with the _Connector Label_.

> 📘 
> 
> If a node output edge has multiple outcomes mapped to it, you will be prompted to select the applicable node outcome.

The following figure illustrates the steps to draw a connector:



![Connecting Nodes in a Flow](https://files.readme.io/750702b-Connectors.jpg)




#### Restrictions

A few restrictions apply while drawing connectors:

- You must configure a node to end the flow if it does not have an outgoing edge.
- You cannot loop back to the immediate previous node.

### Deleting a Connector

To delete a connector, double-click it and select the connector, and then press the **Delete** button on the keyboard. When you delete a connector, it is removed from the flow canvas.

### Connector Colour

To easily understand the flow, the Webex Connect platform supports the color-coding of the outcomes along with the corresponding connectors to match the three-node edges. 



| Connector Colour | Indication |
| --- | --- |
| Green | Indicates the flow continuation outcome of the node  <br>For example: OnMessageSent |
| Orange | Indicates time-bound events of the node  <br>For example: OnTimeOut |
| Red | Indicates the error events of the node  <br>For example: OnDeliveryFailure |

