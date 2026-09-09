# Node Palette - WxEngage standalone

Source: https://help.webexconnect.io/docs/node-palette
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:29+00:00

As part of WxEngage's Live Agent Integration, the following nodes are exposed:



| Node category | Node | Description |
| --- | --- | --- |
| **Message resolution** | Search conversation | This node enables you to resolve a customer's inbound message by searching for an existing conversation based on the customer's address and the associated channel asset on the business end. You can use this node to resolve an incoming message in the following ways:  <br>  <br>- When you need to create a new conversation<br>- When you want to appened a message to an exisitng conversation |
|  | Create conversation | This node enables the creation of a new conversation by providing the customer's identity (specific to the relevant channel), the business channel asset details, the message object, and custom fields (optional). |
|  | Append message | This node enables you to append a message, whether inbound or outbound, sent via BOTs or automated journeys within WxConnect's Flow or an announcement made by a contact-centre user to an existing conversation. |
|  | Update conversation | This node enables you to update an existing conversation's external reference identifier (Alias ID) or update custom fields on this conversation. |
|  | Hold conversation | This node enables you to pause a conversation. |
|  | Close conversation | This node enables you to end a conversation. |
|  | Reopen conversation | This node enables you to re-open a conversation. |
| **Routing conversations** | Fetch team working hours | This node enables you to fetch a specific team's working hours and the out-of-office message configured by the Administrator. |
|  | Transfer conversation | This node enables you to transfer a conversation to a Team or Skill queue. |
| **Utility nodes** | Fetch conversation transcript | This node enables you to fetch the conversation transcript containing messages exchanged between the business user and the end customer using the provided Conversation ID. |

