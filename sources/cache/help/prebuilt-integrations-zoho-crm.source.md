## Introduction

<<prodname>> offers a pre-built integration node for Zoho CRM to make it easier for you to create, view, delete, and/or update tickets or contacts in your Zoho CRM account. 

This node needs to be enabled for your account and is not available by default. Please contact your account manager in case you wish to enable it for your account.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e0af702-image.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


## Version Supported

> 📘 <<prodname>>'s integration is based on Zoho's API version 2.0.

## Pre-requisites

To get Zoho CRM node-enabled:

- Zoho CRM node needs to be enabled for your <<prodname>> tenant and is not available by default. Please contact your account manager in case you wish to enable it for your account.
- Callback URLs for all your pre-built integrations, custom integration configurations, that use OAuth 2.0 authorization with ‘Auth Code’ Grant Type will be updated with <<prodname>>  branded URLs. This doesn’t impact functioning of any of your existing integration configurations until the Refresh Token for that integration expires or until you decide to reauthorize. In either of these two cases, you would need to start using the new Callback URL provided on <<prodname>>  UI in the third-party application you have integrated with. Another example of this is OAuth 2.0 based authentication for Gmail when using SMTP for Outbound Email channel configuration which is currently available only for <<prodname>>  tenants used for Webex Contact Center Integration.  
  Please make sure your applications, firewalls, etc. do not restrict access to these new Callback URLs in case you have an internal policy/practice to add these URLs to the allow/accept/whitelist.
- This integration is available only in the cloud version of <<prodname>>.

## Node Configuration

Drag-and-drop the node onto the visual flow builder and double-click the node to configure it. 

> 📘 Please note that the latest version of the Zoho integration node that you should use is v2.0.<can we move this to versions section>

1. Select the required **Method Name** from the drop-down list box. The following methods are supported currently: 

- [Insert Record](https://help.imiconnect.io/docs/zoho-crm-1#method-name---insert-record)- Allows to add a new record using module API name, company, last name, first name, email etc.
- [Get a Specific Record](https://help.imiconnect.io/docs/zoho-crm-1#method-name---get-a-specific-record)- Allows to retrieve a specific record by Record ID.
- [Update a Specific Record](https://help.imiconnect.io/docs/zoho-crm-1#method-name---update-a-specific-record)- Allows to modify a specific record by the unique identification number of the record.  
- [Delete a Specific Record](https://help.imiconnect.io/docs/zoho-crm-1#method-name---delete-a-specific-record)- Allows to delete a specific record by the Record ID.
- [Add User](https://help.imiconnect.io/docs/zoho-crm-1#method-name---add-user)- Allows to add a new user using the users personal information such as, role ID, email ,first name, profile Id and last name.
- [Get Data of a Specific User](https://help.imiconnect.io/docs/zoho-crm-1#method-name---get-details-of-a-specific-user)-Allows to retrieve data of a specific user using unique identification number of the user.
- [Update User](https://help.imiconnect.io/docs/zoho-crm-1#method-name---update-user)- Allows to modify a user by the User ID.
- [Delete User](https://help.imiconnect.io/docs/zoho-crm-1#method-name---delete-user)- Allows to delete a specific user by the User ID.

2. Provide the Zoho auth token and other request parameters for the selected method and click 'Save'. For example, if you select the 'Insert Record' method, you need to provide parameters such as 'Module API Name', 'Zoho Auth Token', 'Company Name', 'First Name', 'Last Name', 'Email', and more.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/759a5e2-Insert_Record.jpg",
        "Insert Record.jpg",
        "Screenshot of Insert Record method configuration page."
      ],
      "align": "center",
      "caption": "Screenshot of Insert Record method configuration page."
    }
  ]
}
[/block]


3. You can see the data that this node generates under the Output Variables section. These [variables](doc:variable-management) are available for use in subsequent nodes. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5b4c3c7-a95fe9f-IMIconnect_Zoho_Integration_Node_Outcomes.png",
        "a95fe9f-IMIconnect_Zoho_Integration_Node_Outcomes.png",
        "Screenshot of Insert Record method configuration page."
      ],
      "align": "center",
      "caption": "Screenshot of Insert Record method configuration page."
    }
  ]
}
[/block]


4. You can see the list of possible node outcomes for various methods supported by this node under the 'Node Outcomes' section. Examples include, 'Success', 'Error', 'OnTimeout', etc.

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

### Method Name - Insert Record

| <p>Input Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | <p>Output Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | <p>Node Outcomes</p>                                                                                                                                                                                                                                                  |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>Module API Name</strong></p><ul><li>This field specifies the module name to which the API belongs to</li></ul><p><strong>Company</strong></p><ul><li>This field specifies the name of the company</li></ul><p><strong>Last Name</strong></p><ul><li>Customer’s Last Name</li></ul><p><strong>First Name</strong></p><ul><li>Customer’s First Name</li></ul><p><strong>Email</strong></p><ul><li>This field specifies the email id of the user</li></ul><p><strong>State</strong></p><ul><li>This field specifies the state of the record whether <em>Active \_or \_Inactive</em></li></ul><p><strong>Trigger (Optional)</strong></p><ul><li>The trigger input can be workflow, approval, or blueprint. If "trigger" is not mentioned, the workflows, approvals and blueprints related to the API will get executed. Enter the trigger value as \[] to not execute the workflows. </li></ul> | <p><strong>Code </strong></p><ul><li>Contains only text whether "Success", "Invalid_Data", "Mandatory_Not_Found"</li></ul><p><strong>Modified_Time</strong></p><ul><li>Contains the time on which the record is modified</li></ul><p><strong>Modified_By_name</strong></p><ul><li>Contains the name of the user who have modified the record</li></ul><p><strong>Modified_By_id</strong></p><ul><li>Contains the unique identification number of the user</li></ul><p><strong>Created_Time</strong></p><ul><li>Contains the time on which the record is created</li></ul><p><strong>Created_By_name</strong></p><ul><li>Contains the name of the user who has created the record</li></ul><p><strong>Created_By_id</strong></p><ul><li>Contains the unique identification number of the user</li></ul><p><strong>message</strong></p><ul><li>Contains the response of the API executed. </li></ul><p><strong>status</strong></p><ul><li>Contains the status of the record whether <em>Success_or \_Error</em></li></ul><p><strong>responsePayload</strong></p><ul><li>Contains all the response JSON payload</li></ul> | <p><strong>onInsertRecordError</strong></p><ul><li>Contains the details if the insertion of a record is failed for any reason</li></ul><p><strong>onInsertRecordSuccess</strong></p><ul><li>Contains the details if the insertion of a record is successful</li></ul> |

### Method Name - Get a Specific Record

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d300339-Get_A_Specific_Record.jpg",
        "Get A Specific Record.jpg",
        "Screenshot of Get a Specific Record method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Get a Specific Record method configuration page."
    }
  ]
}
[/block]


| <p>Input Variables</p>                                                                                                                                                                                                                           | <p>Output Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | <p>Node Outcomes</p>                                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| <p><strong>Module API Name</strong></p><ul><li>This field specifies the module name to which the API belongs to</li></ul><p><strong>Record ID</strong></p><ul><li>This field specifies the unique identification number of the record </li></ul> | <p><strong>Owner_Name</strong></p><ul><li>Contains the name of the user to which it belongs to</li></ul><p><strong>Owner_id</strong></p><ul><li>Contains the unique identification number of the owner</li></ul><p><strong>Account_Name_name</strong></p><ul><li>Contains the name of the account</li></ul><p><strong>Account_id</strong></p><ul><li>Contains the unique identification number of the account</li></ul><p><strong>Created_Time</strong></p><ul><li>Contains the time on which the record is created. This is in the UTC format</li></ul><p><strong>Created_By_name</strong></p><ul><li>Contains the name of the user who has created the record</li></ul><p><strong>Created_By_id</strong></p><ul><li>Contains the unique identification number of the user</li></ul><p><strong>responsePayload</strong></p><ul><li>Contains all the response JSON payload</li></ul> | <ul><li>onNoRecordsFound<ul><li>onGetRecordFailure</li><li>onGetRecordSuccess</li></ul></li></ul> |

### Method Name - Update a Specific Record

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4eac9c0-Update_Record.jpg",
        "Update Record.jpg",
        "Screenshot of Update a Specific Record method configuration page"
      ],
      "align": "center",
      "caption": "Screenshot of Update a Specific Record method configuration page"
    }
  ]
}
[/block]


| <p>Input Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                           | <p>Output Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | <p>Node Outcomes</p>                                                                                                                                                                                                                                            |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>Module API Name</strong></p><ul><li>This field specifies the module name to which the API belongs to</li></ul><p><strong>Record ID</strong></p><ul><li>This field specifies the unique identification number of the record </li></ul><p><strong>Company</strong></p><ul><li>This field specifies the name of the company</li></ul><p><strong>State</strong></p><ul><li>This field specifies the state of the record whether <em>Active \_or \_Inactive</em></li></ul> | <p><strong>Code </strong></p><ul><li>Contains only text whether "Success", "Invalid_Data", "Mandatory_Not_Found"</li></ul><p><strong>details_created_time<br>\*</strong> Contains the time on which the record is created</p><p><strong>details_modified_time</strong></p><ul><li>Contains the time on which the record is modified</li></ul><p><strong>details_modified_by_name</strong></p><ul><li>Contains the name of the user who has modified the record</li></ul><p><strong>details_modified_by_id</strong></p><ul><li>Contains the unique identification number of the user who has modified the record</li></ul><p><strong>details_created_by_name</strong></p><ul><li>Contains the name of the user who has modified the record</li></ul><p><strong>details_created_by_id</strong></p><ul><li>Contains the unique identification number of the user who has created the record</li></ul><p><strong>message</strong></p><ul><li>Contains the response of the API executed. </li></ul><p><strong>status</strong></p><ul><li>Contains the status of the record whether <em>Success_or \_Error</em></li></ul><p><strong>responsePayload</strong></p><ul><li>Contains all the response JSON payload</li></ul> | <p><strong>onUpdateRecordError</strong></p><ul><li>Contains the details if the update of a record is failed for any reason</li></ul><p><strong>onUpdateRecordSuccess</strong></p><ul><li>Contains the details if the update of a record is successful</li></ul> |

### Method Name - Delete a Specific Record

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ac085aa-Delete_record.jpg",
        "Delete record.jpg",
        "Screenshot of Delete a Specific Record method configuration page."
      ],
      "align": "center",
      "caption": "Screenshot of Delete a Specific Record method configuration page"
    }
  ]
}
[/block]


| <p>Input Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                          | <p>Output Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | <p>Node Outcomes</p>                                                                                                                                                                                                                                                |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p><strong>Module API Name</strong></p><ul><li>This field specifies the module name to which the API belongs to</li></ul><p><strong>Record ID</strong> </p><p><strong>Workflow Trigger</strong><br>This field specifies if the workflow rules are to be triggered upon record deletion. The default value is <strong>True</strong>.<br>Possible values - true: triggers associated workflows; false: does not trigger associated workflows.</p> | <p><strong>Code </strong></p><ul><li>Contains only text whether "Success", "Invalid_Data", "Mandatory_Not_Found"</li></ul><p><strong>details_id</strong></p><ul><li>Contains the id of the record which is deleted</li></ul><p><strong>message</strong></p><ul><li>Contains the response of the API executed. </li></ul><p><strong>status</strong></p><ul><li>Contains the status of the record whether <em>Success_or \_Error</em></li></ul><p><strong>response</strong></p><ul><li>Contains all the response JSON payload</li></ul> | <p><strong>onDeleteRecordSuccess</strong></p><ul><li>Contains the details if the deletion of a record is successful</li></ul><p><strong>onDeleteRecordError</strong></p><ul><li>Contains the details if the deletion of a record is failed for any reason</li></ul> |

### Method Name - Add User

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/017b4eb-image.png",
        null,
        "Screenshot of Add User method configuration page."
      ],
      "align": "center",
      "caption": "Screenshot of Add User method configuration page."
    }
  ]
}
[/block]


| <p>Input Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | <p>Output Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | <p>Node Outcomes</p>                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>Role ID</strong></p><ul><li>This field specifies the unique identification number based on the designation</li></ul><p><strong>Email</strong></p><ul><li>This field specifies the email id of the user</li></ul><p><strong>First Name</strong></p><ul><li>First Name of the user</li></ul><p><strong>Profile ID</strong><br>Specify the unique ID of the profile you want to assign the user with, to decide the user's level of access to CRM data.</p><p><strong>Last Name</strong></p><ul><li>Last name of the user</li></ul> | <p><strong>Code </strong></p><ul><li>Contains only text whether "Success", "Invalid_Data", "Mandatory_Not_Found"</li></ul><p><strong>id</strong></p><ul><li>Contains the unique identification number of the user</li></ul><p><strong>message</strong></p><ul><li>Contains the response of the API executed. </li></ul><p><strong>status</strong></p><ul><li>Contains the status of the record whether <em>Success_or \_Error</em></li></ul><p><strong>responsePayload</strong></p><ul><li>Contains all the response JSON payload</li></ul> | <p><strong>onaddUserError</strong></p><ul><li>Contains the details of the added user has failed for any reason</li></ul><p><strong>onaddUserSuccess</strong></p><ul><li>Contains the details of the user is added successfully</li></ul> |

### Method Name - Get Details of a Specific User

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f41a0f7-Get_Date_of_a_Specific_User.jpg",
        "Get Date of a Specific User.jpg",
        "Screenshot of Get Details of a Specific User method configuration page."
      ],
      "align": "center",
      "caption": "Screenshot of Get Details of a Specific User method configuration page."
    }
  ]
}
[/block]


| <p>Input Variables</p>                                                                                             | <p>Output Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | <p>Node Outcomes</p>                                                                                                                                                                                                              |
| :----------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>User ID</strong></p><ul><li>This field specifies the unique identification number of the user</li></ul> | <p><strong>role_name</strong><br>Represents the name of the role of the user.</p><p><strong>role_id</strong></p><ul><li>Represents the unique identification number of the role of the user.</li></ul><p><strong>language</strong></p><ul><li>Represents the language in which the user accesses the CRM. For instance, 'en_US'.</li></ul><p><strong>locale</strong></p><ul><li>Represents the user's locale. For instance, 'en_IN'.</li></ul><p><strong>microsoft</strong></p><ul><li>Contains the Boolean value. Represents if the user is a Microsoft user.</li><li>True: The user is a Microsoft user.</li><li>False: The user is a Microsoft user.</li></ul><p><strong>Isonline</strong></p><ul><li>Represents if the user is online.</li><li>True: The user is online.</li><li>False: The user is offline.</li></ul><p><strong>modified_by_name</strong></p><ul><li>Contains the name of the user who has modified the record</li></ul><p><strong>modified_by_id</strong></p><ul><li>Contains the unique identification number of the user who has modified the record</li></ul><p><strong>user_id</strong></p><ul><li>Contains the unique identification number of the user</li></ul><p>user_country_locale</p><p><strong>users_first_name</strong></p><ul><li>Contains the first name of the user</li></ul><p><strong>users_email</strong></p><ul><li>Contains the email address of the user</li></ul><p><strong>users_created_time</strong></p><ul><li>Contains the time details at which the user was created</li></ul><p><strong>users_modified_time</strong></p><ul><li>Contains the time on which the record is modified. </li></ul><p><strong>users_time_format</strong></p><ul><li>Contains the time format in  UTC format</li></ul><p>users_offset</p><p><strong>users_profile_name</strong></p><ul><li>Contains the profile name of the user</li></ul><p><strong>users_profile_id</strong></p><ul><li>Contains the unique identification number for the profile</li></ul><p><strong>users_last_name</strong></p><ul><li>Contains the last name of the user</li></ul><p><strong>users_time_zone</strong></p><ul><li>Contains the time zone details of the user</li></ul><p><strong>users_created_by_name</strong></p><ul><li>Contains the name of the user who has created the record</li></ul><p><strong>users_created_by_id</strong></p><ul><li>Contains the unique identification number of the user who has created the record</li></ul><p><strong>users_zuid</strong></p><ul><li>Represents the ZUID of the current user.</li></ul><p><strong>users_confirm</strong></p><ul><li>Represents if the user is a confirmed user.</li><li>True: The user is a confirmed user.</li><li>False: The user is not a confirmed user.</li></ul><p><strong>users_full_name</strong></p><ul><li>Contains the full name of the user</li></ul><p><strong>users_date_format</strong></p><ul><li>Contains the date format . For instance, 'MM/dd/yyyy'.</li></ul><p><strong>users_status</strong></p><ul><li>Contains the status of the record whether <em>Success_or \_Error</em></li></ul><p><strong>responsePayload</strong></p><ul><li>Contains all the response JSON payload</li></ul> | <p><strong>onGetUserError</strong></p><ul><li>Contains thedetails of the user is retrieved has failed for any reason</li></ul><p>onGetUserSuccess</p><ul><li>Contains the details of the user is retrieved successfully</li></ul> |

### Method Name - Update User

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/06b19aa-Update_User.jpg",
        "Update User.jpg",
        "Screenshot of Update User method configuration page."
      ],
      "align": "center",
      "caption": "Screenshot of Update User method configuration page."
    }
  ]
}
[/block]


| <p>Input Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <p>Output Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <p>Node Outcomes</p>                                                                                                                                                                |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>User ID</strong></p><ul><li>This field specifies the unique identification number of the user</li></ul><p><strong>Phone</strong></p><ul><li>This field specifies the phone number of the user</li></ul><p><strong>Email</strong></p><ul><li>This field specifies the email id of the user</li></ul><p><strong>Date of Birth</strong></p><ul><li>This field specifies the date of birth of the user</li></ul><p><strong>Role ID</strong></p><ul><li>This field specifies the unique identification number of the role</li></ul><p><strong>Profile ID</strong></p><ul><li>This field specifies the unique identification number of the profile</li></ul><p><strong>State</strong></p><ul><li>This field specifies the state of the user whether <em>Active \_or \_Inactive</em></li></ul> | <p><strong>users_code</strong></p><ul><li>Contains only text whether "Success", "Invalid_Data", "Mandatory_Not_Found"</li></ul><p><strong>users_details_id</strong></p><ul><li>Contains the id of the record which is deleted</li></ul><p><strong>users_message</strong></p><ul><li>Contains the response of the API executed. </li></ul><p><strong>users_status</strong></p><ul><li>Contains the status of the record whether <em>Success_or \_Error</em></li></ul><p><strong>responsePayload</strong></p><ul><li>Contains all the response JSON payload</li></ul> | <ul><li>onInvalidData<ul><li>onError</li><li>onInvalidChoice</li><li>onauthorizatonfail</li><li>onUpdateUserError</li><li>onUpdateUserSuccess</li><li>onTimeout</li></ul></li></ul> |

### Method Name - Delete User

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6a07b3a-Delete_User.jpg",
        "Delete User.jpg",
        "Screenshot of Delete User method configuration page."
      ],
      "align": "center",
      "caption": "Screenshot of Delete User method configuration page."
    }
  ]
}
[/block]


| <p>Input Variables</p>                                                                                             | <p>Output Variables</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | <p>Node Outcomes</p>                                                                                                                                                                |
| :----------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><strong>User ID</strong></p><ul><li>This field specifies the unique identification number of the user</li></ul> | <p><strong>users_code</strong></p><ul><li>Contains only text whether "Success", "Invalid_Data", "Mandatory_Not_Found"</li></ul><p><strong>users_details</strong></p><ul><li>Contains the id of the record which is deleted</li></ul><p><strong>users_message</strong></p><ul><li>Contains the response of the API executed. </li></ul><p><strong>users_status</strong></p><ul><li>Contains the status of the record whether <em>Success_or \_Error</em></li></ul><p><strong>responsePayload</strong> </p><ul><li>Contains all the response JSON payload</li></ul> | <ul><li>onInvalidData<ul><li>onError</li><li>onInvalidChoice</li><li>onauthorizatonfail</li><li>onDeleteUserError</li><li>onDeleteUserSuccess</li><li>onTimeout</li></ul></li></ul> |