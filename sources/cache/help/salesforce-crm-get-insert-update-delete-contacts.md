# Salesforce CRM

Source: https://help.webexconnect.io/docs/salesforce-crm-get-insert-update-delete-contacts
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:07+00:00

## Introduction

Webex Connect offers an out of the box pre-built integration node for Salesforce that enables you to easily perform CRUD operations on all standard and custom Salesforce objects. You can also use SOQL queries on all standard and custom Salesforce Objects within a Webex Connect flow to retrieve information from your Salesforce CRM.

In previous versions, this integration allows you to insert, update, delete, and retrieve contacts from your Salesforce account within a flow. Additionally, you can get, insert, or update cases in your Salesforce account using this node. It also allows you to Create, Get, Update, or Delete Record in your Salesforce account.



![Screenshot of Salesforce CRM](https://files.readme.io/f78e2b3-Salesforce_Integration_Node.PNG)




## Version Supported

> 📘 
> 
> The latest version (v2.1) of the integration lets you select the Salesforce API version. Where as the versions older to v2.0 uses Salesforce API v43.0.

## Pre-requisites

To get Salesforce nodes enabled:

- This node needs to be enabled for your Webex Connect tenant and is not available by default. Please contact your account manager in case you wish to enable it for your account.
- Tenant would need a Salesforce account.
- This integration is available only in the cloud version of Webex Connect.
- Callback URLs for all your pre-built integrations, custom integration configurations, that use OAuth 2.0 authorization with ‘Auth Code’ Grant Type will be updated with Webex Connect  branded URLs. This doesn’t impact functioning of any of your existing integration configurations until the Refresh Token for that integration expires or until you decide to reauthorize. In either of these two cases, you would need to start using the new Callback URL provided on Webex Connect  UI in the third-party application you have integrated with. Another example of this is OAuth 2.0 based authentication for Gmail when using SMTP for Outbound Email channel configuration which is currently available only for Webex Connect  tenants used for Webex Contact Center Integration.  
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



![Get Contact method configuration page](https://files.readme.io/a8465c0-image.png)




5. You can see the data that this node generates under the Output Variables section. These [variables](https://help.webexconnect.io/docs/variable-management-in-flows) are available for use in subsequent nodes. E.g., Get Contact method returns various fields associated with the searched contact in your Salesforce account. 

6. You can see the list of possible node outcomes for this node under 'Node Outcomes' section. Examples include, 'No Content found', 'Multiple records', 'OnTimeout', etc.

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

### Method Name - Get Contact



![Get Contact method configuration page](https://files.readme.io/b37393a01bb1f58b41199d49f34d94114e739c32cad640a8a370488e0863cbf6-Get_Contact.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> |
| --- | --- | --- |
| <p>Salesforce Org.Instance <ul><li>The unique identifier for salesforce identity</li></ul><p>Field API Name<br>Value to Query</p> | <p>attributesType<br>attributesURL</p><p><strong>contactId</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p>isDeleted<br><strong>accountId</strong></p><ul><li>Contains the unique identification number of the contact</li></ul><p><strong>firstName</strong></p><ul><li>Contains the first name of the user</li></ul><p><strong>lastName</strong></p><ul><li>Contains the last name of the user</li></ul><p><strong>Name</strong></p><ul><li>Contains the full name of the user</li></ul><p><strong>mailingStreet</strong></p><ul><li>Contains the street number</li></ul><p><strong>mailingCity</strong></p><ul><li>Contains the city name</li></ul><p><strong>mailingState</strong></p><ul><li>Contains the state name</li></ul><p><strong>mailingPostalCode</strong></p><ul><li>Contains the postal code of the area</li></ul><p><strong>mailingCountry</strong></p><ul><li>Contains the name of the country</li></ul><p>mailingAddresscity<br>mailingAddressCountry<br>mailingAddressPostalCode<br>mailingAddressState<br>mailingAddressStreet</p><p><strong>Phone</strong></p><ul><li>Contains the phone number of the user</li></ul><p><strong>homePhone</strong></p><ul><li>Contains the home phone number of the user</li></ul><p><strong>assitantPhone</strong></p><ul><li>Contains the phone number of the assitant</li></ul><p><strong>Email</strong></p><ul><li>Contains the email address of the user</li></ul><p>leadSource</p><p><strong>CreatedDate</strong></p><ul><li>Contains the date on which the record is created</li></ul><p><strong>CreatedById</strong></p><ul><li>Contains the unique identification number of the user who created  the record</li></ul><p>lastModifiedDate</p><ul><li>Contains the date on which the record is modified</li></ul><p>systemModStamp</p><p>lastActivityDate</p><p>lastViewedDate<br>lastReferencedDate<br>isEmailBounced<br>photoURL<br>cleanStatus</p> | Success  <br>Multiple records  <br>No content found  <br>Session expired  <br>Error |




### Method Name - Insert Contact



![Insert Contact method configuration page](https://files.readme.io/b8f16041fdefedec8862397e24d35d830b2b190a69025a9dcf4387de825df2d7-Insert_Contact.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> |
| --- | --- | --- |
| <p><strong>Salesforce Org.Instance</strong></p><ul><li>The unique identifier for salesforce identity</li></ul><p><strong>Last Name</strong></p><ul><li>Specifies the last name of the user</li></ul><p>First Name (Optional)</p><ul><li>Specifies the first name of the user</li></ul><p>Salutation (Optional)</p><p><strong>Other Street (Optional)</strong></p><ul><li>Specifies the street number</li></ul><p><strong>Other City (Optional)</strong></p><ul><li>Specifies the name of the city</li></ul><p><strong>Other State (Optional)</strong></p><ul><li>Specifies the name of the state</li></ul><p><strong>Other Postal Code (Optional)</strong></p><ul><li>Specifies the postal code of the area </li></ul><p><strong>Other Country (Optional)</strong></p><ul><li>Specifies the name of country<br>Mailing Street  (Optional)<br>Mailing City  (Optional)<br>Mailing State (Optional)<br>Mailing Postal Code  (Optional)<br>Mailing Country  (Optional)</li></ul><p><strong>Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p>Fax (Optional)</p><ul><li>Specifies the fax number of the user</li></ul><p>Mobile Phone (Optional)</p><ul><li>Specifies the mobile phone number of the user</li></ul><p><strong>Home Phone (Optional)</strong></p><ul><li>Specifies the home phone number of the user</li></ul><p><strong>Other Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p><strong>Assistance Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p>Report to ID (Optional)</p><p><strong>Email (Optional)</strong></p><ul><li>Specifies the email address of the user</li></ul><p><strong>Title (Optional)</strong></p><ul><li>Specifies the title of the user</li></ul><p><strong>Department (Optional)</strong></p><ul><li>Specifies the department name of the user</li></ul><p><strong>Assistant Name (Optional)</strong></p><ul><li>Specifies the name of the assistant</li></ul><p>Lead Source(Optional)</p><p><strong>Birthdate</strong></p><ul><li>Specifies the birthdate of the user</li></ul><p>Description (Optional)</p> | contactId  <br>success  <br>error | Success  <br>Error |




### Method Name - Update Contact



![Update Contact method configuration page](https://files.readme.io/b6e4374cf9dc17a1ba58285ba0bcaa533039537a6161c027c325bbc95a9d96be-Update_Contact.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| <p>Input Variables</p> | <p>Output Variables</p> | <p>Node Outcomes</p> |
| --- | --- | --- |
| <p><strong>Salesforce Org.Instance</strong></p><ul><li>The unique identifier for salesforce identity<br></li></ul><strong>Contact ID</strong></p><ul><li>Specifies the unique identification number of contact</li></ul><p><strong>Last Name</strong></p><ul><li>Specifies the last name of the user</li></ul><p>First Name (Optional)</p><ul><li>Specifies the first name of the user<br>Salutation (Optional)</li></ul><p><strong>Other Street (Optional)</strong></p><ul><li>Specifies the street number</li></ul><p><strong>Other City (Optional)</strong></p><ul><li>Specifies the name of the city</li></ul><p><strong>Other State (Optional)</strong></p><ul><li>Specifies the name of the state</li></ul><p><strong>Other Postal Code (Optional)</strong></p><ul><li>Specifies the postal code of the area</li></ul><p><strong>Other Country (Optional)</strong></p><ul><li>Specifies the name of the country</li></ul><p>Mailing Street  (Optional)<br>Mailing City (Optional)<br>Mailing State (Optional)<br>Mailing Postal Code  (Optional)<br>Mailing Country  (Optional)<br><strong>Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p>Fax (Optional)</p><ul><li>Specifies the fax number of the user</li></ul><p>Mobile Phone (Optional)</p><ul><li>Specifies the mobile phone number of the user</li></ul><p><strong>Home Phone (Optional)</strong></p><ul><li>Specifies the home phone number of the user</li></ul><p><strong>Other Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p><strong>Assistance Phone (Optional)</strong></p><ul><li>Specifies the phone number of the user</li></ul><p>Report to ID (Optional)<br><strong>Email (Optional)</strong></p><ul><li>Specifies the email address of the user</li></ul><p><strong>Title (Optional)</strong></p><ul><li>Specifies the title of the user</li></ul><p><strong>Department (Optional)</strong></p><ul><li>Specifies the department name of the user</li></ul><p><strong>Assistant Name (Optional)</strong></p><ul><li>Specifies the name of the assistant</li></ul><p>Lead Source(Optional)</p><p><strong>Birthdate</strong></p><ul><li>Specifies the birthdate of the user</li></ul><p>Description (Optional)</p> | None | Success  <br>Error |




### Method Name - Delete Contact



![Delete Contact method configuration page](https://files.readme.io/b587fefb5d2c6a0236cf32946e38d6c30973e3153cc308f48872be0387103bf0-Delete_Contact.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Salesforce Org.Instance  <br>  <br><ul><li>The unique identifier for salesforce identity</li></ul>Contact ID | None | Success  <br>Error |




### Method Name - Insert Case



![Insert Case method configuration page](https://files.readme.io/4601e2d902379bf9bd8af1b7fe37f4bf5b426c00fac61ef6e02f0fa705dd8dd1-Insert_Case.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Salesforce Org.Instance  <br>  <br><ul><li>The unique identifier for salesforce identity</li></ul>Contact ID (Optional)<br>Asset ID (Optional)<br>Account ID (Optional)<br>Parent ID (Optional)<br>Supplied Name (Optional)<br>Supplied Email (Optional)<br>Supplied Phone (Optional)<br>Supplied Company (Optional)<br>Type (Optional)<br>Status<br>Reason (Optional)<br>Origin<br>Subject (Optional)<br>Priority (Optional)<br>Description (Optional)<br>Comment (Optional) | caseId  <br>success  <br>error | Success  <br>Error |




### Method Name - Update Case



![Update Case method configuration page](https://files.readme.io/95867080b0aa9865415411430e6db92c83b5933a42cb21d911ea105094c9adcb-Update_Case.png)




### Method Name - Get Case



![ Get Case method configuration page](https://files.readme.io/dc61f632a80e64aa898ebdf13973fecdf0e4d05d3351d93d7207e45ecd90958e-Get_Case.png)




### Method Name - Create Record



![ Create Record method configuration page](https://files.readme.io/d067191bdd136f3a07f567acbc1943ba9e74adf9fe939c211814f7141425cab1-image.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Node Authentication**  <br> •Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  <br>  <br>**Version**  <br>•Select Salesforce object version. It is recommended to use the latest version.  <br>  <br>**Object Name**  <br>•Objects are fetched specific to the version. This includes a list of standard and custom Salesforce objects. For example, select the object name as “Account.”  <br>  <br>**Request Body Object**  <br>•To pass the Complete Object as the request body object in the API request to Salesforce, pass the entire object as JSON in the Field(s).  <br>To pass the Individual Parameters as key value pairs in the request body object. The entered Key value pairs is passed as JSON to Salesforce.  <br>  <br>**Field(s)**  <br>•To include custom fields enable Dynamic Field(s) option and enter the Field API Name and Field Value. | **id **  <br>•The unique record ID of the  created record.  <br>  <br>**inSuccess**  <br>•It is a Boolean value that returns True if the record creation is successful and False if it fails.  <br>  <br>**errorsMessage**  <br>•Error message provided by Salesforce when creating a record.  <br>  <br>**errorCode**  <br>•Error code provided by Salesforce when creating a record.  <br>  <br>**error fields**  <br>•Error fields provide the incorrect field names used in the configuration when creating a record.  <br>  <br>**responsePayload**  <br>•This will contain the entire response after making the create record call to Salesforce. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice **  <br>•Invalid choice.  <br>  <br>**onTimeout**  <br>•When the integration didn’t receive any response before the timeout (10 seconds) duration.  <br>  <br>**onauthorizationfail**  <br>•When the selected Node Authorisation access token (token generated during authorisation) fails to authenticate it self.  <br>  <br>**onCreateRecordSuccess**  <br>•If HTTP  status receive is 201.  <br>  <br>**onBadRequest**  <br>•If HTTP status received is 400.  <br>  <br>**onCreateRecordFailure**  <br>•If the HTTP status code received in the response is anything other than 201 or 400. |




### Method Name - Get Record Using SOQL



![Get Record Using SOQL method configuration page](https://files.readme.io/ae7ccc09121dcbde5cea44c0cf6640d9150d8ebceb804181d1e16e8ce7e41b4a-image.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variable | Output Variable | Node Outcomes |
| --- | --- | --- |
| **Node Authentication**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  <br>  <br>**Version**  <br>•Select Salesforce object version. It is recommended to use the latest version.  <br>  <br>**Query**  <br>•Specify the query to fetch the details using SOQL.  <br>To learn more of SOQL please visit - [Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm)  <br>  <br>We advise to specify the number of rows to be returned by the SOQL query. This can be done using Limit in the query.  <br>  <br>You can use SOQL builder for writing the SOQL Query - [Salesforce Developers](https://developer.salesforce.com/docs/platform/sfvscode-extensions/guide/soql-builder.html) | **totalSize**  <br>• An integer representing the total number of records matching the SOQL query.  <br>For example: Here, 2 represents that 2 records are found by executing the SOQL query  <br>  <br>**isDone **  <br>•It is a Boolean value returns True or False based on the result of the executed query.  <br>  <br>**recordsArrayObject**  <br>•Contains the Records values that are fetched from Salesforce. It contains JSON Array.  <br>For example a sample Account JSON would be :  <br>{  <br>  "done": true,  <br>  "totalSize": 2,  <br>  "records": [  <br>    {  <br>      "attributes": {  <br>        "type": "Account",  <br>        "url": "/services/data/v65.0/sobjects/Account/001xxxxxxxxxxxxxxx"  <br>      },  <br>      "Id": "001xxxxxxxxxxxxxxx",  <br>      "Name": "Sample Account 1"  <br>    },  <br>    {  <br>      "attributes": {  <br>        "type": "Account",  <br>        "url": "/services/data/v65.0/sobjects/Account/001yyyyyyyyyyyyyyyy"  <br>      },  <br>      "Id": "001yyyyyyyyyyyyyyyy",  <br>      "Name": "Sample Account 2"  <br>    }  <br>  ]  <br>}  <br>  <br>In above records parameter contains the record values in array of object format.  <br>  <br>**errorMessage**  <br>•Error message provided by Salesforce when trying to fetch the records.  <br>  <br>**errorCode**  <br>•Error provided by Salesforce when trying to fetch the records.  <br>  <br>**responsePayload**  <br>•This will contain the entire response received from Salesforce. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onTimeout**  <br>•When the integration didn’t receive any response before the timeout (10 seconds) duration.  <br>  <br>**onauthorizationfail**  <br>•When the selected Node Authorisation access token (token generated during authorisation) fails to authenticate it self.  <br>  <br>**onGetRecordSuccess**  <br>•If HTTP status received is 200.  <br>  <br>**onGetRecordFailure**  <br>•If HTTP status received is other than 200 and configured error HTTP status codes.  <br>  <br>**onNoRecordFound**  <br>•During the flow execution this edge will taken when total record size is 0 and HTTP status received is 200. |




### Method Name - Get Record



![ Get Record method configuration page](https://files.readme.io/3afdd86b8dfaf9f7faba5061cac652a4dbfbbd1e0aa28103210d0de9e1be84f0-image.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Node Authentication**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  <br>  <br>**Version**  <br>•Select Salesforce object version. It is recommended to use the latest version.  <br>  <br>**Object Name**  <br>•Objects are fetched specific to the version. This includes a list of standard and custom Salesforce objects. For example, select the object name as “Account.”  <br>  <br>**Object Record**  <br>•Please specify the account ID for which the record should be retrieved.  <br>  <br>**Fields**  <br>•Select the fields you need to fetch. If you have to fetch any dynamic fields. Toggle on the Dynamic fields option and pass the API name of the field, which is available in Salesforce Setup > Object Manager section. Multiple fields can be included using a comma separator. | **attributeType**  <br>•Type of attribute.  <br>  <br>**attributeURL**  <br>•AttributeURL will contain object URL. For Example: For the Account object, the URL will be “ “.  <br>  <br>**errorMessage**  <br>•Error message provided by Salesforce when trying to fetch the records.  <br>  <br>**errorCode**  <br>•Error provided by Salesforce when trying to fetch the records  <br>  <br>**errorFields**  <br>•Error fields provide the incorrect field names used in the configuration when trying to fetch the records.  <br>  <br>**responsePayload**  <br>•This will contain the entire response received from Salesforce. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onTimeout**  <br>•When the integration didn’t receive any response before the timeout (10 seconds) duration.  <br>  <br>**onauthorizationfail**  <br>•When the selected Node Authorisation access token (token generated during authorisation) fails to authenticate it self.  <br>  <br>**onGetRecordSuccess**  <br>•If HTTP status received is 200.  <br>  <br>**onGetRecordFailure**  <br>•If HTTP status received is other than 200 and configured error HTTP status codes.  <br>  <br>**onNoRecordFound**  <br>•This will appear when total record size is 0. |




### Method Name - Update Record



![Update Record method configuration page](https://files.readme.io/86e36d14de555dc589009bb46fe62387f83a49d2c98886d65a0c05efc57604d9-image.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Node Authentication**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  <br>  <br>**Version**  <br>•Select Salesforce object version. It is recommended to use the latest version.  <br>  <br>**Object Name**  <br>•Objects are fetched specific to the version. This includes a list of standard and custom .Salesforce objects. For example, select the object name as “Account.”  <br>  <br>**Object Record**  <br>•Object record variables associated with the variables.  <br>  <br>**Request Body Object**  <br>•To select the Complete Object as the request body object, pass the entire object as JSON in the Field(s).To select the Individual Parameters as the request body object, pass the individual parameter. It will be shown as a key-value pair.  <br>  <br>**Field(s)**  <br>•To include custom fields enable Dynamic Field(s) option and enter the Field API Name and Field Value. | **errorMessage**  <br>•Error message provided by Salesforce when updating a record.  <br>  <br>**errorCode**  <br>•Error code provided by Salesforce when updating a record.  <br>  <br>**errorfields**  <br>•Error fields provide the incorrect field names used in the configuration when updating a record.  <br>  <br>**responsePayload**  <br>•This will contain the entire response received from Salesforce. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onTimeout**  <br>•When the integration didn’t receive any response before the timeout (10 seconds) duration.  <br>  <br>**onauthorizationfail**  <br>•When the selected Node Authorisation access token (tokens configured or fetched during authorisation setup) fails to authenticated by Salesforce.  <br>  <br>**onUpdateRecordSuccess**  <br>•If HTTP status received is 204.  <br>  <br>**onUpdateRecordFailure**  <br>•If HTTP status received is other than 204 and the specific error edges mentioned in the above node outcomes. |




### Method Name - Delete Record



![Delete Record method configuration page](https://files.readme.io/b65150d813f9d1e48f5bd2d5a4df42be78f59bcdc1d938303f26bc1e9759918f-image.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Node Authentication**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Salesforce pre-built integration).  <br>  <br>**Version**  <br>•Select Salesforce object version. It is recommended to use the latest version.  <br>  <br>**Object Name  **  <br>•Objects are fetched specific to the version. This includes a list of standard and custom Salesforce objects. For example, select the object name as “Account.”  <br>  <br>**Object Record**  <br>•Object record variables associated with the variables. | **errorMessage**  <br>•Error message provided by Salesforce when deleting a record.  <br>  <br>**errorCode**  <br>•Error code provided by Salesforce when deleting a record.  <br>  <br>**errorfields**  <br>•Error fields provide the incorrect field names used in the configuration when deleting a record.  <br>  <br>**responsePayload**  <br>•This will contain the entire response received from Salesforce. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onTimeout**  <br>•When the method could not be invoked before the timeout (10 seconds) duration.  <br>  <br>**onauthorizationfail**  <br>•When the selected Node Authorisation access token (token generated during authorisation) fails to authenticate it self.  <br>  <br>**onDeleteRecordSuccess**  <br>•If HTTP status received is 204.  <br>  <br>**onDeleteRecordFailure**  <br>•If HTTP status received is other than 204 and the specific error edges mentioned in the above node outcomes. |

