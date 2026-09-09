# Customer Journey Data

Source: https://help.webexconnect.io/docs/customer-journey-data
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:08+00:00

## Introduction

Customer Journey Data Service (CJDS) is a next generation customer journey management service that enables businesses to capture customer journeys across any channel or application, identify insights, and take real-time actions to provide an excellent customer experience.

This node is available only for all Flex 3 Webex Contact Customers.

> 🚧 
> 
> We recommend dragging a new Journey node onto your canvas and reconfiguring it especially If it was part of a previously executed flow (Early Access). This follows the introduction of the new "Read from CJDS" method and updating the earlier "Read from CJDS"  method to "Read from Progressive File" method. This ensures your flow utilizes the latest functionality.

Journey node facilitates Webex Connect users with the following five methods:

- [Manage Identity](#method-name-manage-identity) - This method merges one or more aliases in JDS.
- [Write to CJDS](#method-name-write-to-cjds) - This method accepts events that describe what occurred, when, and by whom on every interaction across touch points and applications.
- [Get Identity By Aliases](#method-name-get-identity-by-aliases) - This method is used for fetching alias details using alias IDs( if we have to use multiple alias IDs then alias IDs must be comma(,) separated.
- [Read from Progressive Profile](#method-name-read-from-cjds) - This method is used for fetching the progressive history of alias with business.
- [Read from CJDS](#method-name-read-from-cjds) - This method is used for contact centers to access recent customer events and behaviors in real time.

## Version Supported

> 📘 Note
> 
> This integration is based on Customer Journey Data API v1.
> 
> We recommend using the latest version of the Customer Journey Data prebuilt node, v2.1.2. If your flow uses the older v1.0 node, add the latest Customer Journey Data node to the flow canvas, reconfigure it, and test the flow before publishing.
> 
> The older v1.0 node will be deprecated in a future release. Existing v1.0 flows can continue to run until deprecation, but customers should plan to upgrade to the latest node version.

## Prerequisites

To get Journey nodes enabled:

- Webex account backed by Cisco Webex Common Identity (CI) with a Contact Center Administrator role assigned on Control Hub. For more information on how to assign an administrator, refer to the [Administration Guide](https://help.webex.com/en-us/article/n5jdj19/Webex-Contact-Center-Administrator-Roles-and-Privileges) 
- A client ID and client secret pair (request a pair).

## Authentication

The authentication used is standard OAuth2.0 authorization code grant flow. For detailed information, please visit this [Webex Contact Center for Developers](https://developer.webex-cx.com/documentation/authentication).

## Methods and Outcomes

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

### Method Name - Manage Identity

The Manage Identity method allows you to merge multiple customer aliases into a single, unified customer profile. Using the identifier provided by the customer, you can perform a data dip into your CRM or customer repository to retrieve additional details—such as first name, last name, phone number(s), email(s), social ID(s) like Apple ID, and unique customer identifiers like membership numbers. These details can then be passed into the journey node to create a comprehensive customer profile that consolidates all known identities. This ensures you don’t lose track of any customer interactions across channels.

**Additional Use Cases:**

- **Adding a New Alias:**  
  To add a new alias to an existing customer profile, simply update the alias in your CRM or customer repository. Pass the updated values into the journey node as you would when creating a new customer. The profile will automatically update to include the new alias.
- **Removing an Alias:**  
  To remove an alias from a customer profile, set the override flag to true. When new values are passed with this flag enabled, all previous identifiers will be removed and replaced with the new set of values.



![Manage Identity](https://files.readme.io/801e7c523592b3604d75c9c22c7db47e97ebce62e9d6373a4b65f3223f88fe23-CJS_1.png)




**Parameter Table**

Following are the UI parameters that are required to call this method.



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Authorization**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Customer Journey Data pre-built integration).  <br>  <br>**Workspace/Project**  <br>•Select available workspace or project present in customer journey data.  <br>  <br>**Request Body**  <br>•Please specify how you want to pass request body variables. Request body variables can be passed as JSON Object or as a individual key/value pair.  <br>  <br>**First Name**  <br>•You can add multiple first names to the alias.  <br>Example: "John".  <br>  <br>**Last Name**  <br>•You can add multiple last names to the alias.  <br>Example: "Jacob".  <br>  <br>**Aliases**  <br>Phone Number  <br>•Phone number of the Alias, you can add multiple phone number separating them with commas.  <br>  <br>**Email**  <br>•Email of the Alias, you can add multiple email separating them with commas.  <br>  <br>**Customer ID**  <br>•Customer ID of the Alias, you can add multiple customer IDs separating them with commas.  <br>  <br>**Temporary ID**  <br>•Temporary  ID of the Alias, you can add multiple temporary IDs separating them with commas.  <br>  <br>**Overwrite existing person data**  <br>•A Boolean value it can either be true or false. By default it is false. | **firstName**  <br>•Alias first name.  <br>  <br>**lastName**  <br>•Alias last name.  <br>  <br>**aliases**  <br>•Array of all the identities associated with alias. For e.g., array can contain all phone numbers or email ids, social ids, customer ids, temporary ids or can contain all of the elements.  <br>  <br>**phone**  <br>•Array of all phone numbers associated with alias.  <br>  <br>**temporaryId**  <br>•Array of all temporary ids associated with alias.  <br>  <br>**socialId**  <br>•Array of all social ids associated with alias.  <br>  <br>**customerId**  <br>•Array of all customer ids associated with alias.  <br>  <br>**id**  <br>•Alias Id.  <br>  <br>**email**  <br>•Array of all email ids associated with alias.  <br>  <br>**organizationId**  <br>•Unique organization id.  <br>  <br>**status**  <br>•HTTP error name.  <br>  <br>**message**  <br>•Type of error.  <br>  <br>**errors**  <br>•Array of error messages.  <br>  <br>**trackingId**  <br>•Error tracking unique id.  <br>  <br>**responsePayload**  <br>•This will contain all the JSON response object in single variable. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onBadRequest**  <br>•If HTTP status received is 400.  <br>  <br>**onForbidden**  <br>•If HTTP status received is 403.  <br>  <br>**onNotFound**  <br>• If HTTP status received is 404  <br>  <br>**onTooManyRequest**  <br>•If HTTP status received is 429.  <br>  <br>**onInternalServerError**  <br>•If HTTP status received is 500.  <br>  <br>**onCreateMergeAliasesSuccess**  <br>•If HTTP status received is 202.  <br>  <br>**onCreateMergeAliasesFailure**  <br>•If HTTP status received is other than 202 and configured error HTTP status codes.  <br>  <br>**onTimeout**  <br>•When the method could not be invoked before the timeout (10 seconds) duration. |




> 👍 Important
> 
> The Manage Identity method allows you to pass multiple phone number, email id, customer Id, temporary id,and social Id. These values should be separated using comma (',').
> 
> For Example: If you have multiple phone numbers, email id, customer Id, temporary id,and social Id. You can pass them in following format:
> 
> - $(phone1),$(phone2),$(phone3)
> - $(email1),$(email2),$(email3)
> - $(temporaryId1),$(temporaryId2),$(temporaryId3)
> - $(customerId1),$(tcustomerId2),$(customerId3)
> - $(sociald1),$(socialId2),$(tsocialId3)



![Manage Identity Method Showcasing Multiple Aliases ](https://files.readme.io/9031b26a543082f25f6c35c469114b5aa9ddcfaf85cc16e2cc953ab24ee1b2b4-12_10_56.jpg)




**HTTP Status Codes**

| Status code                                                      | Description                 |
| :--------------------------------------------------------------- | :-------------------------- |
| 400                                                              | onBadRequest                |
| 403                                                              | onForbidden                 |
| 404                                                              | onNotFound                  |
| 429                                                              | onTooManyRequest            |
| 500                                                              | onInternalServerError       |
| 202                                                              | onCreateMergeAliasesSuccess |
| All HTTP Status codes other than 400, 403, 404, 429, 500 and 202 | onCreateMergeAliasesFailure |

### Method Name - Write to CJDS

The Write to CJDS method enables you to capture and store data from your flow or third-party applications directly within the Customer Journey Data Service (CJDS). This allows businesses to enhance customer profiles with real-time insights, ensuring agents have the most up-to-date and relevant information to personalize interactions.

By writing data such as IVR menu selections, payment details, or ticket updates into CJDS, you can build a comprehensive view of customer interactions across different touchpoints. This data can then be used to improve decision-making, streamline workflows, and enhance the overall customer experience.

**Example Use Cases:**

- **Enhanced Agent Assistance:**  
  A customer selects a refund request option in the IVR menu. This selection is written to CJDS. When the customer later connects with an agent, the agent immediately sees the refund request in the customer’s journey history, allowing for faster resolution.
- **Proactive Customer Engagement:**  
  A customer makes a payment through a third-party billing system. This transaction data is written to CJDS and flagged for proactive engagement. If the customer calls in with a billing question, the system recognizes the recent payment and routes them directly to the billing support team, avoiding unnecessary transfers.

This method ensures that customer interactions are always contextualized, improving efficiency and delivering a more seamless support experience.



![Write to CJDS](https://files.readme.io/f1fa648b569bb1ec77832e87d6f1d7e60c46a947c97cd23ff77779e70c3b2d86-Write_to_CJDS.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Authorization**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Customer Journey Data pre-built integration)  <br>  <br>**Workspace/Project**  <br>•Select available workspace or project present in customer journey data  <br>  <br>**Request Body Object**  <br>•Please specify how you want to pass request body variables. Request body variables can be passed as JSON Object or as an individual key/value pair  <br>  <br>**Event Id**  <br>•Event Id. Example: "9ab65fdf-9643-417f-9974-ad72cae0e10f"  <br>  <br>**Event Spec Version**  <br>•Event spec version. Example: "1.0"  <br>  <br>**Event Type**  <br>•Event Type. Example: "com.cisco.wxcc.event.agent"  <br>  <br>**Event Source**  <br>•Event source. Example: "/com/cisco/wxcc/123"  <br>  <br>**Event Time**  <br>•Event Time. Example: "2022-08-15T22:29:43.768Z" . In UTC time format  <br>  <br>**Identity Type**  <br>•Identity Type. Example: "email". Identity type could be either email, phone, customerId, socialId or temporaryId  <br>  <br>**Identity**  <br>•Identity. Example: "[sjohndeo@cisco.com](mailto:sjohndeo@cisco.com) "  <br>  <br>**Data Object**  <br>•Data object is multi-select drop-down which contains various options. For e.g., Agent Id, Destination, Profile Type, Current State, Idle Code ID & Created Time  <br>  <br>**Agent Id**  <br>•Agent Id. Example: "109332be-7fc4-4d4d-9488-ebdb8e13b9bbe"  <br>  <br>**Destination**  <br>•Destination. Example: "+12147651210"  <br>  <br>**Profile Type**  <br>•Profile Type. Example: "BLENDED"  <br>  <br>**Current State**  <br>•Current State. Example: "idle"  <br>  <br>**Idle Code ID**  <br>•Idle code id. Example: "AXUr0jX9H5Tuplm_IxiC"  <br>  <br>**Created Time**  <br>•Created Time. Example: "1645819554383". Time in milliseconds | **data**  <br>•Array object that contains details about profile view template id, firstName, lastName, phone array, email array, socialId array, customerId array, temporary Id array, aliases array, organizationId, workspaceId and other information.  <br>  <br>**OrganizationId**  <br>•unique organization id.  <br>  <br>**workspaceId**  <br>•Workspace/Project unique id.  <br>  <br>**status**  <br>•HTTP error name.  <br>	  <br>**message**  <br>•type of error.  <br>  <br>**errors**  <br>•array of error messages.  <br>  <br>**trackingId**  <br>•error tracking unique id.  <br>  <br>**responsePayload**  <br>•This will contain all the JSON response object in single variable. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onBadRequest**  <br>•If HTTP status received is 400.  <br>  <br>**onForbidden**  <br>•If HTTP status received is 403.  <br>  <br>**onNotFound**  <br>•If HTTP status received is 404.  <br>  <br>**onTooManyRequest**  <br>•If HTTP status received is 429.  <br>  <br>**onInternalServerError**  <br>•If HTTP status received is 500.  <br>  <br>**onEventPostSuccess**  <br>•If HTTP status received is 202.  <br>  <br>**onEventPostFailure**  <br>•If HTTP status received is other than 202 and configured error HTTP status codes.  <br>  <br>**onTimeout**  <br>•When the method could not be invoked before the timeout (10 seconds) duration. |




**HTTP Status Codes**

| Status code                                                      | Description           |
| :--------------------------------------------------------------- | :-------------------- |
| 400                                                              | onBadRequest          |
| 403                                                              | onForbidden           |
| 404                                                              | onNotFound            |
| 429                                                              | onTooManyRequest      |
| 500                                                              | onInternalServerError |
| 202                                                              | onEventPostSuccess    |
| All HTTP Status codes other than 400, 403, 404, 429, 500 and 202 | onEventPostFailure    |

### Method Name - Get Identity by Aliases

The Get Identity by Aliases method allows you to retrieve all identities associated with an existing customer profile based on a known alias. This helps in seamlessly linking customer interactions across multiple channels and identifiers.

**Example Use Cases:**

- **Cross-Channel Customer Engagement:**  
  If you have a customer's phone number and want to send them an email update, use this method to fetch their associated email address.
- **Fraud Prevention & Verification:**  
  When a customer contacts support, retrieve their linked identities (such as social IDs or membership numbers) to verify authenticity and prevent fraudulent activity.
- **Omnichannel Personalization:**  
  If a customer logs into a web portal using their social media ID, use this method to pull their phone number or loyalty ID to personalize their experience across digital and voice channels.

This method ensures a seamless and connected customer experience by unifying customer identities across multiple touchpoints.



![Get Identity by Aliases](https://files.readme.io/0a2d189492bfeb75b3b1307b2888f7d00ae40a3b36dbcaa225f2d053a1a623af-2025-06-10_12-37-43.png)




**Parameters Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Authorization**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Customer Journey Data pre-built integration)  <br>  <br>**Workspace/Project**  <br>•Select available workspace or project present in customer journey data  <br>  <br>**Aliases**  <br>•Alias id associated with the particular alias. If we must use multiple alias ids then alias ids must be comma(,) separated. For e.g., [johndoe@domain1.com](mailto:johndoe@domain1.com),2771154. | **data**  <br>•Array object that contains details about profile view template id, firstName, lastName, phone array, email array, socialId array, customerId array, temporary Id array, aliases array, organizationId, workspaceId and other information.  <br>  <br>**organizationId**  <br>•unique organization Id.  <br>  <br>**id**  <br>•Person Id.  <br>  <br>**firstName**  <br>•first name of the person.  <br>  <br>**lastName**  <br>•last name of the person.  <br>  <br>**status**  <br>•HTTP error name.  <br>  <br>**message**  <br>•type of error.  <br>  <br>**errors**  <br>•array of error messages.  <br>  <br>**trackingId**  <br>•error tracking unique id.  <br>  <br>**responsePayload**  <br>•This will contain all the JSON response object in single variable. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onBadRequest**  <br>•If HTTP status received is 400.  <br>  <br>**onForbidden**  <br>•If HTTP status received is 403.  <br>  <br>**onNotFound**  <br>•If HTTP status received is 404.  <br>  <br>**onTooManyRequest**  <br>•If HTTP status received is 429.  <br>  <br>**onInternalServerError**  <br>•If HTTP status received is 500.  <br>  <br>**onGetIdentityByAliasesSuccess**  <br>•If HTTP status received is 200.  <br>  <br>**onGetIdentityByAliasesFailure**  <br>•If HTTP status received is other than 200 and configured error HTTP status codes.  <br>  <br>**onTimeout**  <br>•When the method could not be invoked before the timeout(10 seconds) duration. |




### Method Name - Read from Progressive Profile

The Read from progressive profile method allows you to retrieve a customer’s progressive journey profile in real time and use that data for intelligent call routing. This enables dynamic decision-making based on past interactions, ensuring customers are connected to the most suitable agents.

**Example Use Cases:**

- **Intelligent Call Routing Based on Interaction History:**  
  If a customer has called more than three times in the last 24 hours, you can route their call to an agent with specialized skills—such as a subject matter expert or an agent with higher customer satisfaction (CSAT) ratings—to resolve their issue more efficiently.
- **Priority Handling for High-Value Customers:**  
  Identify VIP customers based on past purchase history, subscription tier, or loyalty status, and automatically route them to a dedicated concierge team for premium support.
- **Proactive Support for Unresolved Issues:**  
  If a customer has an open support ticket or an unresolved complaint, their call can be prioritized and routed to the same agent or department handling their case, reducing customer frustration and improving resolution speed.

This method ensures every customer interaction is contextually informed, leading to better service experiences and increased operational efficiency.



![Read from Progressive Profile](https://files.readme.io/291bbf772ba2ef84434960d8b658eb97c6d0a6f0698a2b6013e4d389c9ceecb1-2025-06-10_13-59-56.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Authorization**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Customer Journey Data pre-built integration).  <br>  <br>**Workspace/Project**  <br>•Select available workspace or project present in customer journey data.  <br>  <br>**Template Name**  <br>•Valid template where progressive profile needs to be searched.  <br>  <br>**Alias ID**  <br>•Alias identifier associated with the alias. For e.g., either Phone Number, Email Address, Social Id, Customer Id or Temporary Id. | **data**  <br>•Array object that contains details about profile view template id, firstName, lastName, phone array, email array, socialId array, customerId array, temporary Id array, aliases array, organizationId, workspaceId and other information.  <br>  <br>**organizationId**  <br>•unique organization Id.  <br>  <br>**status**  <br>•HTTP error name.  <br>  <br>**message**  <br>•type of error.  <br>  <br>**errors**  <br>•array of error messages.  <br>  <br>**trackingId**  <br>•error tracking unique id.  <br>  <br>**responsePayload**  <br>•This will contain all the JSON response object in single variable. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onBadRequest**  <br>•If HTTP status received is 400.  <br>  <br>**onForbidden**  <br>•If HTTP status received is 403.  <br>  <br>**onNotFound**  <br>•If HTTP status received is 404.  <br>  <br>**onTooManyRequest**  <br>•If HTTP status received is 429.  <br>  <br>**onInternalServerError**  <br>•If HTTP status received is 500.  <br>  <br>**onGetIdentityByAliasesSuccess**  <br>•If HTTP status received is 200.  <br>  <br>**onGetIdentityByAliasesFailure**  <br>•If HTTP status received is other than 200 and configured error HTTP status codes.  <br>  <br>**onTimeout**  <br>•When the method could not be invoked before the timeout (10 seconds) duration. |




**HTTP Status Codes**

| Status code                                                      | Description                   |
| :--------------------------------------------------------------- | :---------------------------- |
| 400                                                              | onBadRequest                  |
| 403                                                              | onForbidden                   |
| 404                                                              | onNotFound                    |
| 429                                                              | onTooManyRequest              |
| 500                                                              | onInternalServerError         |
| 200                                                              | onGetIdentityByAliasesSuccess |
| All HTTP Status codes other than 400, 403, 404, 429, 500 and 200 | onGetIdentityByAliasesFailure |

### Method Name - Read from CJDS

Reading from CJDS allows contact centers to access recent customer events and behaviors in real time. By leveraging this data, flow logic can be dynamically adapted based on where the customer is in their journey—enabling more personalized, efficient, and context-aware experiences.

**Example Use Cases:**  
A customer who recently attempted a payment but failed due to a declined card calls back. Using CJDS, the system detects the failed payment event and automatically routes the customer to a billing-specific IVR flow or a specialized agent queue—skipping generic menus and reducing resolution time.



![Read from CJDS](https://files.readme.io/a6c5dca9830e04e4e975aef791aba008fecafed8df62c3643abd3424cd923ded-2025-06-10_13-22-13.png)




**Parameter Table**

Following are the UI parameters that are required to call this method:



| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| **Authorization**  <br>•Need to select valid Authorization configured inside Assets >Integrations >Pre-built Integrations (Authorization configuration must be the first step before using Customer Journey Data pre-built integration).  <br>  <br>**Workspace/Project**  <br>•Select available workspace or project present in customer journey data.  <br>  <br>**Identity**  <br>• Alias identifier associated with the alias. For e.g., either Phone Number, Email Address, Social Id, Customer Id or Temporary Id.  <br>  <br>**Query**  <br>• Filter Query to narrow down the result set. For e.g., filter=type=='agent:state_change'&data=queueId=='8003ddb7-d105-4d04-b1df-a30abc62fd57'&pageSize=1 | **dataArray**  <br>•Array Object that contains workspaceId, templateId, organizationId, templaetId, attributes array object.  <br>  <br>**organizationId**  <br>•unique organization Id.  <br>  <br>**resultCount**  <br>•total count of Events.  <br>  <br>**Identity**  <br>•Person Id.  <br>  <br>**workspaceId**  <br>•Unique workspace Id.  <br>  <br>**status**  <br>•HTTP error name.  <br>  <br>**message**  <br>•type of error.  <br>  <br>**errors**  <br>•array of error messages.  <br>  <br>**trackingId**  <br>•error tracking unique id.  <br>  <br>**responsePayload**  <br>•This will contain all the JSON response object in single variable. | **onInvalidData**  <br>•Invalid data.  <br>  <br>**onError**  <br>•Error while invoking the method.  <br>  <br>**onInvalidChoice**  <br>•Invalid choice.  <br>  <br>**onBadRequest**  <br>•If HTTP status received is 400  <br>  <br>**onForbidden**  <br>•If HTTP status received is 403.  <br>  <br>**onNotFound**  <br>•If HTTP status received is 404.  <br>  <br>**onTooManyRequest**  <br>•If HTTP status received is 429.  <br>  <br>**onInternalServerError**  <br>•If HTTP status received is 500.  <br>  <br>**onReadfromCJDSSuccess**  <br>•If HTTP status received is 200.  <br>  <br>**onReadfromCJDSFailure**  <br>•If HTTP status received is other than 200 and configured error HTTP status codes.  <br>  <br>**onTimeout**  <br>•When the method could not be invoked before the timeout (10 seconds) duration. |




**HTTP Status Codes**

| Status code                                                      | Description           |
| :--------------------------------------------------------------- | :-------------------- |
| 400                                                              | onBadRequest          |
| 403                                                              | onForbidden           |
| 404                                                              | onNotFound            |
| 429                                                              | onTooManyRequest      |
| 500                                                              | onInternalServerError |
| 200                                                              | onReadfromCJDSSuccess |
| All HTTP Status codes other than 400, 403, 404, 429, 500 and 200 | onReadfromCJDSFailure |