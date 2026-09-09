Each node contains specific configurable properties, which appear when you double-click that node. You can then configure those properties with appropriate data.

Once a node is configured, you can connect it to other nodes in a logical sequence using connectors and create the flow. If you delete a node in a flow, the immediate connectors attached to the node are also deleted and you need to reconstruct the flow.

## List of Nodes

The following table lists the nodes depending on the type of flow:

[block:parameters]
{
  "data": {
    "h-0": "Flow Nodes",
    "h-1": "Voice Flow Nodes",
    "0-0": "[Start](doc:start-node)  \n[End]  \n  \n**Utilities**  \n   [Evaluate](doc:evaluate)  \n   [Branch](doc:branch)  \n   [HTTP request](doc:http-request)  \n   [Delay](doc:delay)  \n   [DataParser](doc:data-parser)  \n   [Data Transform](doc:data-transform)  \n   [Call Workflow](doc:call-workflow)  \n   [Page connector](doc:page-connector)  \n   [Profile](doc:profile-node)  \n   [Generate OTP](doc:generate-otp)  \n   [Validate OTP](doc:validate-otp)  \n   [SocialHour](doc:social-hour)  \n   [Cryptographic Hash](doc:cryptographic-hash-1)  \n   [Decryption](doc:decryption)  \n   [Encryption](doc:encryption)  \n  \n**Channels**  \n   [Send SMS](doc:send-sms)  \n   [Push](doc:push)  \n [RCS Capability](doc:rcs-capability-node)  \n [RCS Message](doc:rcs-message-node)  \n   [In-app messaging](doc:in-app-messaging)  \n   [Email](https://help.imiconnect.io/docs/email-node)  \n   [Messenger](doc:messenger)  \n   [Send Voice](doc:voice-1)  \n   [Apple Messages for Business](https://help.imiconnect.io/docs/apple-messages-for-business)  \n   [WhatsApp](https://help.imiconnect.io/docs/whatsapp-node)  \n   [Receive](doc:receive)  \n   **Embedded Voice Nodes**  \n   [Call User Node](doc:voice-call-user)  \n   [Voice Node Group](doc:voice-node-group)  \n   [Play Node](doc:play-node)  \n   [Record Node](doc:record-node)  \n   [Collect Input Node](doc:collect-input-node)  \n   [IVR Menu Node](doc:voice-ivr-menu)  \n   [Call Patch Node](doc:call-patch-node)  \n  \n**Integrations**  \n   [Create Chat](doc:create-chat)  \n   [Validate Chat](doc:validate-chat)  \n   [Inbound Webhooks](doc:inbound-webhooks)  \n   [Outbound Webhooks](doc:outbound-webhooks)  \n   [Custom Events](doc:custom-events)  \n   [Generic Bot](doc:generic-bot)  \n   [Custom Node](doc:custom-nodes)",
    "0-1": "The voice flow nodes will be deprecated in one of the upcoming releases. Use the Embedded Voice Nodes instead of these nodes.  \n  \n[Start](doc:voice-start) (To be depreceated soon)  \n[Disconnect](doc:voice-disconnect) (To be depreceated soon)  \n  \n**Voice nodes**  \n   [Play](doc:voice-play) (To be depreceated soon)  \n   [Collect Input](doc:voice-collect-input) (To be depreceated soon)  \n   [Call URL](doc:voice-call-url) (To be depreceated soon)  \n   [Evaluate](doc:voice-evaluate) (To be depreceated soon)  \n   [Call Transfer](doc:voice-transfer) (To be depreceated soon)  \n   [Dial DTMF](doc:voice-dial-dtmf) (To be depreceated soon)  \n   [Send](doc:voice-send) (To be depreceated soon)  \n   [Record](doc:voice-record) (To be depreceated soon)  \n   [Call Project](doc:voice-call-project) (To be depreceated soon)"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### Adding a Node to Flow Canvas

Nodes are available in the [Node Palette](doc:flows#section-2-node-palette). Nodes are classified into different categories for easy identification based on their configurable properties. A few key points about nodes are that:

- You can drag-and-drop a node from the Node Palette onto the Flow Canvas. When dropped, the node snaps to the canvas grid.
- You can click any node on the canvas to select it. 
- You can drag a selected node to an empty position on the canvas grid and re-arrange it. However, you cannot drop it on another node.
- You can double-click any node on the canvas to bring up the Node Configuration dialog box.

## Node Configuration

The Node Configuration dialog box appears with a split-screen view.

- The main area of the dialog box is dedicated to configuration. 
- The split view on the right presents contextual information related to the node configuration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c918dd3-4c5021a-Nodes.jpg",
        "receive_node_split_view.png",
        "Screenshot of Node Configuration Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Node Configuration Page."
    }
  ]
}
[/block]


## Configuration Area

It consists of three tabs:

1. **Configuration**: the main tab (default view) lists all the mandatory and optional fields required for configuring the node.
2. **Transition actions**: this tab lists the node transition actions, that is actions to be performed by the flow while entering/leaving this node. A transition action can be configured to run on entering a node or while exiting a node. For more information, see [Node Transition Actions](doc:transition-actions).
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

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/750702b-Connectors.jpg",
        "Connectors.jpg",
        "Screenshot of Connecting Nodes in a Flow."
      ],
      "align": "center",
      "border": true,
      "caption": "Connecting Nodes in a Flow"
    }
  ]
}
[/block]


#### Restrictions

A few restrictions apply while drawing connectors:

- You must configure a node to end the flow if it does not have an outgoing edge.
- You cannot loop back to the immediate previous node.

### Deleting a Connector

To delete a connector, double-click it and select the connector, and then press the **Delete** button on the keyboard. When you delete a connector, it is removed from the flow canvas.

### Connector Colour

To easily understand the flow, the <<prodname>> platform supports the color-coding of the outcomes along with the corresponding connectors to match the three-node edges. 

[block:parameters]
{
  "data": {
    "h-0": "Connector Colour",
    "h-1": "Indication",
    "0-0": "Green",
    "0-1": "Indicates the flow continuation outcome of the node  \nFor example: OnMessageSent",
    "1-0": "Orange",
    "1-1": "Indicates time-bound events of the node  \nFor example: OnTimeOut",
    "2-0": "Red",
    "2-1": "Indicates the error events of the node  \nFor example: OnDeliveryFailure"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]