# Webex Campaign Integration with Webex Connect

Source: https://help.webexconnect.io/docs/webex-campaign-integration-with-webex-connect
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:31+00:00

The Webex Connect integration with Webex Campaign allows you to send messages or configure campaign instances within the application. The purpose of the integration is to provide reports for the messages sent and received for Webex Campaign via the Webex Connect application. 

A workflow should first be configured in Webex Connect for the digital channels WhatsApp and RCS after which they will be displayed in the drop-menu as options while configuring in the Webex ConnectCampaign application. Webex Campaign should be selected during configuration in the Send and Receive nodes of Webex Connect for the live messaging status to be received in reports. 

## Prerequisites

- You must have a tenant for the Webex Campaign application.
- You must have Webex Campaign integration enabled for your Webex Connect tenant.

### Viewing Webex Campaign tenant information in Webex Connect

1. Login to the Webex Connect platform.
2. Navigate to **Assets** > **Integrations**.
3. In the search bar, search for **Webex Campaign**.  
   You will be able to view the services where the node is used as the last entry.
4. Under **Actions**, click **Manage**.  
   In the **Manage Integration** - **Data Streams** page, under Data Streams, you should be able to view Webex Campaign.

> 📘 Note
> 
> The Webex Campaign node is a pre-authorized node. Access to the application is directly provided in Webex Connect if the tenant is enabled.

### Integrating Webex Campaign in Webex Connect Flows

1. Login to the Webex Connect platform.
2. In the Flow Builder, create a flow.
3. In the **Configure Webhook** node > Data Stream (Optional) tab, click **Add Data Stream**.

> 📘 Note
> 
> This tab is displayed only when the Webex Campaign Data Stream is enabled for your tenant.

4. In the **Choose Integration** drop-down menu, select **Webex Campaign**.
5. In the **Parameter Name **as** campCorrelationId**,  and its input for** Value as $(unique_id)**.  
   **Parameter Name **as** deploydate**,  and its input for** Value as $(deploydate)**.  
   **Parameter Name **as** deploymentId**,  and its input for** Value as $(deploymentId)**.  
   **Parameter Name **as** wfUserId**,  and its input for** Value as $(userId)**.



![Screenshot of Configuring the Webhook](https://files.readme.io/fa6427d-image001.png)




6. Click **Save**.

> 📘 Note
> 
> Whenever a message is sent/received through the WhatsApp node, the data is shared for Webex Campaign through the Webex Data Stream. If there are multiple send and receive WhatsApp nodes, then Webex Campaign should be selected in the Data Stream for every node. The flows are displayed in Webex Campaign only when they are made live. Draft flows are not displayed. The channels supported for Data Stream integration for Webex Campaign are WhatsApp and RCS.

### Making a Flow Live

When you create a flow and click the **Make Live** button, the Make Live Configuration window is displayed. Under App Selection, for Application, select an option from the drop-down menu.

> 📘 Note
> 
> When the Data Stream option is enabled while configuring the nodes for Webex Campaign, the Data Stream option should not be selected while configuring assets under Apps. Doing this will create duplication in shared reports.