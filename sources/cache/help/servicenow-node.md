# ServiceNow

Source: https://help.webexconnect.io/docs/servicenow-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:08+00:00

## Introduction

ServiceNow is being used to track and manage incidents within a large organization, with integration primarily focusing on incidents. ServiceNow facilitates Webex Connect users with three of its methods:

- [Create Incident](https://help.webexconnect.io/docs/servicenow-node#create-incident)- This method creates incident tickets in the ServiceNow Desk.
- [Get Incident](https://help.webexconnect.io/docs/servicenow-node#get-incident)- This method fetches incident tickets in the ServiceNow Desk.
- [Update Incident](https://help.webexconnect.io/docs/servicenow-node#update-incident)- This method updates existing incident tickets in the ServiceNow Desk.

This node needs to be enabled for your account and is not available by default. Please contact your account manager in case you wish to enable it for your account.



![Screenshot of ServiceNow ](https://files.readme.io/ad30beb0e34996ee2395012de0672685fd146db365068618cf71e1af081b899b-image.png)




## Version Supported

> 📘 
> 
> This integration is based on ServiceNow API v1.0.0

## Pre-requisites

To enable the ServiceNow node, the following are the mandatory steps that need to be performed at the ServiceNow portal:

1. [Enable client credential system properties.](https://help.webexconnect.io/docs/servicenow-node#step-1-enable-client-credential-system-property)
2. [Add User and Assign roles.](https://help.webexconnect.io/docs/servicenow-node#step-2-add-user-and-assign-roles)
3. [Register system OAuth client from application registry(endpoints for client to access the instance).](https://help.webexconnect.io/docs/servicenow-node#step-3-create-an-endpoint-for-the-client-to-access-the-instance)

## Step 1: Enable Client Credential System Property

Create the _glide.oauth.inbound.client.credential.grant_type.enabled_ system property to use Client Credentials grant type for OAuth inbound integrations.

**Before you begin**  
Role required: admin

Plugin required: OAuth 2.0.

**Procedure**

1. In the navigation filter, enter **sys_properties.list**.  
   The entire list of properties in the System Properties [sys_properties] table appears.
2. Select **New**.
3. On the form, fill in the following fields.



| Fields | Description |
| --- | --- |
| Name | Name of the property you’re creating. In this case,_  <br>glide.oauth.inbound.client.credential.grant_type_ enabled. |
| Description | Type a brief, descriptive phrase describing the function of the property. |
| Type | Select the appropriate data type from the list. The possible values for the field are True and False. |
| Value | To enable the client credentials grant type for OAuth inbound integrations, you should set the desired property to True. The possible values for the field are True and False. |




> 📘 Note
> 
> Other fields in the form such as Choices, Ignore cache, Private, Read roles, and Write roles can be configured according to your requirements.



![Enable Client Credential System Property](https://files.readme.io/28872f065aed974fcfd578296da98ead20bf03f5a508bba9cc35b68151f8b243-image.png)




4. Select **Submit**

> 📘 Note
> 
> If the Ignore cache check box is selected, the system flushes the server cache when the parameter is changed.  
> Next, you must create an OAuth client (OAuth API endpoint for external client) and add OAuth Application User field to the OAuth client record.  
> For detailed steps, refer to [ServiceNow documentation](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/integrate/authentication/task/create-cc-sys-prop.html)to enable client credential system properties.

## Step 2: Add User and Assign Roles

You can add a user to your instance to enable them to log in and use designated application features.

**Before you begin**

Role required: user_admin

**Procedure**

1. Navigate to **All** > **User Administration** > **Users**.
2. Select **New**.
3. On the form, fill in the fields:

   

| Field | Description |
| --- | --- |
| User ID | Create a unique identifier for this user's ServiceNow login user name. Examples of user IDs are cwitherspoon and charlie.witherspoon.  <br>  <br>Note:You can’t create a user whose User ID duplicates an existing user. If you do import duplicates from an update set, the more recently created name takes the duplicate User ID.  <br>  <br>Example:  <br>For a user named "Charlie Witherspoon":  <br>  <br>1. Start with the base ID: cwitherspoon.<br><br>2. Check for duplicates:<br><br>   - If none exist, assign the ID.<br><br>   - If a conflict arises, append a unique suffix: cwitherspoon1, cwitherspoon_20231205, etc. |
| Given name | Enter the user's given (often their first) name. |
| Family name | Enter the user's family name.  <br>_**Note**: You can clear the First Name field, or the Last Name field in an existing user record, but you can’t clear both at the same time._ |
| Title | Enter a title or job description, or select one from the list. |
| Department | Select the user's department from the list. |
| Password | Assign a password to the user. This password can be permanent or temporary. |
| Password needs reset | Select this check box to enforce a password change upon the user's first login. |
| Locked out | Select this check box to lock the user out of the instance and terminate all active sessions. The system includes safeguards to prevent users with the admin role from locking themselves out. |
| Active | Select this check box to make user active. Inactive users are visible only to administrators in the following areas:  <br>o User lists.  <br>o Selection list on reference fields (accessed via the magnifying glass icon)  <br>o Auto-complete list that appears when typing into a reference field |
| Web service access only | Select this check box to designate the user as a non-interactive user. This field is applicable for[ Non-Interactive Sessions.  ](https://www.servicenow.com/docs/bundle/xanadu-platform-administration/page/administer/users-and-groups/concept/c_NonInteractiveSessions.html)  <br>_Note: In our case leave this checkbox un-checked_ |
| Internal Integration User | Select this check box to designate this user as an  <br>[ Mark service accounts as internal integration users.](https://www.servicenow.com/docs/csh?topicname=t_MarkSvcAcctsAsInternalIntegUsers&version=xanadu&pubname=xanadu-api-reference)  <br>_Note: In our case leave this checkbox un-checked_ |
| Date format | Select the user's preferred date format. |
| Email | Enter the user's email address.  <br>To enter a non-standard email address that fails field validation, deactivate the validation script first.  <br>  <br>To deactivate the validation script:  <br>a.Navigate to System Definition > Validation Scripts.  <br>b.Select the email validation script record.  <br>c.Clear the Active check box and Save the change.  <br>d.Complete the user profile, including the email address.  <br>e.Update or Submit the record.  <br>f.Reactivate the email validation script by selecting the Active check box and saving the changes. |
| Notification | Specify if email notifications should be sent to the user.  <br>o**Enable**: Select Enable to send email notifications to the user.  <br>o**Disable: **to allow the user to receive notifications only if they subscribe to the notification or are specified as a recipient in the Email and SMS notifications form.  <br>To prevent notification completely, configure a condition on the email notification form to block delivery when this field is set to **Disable**. |
| Calendar integration | Select **Outlook **to enable the user to receive meeting notifications directly via email to the calendar. Select **None **if no meeting notifications should be sent. |
| Time zone | Select the user's time zone. |
| Business phone | Enter this user's business phone number. |
| Mobile phone | Enter this user's mobile phone number. |
| Photo | If appropriate,attach a photo of the user. |
| Geolocation tracked | Select the check box to enable location tracking. The Geolocation tracked field,  <br>is applicable, upon activation of[ Geolocation](https://www.servicenow.com/docs/csh?topicname=c_Geolocation&version=xanadu&pubname=xanadu-servicenow-platform)and provides the option to track a user's location. |
| Location | Select the user's location. This field appears when geolocation is enabled. |



Optionally, you can customize the user form by adding fields such as Company, Location, and other fields available in ServiceNow, based on your requirements

**Set Password**  
Click on the Set Password field and create a password for the user. Ensure the password is stored securely.

**Add Roles**  
After filling in the above fields, we must assign below roles to the user:-

itil, itil_admin, admin, agent_admin, approval_admin, approver_user,  app_engine_admin, catalog_admin, catalog_editor, category_manager, credential_admin, data_manager_admin, rest_api_explorer, sn_incident_read, sn_incident_write

For detailed steps, refer to [create/add a user](https://cisco-my.sharepoint.com/:w:/r/personal/krvikash_cisco_com/Documents/ServiceNow%20Prebuilt%20Integration-%20v1.0.0.docx?d=w6f0001c4b228475a969ec840bc059319&csf=1&web=1&e=mmrSAo).

## Step 3: Create an endpoint for the Client to Access the Instance

Create an OAuth application endpoint for external client applications to access the ServiceNow instance.

**Before you begin**  
Role required: admin

**Procedure**

1. Navigate to **All > System OAuth > Application Registry **and then click **New**.
2. On the interceptor page, click **Create an OAuth API endpoint for external clients **and then fill in the form.

   

| Field | Descriptions |
| --- | --- |
| Name | A unique name that identifies the application requiring OAuth access. |
| Client ID | [Read-Only] The auto-generated unique ID of the application.  <br>The instance uses the client ID to request an access token. |
| Client Secret | [Required] The shared secret string used by both the instance and the client application or  <br>website to authorize communications. The instance uses the client's secret when requesting an access token.  <br>Leave this field blank to have the instance  <br>auto-generate a client secret. To display existing client secrets, click the lock icon. |
| Redirect URL | The callback URL to which the authorization server redirects. Enter the full URLs of the clients  requesting access to the resource, appending by /oauth_redirect.do.  <br>  <br>For example, http\://token_consumer:port/oauth_redirect.do.  <br>Enter as many URLs as needed for all possible token consumers. The instance matches the URL of the incoming request to one of the redirect URLs. If no match is made, the instance uses the first redirect URL.  <br>  <br>_Note: For Client credentials, we don’t need to fill any callback URLs_ |
| Logo URL | The URL of the image to use as the application logo.  <br>  <br>The logo appears on the approval page when the user is prompted to grant a client  <br>application access to a restricted resource on the instance. |
| Active | Select the check box to activate the application registry. |
| Refresh Token   Lifespan | The number of seconds a refresh token is valid. The instance uses the lifespan value to request a refresh token. By default, refresh tokens expire in 100 days (8640000 seconds). |
| Enforce Token   Restrictions | Select this option to restrict tokens to APIs configured to allow the authentication profile.You can grant access by setting an API access policy.  <br>  <br>For more information, see  <br>Create REST API access policy.  <br>Default: Unselected. |
| Mobile Client | Represents the entity for a mobile app or web. This information is used to analyze the login  <br>information with mobile or web. |
| Access Token Lifespan | The number of seconds a access token is valid. The instance uses the lifespan value to request an access token. By default, access tokens expire in 30 minutes (1800 seconds). |
| Comments | Additional information to associate with the application. |



   ### **Add the OAuth Application User**

   Add the OAuth Application User field on the OAuth Entity form to use the Client Credentials grant type for OAuth inbound integrations.

   **Before you begin**  
   Role required: admin  
   Plugin required: OAuth 2.0.

   **Procedure**

   1. Open the OAuth client record that was created.
   2. Select the **More** options icon on the page header.
   3. Select **Configure > Form Design.**
   4. On the Form Design page, add OAuth Application User from the list of fields.
   5. Click **Save** or **Update **the form.
   6. Select the user for the **OAuth Application User.**  
      For example, System Administrator. In our case, search and select the user that is created through step 2(Add user step)
3. Click** Submit**.

For detailed steps, refer to [create an OAuth application endpoint](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/security/task/t_CreateEndpointforExternalClients.html) for external client applications.

> 📘 Note for known limitation
> 
> When duplicate keys are passed dynamically in Create or Update incident by selecting request body as “Individual Parmeter”,the node will fail and follow the “onerror” edge. Adding this space ensures the variable persists after you save the node. If you do not add the space, the variable will not remain persistent.

## Adding a New Authorization

To create a new authorization:

1. Login to the Webex Connect platform.
2. Navigate to Integrations.
3. Filter the Integrations page with **Pre-built Integrations **or search for **ServiceNow**.
4. Select ServiceNow and click **Actions > Manage**.
5. On the **Manage Integrations** – **ServiceNow **screen, under **Node Authorizations**, click the dropdown in the **Action** column and then click **Add authentication**.

   

![Add New Authentication](https://files.readme.io/95d13054ec1b2cc02a4f9bebda7b9be30173a1c64f045c64200cf41b66b34f51-image.png)


6. Enter an appropriate **Authentication Name**.
7. Enter the **Client ID**, and **Client Secret **details. For more information on obtaining the Client ID and Client Secret of ServiceNow, refer [here].
8. Enter **Access Token URL **and **Refresh Token URL**, obtained only after registering for **Oauth Application registry **in ServiceNow.  
   [https://{org-instanceId}.service-now.com/oauth_token.do]
   > 📘 Note
   > 
   > Every user has their own organizational instance ID associated with ServiceNow account and Please modify ‘org-instanceId’ in the URL to reflect your organization instanceId.
9. Click **Authenticate**.  
   If the credentials are successfully verified by ServiceNow, then a new authorization is added, and the access token is saved to theWebex Connect.

Upon successful authentication, a new tab is displayed to capture the credentials of your ServiceNow account



![Authentication added successfully](https://files.readme.io/85718b163da43266a0bdb393d996ea0446b66d1d45020091a8ed60a608b133a5-image.png)




### Obtaining the Client ID and Client Secret of ServiceNow

1. Login to the **ServiceNow Instance**.
2. Navigate to **All**, search for **oAuth **then click **Application Registry **from the search results.
3. Click **New > Create an oAuth API endpoint **for external clients.
4. Enter an appropriate **Name** for the OAuth 2.0 client.
5. Client ID is prefilled. When provided with mandatory information, click **Submit**.
6. Upon submitting the request, the Client Secret gets auto-populated. Click the lock icon adjacent to the Client Secret to reveal the Client Secret Key.  
   The created **Client ID** and **Client Secret **can be used for authentication in Webex Connect.

   

![Obtaining the Client ID and Client Secret of ServiceNow](https://files.readme.io/42a980e1d72f47353785a7242e15dbd6bb6ffd9f78bbeedc69f0edf7914f5f5f-image.png)



## Configuring ServiceNow node in flows

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

> 📘 Known Limitation-Adding Values from Input Variables
> 
> When you retrieve values from Input Variables (Custom Variables, Start Node Variables), ensure you add a space after entering values in subsequent fields. Adding this space ensures the variable persists after you save the node. If you do not add the space, the variable will not remain persistent.

### Method Name-Create Incident

This method is used for creating incident tickets in ServiceNow Desk. Below, are the UI parameters that are required to call this method.



![Screenshot of Create Incident method configuration page.](https://files.readme.io/c132f873ba4d2f362e3d375907476b57d1b3567622ff01e0c4b612fdca699fa0-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Authorization  <br>•Need to select valid Authorization configured inside Assets>Integration>Pre-built Integration(Authorization configuration must be the first step before using ServiceNow pre-built integration)  <br>  <br>InstanceId  <br>•	The unique identifier for your ServiceNow instance and is used to differentiate between multiple instances of ServiceNow that may exist | Number  <br>•incident number  <br>  <br>sys_id  <br>•unique GUID of the incident  <br>  <br>task_effective_number  <br>•Incident number.  <br>  <br>responsePayload  <br>•This will contain all the JSON response objects in a single variable. | onInvalidData  <br>•Invalid data  <br>  <br>onError  <br>•Error while invoking the method  <br>  <br>onInvalidChoice  <br>•Invalid choice  <br>  <br>onBadRequest  <br>•If HTTP status received is 400  <br>  <br>onNotFound  <br>•If HTTP status received is 404  <br>  <br>onIncidentCreated  <br>•If HTTP status received is 201  <br>  <br>onCreateIncidentFailure  <br>•If HTTP status received is other than 201 and configured error HTTP status codes  <br>  <br>onTimeout  <br>•When the method could not be invoked before the timeout(5 seconds) duration |




**HTTP Status Codes**

| Status code                                        | Description             |
| :------------------------------------------------- | :---------------------- |
| 400                                                | onBadRequest            |
| 201                                                | onIncidentCreated       |
| All HTTP Status codes other than 400, 404, and 201 | onCreateIncidentFailure |

### Method Name-Get Incident

This method is used for fetching incident tickets in ServiceNow Desk. Below, are the UI parameters that are required to call this method.



![Screenshot of Get Incident method configuration page.](https://files.readme.io/2d7c1f71307f759c5383835d69b9dc94c45962795bb95ee73197969f63878b43-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Authorization  <br>•Need to select valid Authorization configured inside Assets>Integration>Pre-built Integration(Authorization configuration must be the first step before using ServiceNow pre-built integration).  <br>  <br>InstanceId  <br>•The unique identifier for your ServiceNow instance and is used to differentiate between multiple instances of ServiceNow that may exist.  <br>  <br>Incident Id  <br>•Please specify the `number` output variable received from `Create Incident` method. | parent  <br>•a parent incident is a way to link related incidents together. This functionality is used to handle multiple incidents that have the same categorization and communication needs.  <br>For example: {"display_value":"CHG0000003","link":"https\://{domain}.service-now.com/api/now/table/task/46e9b4afa9fe198101026e122b85f442"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>caused_by  <br>•a reference field that points to the change_request table. This field is used to indicate that an incident was caused by a change.  <br>For example {"display_value":"CHG0040007","link":"https\://{domain}.service-now.com/api/now/table/change_request/c83c5e5347c12200e0ef563dbb9a7190"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node. _  <br>  <br>watch_list  <br>•the list of people like caller or other user who might like to know about any updates or progress with the task  <br>For example: System Administrator, Sean Bonnet  <br>  <br>State  <br>•the stage of the incident's life cycle. For example: Closed  <br>  <br>Impact  <br>•a measure of the negative consequences of an incident on an organization, its customers, its stakeholders, and its reputation. It is based on how the quality of service is affected. For example: 3 – Low  <br>  <br>active  <br>•represents the users which are presents on the ServiceNow and will do tasks or based on the role other criteria they will perform.  If Active is false they will not able log into the ServiceNow. For example: false  <br>  <br>priority  <br>•The priority field in a ServiceNow incident indicates the order in which the incident should be resolved. For example:5 – Planning  <br>  <br>assigned_to  <br>•a reference field that points to the Users table and is used to designate a user to work on or be responsible for a task.  <br>For example: {"display_value":"Fred Luddy","link":"https\://{domain}.service-now.com/api/now/table/sys_user/5137153cc611227c000bbd1bd8cd2005"}-\`\`  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node. _  <br>  <br>task_effective_number  <br>•displays the display number of a Universal Request (UR) ticket as a string. For example: INC0010030  <br>  <br>opened_by  <br>•opened by is a reference to the user table that created the incident.  <br>For example:{"display_value":"John Wick","link":"https\://{domain}.service-now.com/api/now/table/sys_user/f19d5ff183d15210d81dc590ceaad3d7"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>sys_created_on  <br>•contains the date and time when a task record was created. For example: 2024-10-28 04:14:47  <br>  <br>opened_at  <br>•the field that is populated when the incident form is opened in the user interface (UI). For example:  2024-10-28 04:14:47  <br>  <br>sys_id  <br>•the sys_id is basically a record's fingerprint. It's a unique identifier that the system assigns to every single record. For example: 189d7fc183a51210d81dc590ceaad387  <br>  <br>number  <br>•a unique number and prefix that automatically numbers records. The "Number" field is a string that is made up of a prefix and a number that is specific to the task class.  <br>For example: INC0010030  <br>  <br>contact_type  <br>•indicates the type of contact for the incident  <br>For example: Walk-in  <br>  <br>made_sla  <br>•a legacy field that was part of the old SLA engine  <br>  <br>upon_reject For example: true  <br>•a string data type field that is eligible for mapping  <br>For example: Cancel all future Tasks  <br>  <br>sys_updated_on  <br>•is the timestamp for system updates  <br>For example: 2024-11-03 23:07:58  <br>  <br>child_incidents  <br>•used to link a child incident to a parent incident  <br>For example: 1  <br>  <br>hold_reason  <br>•field in ServiceNow's Incident table is used to indicate why an incident is being paused  <br>  <br>approval_history  <br>•System Administrator (Approval history)a journal field that tracks approval details for a record. For example:  2024-10-30 00:25:33  <br>  <br>resolved_by  <br>•indicates who resolved the incident  <br>For example: {"display_value":"System Administrator","link":"https\://{domain}.service-now.com/api/now/table/sys_user/6816f79cc0a8016401c5a33be04be441"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>sys_updated_by  <br>•a system field that displays the UserID of the user who most recently updated the incident admin For example: admin  <br>  <br>user_input  <br>•is used to capture input provided by users, typically in the context of workflows, surveys, or other interactive processes For example: user input by {user_name}  <br>  <br>sys_domain  <br>•	identifies the domain of an override record in a table. For example: {"display_value":"global","link":"https\://{domain}.service-now.com/api/now/table/sys_user_group/global"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>sys_created_by  <br>•a system field that stores the user ID of the person who created the incident For example: John wick  <br>  <br>knowledge  <br>•allows users to attach knowledge base articles to incidents For example: true  <br>  <br>order  <br>•controls the order of items in category lists For example:10  <br>  <br>calendar_stc  <br>•field in an incident uses the dateDiff function to calculate the duration between when an incident is opened and resolved. For example:589,991  <br>  <br>closed_at  <br>•records the date when the incident was closed. For example:2024-10-29 23:59:25  <br>  <br>cmdb_ci  <br>•is a Configuration Item field that displays CIs that match the incident's company. The cmdb_ci field's dictionary entry has a dependent field called "company". When an incident is created, the "company" field is empty, so all CIs are displayed. When the incident is saved, the "company" field is populated with the caller's company. For example: {"display_value":"\*BETH-IBM","link":"https\://{domain}.service-now.com/api/now/table/cmdb_ci/affd3c8437201000deeabfc8bcbe5dc3"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>delivery_plan  <br>•is used to sequence work, and to describe when the work will take place and when it is expected to be finished. For example: {"display_value":"Blackberry Delivery Plan","link":"https\://{domain}.service-now.com/api/now/table/sc_cat_item_delivery_plan/8bb57b8ac0a8006400e2e4d738d24dde"}  <br>  <br>work_notes_list  <br>•is a list of people who are working on an incident. For example: System Administrator  <br>  <br>business_service  <br>•allows users to select a business service and see the available service offerings. The Service Offering field is dependent on the Business Service that is chosen  <br>For example: {"display_value":"Email","link":"https\://{domain}.service-now.com/api/now/table/cmdb_ci_service/27d32778c0a8000b00db970eeaa60f16"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>business_impact  <br>•is part of a business impact analysis (BIA), which is a process that assesses the potential impact of a disruption on a business  <br>For example: Business impact reason to be filled by John Wick  <br>  <br>sys_domain_path  <br>•The sys_domain_path value is unique in the Domain table  <br>  <br>rfc  <br>•stands for Request for Change, which is a formal request to implement a change in  <br>ServiceNow  <br>For example:  <br>{"display_value":"CHG0040007","link":"https\://{domain}.service-now.com/api/now/table/change_request/c83c5e5347c12200e0ef563dbb9a7190"} -  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>time_worked  <br>•is a time-tracking field in the Task table that can be used for incidents For example: 1 Hour  <br>  <br>expected_start  <br>•is populated with the task's created time when a new Catalog Task is created from a workflow. For example: 2024-10-22 00:26:20  <br>  <br>business_duration  <br>•is the time difference between the incident's opened and closed times. For example:1 Day 16 Hours  <br>  <br>group_list  <br>•interested groups For example: Analytics Settings Managers  <br>  <br>caller_id  <br>•is a reference field that identifies the caller of an incident For example: {"display_value":"John Wick","link":"https\://{domain}.service-now.com/api/now/table/sys_user/f19d5ff183d15210d81dc590ceaad3d7"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>reopened_time  <br>•is a field that indicates the last time the incident was reopened For example: 2024-11-03 22:46:34  <br>  <br>resolved_at  <br>•is the date and time when an incident is resolved For example: 2024-11-03 23:07:58  <br>  <br>approval_set  <br>•is a glide_date_time data type field For example:  2024-10-29 00:24:25  <br>  <br>subcategory  <br>•is used to provide more specific divisions within broad topics represented by categories For example: Email  <br>  <br>short_description  <br>•is a field for a short description of the task (with a default character limit of 255), whereas Description [description] field is for a more comprehensive explanation of the issue, often tincluding specific instructions. For example: Short Description by John Wick  <br>  <br>close_code  <br>•is the Resolution Code field, which is required to be populated when an incident is set to Resolved or Closed. For example: User error  <br>  <br>correlation_display  <br>•is used to identify the source of an incident For example: correlation display by John Wick  <br>  <br>delivery_task  <br>•For example: {"display_value":"Procure PC Hardware","link":"https\://{domain}.service-now.com/api/now/table/sc_cat_item_delivery_task/8a3ff7dbc61122780008ffafccebb2a2"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>assignment_group  <br>•The "assignment_group" field in a ServiceNow incident is a field that can be constrained  <br>For example:  <br>{"display_value":"Help Desk","link":"https\://{domain}.service-now.com/api/now/table/sys_user_group/679434f053231300e321ddeeff7b12d8"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>additional_assignee_list  <br>•is a tool that allows users to select multiple additional assignees for an incident  <br>For example: System Administrator  <br>  <br>business_stc  <br>•is the data type for the business resolve time of an incident For example:144,000  <br>  <br>description  <br>•is a place to provide a detailed explanation of the issue, often including specific instructions. For example: Description from John Wick  <br>  <br>calendar_duration  <br>•is one of two duration fields that calculate the time difference between an incident's open and closed times For example:6 Days 19 Hours 53 Minutes  <br>  <br>close_notes  <br>•the Resolution Notes field that must be populated when an incident is set to Resolved or Closed For example: user error  <br>  <br>notify  <br>•allows users to communicate with customers. Email notifications, SMS notifications, and Push notifications. For example: Do Not Notify  <br>  <br>service_offering  <br>•is used to define the level of service for a given request. For example: {"display_value":"service2828","link":"https\://{domain}.service-now.com/api/now/table/service_offering/39a1a17d8365d210d81dc590ceaad3ec"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>sys_class_name  <br>•also known as the Task Type field, indicates the type of task a record is, such as an incident, change, or problem For example: Incident  <br>  <br>closed_by  <br>•indicates who closed the incident  <br>For example: {"display_value":"System Administrator","link":"https\://{domain}.service-now.com/api/now/table/sys_user/6816f79cc0a8016401c5a33be04be441"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>parent_incident  <br>•is used to establish a parent-child relationship between incidents For example: {"display_value":"INC0010031","link":"https\://{domain}.service-now.com/api/now/table/incident/1f46c05183e51210d81dc590ceaad34f"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>reopened_by  <br>•is used to track user who has opened the resolved incident  For example: {"display_value":"System Administrator","link":"https\://{domain}.service-now.com/api/now/table/sys_user/6816f79cc0a8016401c5a33be04be441"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>incident_state  <br>•is used to track the state of an incident For example:Closed  <br>  <br>urgency  <br>•is a measure of how quickly a resolution is required for the incident For example: 3 – Low  <br>  <br>problem_id  <br>•In incidents the problem_id field is a reference to the problem table For example: {"display_value":"PRB0001002","link":"https\://{domain}.service-now.com/api/now/table/problem/6632130c730123002728660c4cf6a734"} -  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>company  <br>•is a lookup list that allows users to specify the company associated with an incident For example: {"display_value":"ACME North America","link":"https\://{domain}.service-now.com/api/now/table/core_company/31bea3d53790200044e0bfc8bcbe5dec"} -  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>reassignment_count  <br>•how many times an incident has been reassigned between groups For example:1  <br>  <br>activity_due  <br>•is a due date field that indicates when an activity is expected to be completed For example: UNKNOWN  <br>  <br>severity  <br>•measures the impact an incident has on a business For example:3 – Low  <br>  <br>comments  <br>•is called the "Additional Comments" field. It's where users can add comments to an incident  <br>2024-11-03 22:46:34 - System Administrator (Additional comments)  <br>For example:  <br>Hold by John Wick /n 2024-11-03 22:43:20 - System Administrator (Additional comments) /John Wick wants to reopen the incident  <br>  <br>approval  <br>•is a process that assigns a group, user, or authorized member to either approve or reject a task  <br>For example: Not Yet Requested  <br>  <br>sla_due  <br>•is part of the legacy SLA engine, which is used to associate a single SLA with each Task record  <br>For example: UNKNOWN  <br>  <br>comments_and_work_notes  <br>•visible entries and IT-team-only entries  <br>For example: contains both customer  <br>  <br>due_date  <br>•It is essentially a date field that can be used to track and capture follow-up dates or deadlines related to specific records or tasks For example: 2024-10-30 00:26:12  <br>  <br>sys_mod_count  <br>•is a counter that increases each time a record is updated For example: 33  <br>  <br>reopen_count  <br>•tracks the number of times an incident has been reopened For example:2  <br>  <br>escalation  <br>•is a UI option that can be used to escalate an incident to a more experienced resource for help For example: Normal  <br>  <br>upon_approval  <br>•stores work instructions if the incident is approved For example: Proceed to Next Task  <br>  <br>correlation_id  <br>•stores the unique identifier for an incoming task or alert from another system For example: Correlation ID goes here  <br>  <br>location  <br>•populates information from the location field in the user record  <br>For example: {"display_value":"3260 Street, CA","link":"https\://{domain}.service-now.com/api/now/table/cmn_location/6808184aeb211100420124e05206fe12"}  <br>\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  <br>  <br>category  <br>•is a choice field that helps define incidents better. Incidents can be categorized based on the nature of the issue, the service or application affected, or the impact on the business  <br>For example: Inquiry / Help  <br>responsePayload | onInvalidData  <br>•Invalid data  <br>  <br>onError  <br>•Error while invoking the method  <br>  <br>onInvalidChoice  <br>•Invalid choice  <br>  <br>onTimeout  <br>•When the method could not be invoked before the timeout(5 seconds) duration  <br>onauthorizationfail  <br>  <br>onGetIncidentSuccess  <br>•If HTTP status received is 200 and X-Total-Count header response = 1.  <br>  <br>onIncidentNotFound  <br>•If HTTP status received is 200 and X-Total-Count header response = 0.  <br>  <br>onGetIncidentFailure  <br>•If HTTP status received is other than 200 and configured error HTTP status codes |




<br />

**HTTP Status Codes**

| Status code                          | Description          |
| :----------------------------------- | :------------------- |
| 404                                  | onIncidentNotFound   |
| 200                                  | onGetIncidentSuccess |
| All HTTP Status codes other than 200 | onGetIncidentFailure |

### Method Name- Update Incident

This method is used for updating existing incident ticket in ServiceNow Desk. Below, are the UI parameters that are required to call this method.



![Screenshot of Update Incident method configuration page.](https://files.readme.io/8e195ab7c0614f3e1b82fca927eb37a3e1afb3138e13c94510f19e0dae76f610-image.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Authorization  <br>•Need to select valid Authorization configured inside Assets>Integration>Pre-built Integration(Authorization configuration must be the first step before using ServiceNow pre-built integration)  <br>  <br>InstanceId  <br>•The unique identifier for your ServiceNow instance and is used to differentiate between multiple instances of ServiceNow that may exist.  <br>  <br>Sys Id  <br>•Please specify the `sys_id`(unique GUID of incident ticket) output variable received from `Create Incident` or `Get Incident`  method.  <br>  <br>Request Body  <br>•Please specify how you want to pass request body variables. Request body variables can be passed as JSON Object or as a individual key/value pair.	number   | number  <br>•incident number  <br>  <br>task_effective_number  <br>•Incident number.  <br>  <br>sys_id  <br>•unique GUID of the incident  <br>.  <br>responsePayload  <br>•This will contain all the JSON response object in single variable. | onInvalidData  <br>•Invalid data  <br>  <br>onError  <br>•Error while invoking the method  <br>  <br>onInvalidChoice  <br>•Invalid choice  <br>  <br>onIncidentUpdateSuccess  <br>•If HTTP status received is 200  <br>  <br>onBadRequest  <br>•If HTTP status received is 400  <br>  <br>onIncidentNotFound  <br>•If HTTP status received is 404  <br>  <br>onIncidentUpdateFailure  <br>•If HTTP status received is other than 200 and configured error HTTP status codes  <br>  <br>onTimeout  <br>•When the method could not be invoked before the timeout(5 seconds) duration |




**HTTP Status Codes**

| Status code                                       | Description              |
| :------------------------------------------------ | :----------------------- |
| 400                                               | onBadRequest             |
| 404                                               | onIncidentNotFound       |
| 200                                               | onIncidentUpdateSuccess  |
| All HTTP Status codes other than 400, 404 and 200 | ontIncidentUpdateFailure |