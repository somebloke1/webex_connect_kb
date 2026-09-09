The <<prodname>> integration with <<WCamp>> allows you to send messages or configure campaign instances within the application. The purpose of the integration is to provide reports for the messages sent and received for <<WCamp>> via the <<prodname>> application. 

A workflow should first be configured in <<prodname>> for the digital channels WhatsApp and RCS after which they will be displayed in the drop-menu as options while configuring in the <<prodname>>Campaign application. <<WCamp>> should be selected during configuration in the Send and Receive nodes of <<prodname>> for the live messaging status to be received in reports. 

## Prerequisites

- You must have a tenant for the <<WCamp>> application.
- You must have <<WCamp>> integration enabled for your <<prodname>> tenant.

### Viewing <<WCamp>> tenant information in <<prodname>>

1. Login to the <<prodname>> platform.
2. Navigate to **Assets** > **Integrations**.
3. In the search bar, search for **<<WCamp>>**.  
   You will be able to view the services where the node is used as the last entry.
4. Under **Actions**, click **Manage**.  
   In the **Manage Integration** - **Data Streams** page, under Data Streams, you should be able to view <<WCamp>>.

> 📘 Note
> 
> The <<WCamp>> node is a pre-authorized node. Access to the application is directly provided in <<prodname>> if the tenant is enabled.

### Integrating <<WCamp>> in <<prodname>> Flows

1. Login to the <<prodname>> platform.
2. In the Flow Builder, create a flow.
3. In the **Configure Webhook** node > Data Stream (Optional) tab, click **Add Data Stream**.

> 📘 Note
> 
> This tab is displayed only when the <<WCamp>> Data Stream is enabled for your tenant.

4. In the **Choose Integration** drop-down menu, select **<<WCamp>>**.
5. In the **Parameter Name **as** campCorrelationId**,  and its input for** Value as $(unique_id)**.  
   **Parameter Name **as** deploydate**,  and its input for** Value as $(deploydate)**.  
   **Parameter Name **as** deploymentId**,  and its input for** Value as $(deploymentId)**.  
   **Parameter Name **as** wfUserId**,  and its input for** Value as $(userId)**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fa6427d-image001.png",
        "",
        "Screenshot of Configuring the Webhook"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the Webhook"
    }
  ]
}
[/block]


6. Click **Save**.

> 📘 Note
> 
> Whenever a message is sent/received through the WhatsApp node, the data is shared for <<WCamp>> through the Webex Data Stream. If there are multiple send and receive WhatsApp nodes, then <<WCamp>> should be selected in the Data Stream for every node. The flows are displayed in <<WCamp>> only when they are made live. Draft flows are not displayed. The channels supported for Data Stream integration for <<WCamp>> are WhatsApp and RCS.

### Making a Flow Live

When you create a flow and click the **Make Live** button, the Make Live Configuration window is displayed. Under App Selection, for Application, select an option from the drop-down menu.

> 📘 Note
> 
> When the Data Stream option is enabled while configuring the nodes for <<WCamp>>, the Data Stream option should not be selected while configuring assets under Apps. Doing this will create duplication in shared reports.