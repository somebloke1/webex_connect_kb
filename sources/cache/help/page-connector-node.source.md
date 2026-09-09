When you use <<prodname>> for orchestrating a sophisticated, multi-step, multi-branch flow, you may have certain operations that may be needed across various branches. For example, if you configure a self-service automation flow using Carousels in Facebook Messenger or RCS Business Messaging, wherein each card provides customers with a different start point (e.g., booking a flight ticket, canceling a flight ticket, web check-in, etc.) at some point you may want to provide the customer with an option to get connected with an agent.

In such cases, while you can repeat the node sequence for transferring a conversation to an agent, you can reduce the configuration effort and modularise your flow by configuring this node sequence on a separate page, and then connecting it with relevant points in your overall flow using the Page Connector node. Typically the flow canvas loading starts to slow down once you have more than 200 nodes on the flow designer canvas.

Page Connector node allows you to connect flows that are split across multiple pages within the flow builder canvas.

## Creating a Page to modularize reusable parts

Click on the '+' symbol next to the main flow tab on the top right corner of the flow builder canvas. Provide the contextual name for the flow part that you modularize. For example, escalate a conversation to an agent. Click 'OK'. The new page tab will be created to the left side of the existing pages. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/05eafe1-Page_Connector_Creating_a_Page_for_modularizing_a_Reusable_Node_Sequence_in_a_Flow.png",
        "Page Connector Creating a Page for modularizing a Reusable Node Sequence in a Flow.png",
        "Screenshot of Creating a Page for Modularizing a Reusable Node Sequence in a Flow."
      ],
      "align": "center",
      "caption": "Creating a Page for Modularizing a Reusable Node Sequence in a Flow"
    }
  ]
}
[/block]


Once the new page has been created, configure the node sequence that you want to use at various stages within the overall flow.

### Using Page Connector Node

Drag-drop a Page Connector node on the canvas and double-click the node to open for configuration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/74e8c41-Page_Connector_-_Using_Page_Connector_Mode.png",
        "Page Connector - Using Page Connector Mode.png",
        "Screenshot of Page Connector Node Configuration Page."
      ],
      "align": "center",
      "caption": "Page Connector Node Configuration Page."
    }
  ]
}
[/block]


From the drop-down, either create a new page or select an existing page to connect the flow with the flow on the selected page and then click **Save**.  The Page Connector node becomes the source node and any new node that is added must have connectivity from the Page Connector node. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5245e92-Page_Connector_Node.png",
        "Page Connector Node.png",
        "Screenshot of Using Page Connector Node in the main flow."
      ],
      "align": "center",
      "border": true,
      "caption": "Using Page Connector Node in the main flow"
    }
  ]
}
[/block]


> 📘 
> 
> You must connect the Page Connector node to the target node. Otherwise, the flow may not execute properly.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/62e90a0-Configuring_Page_Connector_Node.png",
        "Configuring Page Connector Node.png",
        "Screenshot of Connections with the Modularized Flow Segment."
      ],
      "align": "center",
      "border": true,
      "caption": "Connections with the Modularized Flow Segment"
    }
  ]
}
[/block]


> 📘 Variable Management when using Page Connector Node
> 
> Flow variables aren't automatically shared across pages. You can use custom variables to selectively share the relevant variables across various pages.