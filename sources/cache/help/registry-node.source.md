> 📘 Deprecation Alert
> 
> Please note that this node is being deprecated and will not be offered in the future. This decision does not impact the existing tenants that have access to and are using this node.

The Registry node enables you to set, get or delete data from your instance by referencing user key. You can set or get the data either from structured data or open format.

As part of these operations, you need to specify the store name (where the values are stored) along with the user key.

When you double-click this node, the Registry screen appears with two tabs: Configuration and Transition Actions. The Configuration tab enables you to configure the settings to get, delete, and set operations whereas the Transitions tab provides configuring the node on-enter/on-leave operations.

Here is the node image:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8640330-Registry.png",
        "Registry.png",
        "Screenshot of Registry Node."
      ],
      "align": "center",
      "caption": "Screenshot of Registry Node."
    }
  ]
}
[/block]


## Interface Elements

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0c1ec82-Registry_Click_the_image_to_view_it_larger.png",
        "Registry Click the image to view it larger.png",
        "Screenshot of Registry Node Configuration Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Registry Node Configuration Page."
    }
  ]
}
[/block]


Here is the description for the interface elements:

[block:parameters]
{
  "data": {
    "h-0": "S. No",
    "h-1": "Element",
    "h-2": "Description",
    "0-0": "1",
    "0-1": "Configuration tab",
    "0-2": "Use this tab to configure the registry operations including get, delete, and set.  \n  \nHere is the description for the fields:  \n  \n**Instance Name**  \nUse this drop-down box to specify the application from which you wish to get, delete, or set the data.  \n  \n**Operation**  \nUse  this drop-down box to select get, delete, or set.  \n  \n**Store Name**  \nUse this drop-down box to select the store where the values are stored.  \n  \n**User Key**  \nUse this field to specify the user key corresponding to the selected store.  \n  \n**Structured Data and Open Format**  \nThese two options appear when the Get and Set options are selected.",
    "1-0": "2",
    "1-1": "Transition Actions tab",
    "1-2": "Use this tab to configure node on-enter/on-leave operations.  \n  \nHere is the description for the fields:  \n  \nAdd action link - Click it to view the Transition action fields.",
    "2-0": "3",
    "2-1": "Input Variable",
    "2-2": "Click this collapsible panel to view the list of all the available flow variables. You can search for a variable using the Search field. You can also add a variable to the flow variables list by clicking the Add new flow variable link at the bottom of the list.",
    "3-0": "4",
    "3-1": "Output Variables",
    "3-2": "Click this collapsible panel to view the output variables. The data generated through the **Get** operation is displayed as variable here.",
    "4-0": "5",
    "4-1": "Node Outcomes",
    "4-2": "Click this collapsible panel to view the list of possible node outcomes. You can also customize the node labels by clicking the Edit icon."
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Configuring Registry Operations

You can get, delete, or set data in your instance by referencing the user key.

Here are the steps:

### Getting Data from a Store

1. Double click the **Registry** node.  
   The Registry screen appears. 
2. On the **Registry** screen: 

- From the **Instance** drop-down box, select the **instance** from which you wish to get the data.
- From the **Operation** drop-down box, select **Get.**
- From the **Store** drop-down box, select the **store** where the variables are stored.
- Specify the **User Key**  corresponding to the selected **store**.
- In the **Select Data Format **area, select **Structured Data** or **Open Format**. 
- If the selected option is **Structured Data**, then specify the **Variable Name** (in which the data is stored) and **Column Name**.
- Click the **Save** button at the bottom.  
  The data is fetched from the selected store and is displayed in the Output Variables collapsible panel.

### Deleting a Store

1. Double click the **Registry** node.  
   The Registry screen appears. 
2. On the **Registry** screen: 

- From the **Instance** drop-down box, select the **instance** from which you wish to delete the data.
- From the **Operation** drop-down box, select **Delete.**
- From the **Store** drop-down box, select the **store** where the variables are stored.
- Specify the **User Key**  corresponding to the selected **store**.
- Click the **Save** button at the bottom.  
  The selected store is deleted.

### Setting Data in a Store

1. Double click the **Registry** node.  
   The Registry screen appears. 
2. On the **Registry** screen: 

- From the **Instance** drop-down box, select the **instance** from which you wish to get the data.
- From the **Operation** drop-down box, select **Set.**
- From the **Store** drop-down box, select the **store** where the variables are stored.
- Specify the **User Key**  corresponding to the selected **store**.
- In the **Select Data Format **area, select **Structured Data** or **Open Format**. 
- If the selected option is **Structured Data**
- Specify the **Column Name** and **Column Value.** which is to be set.

**If the selected option is 'Structured Data'**

- Specify the **Column Name** and **Column Value.** from which the data is to be set.  
  **Note:** **Click Add New** if you need more columns.  

**If the selected option is 'Open Format'**

- In the **Data Value box,** specify the **data**, which is to be set.  
  Note: You can specify any data in any format. It gets stored in the selected store in the same format.
- Click the **Save** button at the bottom.  
  The data is set in the store.

## Configuring Transitions

As part of configuring transition actions, you can configure on-enter/on-leave operations. However, configuring these are optional.

Here are the steps:

1. On the **Registry** screen, click the **Transition Actions** tab.
2. On the **Transition Actions** tab, click **Add Action**.  
   The Transition Actions area appears.
3. On the **Transition Actions** area:

- From the **Time** drop-down box, select **On-enter** or **On-leave**. For example, On-enter.
- From the **Acton** drop-down box, select an **action** choosing from the pre-built options.

> 📘 Tip
> 
> To delete an event, click the delete button corresponding to that event. See the image below.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e6afcd5-Delete_button.jpg",
        "Delete button.jpg",
        "Screenshot of Delete Button."
      ],
      "align": "center",
      "border": true,
      "caption": "Delete Button"
    }
  ]
}
[/block]


4. Finally, click the **Save** button at the bottom.  
   The transition actions are configured.