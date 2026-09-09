# Agile CRM

Source: https://help.webexconnect.io/docs/agile-crm-create-get-delete-update
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:07+00:00

## Introduction

Agile CRM (Customer Relationship Management) is an All-in-One CRM with Sales, Service automation, and Marketing in a single platform.

Webex Connect offers a pre-built integration node for Agile CRM to make it easier for you to create, view, delete, and/or update tickets and contacts in your Agile CRM account. 

This node needs to be enabled for your account and is not available by default. Please contact your account manager in case you wish to enable it for your account. 



![Screenshot of Agile CRMs Node](https://files.readme.io/957bad6-image.png)




## Version Supported

Please note that the latest version of the Agile CRM integration node that you should use is v1.7.

## Pre-requisites

To enable Agile CRM node: 

- Agile CRM node needs to be enabled for your Webex Connect tenant and is not available by default. Please contact your account manager in case you wish to enable it for your account.

- Tenant needs an account with Agile CRM.

- This integration is available only in the cloud version of Webex Connect.

## Node Configuration

Drag-and-drop the node on to the visual flow builder and double-click the node to configure it.

1. Select the required **Method Name** from the drop-down list box. The following methods are supported currently: 

   - [Create a ticket](https://help.imiconnect.io/docs/agile-crm-1#method-name---create-a-ticket)- Allows to create a ticket using the requester email ID .
   - [Get all tickets](https://help.imiconnect.io/docs/agile-crm-1#method-name---get-all-ticket)- Allows to retrieve all the tickets with the unique identification number of the ticket.
   - [Delete a ticket](https://help.imiconnect.io/docs/agile-crm-1#method-name---delete-a-ticket)- Allows to delete a ticket with specific identification number of the ticket.
   - [Creating a contact](https://help.imiconnect.io/docs/agile-crm-1#method-name---creating-a-contact)- Allows to create a contact with customer’s personal details such as first name, last name, email, address, zipcode etc. 
   - [Get contact by ID](https://help.imiconnect.io/docs/agile-crm-1#method-name---get-contact-by-id)- Allows to search the contact by contact ID.
   - [Update properties of a contact by ID](https://help.imiconnect.io/docs/agile-crm-1#method-name---update-properties-of-a-contact-by-id)- Allows to update the properties of a contact by unique ID of the contact.
   - [Delete single contact](https://help.imiconnect.io/docs/agile-crm-1#method-name---delete-single-contact)- Allows to delete a single contact by specifying the  unique identification number of the contact.

2. Select add new authorization if you're using this node for the first time. You can select an existing authorization in case you've used this node in the past and have saved authorization credentials.

3. If you select the option to add new authorization, you will be asked to provide a name for this authorization to be able to reuse it later on. In addition, you need to provide the username and password of your Agile CRM account to complete the authorization.

4. Once the authorization has been completed, add the request parameters such as 'REQUESTER NAME', 'REQUESTER NAME', 'SUBJECT', 'PRIORITY', etc. for the 'Create a ticket' method and click save.



![Screenshot of Agile CRM Configuration Page](https://files.readme.io/de884eb-Agileconfig.jpg)




5. You can see the data that this node generates under the Output Variables section. These [variables](https://help.webexconnect.io/docs/variable-management-in-flows) are available for use in subsequent nodes. (Ref: right panel in the below image).



![Screenshot of Create a ticket method configuration page.](https://files.readme.io/6ad6cf1-image.png)




6. You can see the list of possible node outcomes for various methods supported by this node under the 'Node Outcomes' section. Examples include, 'Success', 'Error', 'OnTimeout', etc.

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

### Method Name - Create a Ticket



![Screenshot of Create a ticket method configuration page.](https://files.readme.io/76c3a90-image.png)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> | <p>Version</p> |
| --- | --- | --- | --- |
| <p><strong>Requester Name</strong></p><ul><li>Specifies the name of the requester</li></ul><p><strong>Requester Email<br></strong>  \* Specifies the email address of the requester</p><p><strong>Subject</strong></p><ul><li>Specifies the subject of a ticket</li></ul><p><strong>Priority</strong></p><ul><li>Specifies the nature of the ticket based on the content</li></ul><p><strong>Status</strong></p><ul><li>Specifies the status of the ticket</li></ul><p><strong>Group ID</strong></p><ul><li>Specifies the group unique identification number</li></ul><p>HTML Text</p><p><strong>CC</strong></p><ul><li>Specifies the status of the ticket</li></ul><p>Labels</p> | <p><strong>id</strong></p><ul><li>Contains the unique identification number of the ticket</li></ul><p><strong>groupID</strong></p><ul><li>Contains the group unique identification number</li></ul><p><strong>assigned_to_group</strong></p><p><strong>requester_name</strong></p><ul><li>Contains the name of the requester</li></ul><p><strong>requester_email</strong></p><ul><li>Contains  the email address of the requester</li></ul><p><strong>contactID</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p><strong>subject</strong></p><ul><li>Contains the subject of a ticket</li></ul><p><strong>cc_emails</strong></p><ul><li>Contains the cc email address</li></ul><p><strong>created_time</strong></p><ul><li>Contains the time at which of ticket is created </li></ul><p><strong>last_updated_time</strong></p><ul><li>Contains the time at which of ticket was last updated</li></ul><p><strong>last_updated_by</strong></p><ul><li>Contains the name of the user who has updated the ticket </li></ul><p>last_customer_replied_time</p><p>first_notes_text<br>last_reply_text<br>is_compressed</p><p><strong>status</strong></p><ul><li>Contains the status for the ticket</li></ul><p><strong>priority</strong></p><ul><li>Contains the nature of the ticket based on the content<br>source</li></ul><p><strong>created_by</strong></p><ul><li>Contains the name of the user who has created the ticket</li></ul><p>user_replies_count<br>no_of_reopens<br>attachements_exists<br>is_favourite<br>is_spam<br>requester_ip_address<br>html_text<br>entity_type<br>isPrivate</p><p><strong>contact_id</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p><strong>contact_type</strong></p><p>contact_properties_type<br>contact_properties_name<br>dueOn</p><p><strong>createdOn</strong></p><ul><li>Contains the date on which of ticket is created </li></ul><p><strong>lastUpdatedOn</strong><br>Contains the date on which of ticket is last updated</p><p>attachements_existsString<br>is_favouriteString<br>stringTicketID</p><p><strong>closedOn</strong></p><ul><li>Contains the date on which of ticket was closed</li></ul><p>statusName<br>priorityName<br>soruceFrom</p><p><strong>responsePayload</strong> </p><ul><li>Contains all the response JSON payload</li></ul> | onCreateticketFailure  <br>onCreateticketSuccess |  |




### Method Name - Get all Ticket



![Screenshot of Get all tickets method configuration page.](https://files.readme.io/2abce7f-image.png)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> | <p>Version</p> |
| --- | --- | --- | --- |
| <p><strong>Filter ID</strong> </p><ul><li>Specifies the unique identification number of the filter</li></ul> | <p><strong>id</strong></p><ul><li>Contains the unique identification number of the ticket</li></ul><p><strong>groupID</strong></p><ul><li>Contains the group unique identification number</li></ul><p><strong>group_group_name</strong></p><ul><li>Contains the name of the group</li></ul><p><strong>group_group_email</strong></p><ul><li>Contains the email address of the group</li></ul><p><strong>assigned_to_group</strong></p><ul><li>Contains the details of the assignee group</li></ul><p><strong>assigneeID</strong></p><ul><li>Contains the unique identification number of the assignee</li></ul><p>assignee_time</p><p><strong>assignee_id</strong></p><ul><li>Contains the unique identification number of the assignee</li></ul><p>assignee_domain</p><p><strong>assignee_email</strong></p><ul><li>Contains the email address of the assignee</li></ul><p><strong>assignee_phone</strong></p><ul><li>Contains the phone number of the assignee</li></ul><p><strong>assignee_name</strong></p><ul><li>Contains the name of the assignee</li></ul><p><strong>assignee_pic</strong></p><ul><li>Contains the picture of the assignee</li></ul><p>assignee_schedule_id</p><p><strong>requester_name</strong></p><ul><li>Contains the name of the requester</li></ul><p><strong>requester_email</strong></p><ul><li>Contains  the email address of the requester</li></ul><p><strong>contactID</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p><strong>subject</strong></p><ul><li>Contains the subject of a ticket</li></ul><p><strong>status</strong></p><ul><li>Contains the status for the ticket</li></ul><p><strong>priority</strong></p><ul><li>Contains the nature of the ticket based on the content<br>source</li></ul><p>type</p><p>source</p><p><strong>created_by</strong></p><ul><li>Contains the name of the user who has created the ticket</li></ul><p>no_of_reopens<br>html_text</p><p><strong>contact_id</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p>contact_type</p><p><strong>responsePayload</strong> </p><ul><li>Contains all the response JSON payload</li></ul> | onGetAllTicketsFailure  <br>onGetAllTicketsSuccess |  |




### Method Name - Delete a Ticket



![Screenshot of Delete a ticket method configuration page.](https://files.readme.io/bb7ee9d-image.png)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> | <p>Version</p> |
| --- | --- | --- | --- |
| <p><strong>Ticket ID</strong> </p><ul><li>Specifies the unique identification number of the ticket</li></ul> | <p><strong>status</strong> </p><ul><li>Contains the status for the ticket</li></ul> | onDeleteTicketFailure  <br>onDeleteTicketSuccess |  |




### Method Name - Creating a Contact



![Screenshot of Creating a contact method configuration page.](https://files.readme.io/a80dc5e-image.png)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> | <p>Version</p> |
| --- | --- | --- | --- |
| <p>Start Value<br>Lead Score<br>Tags</p><p><strong>First Name</strong></p><ul><li>Specifies the customer’s First Name</li></ul><p><strong>Last Name</strong></p><ul><li>Specifies the customer’s last name</li></ul><p><strong>Email</strong></p><ul><li>Specifies the email address of the user</li></ul><p><strong>Address</strong></p><ul><li>Specifies the address of the user</li></ul><p><strong>City</strong></p><ul><li>Specifies the city of the user</li></ul><p><strong>State</strong></p><ul><li>Specifies the name of state in which the user currently in</li></ul><p><strong>Zip Code<br></strong>  \* Specifies the zip code of the user</p><p><strong>Country</strong> </p><ul><li>Specifies the name of country in which the user currently in</li></ul> | <p><strong>id</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p>type</p><p><strong>created_time</strong></p><ul><li>Contains the time on which the record is created. This is in the UTC format</li></ul><p><strong>responsePayload</strong> </p><ul><li>Contains all the response JSON payload</li></ul> | onCreateContactFailure  <br>onCreateContactSuccess |  |




### Method Name - Get Contact by ID



![Screenshot of Get contact by ID method configuration page.](https://files.readme.io/a32d80a-Get_Contact_by_ID.jpg)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> | <p>Version</p> |
| --- | --- | --- | --- |
| <p><strong>Contact ID</strong> </p><ul><li>Specifies the unique identification number of the contact</li></ul> | <p><strong>id</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p>type</p><p><strong>created_time</strong></p><ul><li>Contains the time on which the record is created. This is in the UTC format</li></ul><p><strong>updated_time</strong></p><ul><li>Contains the time on which the record is updated. This is in the UTC format</li></ul><p>star_value<br>lead_score<br>contact_company_id</p><p><strong>owner_id</strong></p><ul><li>Contains the unique identification number of the owner</li></ul><p><strong>owner_email</strong></p><ul><li>Contains the email address  of the owner</li></ul><p><strong>owner_phone</strong></p><ul><li>Contains the phone number of the owner</li></ul><p><strong>owner_name</strong></p><ul><li>Contains the name of the owner</li></ul><p><strong>responsePayload</strong> </p><ul><li>Contains all the response JSON payload</li></ul> | onGetContactByIDSuccess  <br>onGetContactByIDFailure |  |




### Method Name - Update Properties of a Contact by ID



![Screenshot of Update Properties of a Contact by ID method configuration page.](https://files.readme.io/59f8b95-image.png)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> | <p>Version</p> |
| --- | --- | --- | --- |
| <p>ID</p><p>First Name</p> | <p><strong>id</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p><strong>created_time</strong></p><ul><li>Contains the time on which the record is created. This is in the UTC format</li></ul><p><strong>updated_time</strong></p><ul><li>Contains the time on which the record is updated. This is in the UTC format<br>entity_type</li></ul><p><strong>responsePayload</strong> </p><ul><li>Contains all the response JSON payload</li></ul> | onUpdatePropertiesOfContactByIDSuccess  <br>onUpdatePropertiesOfContactByIDFailure |  |




### Method Name - Delete Single Contact



![Screenshot of Delete Single Contact method configuration page.](https://files.readme.io/e148569-Delete_Single_Contact.jpg)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> | <p>Version</p> |
| --- | --- | --- | --- |
| <p><strong>Contact ID</strong> </p><ul><li>Specifies the unique identification number of the contact</li></ul> | none | onDeleteSingleContactSuccess  <br>onDeleteSingleContactFailure |  |




### Method Name - Get all Filter IDs



![Screenshot of Get all Filter IDs method configuration page.](https://files.readme.io/c4ce423-Get_all_Filter_IDs.jpg)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> | <p>Version</p> |
| --- | --- | --- | --- |
|  | <p><strong>responsePayload</strong> </p><ul><li>Contains all the response JSON payload</li></ul> | onGetAllFilterIDsSuccess  <br>onGetAllFilterIDsError |  |

