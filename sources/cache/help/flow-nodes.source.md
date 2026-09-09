A _node_ is a building block for constructing flows. Node is a discrete function that executes within a flow. Nodes encapsulate an action or a decision to form the basis of a flow. Each node performs a specific function, in some cases depending on the outcome, and can decide between two or more possible paths to continue the execution.<br>

You can drag-and-drop the nodes to place them on the flow canvas. When you drag-and-drop a node, the node snaps to the canvas-grid. You can move the node to any empty space on the canvas grid, however, you cannot superimpose one node on another.<br>

You must connect all the nodes, in a logical sequence, using the connectors to form a meaningful flow. Each node has a set of configurable properties and events. Double-click any node to open the configuration window where you can configure the properties and events. Every node accepts input and provides output. Based on your requirements, you also need to configure the events that the node needs to execute.<br>

> 📘 
> 
> Please note that all flow variables are case-sensitive.

Except for the _Start_ node, all nodes have pre-defined edges. You can configure the **End Flow** settings and use a node edge to end the flow.

The nodes are classified into the following categories based on their configurable properties:

[block:parameters]
{
  "data": {
    "h-0": "Utilities",
    "h-1": "Channels",
    "h-2": "Pre-built Integrations",
    "0-0": "[Evaluate](doc:evaluate)",
    "0-1": "[Send SMS](doc:send-sms)",
    "0-2": "[IMIcampaign Profile Node](doc:campaign-profile-node)  \n  \n**Note**: You can see this node only if it has been enabled by the Admin.",
    "1-0": "[Branch](doc:branch)",
    "1-1": "RCS  \n> _ [RCS Capability Node](doc:rcs-capability-node)  \n> _ [RCS Message Node](doc:rcs-message-node)",
    "1-2": "[Create Chat](doc:create-chat)",
    "2-0": "[HTTP Request](doc:http-request)",
    "2-1": "[Push](doc:push)",
    "2-2": "Cisco Webex Contact Center Nodes  \n  \n  _ [Create Task](doc:create-task)  \n  _ [Queue Task](doc:queue-task)  \n  _ [Screen Pop](doc:screen-pop)  \n  _ [Routed Notification](doc:routed-notification)  \n  _ [Modify Notification](doc:modify-notification)  \n  _ [Close Task](doc:close-task)  \n  _ [Search Conversation](doc:search-conversation)  \n  _ [Append Conversation](doc:append-conversation)  \n  _ [Create Conversation](doc:create-conversation)  \n  _ [Add Participant](doc:add-participant)  \n  _ [Remove Participant](doc:remove-participant)  \n  _ [Close Conversation](doc:close-conversation)  \n  \\* [Update Conversation](doc:update-conversation)",
    "3-0": "[Delay](doc:delay)",
    "3-1": "[Live Chat / In-app Messaging](doc:in-app-messaging)",
    "3-2": "Cisco Contact Center Nodes  \n  \n  _ [ECE Login](doc:ece-login)  \n  _ [Search Customer](doc:search-customer)  \n  _ [Edit Customer](doc:edit-customer)  \n  _ [Entrypoint Configuration](doc:entrypoint-configuration)  \n  _ [Agent Availability](doc:agent-availability)  \n  _ [Start Conversation](doc:start-conversation)  \n  _ [Send Message](doc:send-message)  \n  _ [Process ECE Events](doc:process-ece-events)  \n  \\* [Get File Info](doc:get-file-info) ",
    "4-0": "[Data Parser](doc:data-parser)",
    "4-1": "[Email](https://help.imiconnect.io/docs/email-node)",
    "4-2": "",
    "5-0": "[Data Transform](doc:data-transform)",
    "5-1": "[Apple Messages for Business](https://help.imiconnect.io/docs/apple-messages-for-business)",
    "5-2": "",
    "6-0": "[Call Workflow](doc:call-workflow)",
    "6-1": "[Messenger](doc:messenger)",
    "6-2": "",
    "7-0": "[Page Connector](doc:page-connector)",
    "7-1": "[WhatsApp](https://help.imiconnect.io/docs/whatsapp)",
    "7-2": "",
    "8-0": "[Profile](doc:profile-node)",
    "8-1": "",
    "8-2": "",
    "9-0": "[Generate OTP](doc:generate-otp)",
    "9-1": "[Receive](doc:receive)",
    "9-2": "",
    "10-0": "[Validate OTP](doc:validate-otp)",
    "10-1": "[Send Voice](doc:voice-1)",
    "10-2": "",
    "11-0": "[Social Hour](doc:social-hour)",
    "11-1": "[Voice Node Group](doc:voice-node-group)",
    "11-2": "",
    "12-0": "[Cryptographic Hash](doc:cryptographic-hash-1)",
    "12-1": "[Play Node](doc:play-node)",
    "12-2": "",
    "13-0": "[Decryption](doc:decryption)",
    "13-1": "[Call User Node](doc:voice-call-user)",
    "13-2": "",
    "14-0": "[Encryption](doc:encryption)",
    "14-1": "[Record Node](doc:record-node)",
    "14-2": "",
    "15-0": "",
    "15-1": "[Collect Input Node](doc:collect-input-node)",
    "15-2": "",
    "16-0": "",
    "16-1": "[IVR Menu Node](doc:voice-ivr-menu)",
    "16-2": "",
    "17-0": "",
    "17-1": "[Call Patch Node](doc:call-patch-node)",
    "17-2": ""
  },
  "cols": 3,
  "rows": 18,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> You can now delete authorizations of a pre-built integration from integration as well as from the integration node configuration window. In case, any live flow uses the authorization, you will be alerted about the flows which will get affected.