## Introduction

Webex Connect offers an out of the box pre-built integration node for Salesforce that enables you to easily perform CRUD operations on all standard and custom Salesforce objects. You can also use SOQL queries on all standard and custom Salesforce Objects within a Webex Connect flow to retrieve information from your Salesforce CRM.

In previous versions, this integration allows you to insert, update, delete, and retrieve contacts from your Salesforce account within a flow. Additionally, you can get, insert, or update cases in your Salesforce account using this node. It also allows you to Create, Get, Update, or Delete Record in your Salesforce account.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f78e2b3-Salesforce_Integration_Node.PNG",
        "Salesforce Integration Node.PNG",
        "Screenshot of Salesforce CRM."
      ],
      "align": "center",
      "caption": "Screenshot of Salesforce CRM"
    }
  ]
}
[/block]


## Version Supported

> 📘 
> 
> The latest version (v2.1) of the integration lets you select the Salesforce API version. Where as the versions older to v2.0 uses Salesforce API v43.0.

## Pre-requisites

To get Salesforce nodes enabled:

- This node needs to be enabled for your <<prodname>> tenant and is not available by default. Please contact your account manager in case you wish to enable it for your account.
- Tenant would need a Salesforce account.
- This integration is available only in the cloud version of Webex Connect.
- Callback URLs for all your pre-built integrations, custom integration configurations, that use OAuth 2.0 authorization with ‘Auth Code’ Grant Type will be updated with <<prodname>>  branded URLs. This doesn’t impact functioning of any of your existing integration configurations until the Refresh Token for that integration expires or until you decide to reauthorize. In either of these two cases, you would need to start using the new Callback URL provided on <<prodname>>  UI in the third-party application you have integrated with. Another example of this is OAuth 2.0 based authentication for Gmail when using SMTP for Outbound Email channel configuration which is currently available only for <<prodname>>  tenants used for Webex Contact Center Integration.  
  Please make sure your applications, firewalls, etc. do not restrict access to these new Callback URLs in case you have an internal policy/practice to add these URLs to the allow/accept. 
- Know your Salesforce Org. Instance  – Salesforce Org. instance ID is used in the API to connect with Salesforce. Each Salesforce org. has a unique instance, and the same can be obtained from Salesforce.
  - **For Classic**: **Click on Setup | Under Administer | Company Profile| Company Information**
  - **For Lightning**: **Click on Gear Icon|Setup|Company Settings|Company information**  
    **Some examples-**  
    Example 1- if your domain is <https://na91.salesforce.com> then your Salesforce Org. instance should be na91  
    Example 2 – if your domain is <https://acme.my.salesforce.com> then your Salesforce Org. instance should be acme.my  
    For more information, refer to [Salesforce Org instances](https://help.salesforce.com/s/articleView?id=000385215&type=1).

## Node Configuration

Drag-and-drop the node onto the visual flow builder and double-click the node to configure it. 

> 📘 Note
> 
> Please note that the latest version of the Salesforce CRM node that you should use is v1.1 which uses UTF-8 encoding and v1.0 does not use UTF-8 encoding.

1. Select the required **Method Name** from the drop-down list box. Examples include methods such as **Get Contact**, **Insert Contact**, **Update Contact**, **Delete Contact**, **Insert Case**,**Create Record**, **Get Record**, **Get Record Using SOQL (Salesforce Object Query Language)**, **Update Record**, and **Delete Record**. etc. The following methods are supported currently: 
   - [Get Contact](https://help.imiconnect.io/docs/salesforce-node-1#method-name---get-contact)-  Allows to retrieve a contact with the unique identification number of the contact. 
   - [Insert Contact](https://help.imiconnect.io/docs/salesforce-node-1#method-name---insert-contact)- Allows to add a new contact using the customer’s personal details such as first name, last name, address, phone number, etc.
   - [Update Contact](https://help.imiconnect.io/docs/salesforce-node-1#method-name---update-contact)- Allows modifying the contact with a specific unique identification number of the contact.
   - [Delete Contact](https://help.imiconnect.io/docs/salesforce-node-1#method-name---delete-contact)- Allows to delete a specific contact by contact ID.
   - [Insert Case](https://help.imiconnect.io/docs/salesforce-node-1#method-name---insert-case)- Allows to add a case with customer’s contact details.
   - [Update Case](https://help.imiconnect.io/docs/salesforce-node-1#method-name---update-case)- Allows to modify the case by the Cased ID.
   - [Get Case](https://help.webexconnect.io/docs/salesforce-node-1#method-name--get-case) - Allows to get the case record with the customer's contact details.
   - [Create Record](#method-name---create-record) - Allows to create a new record in any standard or custom Salesforce object.
   - [Get Record](#method-name---get-record) - Allows to retrieve any records from any standard or custom Salesforce objects.
   - [Get Record Using SOQL](#method-name---get-record-using-soql) - Allows to fetch records details of any standard or custom Salesforce objects using SOQL queries.
   - [Update Record](#method-name---update-record) - Allows to update an existing record in any standard or custom Salesforce object.
   - [Delete Record](#method-name---delete-record) - Allows to delete a record from any standard or custom Salesforce object.
     > 📘 Note
     > 
     > Version 1.0 and 1.2 supports Get Contact, Insert Contact, Update Contact, Delete Contact, Insert Case only.  
     > Version 2.0 to supports Create, Update, Read, and Delete operations  of the Salesforce objects. This enables retrieving information from Salesforce your object using query language i.e., Get Record using SOQL.

2. You can select an existing authorization in case you've used this node in the past and have saved authorization credentials.

3. If you select the option to add a new authorization, you will be asked to provide a name for this authorization to be able to reuse it later on. You need to provide the following details at this step:

- 'Consumer ID' and 'Consumer Secret' for completing the authorization. 
  - Authorization URL (E.g., <https://login.salesforce.com/services/oauth2/authorize> or https\://\<mydomain_url or site_url>.salesforce.com/services/oauth2/authorize in case you are using SSO)
- Access Token URL (E.g., https\://\<login/mydomain_url or site_url>.salesforce.com/services/oauth2/token)
- Refresh Token URL (E.g., https\://\<login/mydomain_url or site_url>.salesforce.com/services/oauth2/token)

> 📘 Salesforce App Configuration and Callback URL
> 
> Please note that the Callback URL that's displayed on the Add Authorization screen when you add a new authorization needs to be configured in your Salesforce application as a pre-requisite. You would need to create a connected app in Salesforce for the integration. 
> 
> [Here's the link to Salesforce documentation](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_api_integration.htm&type=5) that covers the details of Connected App creation and permissions configuration. 
> 
> You would need to mention the scope as 'Full Access' with 'Perform requests at any time (refresh_token) option.

4. Once the authorization has been completed, add the request parameters for the selected method and click save. You can pass the available Input Variables or Custom Variables as request parameters. E.g., in case of 'Get Contact' method, you need to provide the Salesforce Org Instance (i.e., server that your Salesforce organization is hosted on. It can be found under Set-up/Company Information section in your Salesforce org), the field name and value using which you want to search the contact. Please note that only indexed fields can be used for searching the contacts within Salesforce.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a8465c0-image.png",
        null,
        "Screenshot of Get Contact method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Get Contact method configuration page"
    }
  ]
}
[/block]


5. You can see the data that this node generates under the Output Variables section. These [variables](doc:variable-management) are available for use in subsequent nodes. E.g., Get Contact method returns various fields associated with the searched contact in your Salesforce account. 

6. You can see the list of possible node outcomes for this node under 'Node Outcomes' section. Examples include, 'No Content found', 'Multiple records', 'OnTimeout', etc.

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

### Method Name - Get Contact

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b37393a01bb1f58b41199d49f34d94114e739c32cad640a8a370488e0863cbf6-Get_Contact.png",
        null,
        "Screenshot of Get Contact method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Get Contact method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "<p>Input Variables</p>",
    "h-1": "<p>Output Variables</p>",
    "h-2": "<p>Node Outcomes</p>",
    "0-0": "<p>Salesforce Org.Instance <ul><li>The unique identifier for salesforce identity</li></ul><p>Field API Name<br>Value to Query</p>",
    "0-1": "<p>attributesType<br>attributesURL</p><p><strong>contactId</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p>isDeleted<br><strong>accountId</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p><strong>firstName</strong></p><ul><li>Contains the first name of the user</li></ul><p><strong>lastName</strong></p><ul><li>Contains the last name of the user</li></ul><p><strong>Name</strong></p><ul><li>Contains the full name of the user</li></ul><p><strong>mailingStreet</strong></p><ul><li>Contains the street number</li></ul><p><strong>mailingCity</strong></p><ul><li>Contains the city name</li></ul><p><strong>mailingState</strong></p><ul><li>Contains the state name</li></ul><p><strong>mailingPostalCode</strong></p><ul><li>Contains the postal code of the area</li></ul><p><strong>mailingCountry</strong></p><ul><li>Contains the name of the country</li></ul><p>mailingAddresscity<br>mailingAddressCountry<br>mailingAddressPostalCode<br>mailingAddressState<br>mailingAddressStreet</p><p><strong>Phone</strong></p><ul><li>Contains the phone number of the user</li></ul><p><strong>homePhone</strong></p><ul><li>Contains the home phone number of the user</li></ul><p><strong>assitantPhone</strong></p><ul><li>Contains the phone number of the assitant</li></ul><p><strong>Email</strong></p><ul><li>Contains the email address of the user</li></ul><p>leadSource</p><p><strong>CreatedDate</strong></p><ul><li>Contains the date on which the record is created</li></ul><p><strong>CreatedById</strong></p><ul><li>Contains the unique identification number of the user who created  the record</li></ul><p>lastModifiedDate</p><ul><li>Contains the date on which the record is modified</li></ul><p>systemModStamp</p><p>lastActivityDate</p><p>lastViewedDate<br>lastReferencedDate<br>isEmailBounced<br>photoURL<br>cleanStatus</p>",
    "0-2": "Success  \nMultiple records  \nNo content found  \nSession expired  \nError"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Insert Contact

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b8f16041fdefedec8862397e24d35d830b2b190a69025a9dcf4387de825df2d7-Insert_Contact.png",
        "Salesforce_Insert Contact.jpg",
        "Screenshot of Insert Contact method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Insert Contact method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "<p>Input Variables</p>",
    "h-1": "<p>Output Variables</p>",
    "h-2": "<p>Node Outcomes</p>",
    "0-0": "<p><strong>Salesforce Org.Instance</strong></p><ul><li>The unique identifier for salesforce identity</li></ul><p><strong>Last Name</strong></p><ul><li>Specifies the last name of the user</li></ul><p>First Name (Optional)</p><ul><li>Specifies the first name of the user</li></ul><p>Salutation (Optional)</p><p><strong>Other Street (Optional)</strong></p><ul><li>Specifies the street number</li></ul><p><strong>Other City (Optional)</strong></p><ul><li>Specifies the name of the city</li></ul><p><strong>Other State (Optional)</strong></p><ul><li>Specifies the name of the state</li></ul><p><strong>Other Postal Code (Optional)</strong></p><ul><li>Specifies the postal code of the area </li></ul><p><strong>Other Country (Optional)</strong></p><ul><li>Specifies the name of country<br>Mailing Street  (Optional)<br>Mailing City  (Optional)<br>Mailing State (Optional)<br>Mailing Postal Code  (Optional)<br>Mailing Country  (Optional)</li></ul><p><strong>Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p>Fax (Optional)</p><ul><li>Specifies the fax number of the user</li></ul><p>Mobile Phone (Optional)</p><ul><li>Specifies the mobile phone number of the user</li></ul><p><strong>Home Phone (Optional)</strong></p><ul><li>Specifies the home phone number of the user</li></ul><p><strong>Other Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p><strong>Assistance Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p>Report to ID (Optional)</p><p><strong>Email (Optional)</strong></p><ul><li>Specifies the email address of the user</li></ul><p><strong>Title (Optional)</strong></p><ul><li>Specifies the title of the user</li></ul><p><strong>Department (Optional)</strong></p><ul><li>Specifies the department name of the user</li></ul><p><strong>Assistant Name (Optional)</strong></p><ul><li>Specifies the name of the assistant</li></ul><p>Lead Source(Optional)</p><p><strong>Birthdate</strong></p><ul><li>Specifies the birthdate of the user</li></ul><p>Description (Optional)</p>",
    "0-1": "contactId  \nsuccess  \nerror",
    "0-2": "Success  \nError"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Update Contact

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b6e4374cf9dc17a1ba58285ba0bcaa533039537a6161c027c325bbc95a9d96be-Update_Contact.png",
        "Salesforce_UpdateContact.jpg",
        "Screenshot of Update Contact method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Update Contact method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "<p>Input Variables</p>",
    "h-1": "<p>Output Variables</p>",
    "h-2": "<p>Node Outcomes</p>",
    "0-0": "<p><strong>Salesforce Org.Instance</strong></p><ul><li>The unique identifier for salesforce identity<br></li></ul><strong>Contact ID</strong></p><ul><li>Specifies the unique identification number of contact</li></ul><p><strong>Last Name</strong></p><ul><li>Specifies the last name of the user</li></ul><p>First Name (Optional)</p><ul><li>Specifies the first name of the user<br>Salutation (Optional)</li></ul><p><strong>Other Street (Optional)</strong></p><ul><li>Specifies the street number</li></ul><p><strong>Other City (Optional)</strong></p><ul><li>Specifies the name of the city</li></ul><p><strong>Other State (Optional)</strong></p><ul><li>Specifies the name of the state</li></ul><p><strong>Other Postal Code (Optional)</strong></p><ul><li>Specifies the postal code of the area</li></ul><p><strong>Other Country (Optional)</strong></p><ul><li>Specifies the name of the country</li></ul><p>Mailing Street  (Optional)<br>Mailing City (Optional)<br>Mailing State (Optional)<br>Mailing Postal Code  (Optional)<br>Mailing Country  (Optional)<br><strong>Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p>Fax (Optional)</p><ul><li>Specifies the fax number of the user</li></ul><p>Mobile Phone (Optional)</p><ul><li>Specifies the mobile phone number of the user</li></ul><p><strong>Home Phone (Optional)</strong></p><ul><li>Specifies the home phone number of the user</li></ul><p><strong>Other Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p><strong>Assistance Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p>Report to ID (Optional)<br><strong>Email (Optional)</strong></p><ul><li>Specifies the email address of the user</li></ul><p><strong>Title (Optional)</strong></p><ul><li>Specifies the title of the user</li></ul><p><strong>Department (Optional)</strong></p><ul><li>Specifies the department name of the user</li></ul><p><strong>Assistant Name (Optional)</strong></p><ul><li>Specifies the name of the assistant</li></ul><p>Lead Source(Optional)</p><p><strong>Birthdate</strong></p><ul><li>Specifies the birthdate of the user</li></ul><p>Description (Optional)</p>",
    "0-1": "None",
    "0-2": "Success  \nError"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Delete Contact

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b587fefb5d2c6a0236cf32946e38d6c30973e3153cc308f48872be0387103bf0-Delete_Contact.png",
        "Salesforce_DeleteContact.jpg",
        "Screenshot of Delete Contact method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Delete Contact method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Salesforce Org.Instance  \n  \n<ul><li>The unique identifier for salesforce identity</li></ul>Contact ID",
    "0-1": "None",
    "0-2": "Success  \nError"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Insert Case

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4601e2d902379bf9bd8af1b7fe37f4bf5b426c00fac61ef6e02f0fa705dd8dd1-Insert_Case.png",
        "Salesforce_Insert Case.jpg",
        "Screenshot of Insert Case method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Insert Case method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Salesforce Org.Instance  \n  \n<ul><li>The unique identifier for salesforce identity</li></ul>Contact ID (Optional)\nAsset ID (Optional)\nAccount ID (Optional)\nParent ID (Optional)\nSupplied Name (Optional)\nSupplied Email (Optional)\nSupplied Phone (Optional)\nSupplied Company (Optional)\nType (Optional)\nStatus\nReason (Optional)\nOrigin\nSubject (Optional)\nPriority (Optional)\nDescription (Optional)\nComment (Optional)",
    "0-1": "caseId  \nsuccess  \nerror",
    "0-2": "Success  \nError"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Update Case

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/95867080b0aa9865415411430e6db92c83b5933a42cb21d911ea105094c9adcb-Update_Case.png",
        "Salesforce_Update Case.jpg",
        "Screenshot of Update Case method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Update Case method configuration page"
    }
  ]
}
[/block]


### Method Name - Get Case

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dc61f632a80e64aa898ebdf13973fecdf0e4d05d3351d93d7207e45ecd90958e-Get_Case.png",
        "",
        "Screenshot of Get Case method configuration page."
      ],
      "align": "center",
      "caption": " Get Case method configuration page"
    }
  ]
}
[/block]


### Method Name - Create Record

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d067191bdd136f3a07f567acbc1943ba9e74adf9fe939c211814f7141425cab1-image.png",
        null,
        "Screenshot of Create Record method configuration page"
      ],
      "align": "center",
      "border": true,
      "caption": " Create Record method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "**Node Authentication**  \n •Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  \n  \n**Version**  \n•Select Salesforce object version. It is recommended to use the latest version.  \n  \n**Object Name**  \n•Objects are fetched specific to the version. This includes a list of standard and custom Salesforce objects. For example, select the object name as “Account.”  \n  \n**Request Body Object**  \n•To pass the Complete Object as the request body object in the API request to Salesforce, pass the entire object as JSON in the Field(s).  \nTo pass the Individual Parameters as key value pairs in the request body object. The entered Key value pairs is passed as JSON to Salesforce.  \n  \n**Field(s)**  \n•To include custom fields enable Dynamic Field(s) option and enter the Field API Name and Field Value.",
    "0-1": "**id **  \n•The unique record ID of the  created record.  \n  \n**inSuccess**  \n•It is a Boolean value that returns True if the record creation is successful and False if it fails.  \n  \n**errorsMessage**  \n•Error message provided by Salesforce when creating a record.  \n  \n**errorCode**  \n•Error code provided by Salesforce when creating a record.  \n  \n**error fields**  \n•Error fields provide the incorrect field names used in the configuration when creating a record.  \n  \n**responsePayload**  \n•This will contain the entire response after making the create record call to Salesforce.",
    "0-2": "**onInvalidData**  \n•Invalid data.  \n  \n**onError**  \n•Error while invoking the method.  \n  \n**onInvalidChoice **  \n•Invalid choice.  \n  \n**onTimeout**  \n•When the integration didn’t receive any response before the timeout (10 seconds) duration.  \n  \n**onauthorizationfail**  \n•When the selected Node Authorisation access token (token generated during authorisation) fails to authenticate it self.  \n  \n**onCreateRecordSuccess**  \n•If HTTP  status receive is 201.  \n  \n**onBadRequest**  \n•If HTTP status received is 400.  \n  \n**onCreateRecordFailure**  \n•If the HTTP status code received in the response is anything other than 201 or 400."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Get Record Using SOQL

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ae7ccc09121dcbde5cea44c0cf6640d9150d8ebceb804181d1e16e8ce7e41b4a-image.png",
        null,
        "Screenshot of Get Record Using SOQL method configuration page"
      ],
      "align": "center",
      "border": true,
      "caption": "Get Record Using SOQL method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "Input Variable",
    "h-1": "Output Variable",
    "h-2": "Node Outcomes",
    "0-0": "**Node Authentication**  \n•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  \n  \n**Version**  \n•Select Salesforce object version. It is recommended to use the latest version.  \n  \n**Query**  \n•Specify the query to fetch the details using SOQL.  \nTo learn more of SOQL please visit - [Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)  \n  \nWe advise to specify the number of rows to be returned by the SOQL query. This can be done using Limit in the query.  \n  \nYou can use SOQL builder for writing the SOQL Query - [Salesforce Developers](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/soql-builder.html)",
    "0-1": "**totalSize**  \n• An integer representing the total number of records matching the SOQL query.  \nFor example: Here, 2 represents that 2 records are found by executing the SOQL query  \n  \n**isDone **  \n•It is a Boolean value returns True or False based on the result of the executed query.  \n  \n**recordsArrayObject**  \n•Contains the Records values that are fetched from Salesforce. It contains JSON Array.  \nFor example a sample Account JSON would be :  \n{  \n  \"done\": true,  \n  \"totalSize\": 2,  \n  \"records\": [  \n    {  \n      \"attributes\": {  \n        \"type\": \"Account\",  \n        \"url\": \"/services/data/v65.0/sobjects/Account/001xxxxxxxxxxxxxxx\"  \n      },  \n      \"Id\": \"001xxxxxxxxxxxxxxx\",  \n      \"Name\": \"Sample Account 1\"  \n    },  \n    {  \n      \"attributes\": {  \n        \"type\": \"Account\",  \n        \"url\": \"/services/data/v65.0/sobjects/Account/001yyyyyyyyyyyyyyyy\"  \n      },  \n      \"Id\": \"001yyyyyyyyyyyyyyyy\",  \n      \"Name\": \"Sample Account 2\"  \n    }  \n  ]  \n}  \n  \nIn above records parameter contains the record values in array of object format.  \n  \n**errorMessage**  \n•Error message provided by Salesforce when trying to fetch the records.  \n  \n**errorCode**  \n•Error provided by Salesforce when trying to fetch the records.  \n  \n**responsePayload**  \n•This will contain the entire response received from Salesforce.",
    "0-2": "**onInvalidData**  \n•Invalid data.  \n  \n**onError**  \n•Error while invoking the method.  \n  \n**onInvalidChoice**  \n•Invalid choice.  \n  \n**onTimeout**  \n•When the integration didn’t receive any response before the timeout (10 seconds) duration.  \n  \n**onauthorizationfail**  \n•When the selected Node Authorisation access token (token generated during authorisation) fails to authenticate it self.  \n  \n**onGetRecordSuccess**  \n•If HTTP status received is 200.  \n  \n**onGetRecordFailure**  \n•If HTTP status received is other than 200 and configured error HTTP status codes.  \n  \n**onNoRecordFound**  \n•During the flow execution this edge will taken when total record size is 0 and HTTP status received is 200."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Get Record

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3afdd86b8dfaf9f7faba5061cac652a4dbfbbd1e0aa28103210d0de9e1be84f0-image.png",
        null,
        "Screenshot of Get Record configuration page"
      ],
      "align": "center",
      "border": true,
      "caption": " Get Record method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "**Node Authentication**  \n•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  \n  \n**Version**  \n•Select Salesforce object version. It is recommended to use the latest version.  \n  \n**Object Name**  \n•Objects are fetched specific to the version. This includes a list of standard and custom Salesforce objects. For example, select the object name as “Account.”  \n  \n**Object Record**  \n•Please specify the account ID for which the record should be retrieved.  \n  \n**Fields**  \n•Select the fields you need to fetch. If you have to fetch any dynamic fields. Toggle on the Dynamic fields option and pass the API name of the field, which is available in Salesforce Setup > Object Manager section. Multiple fields can be included using a comma separator.",
    "0-1": "**attributeType**  \n•Type of attribute.  \n  \n**attributeURL**  \n•AttributeURL will contain object URL. For Example: For the Account object, the URL will be “ “.  \n  \n**errorMessage**  \n•Error message provided by Salesforce when trying to fetch the records.  \n  \n**errorCode**  \n•Error provided by Salesforce when trying to fetch the records  \n  \n**errorFields**  \n•Error fields provide the incorrect field names used in the configuration when trying to fetch the records.  \n  \n**responsePayload**  \n•This will contain the entire response received from Salesforce.",
    "0-2": "**onInvalidData**  \n•Invalid data.  \n  \n**onError**  \n•Error while invoking the method.  \n  \n**onInvalidChoice**  \n•Invalid choice.  \n  \n**onTimeout**  \n•When the integration didn’t receive any response before the timeout (10 seconds) duration.  \n  \n**onauthorizationfail**  \n•When the selected Node Authorisation access token (token generated during authorisation) fails to authenticate it self.  \n  \n**onGetRecordSuccess**  \n•If HTTP status received is 200.  \n  \n**onGetRecordFailure**  \n•If HTTP status received is other than 200 and configured error HTTP status codes.  \n  \n**onNoRecordFound**  \n•This will appear when total record size is 0."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Update Record

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/86e36d14de555dc589009bb46fe62387f83a49d2c98886d65a0c05efc57604d9-image.png",
        null,
        "Screenshot of Update Record method configuration page"
      ],
      "align": "center",
      "border": true,
      "caption": "Update Record method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "**Node Authentication**  \n•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  \n  \n**Version**  \n•Select Salesforce object version. It is recommended to use the latest version.  \n  \n**Object Name**  \n•Objects are fetched specific to the version. This includes a list of standard and custom .Salesforce objects. For example, select the object name as “Account.”  \n  \n**Object Record**  \n•Object record variables associated with the variables.  \n  \n**Request Body Object**  \n•To select the Complete Object as the request body object, pass the entire object as JSON in the Field(s).To select the Individual Parameters as the request body object, pass the individual parameter. It will be shown as a key-value pair.  \n  \n**Field(s)**  \n•To include custom fields enable Dynamic Field(s) option and enter the Field API Name and Field Value.",
    "0-1": "**errorMessage**  \n•Error message provided by Salesforce when updating a record.  \n  \n**errorCode**  \n•Error code provided by Salesforce when updating a record.  \n  \n**errorfields**  \n•Error fields provide the incorrect field names used in the configuration when updating a record.  \n  \n**responsePayload**  \n•This will contain the entire response received from Salesforce.",
    "0-2": "**onInvalidData**  \n•Invalid data.  \n  \n**onError**  \n•Error while invoking the method.  \n  \n**onInvalidChoice**  \n•Invalid choice.  \n  \n**onTimeout**  \n•When the integration didn’t receive any response before the timeout (10 seconds) duration.  \n  \n**onauthorizationfail**  \n•When the selected Node Authorisation access token (tokens configured or fetched during authorisation setup) fails to authenticated by Salesforce.  \n  \n**onUpdateRecordSuccess**  \n•If HTTP status received is 204.  \n  \n**onUpdateRecordFailure**  \n•If HTTP status received is other than 204 and the specific error edges mentioned in the above node outcomes."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Method Name - Delete Record

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b65150d813f9d1e48f5bd2d5a4df42be78f59bcdc1d938303f26bc1e9759918f-image.png",
        null,
        "Delete Record method configuration page"
      ],
      "align": "center",
      "border": true,
      "caption": "Delete Record method configuration page"
    }
  ]
}
[/block]


**Parameter Table**

Following are the UI parameters that are required to call this method:

[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "**Node Authentication**  \n•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  \n  \n**Version**  \n•Select Salesforce object version. It is recommended to use the latest version.  \n  \n**Object Name  **  \n•Objects are fetched specific to the version. This includes a list of standard and custom Salesforce objects. For example, select the object name as “Account.”  \n  \n**Object Record**  \n•Object record variables associated with the variables.",
    "0-1": "**errorMessage**  \n•Error message provided by Salesforce when deleting a record.  \n  \n**errorCode**  \n•Error code provided by Salesforce when deleting a record.  \n  \n**errorfields**  \n•Error fields provide the incorrect field names used in the configuration when deleting a record.  \n  \n**responsePayload**  \n•This will contain the entire response received from Salesforce.",
    "0-2": "**onInvalidData**  \n•Invalid data.  \n  \n**onError**  \n•Error while invoking the method.  \n  \n**onInvalidChoice**  \n•Invalid choice.  \n  \n**onTimeout**  \n•When the method could not be invoked before the timeout (10 seconds) duration.  \n  \n**onauthorizationfail**  \n•When the selected Node Authorisation access token (token generated during authorisation) fails to authenticate it self.  \n  \n**onDeleteRecordSuccess**  \n•If HTTP status received is 204.  \n  \n**onDeleteRecordFailure**  \n•If HTTP status received is other than 204 and the specific error edges mentioned in the above node outcomes."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]