# Call Transfer Node

Source: https://help.webexconnect.io/docs/call-transfer-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:58+00:00

Using the Call Transfer node, you can transfer calls to the number configured in the node. You can also configure if the call must be blind transfer or warm transfer. You can select either of these options.



![Call Transfer Node](https://files.readme.io/7adacca-Call_Transfer.png)




Following are the details about this node:

- Play Audio: If you want to configure play audio, see [Node Configuration steps](https://help.webexconnect.io/docs/play-node#section-node-configuration).
  > 📘 Note
  > 
  > The Standard Voice Type is no longer supported by Webex Connect, as Azure has deprecated it. Hence, you must make sure that all the flows with Text-to-Speech have Neural selected as Voice Type and a corresponding neural voice is selected for the opted language. Otherwise, the flow will not be processed in Webex Connect.
  > 
  > The Destination number should be in E.164 format. In case of any errors in format the node will exit through ErrorEdge.
- To Number: Configure the number to which the call must be transferred.
- Transfer Type: Blind transfer or Warm transfer.
- Blind transfer: Call will be disconnected at Webex Connect when the call starts ringing at the transferee’s end.
- Warm transfer: Call will be disconnected at Webex Connect when the transferee answers the call. If the call is not answered then the node will exit from from TransferFailed edge which can be connected to the next node. 

> 📘 Note
> 
> The Call Transfer node is available only on request. Reach out to your account manager to get it enabled for your tenant.
> 
> This feature is not available in the London and Europe regions.



![Screenshot of Call Transfer Configuration Page.](https://files.readme.io/37260a6-Call_Transfer1.png)

