# Profile Node

Source: https://help.webexconnect.io/docs/profile-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:56+00:00

The _Profile_ node enables you to manage customer profiles. The task of managing customer profiles includes creating, updating, fetching, and deleting them.



![Profile Node](https://files.readme.io/ee0f4a9-profile_node_icon.png)




## Node Configuration

Use this node to perform regular CRUD operations with customer profiles on Webex Connect. Double-click the node to configure it.



![Node Configuration](https://files.readme.io/c2be3b3-Profile_Node.jpg)




## Fetch a Profile

To fetch a profile:

1. Select **Fetch profile** in the **Action** drop-down list box.
2. Select the required **Profile Type**.
   - **Customer profile** - to fetch/update/create/delete customer profiles
   - **Application profile** - for channel profile details.
3. Select the **Identifier Type** of the channel to perform the selected action on the customer profile.
4. Enter the Identifier Value for the selected identifier type. 
5. Under the **Profile Details** section, select the **Variable** that contains the **Profile Attribute** that you want to fetch from the customer profile. The profile attribute will depend on the type of profile and the channel you selected. The available profile attributes are:



| Profile Type | Identifier Type | Profile Attribute |
| --- | --- | --- |
| Customer Profile | - | All  <br>customerid  <br>email  <br>msisdn  <br>name |
| Application Profile | Messenger | All  <br>FB_PSID  <br>birthday  <br>email  <br>first_name  <br>gender  <br>last_name  <br>location  <br>middle_name  <br>name  <br>timezone  <br>message |
|  | App  | ALL  <br>IMEI  <br>OS  <br>Model  <br>Telecom  <br>IMSI  <br>Location  <br>Language  <br>pushId  <br>userId  <br>name  <br>oldlocation  <br>mcc  <br>mnc  <br>message  <br>time  <br>userId  <br>customerId  <br>deviceId  <br>last_opened  <br>ios_fcmpushid  <br>timezone  <br>foreground  <br>guest  <br>status  <br>created_on |




6. Click **Add New** if you want to add more profile attributes.
7. Click **Save**.



![Fetch Profile](https://files.readme.io/25d540f-Profile_Node_Fetch_Profile.png)




The specified customer profile is fetched. 

## Update a Profile

To update a profile:

1. Select **Update profile** in the **Action** drop-down list box.
2. Select the required **Profile Type**.
   - **Master profile** - to fetch/update/create/delete customer profiles
   - **Application profile** - for channel profile details.



![Update Profile](https://files.readme.io/7dcfd13-Profile_Node_Update_Profile.png)




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



![Create Profile](https://files.readme.io/8b01ca5-Profile_Node_Create_Profile.png)




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
> The customer profile is not created by default on Webex Connect tenants that do not have one of - Push, Live Chat, or In-App Messaging channels enabled. Please reach out to Webex Connect support team if you need any additional information.

## Delete a Profile

To delete a profile:

1. Select **Delete Profile** in the **Actions** drop-down list box.
2. Select the required **Profile Type**.
   - **Master profile** - to fetch/update/create/delete customer profiles
   - **Application profile** - for channel profile details.
3. Enter the **Identifier Value** that uniquely identifies the customer.



![Delete Profile](https://files.readme.io/dbd444e-Profile_Node_Delete_Profile.png)




4. Click **Save**.

The specified customer profile is deleted. 

## Input Variables

You can see a list of all the flow variables available for this node under this pane. You can also search for a variable using the Search field. For more information, see the [Variable Management](https://help.webexconnect.io/docs/variable-management-in-flows) section.

## Custom Variables

You can see the list of variables that you explicitly create and configure for this node under the Custom Variables pane. For more information, see the [Variable Management](https://help.webexconnect.io/docs/variable-management-in-flows) section.

## Output Variables

This node has no output variables.

## Node Outcomes

You can see the list of possible node outcomes for this node under the **Node Outcomes** pane.

| Node Edge       | Node Event/Outcome                                                                                                               |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| Success (green) | **onSuccess** - the flow exits through this node when the selected profile action is a success                                   |
| Error (red)     | **onError** - the flow exits through this node outcome when the selected profile action cannot be processed due to invalid input |

## Transition Actions

Use this tab to configure the transition actions for `On-enter`/`On-leave` events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](https://help.webexconnect.io/docs/transition-actions).