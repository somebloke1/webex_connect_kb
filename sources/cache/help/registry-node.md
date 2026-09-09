# Registry Node [Deprecated]

Source: https://help.webexconnect.io/docs/registry-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:56+00:00

> 📘 Deprecation Alert
> 
> Please note that this node is being deprecated and will not be offered in the future. This decision does not impact the existing tenants that have access to and are using this node.

The Registry node enables you to set, get or delete data from your instance by referencing user key. You can set or get the data either from structured data or open format.

As part of these operations, you need to specify the store name (where the values are stored) along with the user key.

When you double-click this node, the Registry screen appears with two tabs: Configuration and Transition Actions. The Configuration tab enables you to configure the settings to get, delete, and set operations whereas the Transitions tab provides configuring the node on-enter/on-leave operations.

Here is the node image:



![Screenshot of Registry Node.](https://files.readme.io/8640330-Registry.png)




## Interface Elements



![Screenshot of Registry Node Configuration Page.](https://files.readme.io/0c1ec82-Registry_Click_the_image_to_view_it_larger.png)




Here is the description for the interface elements:



| S. No | Element | Description |
| --- | --- | --- |
| 1 | Configuration tab | Use this tab to configure the registry operations including get, delete, and set.  <br>  <br>Here is the description for the fields:  <br>  <br>**Instance Name**  <br>Use this drop-down box to specify the application from which you wish to get, delete, or set the data.  <br>  <br>**Operation**  <br>Use  this drop-down box to select get, delete, or set.  <br>  <br>**Store Name**  <br>Use this drop-down box to select the store where the values are stored.  <br>  <br>**User Key**  <br>Use this field to specify the user key corresponding to the selected store.  <br>  <br>**Structured Data and Open Format**  <br>These two options appear when the Get and Set options are selected. |
| 2 | Transition Actions tab | Use this tab to configure node on-enter/on-leave operations.  <br>  <br>Here is the description for the fields:  <br>  <br>Add action link - Click it to view the Transition action fields. |
| 3 | Input Variable | Click this collapsible panel to view the list of all the available flow variables. You can search for a variable using the Search field. You can also add a variable to the flow variables list by clicking the Add new flow variable link at the bottom of the list. |
| 4 | Output Variables | Click this collapsible panel to view the output variables. The data generated through the **Get** operation is displayed as variable here. |
| 5 | Node Outcomes | Click this collapsible panel to view the list of possible node outcomes. You can also customize the node labels by clicking the Edit icon. |




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



![Delete Button](https://files.readme.io/e6afcd5-Delete_button.jpg)




4. Finally, click the **Save** button at the bottom.  
   The transition actions are configured.