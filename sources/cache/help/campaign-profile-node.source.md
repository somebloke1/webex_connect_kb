The _<<Webex Campaign>> Profile_ node enables you to manage any profile of selected <<imicampaign>>  accounts, which includes creating, updating, fetching, and deleting them.

> 📘 Note:
> 
> This node is available in Node Palette only if it has been provisioned for you.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/39490e9-campaign_profile_node.png",
        "campaign_profile_node.png",
        "Screenshot of Webex Campaign Profile Node."
      ],
      "align": "center",
      "sizing": "smart",
      "caption": "<<Webex Campaign>> Profile Node"
    }
  ]
}
[/block]


## Manage Customer Profiles

Use this node to perform regular CRUD operations with profiles directly on <<imicampaign>> from <<prodname>>. Double-click the node to configure it.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7bf3384-node_configuration.png",
        "node_configuration.png",
        "Screenshot of Profile Node Configuration Page."
      ],
      "align": "center",
      "caption": "Node Configuration"
    }
  ]
}
[/block]


## Fetch a Profile##

To fetch a profile:

1. Select **Fetch Profile** in the **Actions** drop-down list box.
2. Select the required **Profile**. The **Profile** corresponds to an account on <<imicampaign>>.
3. Select the **Group** to which the selected profile belongs.
4. Enter a **Primary Key** that uniquely identifies the selected profile.
5. Click **Save**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/eb9fe0a-fetch_profile.png",
        "fetch_profile.png",
        "Screenshot of Fetch a Profile."
      ],
      "align": "center",
      "caption": "Fetch Profile"
    }
  ]
}
[/block]


The specified customer profile is fetched. 

## Update a Profile##

To update a profile:

1. Select **Update Profile** in the **Actions** drop-down list box.
2. Select the required **Profile**. The **Profile** corresponds to an account on <<imicampaign>> .

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0cbc316-update_profile.png",
        "update_profile.png",
        "Screenshot of Update a Profile"
      ],
      "align": "center",
      "caption": "Update Profile"
    }
  ]
}
[/block]


3. Select the **Group** to which the selected profile belongs.
4. Enter a **Primary Key** that uniquely identifies the selected profile.
5. Select the **Attribute** that you want to update. The available attributes are:
   - **MSISDN** - the mobile number of the customer
   - **Email** - the email address of the customer
   - **Country** - the country of residence of the customer.
6. Enter a **Value** for the selected attribute.
7. Click **Add Attribute** if you want to add other attributes and repeat steps 5 and 6.
8. Click **Save**.

The specified customer profile is updated. 

## Create a Profile##

To update a profile:

1. Select **Create Profile** in the **Actions** drop-down list box.
2. Select the required **Profile**. The **Profile** corresponds to an account on <<imicampaign>>.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/293f8d4-create_profile.png",
        "create_profile.png",
        "Screenshot of Create Profile"
      ],
      "align": "center",
      "caption": "Create Profile"
    }
  ]
}
[/block]


3. Select the **Group** to which the selected profile belongs.
4. Enter a **Primary Key** that uniquely identifies the selected profile.
5. Select the **Attribute** that you want to update. The available attributes are:
   - **MSISDN** - the mobile number of the customer
   - **Email** - the email address of the customer
   - **Country** - the country of residence of the customer.
6. Enter a **Value** for the selected attribute.
7. Click **Add Attribute** if you want to add other attributes and repeat steps 5 and 6.
8. Click **Save**.

A customer profile with specified details is created. 

## Delete a Profile##

To delete a profile:

1. Select **Fetch Profile** in the **Actions** drop-down list box.
2. Select the required **Profile**. The **Profile** corresponds to an account on <<imicampaign>>.
3. Enter a **Primary Key** that uniquely identifies the selected profile.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1d90f4e-delete_profile.png",
        "delete_profile.png",
        "Screenshot of Delete Profile"
      ],
      "align": "center",
      "caption": "Delete Profile"
    }
  ]
}
[/block]


4. Click **Save**.

The specified customer profile is deleted. 

## Node Outcomes

You can see the list of possible node outcomes for this node under the **Node Outcomes** pane.

| Node Edge       | Node Event/Outcome                                                            |
| :-------------- | :---------------------------------------------------------------------------- |
| Success (green) | **onSuccess** - the flow exits through this node when it is a success         |
| Error (red)     | **onError** - the flow exits through this node outcome when there is an error |

## Transition Actions

Use this tab to configure the transition actions for `On-enter`/`On-leave` events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).