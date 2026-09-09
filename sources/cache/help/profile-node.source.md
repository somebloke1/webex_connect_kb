The _Profile_ node enables you to manage customer profiles. The task of managing customer profiles includes creating, updating, fetching, and deleting them.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ee0f4a9-profile_node_icon.png",
        "profile_node_icon.png",
        "Screenshot of Profile Node."
      ],
      "align": "center",
      "caption": "Profile Node"
    }
  ]
}
[/block]


## Node Configuration

Use this node to perform regular CRUD operations with customer profiles on <<prodname>>. Double-click the node to configure it.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c2be3b3-Profile_Node.jpg",
        "Profile Node Node Configuration.png",
        "Screenshot of Configuring a Profile Node "
      ],
      "align": "center",
      "border": true,
      "caption": "Node Configuration"
    }
  ]
}
[/block]


## Fetch a Profile

To fetch a profile:

1. Select **Fetch profile** in the **Action** drop-down list box.
2. Select the required **Profile Type**.
   - **Customer profile** - to fetch/update/create/delete customer profiles
   - **Application profile** - for channel profile details.
3. Select the **Identifier Type** of the channel to perform the selected action on the customer profile.
4. Enter the Identifier Value for the selected identifier type. 
5. Under the **Profile Details** section, select the **Variable** that contains the **Profile Attribute** that you want to fetch from the customer profile. The profile attribute will depend on the type of profile and the channel you selected. The available profile attributes are:

[block:parameters]
{
  "data": {
    "h-0": "Profile Type",
    "h-1": "Identifier Type",
    "h-2": "Profile Attribute",
    "0-0": "Customer Profile",
    "0-1": "-",
    "0-2": "All  \ncustomerid  \nemail  \nmsisdn  \nname",
    "1-0": "Application Profile",
    "1-1": "Messenger",
    "1-2": "All  \nFB_PSID  \nbirthday  \nemail  \nfirst_name  \ngender  \nlast_name  \nlocation  \nmiddle_name  \nname  \ntimezone  \nmessage",
    "2-0": "",
    "2-1": "App ",
    "2-2": "ALL  \nIMEI  \nOS  \nModel  \nTelecom  \nIMSI  \nLocation  \nLanguage  \npushId  \nuserId  \nname  \noldlocation  \nmcc  \nmnc  \nmessage  \ntime  \nuserId  \ncustomerId  \ndeviceId  \nlast_opened  \nios_fcmpushid  \ntimezone  \nforeground  \nguest  \nstatus  \ncreated_on"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


6. Click **Add New** if you want to add more profile attributes.
7. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/25d540f-Profile_Node_Fetch_Profile.png",
        "Profile Node Fetch Profile.png",
        "Screenshot of Fetch a Profile."
      ],
      "align": "center",
      "caption": "Fetch Profile"
    }
  ]
}
[/block]


The specified customer profile is fetched. 

## Update a Profile

To update a profile:

1. Select **Update profile** in the **Action** drop-down list box.
2. Select the required **Profile Type**.
   - **Master profile** - to fetch/update/create/delete customer profiles
   - **Application profile** - for channel profile details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7dcfd13-Profile_Node_Update_Profile.png",
        "Profile Node Update Profile.png",
        "Screenshot of Update a Profile."
      ],
      "align": "center",
      "caption": "Update Profile"
    }
  ]
}
[/block]


3. Enter the **Identifier Value** that uniquely identifies the customer.
4. Under the **Profile Details** section, select the **Profile Attribute** and the **Variable** that contains the value of the selected attribute. The available profile attributes are:
   - **customerid** - use this attribute when you want to update the customer id within the customer profile
   - **email** - use this attribute when you want to update the email address of the customer within the customer profile
   - **msisdn** - use this attribute when you want to update the mobile number of the customer within the customer profile
   - **name** - use this attribute when you want to update the name of the customer within the customer profile.
5. Click **Add New** if you want to add more profile attributes.
6. Click **Save**.

The specified customer profile is updated. 

## Create a Profile

To create a profile:

1. Select **Create profile** in the **Action** drop-down list box.
2. Select the required **Profile Type**.
   - **Master profile** - to fetch/update/create/delete customer profiles
   - **Application profile** - for channel profile details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8b01ca5-Profile_Node_Create_Profile.png",
        "Profile Node Create Profile.png",
        "Screenshot of Create Profile."
      ],
      "align": "center",
      "caption": "Create Profile"
    }
  ]
}
[/block]


3. Enter the **Identifier Value** that uniquely identifies the customer.
4. Under the **Profile Details** section, select the **Profile Attribute** and the **Variable** that contains the value of the selected attribute. The available profile attributes are:
   - **customerid** - use this attribute for the customer id within the customer profile
   - **email** - use this attribute for the email address of the customer within the customer profile
   - **msisdn** - use this attribute for the mobile number of the customer within the customer profile
   - **name** - use this attribute for the name of the customer within the customer profile.
5. Click **Save**.

A customer profile with specified details is created. 

> 📘 Profile Creation
> 
> The customer profile is not created by default on <<prodname>> tenants that do not have one of - Push, Live Chat, or In-App Messaging channels enabled. Please reach out to <<prodname>> support team if you need any additional information.

## Delete a Profile

To delete a profile:

1. Select **Delete Profile** in the **Actions** drop-down list box.
2. Select the required **Profile Type**.
   - **Master profile** - to fetch/update/create/delete customer profiles
   - **Application profile** - for channel profile details.
3. Enter the **Identifier Value** that uniquely identifies the customer.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dbd444e-Profile_Node_Delete_Profile.png",
        "Profile Node Delete Profile.png",
        "Screenshot of Delete Profile."
      ],
      "align": "center",
      "caption": "Delete Profile"
    }
  ]
}
[/block]


4. Click **Save**.

The specified customer profile is deleted. 

## Input Variables

You can see a list of all the flow variables available for this node under this pane. You can also search for a variable using the Search field. For more information, see the [Variable Management](doc:variable-management) section.

## Custom Variables

You can see the list of variables that you explicitly create and configure for this node under the Custom Variables pane. For more information, see the [Variable Management](doc:variable-management) section.

## Output Variables

This node has no output variables.

## Node Outcomes

You can see the list of possible node outcomes for this node under the **Node Outcomes** pane.

| Node Edge       | Node Event/Outcome                                                                                                               |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| Success (green) | **onSuccess** - the flow exits through this node when the selected profile action is a success                                   |
| Error (red)     | **onError** - the flow exits through this node outcome when the selected profile action cannot be processed due to invalid input |

## Transition Actions

Use this tab to configure the transition actions for `On-enter`/`On-leave` events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).