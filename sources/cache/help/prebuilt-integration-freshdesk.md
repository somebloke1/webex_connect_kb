# Freshdesk

Source: https://help.webexconnect.io/docs/prebuilt-integration-freshdesk
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:09+00:00

## Introduction

Webex Connect offers a pre-built integration node for Freshdesk to make it easier for you to create, view, update, and/or delete tickets or contacts in your Freshdesk account within an Webex Connect flow.

This node needs to be enabled for your account and is not available by default. Please contact your account manager in case you wish to enable it for your account.



![Screenshot of Fresh Desk CRM ](https://files.readme.io/0cd3fe9-image.png)




## Version Supported

This integration is based on Freshdesk API v2.

## Pre-requisites

- The tenant would need a Freshdesk account.
- This node needs to be enabled for your Webex Connect tenant and is not available by default. Please contact your account manager in case you wish to enable it for your account.
- This integration is available only in the cloud version of Webex Connect.

## Node Configuration

Drag-and-drop the node on to the visual flow builder and double-click the node to configure it.

> 📘 Please note that the latest version of the Fresh desk integration node that you should use is v1.4.

1. Select the required **Method Name** from the drop-down list box. The following methods are supported currently: 

   - [Create a Ticket](https://help.webexconnect.io/docs/freshdesk-node-1#method-name---create-a-ticket)-  Allows to create a ticket with subject, priority and description of the ticket.
   - [View a Ticket](https://help.webexconnect.io/docs/freshdesk-node-1#method-name---view-a-ticket)- Allows to view a ticket by the ticket ID.
   - [Update a Ticket](https://help.webexconnect.io/docs/freshdesk-node-1#method-name---update-a-ticket)- Allows to modify the ticket by unique ticket ID.
   - [Delete a Ticket](https://help.webexconnect.io/docs/freshdesk-node-1#method-name---delete-a-ticket)- Allows to delete a ticket using the unique identification of ticket.
   - [Create a Contact](https://help.webexconnect.io/docs/freshdesk-node-1#method-name---create-a-contact)- Allows to add a new contact with customer’s personal details using the first name, last name, phone, address etc.
   - [View a Contact](https://help.webexconnect.io/docs/freshdesk-node-1#method-name---view-a-contact)- Allows to view a contact by contact ID.
   - [Update a Contact](https://help.webexconnect.io/docs/freshdesk-node-1#method-name---update-a-contact)- Allows to modify a contact by unique identification number of the ticket.
   - [Soft Delete a Contact](https://help.webexconnect.io/docs/freshdesk-node-1#method-name---soft-delete-a-contact)- Allows to delete a contact temporarily by the contact ID.

2. Select add new authorization if you're using this node for the first time. You can select an existing authorization in case you've used this node in the past and have saved authorization credentials.

3. If you select the option to add new authorization, you will be asked to provide a name for this authorization to be able to reuse it later on. In addition, you need to provide the username and password of your Freshdesk account to complete the authorization.

4. Once the authorization has been completed, add the request parameters such as 'Ticket ID' for the selected method and click save.



![Screenshot of View a Contact method configuration page.](https://files.readme.io/cf2e357-Freshdesk.jpg)




5. You can see the data that this node generates under the Output Variables section. These [variables](https://help.webexconnect.io/docs/variable-management-in-flows) are available for use in subsequent nodes. E.g., company_id, name, email, etc. in the above screenshot.

6. You can see the list of possible node outcomes for various methods supported by this node under the 'Node Outcomes' section. Examples include, 'Success', 'Error', 'OnTimeout', etc.

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

### Method Name - Create a Ticket



![Screenshot of Create a Ticket method configuration page.](https://files.readme.io/69c1f37-image.png)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> |
| --- | --- | --- |
| <p><strong>Description</strong></p><ul><li>Specifies the description of a ticket</li></ul><p><strong>Subject</strong></p><ul><li>Specifies the subject of a ticket</li></ul><p><strong>Email</strong></p><ul><li>Specifies the email address</li></ul><p><strong>Priority</strong></p><ul><li>Specifies the nature of the ticket based on the content</li></ul><p><strong>Status</strong></p><ul><li>Specifies the status of the ticket </li></ul><p><strong>CC_Emails</strong><br>Specifies the cc email address</p> | <p><strong>cc_emails</strong></p><ul><li>Contains the cc email address</li></ul><p>reply_cc_emails</p><p><strong>priority</strong></p><ul><li>Contains the nature of the ticket based on the content</li></ul><p><strong>requester_id</strong></p><ul><li>Contains the unique identification number of the requester</li></ul><p><strong>source</strong></p><p><strong>status</strong></p><ul><li>Contains the status for the ticket</li></ul><p><strong>subject</strong></p><ul><li>Contains the subject for the ticket</li></ul><p><strong>company_id</strong></p><ul><li>Contains the company unique identification number</li></ul><p><strong>id</strong><br>Contains the unique identification number of the ticket</p><p>type<br>fr_escalated<br>spam<br>urgent<br>is_escalated</p><p><strong>created_at</strong></p><ul><li>Contains the details of the place the ticket is created at</li></ul><p><strong>updated_at</strong></p><ul><li>Contains the details of the place the ticket is updated at</li></ul><p>due_by<br>fr_due_by<br>description_text<br>description</p> | onCreateTicketFailure  <br>onCreateTicketSuccess |




### Method Name - View a Ticket



![Screenshot of View a Ticket method configuration page.](https://files.readme.io/c97aabf-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Ticket ID | cc_emails  <br>reply_cc_emails  <br>priority  <br>requester_id  <br>source  <br>status  <br>subject  <br>company_id  <br>id  <br>type  <br>fr_escalated  <br>spam  <br>urgent  <br>is_escalated  <br>created_at  <br>updated_at  <br>due_by  <br>fr_due_by  <br>description_text  <br>description  <br>custom_fields_category | onViewTicketFailure  <br>onViewTicketSuccess |




### Method Name - Update a Ticket



![Screenshot of Update a Ticket method configuration page.](https://files.readme.io/71d6553-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Ticket ID  <br>Priority  <br>Status | description_text  <br>description  <br>fr_escalated  <br>spam  <br>priority  <br>requester_id  <br>source  <br>status  <br>subject  <br>id  <br>is_escalated  <br>created_at  <br>updated_at  <br>due_by  <br>fr_due_by | onUpdateTicketFailure  <br>onUpdateTicketSuccess |




### Method Name - Delete a Ticket



![Screenshot of Delete a Ticket method configuration page.](https://files.readme.io/08923ac-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Ticket ID | None | onDeleteTicketFailure  <br>onDeleteTicketSuccess |




### Method Name - Create a Contact



![Screenshot of Create a Contact method configuration page.](https://files.readme.io/bef506d-image.png)






| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> |
| --- | --- | --- |
| <p><strong>Name</strong></p><ul><li>Specifies the name of the contact</li></ul><p><strong>Email</strong></p><ul><li>Specifies the email address of the contact</li></ul><p>Other Emails</p><ul><li>Specifies the alternate email address of the contact</li></ul> | <p>active</p><p><strong>company_id</strong></p><ul><li>Contains the company unique identification number</li></ul><p>view_all_tickets<br>deleted</p><p><strong>email</strong></p><ul><li>Contains the email address of the contact</li></ul><p><strong>id</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p><strong>language</strong></p><ul><li>Contains the type of language selected by the contact</li></ul><p><strong>name</strong></p><ul><li>Contains the name of the contact</li></ul><p><strong>time_zone</strong></p><ul><li>Contains the time zone details of the contact</li></ul><p><strong>other_emails</strong></p><ul><li>Contains  the alternate email address of the contact</li></ul><p>other_companies</p><p><strong>created_at</strong></p><ul><li>Contains the details of the place the contact is created at</li></ul><p><strong>updated_at</strong></p><ul><li>Contains the details of the place the contact is updated at</li></ul><p><strong>tags</strong></p><p><strong>avatar</strong></p><p><strong>mobile</strong></p><ul><li>Contains the phone number of the contact</li></ul><p><strong>phone</strong></p><ul><li>Contains the phone number of the contact</li></ul><p><strong>description</strong></p><ul><li>Contains the description of a ticket</li></ul><p><strong>address</strong><br>Contains the address of the contact</p> | onCreateContactFailure  <br>onCreateContactSuccess |




### Method Name - View a Contact



![Screenshot of View a Contact method configuration page.](https://files.readme.io/6201342-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Contact ID | active  <br>company_id  <br>view_all_tickets  <br>email  <br>id  <br>language  <br>name  <br>time_zone  <br>other_companies  <br>created_at  <br>updated_at  <br>custom_fields  <br>avatar | onViewContactFailure  <br>onViewContactSuccess |




### Method Name - Update a Contact



![Screenshot of Update a Contact method configuration page.](https://files.readme.io/7e6dc1d-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Contact ID  <br>Name  <br>Job Title  <br>Other Emails | active  <br>company_id  <br>view_all_tickets  <br>deleted  <br>email  <br>id  <br>job_title  <br>language  <br>name  <br>time_zone  <br>other_emails  <br>other_companies  <br>created_at  <br>updated_at | onUpdateContactFailure  <br>onUpdateContactSuccess |




### Method Name - Soft Delete a Contact



![Screenshot of Soft Delete a Contact method configuration page.](https://files.readme.io/41af855-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Contact ID | response | onSoftDeleteContactFailure  <br>onSoftDeleteContactSuccess |

