## Introduction

ServiceNow is being used to track and manage incidents within a large organization, with integration primarily focusing on incidents. ServiceNow facilitates <<prodname>> users with three of its methods:

- [Create Incident](https://help.webexconnect.io/docs/servicenow-node#create-incident)- This method creates incident tickets in the ServiceNow Desk.
- [Get Incident](https://help.webexconnect.io/docs/servicenow-node#get-incident)- This method fetches incident tickets in the ServiceNow Desk.
- [Update Incident](https://help.webexconnect.io/docs/servicenow-node#update-incident)- This method updates existing incident tickets in the ServiceNow Desk.

This node needs to be enabled for your account and is not available by default. Please contact your account manager in case you wish to enable it for your account.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ad30beb0e34996ee2395012de0672685fd146db365068618cf71e1af081b899b-image.png",
        null,
        "Screenshot of ServiceNow Node"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of ServiceNow "
    }
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Description",
    "0-0": "Name",
    "0-1": "Name of the property you’re creating. In this case,_  \nglide.oauth.inbound.client.credential.grant_type_ enabled.",
    "1-0": "Description",
    "1-1": "Type a brief, descriptive phrase describing the function of the property.",
    "2-0": "Type",
    "2-1": "Select the appropriate data type from the list. The possible values for the field are True and False.",
    "3-0": "Value",
    "3-1": "To enable the client credentials grant type for OAuth inbound integrations, you should set the desired property to True. The possible values for the field are True and False."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note
> 
> Other fields in the form such as Choices, Ignore cache, Private, Read roles, and Write roles can be configured according to your requirements.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/28872f065aed974fcfd578296da98ead20bf03f5a508bba9cc35b68151f8b243-image.png",
        null,
        "Screenshot of Enabling Client Credential System Property"
      ],
      "align": "center",
      "border": true,
      "caption": "Enable Client Credential System Property"
    }
  ]
}
[/block]


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

   [block:parameters]{"data":{"h-0":"Field","h-1":"Description","0-0":"User ID","0-1":"Create a unique identifier for this user's ServiceNow login user name. Examples of user IDs are cwitherspoon and charlie.witherspoon.  \n  \nNote:You can’t create a user whose User ID duplicates an existing user. If you do import duplicates from an update set, the more recently created name takes the duplicate User ID.  \n  \nExample:  \nFor a user named \"Charlie Witherspoon\":  \n  \n1. Start with the base ID: cwitherspoon.\n\n2. Check for duplicates:\n\n   - If none exist, assign the ID.\n\n   - If a conflict arises, append a unique suffix: cwitherspoon1, cwitherspoon_20231205, etc.","1-0":"Given name","1-1":"Enter the user's given (often their first) name.","2-0":"Family name","2-1":"Enter the user's family name.  \n_**Note**: You can clear the First Name field, or the Last Name field in an existing user record, but you can’t clear both at the same time._","3-0":"Title","3-1":"Enter a title or job description, or select one from the list.","4-0":"Department","4-1":"Select the user's department from the list.","5-0":"Password","5-1":"Assign a password to the user. This password can be permanent or temporary.","6-0":"Password needs reset","6-1":"Select this check box to enforce a password change upon the user's first login.","7-0":"Locked out","7-1":"Select this check box to lock the user out of the instance and terminate all active sessions. The system includes safeguards to prevent users with the admin role from locking themselves out.","8-0":"Active","8-1":"Select this check box to make user active. Inactive users are visible only to administrators in the following areas:  \no User lists.  \no Selection list on reference fields (accessed via the magnifying glass icon)  \no Auto-complete list that appears when typing into a reference field","9-0":"Web service access only","9-1":"Select this check box to designate the user as a non-interactive user. This field is applicable for[ Non-Interactive Sessions.  ](https://www.servicenow.com/docs/bundle/xanadu-platform-administration/page/administer/users-and-groups/concept/c_NonInteractiveSessions.html)  \n_Note: In our case leave this checkbox un-checked_","10-0":"Internal Integration User","10-1":"Select this check box to designate this user as an  \n[ Mark service accounts as internal integration users.](https://www.servicenow.com/docs/csh?topicname=t_MarkSvcAcctsAsInternalIntegUsers&version=xanadu&pubname=xanadu-api-reference)  \n_Note: In our case leave this checkbox un-checked_","11-0":"Date format","11-1":"Select the user's preferred date format.","12-0":"Email","12-1":"Enter the user's email address.  \nTo enter a non-standard email address that fails field validation, deactivate the validation script first.  \n  \nTo deactivate the validation script:  \na.Navigate to System Definition > Validation Scripts.  \nb.Select the email validation script record.  \nc.Clear the Active check box and Save the change.  \nd.Complete the user profile, including the email address.  \ne.Update or Submit the record.  \nf.Reactivate the email validation script by selecting the Active check box and saving the changes.","13-0":"Notification","13-1":"Specify if email notifications should be sent to the user.  \no**Enable**: Select Enable to send email notifications to the user.  \no**Disable: **to allow the user to receive notifications only if they subscribe to the notification or are specified as a recipient in the Email and SMS notifications form.  \nTo prevent notification completely, configure a condition on the email notification form to block delivery when this field is set to **Disable**.","14-0":"Calendar integration","14-1":"Select **Outlook **to enable the user to receive meeting notifications directly via email to the calendar. Select **None **if no meeting notifications should be sent.","15-0":"Time zone","15-1":"Select the user's time zone.","16-0":"Business phone","16-1":"Enter this user's business phone number.","17-0":"Mobile phone","17-1":"Enter this user's mobile phone number.","18-0":"Photo","18-1":"If appropriate,attach a photo of the user.","19-0":"Geolocation tracked","19-1":"Select the check box to enable location tracking. The Geolocation tracked field,  \nis applicable, upon activation of[ Geolocation](https://www.servicenow.com/docs/csh?topicname=c_Geolocation&version=xanadu&pubname=xanadu-servicenow-platform)and provides the option to track a user's location.","20-0":"Location","20-1":"Select the user's location. This field appears when geolocation is enabled."},"cols":2,"rows":21,"align":["left","left"]}[/block]

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

   [block:parameters]{"data":{"h-0":"Field","h-1":"Descriptions","0-0":"Name","0-1":"A unique name that identifies the application requiring OAuth access.","1-0":"Client ID","1-1":"[Read-Only] The auto-generated unique ID of the application.  \nThe instance uses the client ID to request an access token.","2-0":"Client Secret","2-1":"[Required] The shared secret string used by both the instance and the client application or  \nwebsite to authorize communications. The instance uses the client's secret when requesting an access token.  \nLeave this field blank to have the instance  \nauto-generate a client secret. To display existing client secrets, click the lock icon.","3-0":"Redirect URL","3-1":"The callback URL to which the authorization server redirects. Enter the full URLs of the clients  requesting access to the resource, appending by /oauth_redirect.do.  \n  \nFor example, http\\://token_consumer:port/oauth_redirect.do.  \nEnter as many URLs as needed for all possible token consumers. The instance matches the URL of the incoming request to one of the redirect URLs. If no match is made, the instance uses the first redirect URL.  \n  \n_Note: For Client credentials, we don’t need to fill any callback URLs_","4-0":"Logo URL","4-1":"The URL of the image to use as the application logo.  \n  \nThe logo appears on the approval page when the user is prompted to grant a client  \napplication access to a restricted resource on the instance.","5-0":"Active","5-1":"Select the check box to activate the application registry.","6-0":"Refresh Token   Lifespan","6-1":"The number of seconds a refresh token is valid. The instance uses the lifespan value to request a refresh token. By default, refresh tokens expire in 100 days (8640000 seconds).","7-0":"Enforce Token   Restrictions","7-1":"Select this option to restrict tokens to APIs configured to allow the authentication profile.You can grant access by setting an API access policy.  \n  \nFor more information, see  \nCreate REST API access policy.  \nDefault: Unselected.","8-0":"Mobile Client","8-1":"Represents the entity for a mobile app or web. This information is used to analyze the login  \ninformation with mobile or web.","9-0":"Access Token Lifespan","9-1":"The number of seconds a access token is valid. The instance uses the lifespan value to request an access token. By default, access tokens expire in 30 minutes (1800 seconds).","10-0":"Comments","10-1":"Additional information to associate with the application."},"cols":2,"rows":11,"align":["left","left"]}[/block]

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

1. Login to the <<prodname>> platform.
2. Navigate to Integrations.
3. Filter the Integrations page with **Pre-built Integrations **or search for **ServiceNow**.
4. Select ServiceNow and click **Actions > Manage**.
5. On the **Manage Integrations** – **ServiceNow **screen, under **Node Authorizations**, click the dropdown in the **Action** column and then click **Add authentication**.

   [block:image]{"images":[{"image":["https://files.readme.io/95d13054ec1b2cc02a4f9bebda7b9be30173a1c64f045c64200cf41b66b34f51-image.png",null,"Screenshot of Add New Authentication"],"align":"center","border":true,"caption":"Add New Authentication"}]}[/block]
6. Enter an appropriate **Authentication Name**.
7. Enter the **Client ID**, and **Client Secret **details. For more information on obtaining the Client ID and Client Secret of ServiceNow, refer [here].
8. Enter **Access Token URL **and **Refresh Token URL**, obtained only after registering for **Oauth Application registry **in ServiceNow.  
   [https://{org-instanceId}.service-now.com/oauth_token.do]
   > 📘 Note
   > 
   > Every user has their own organizational instance ID associated with ServiceNow account and Please modify ‘org-instanceId’ in the URL to reflect your organization instanceId.
9. Click **Authenticate**.  
   If the credentials are successfully verified by ServiceNow, then a new authorization is added, and the access token is saved to the<<prodname>>.

Upon successful authentication, a new tab is displayed to capture the credentials of your ServiceNow account

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/85718b163da43266a0bdb393d996ea0446b66d1d45020091a8ed60a608b133a5-image.png",
        null,
        "Screenshot of Authentication Added Successfully"
      ],
      "align": "center",
      "border": true,
      "caption": "Authentication added successfully"
    }
  ]
}
[/block]


### Obtaining the Client ID and Client Secret of ServiceNow

1. Login to the **ServiceNow Instance**.
2. Navigate to **All**, search for **oAuth **then click **Application Registry **from the search results.
3. Click **New > Create an oAuth API endpoint **for external clients.
4. Enter an appropriate **Name** for the OAuth 2.0 client.
5. Client ID is prefilled. When provided with mandatory information, click **Submit**.
6. Upon submitting the request, the Client Secret gets auto-populated. Click the lock icon adjacent to the Client Secret to reveal the Client Secret Key.  
   The created **Client ID** and **Client Secret **can be used for authentication in <<prodname>>.

   [block:image]{"images":[{"image":["https://files.readme.io/42a980e1d72f47353785a7242e15dbd6bb6ffd9f78bbeedc69f0edf7914f5f5f-image.png",null,"Screenshot of Obtaining the Client ID and Client Secret of ServiceNow"],"align":"center","border":true,"caption":"Obtaining the Client ID and Client Secret of ServiceNow"}]}[/block]

## Configuring ServiceNow node in flows

Here’s a brief description of various methods, and corresponding output variables and node outcomes associated with each of the methods.

> 📘 Known Limitation-Adding Values from Input Variables
> 
> When you retrieve values from Input Variables (Custom Variables, Start Node Variables), ensure you add a space after entering values in subsequent fields. Adding this space ensures the variable persists after you save the node. If you do not add the space, the variable will not remain persistent.

### Method Name-Create Incident

This method is used for creating incident tickets in ServiceNow Desk. Below, are the UI parameters that are required to call this method.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c132f873ba4d2f362e3d375907476b57d1b3567622ff01e0c4b612fdca699fa0-image.png",
        null,
        "Screenshot of Create Incident method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Create Incident method configuration page."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Authorization  \n•Need to select valid Authorization configured inside Assets>Integration>Pre-built Integration(Authorization configuration must be the first step before using ServiceNow pre-built integration)  \n  \nInstanceId  \n•\tThe unique identifier for your ServiceNow instance and is used to differentiate between multiple instances of ServiceNow that may exist",
    "0-1": "Number  \n•incident number  \n  \nsys_id  \n•unique GUID of the incident  \n  \ntask_effective_number  \n•Incident number.  \n  \nresponsePayload  \n•This will contain all the JSON response objects in a single variable.",
    "0-2": "onInvalidData  \n•Invalid data  \n  \nonError  \n•Error while invoking the method  \n  \nonInvalidChoice  \n•Invalid choice  \n  \nonBadRequest  \n•If HTTP status received is 400  \n  \nonNotFound  \n•If HTTP status received is 404  \n  \nonIncidentCreated  \n•If HTTP status received is 201  \n  \nonCreateIncidentFailure  \n•If HTTP status received is other than 201 and configured error HTTP status codes  \n  \nonTimeout  \n•When the method could not be invoked before the timeout(5 seconds) duration"
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


**HTTP Status Codes**

| Status code                                        | Description             |
| :------------------------------------------------- | :---------------------- |
| 400                                                | onBadRequest            |
| 201                                                | onIncidentCreated       |
| All HTTP Status codes other than 400, 404, and 201 | onCreateIncidentFailure |

### Method Name-Get Incident

This method is used for fetching incident tickets in ServiceNow Desk. Below, are the UI parameters that are required to call this method.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2d7c1f71307f759c5383835d69b9dc94c45962795bb95ee73197969f63878b43-image.png",
        null,
        "Screenshot of Get Incident method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Get Incident method configuration page."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Authorization  \n•Need to select valid Authorization configured inside Assets>Integration>Pre-built Integration(Authorization configuration must be the first step before using ServiceNow pre-built integration).  \n  \nInstanceId  \n•The unique identifier for your ServiceNow instance and is used to differentiate between multiple instances of ServiceNow that may exist.  \n  \nIncident Id  \n•Please specify the `number` output variable received from `Create Incident` method.",
    "0-1": "parent  \n•a parent incident is a way to link related incidents together. This functionality is used to handle multiple incidents that have the same categorization and communication needs.  \nFor example: {\"display_value\":\"CHG0000003\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/task/46e9b4afa9fe198101026e122b85f442\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \ncaused_by  \n•a reference field that points to the change_request table. This field is used to indicate that an incident was caused by a change.  \nFor example {\"display_value\":\"CHG0040007\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/change_request/c83c5e5347c12200e0ef563dbb9a7190\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node. _  \n  \nwatch_list  \n•the list of people like caller or other user who might like to know about any updates or progress with the task  \nFor example: System Administrator, Sean Bonnet  \n  \nState  \n•the stage of the incident's life cycle. For example: Closed  \n  \nImpact  \n•a measure of the negative consequences of an incident on an organization, its customers, its stakeholders, and its reputation. It is based on how the quality of service is affected. For example: 3 – Low  \n  \nactive  \n•represents the users which are presents on the ServiceNow and will do tasks or based on the role other criteria they will perform.  If Active is false they will not able log into the ServiceNow. For example: false  \n  \npriority  \n•The priority field in a ServiceNow incident indicates the order in which the incident should be resolved. For example:5 – Planning  \n  \nassigned_to  \n•a reference field that points to the Users table and is used to designate a user to work on or be responsible for a task.  \nFor example: {\"display_value\":\"Fred Luddy\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sys_user/5137153cc611227c000bbd1bd8cd2005\"}-\\`\\`  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node. _  \n  \ntask_effective_number  \n•displays the display number of a Universal Request (UR) ticket as a string. For example: INC0010030  \n  \nopened_by  \n•opened by is a reference to the user table that created the incident.  \nFor example:{\"display_value\":\"John Wick\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sys_user/f19d5ff183d15210d81dc590ceaad3d7\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nsys_created_on  \n•contains the date and time when a task record was created. For example: 2024-10-28 04:14:47  \n  \nopened_at  \n•the field that is populated when the incident form is opened in the user interface (UI). For example:  2024-10-28 04:14:47  \n  \nsys_id  \n•the sys_id is basically a record's fingerprint. It's a unique identifier that the system assigns to every single record. For example: 189d7fc183a51210d81dc590ceaad387  \n  \nnumber  \n•a unique number and prefix that automatically numbers records. The \"Number\" field is a string that is made up of a prefix and a number that is specific to the task class.  \nFor example: INC0010030  \n  \ncontact_type  \n•indicates the type of contact for the incident  \nFor example: Walk-in  \n  \nmade_sla  \n•a legacy field that was part of the old SLA engine  \n  \nupon_reject For example: true  \n•a string data type field that is eligible for mapping  \nFor example: Cancel all future Tasks  \n  \nsys_updated_on  \n•is the timestamp for system updates  \nFor example: 2024-11-03 23:07:58  \n  \nchild_incidents  \n•used to link a child incident to a parent incident  \nFor example: 1  \n  \nhold_reason  \n•field in ServiceNow's Incident table is used to indicate why an incident is being paused  \n  \napproval_history  \n•System Administrator (Approval history)a journal field that tracks approval details for a record. For example:  2024-10-30 00:25:33  \n  \nresolved_by  \n•indicates who resolved the incident  \nFor example: {\"display_value\":\"System Administrator\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sys_user/6816f79cc0a8016401c5a33be04be441\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nsys_updated_by  \n•a system field that displays the UserID of the user who most recently updated the incident admin For example: admin  \n  \nuser_input  \n•is used to capture input provided by users, typically in the context of workflows, surveys, or other interactive processes For example: user input by {user_name}  \n  \nsys_domain  \n•\tidentifies the domain of an override record in a table. For example: {\"display_value\":\"global\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sys_user_group/global\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nsys_created_by  \n•a system field that stores the user ID of the person who created the incident For example: John wick  \n  \nknowledge  \n•allows users to attach knowledge base articles to incidents For example: true  \n  \norder  \n•controls the order of items in category lists For example:10  \n  \ncalendar_stc  \n•field in an incident uses the dateDiff function to calculate the duration between when an incident is opened and resolved. For example:589,991  \n  \nclosed_at  \n•records the date when the incident was closed. For example:2024-10-29 23:59:25  \n  \ncmdb_ci  \n•is a Configuration Item field that displays CIs that match the incident's company. The cmdb_ci field's dictionary entry has a dependent field called \"company\". When an incident is created, the \"company\" field is empty, so all CIs are displayed. When the incident is saved, the \"company\" field is populated with the caller's company. For example: {\"display_value\":\"\\*BETH-IBM\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/cmdb_ci/affd3c8437201000deeabfc8bcbe5dc3\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \ndelivery_plan  \n•is used to sequence work, and to describe when the work will take place and when it is expected to be finished. For example: {\"display_value\":\"Blackberry Delivery Plan\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sc_cat_item_delivery_plan/8bb57b8ac0a8006400e2e4d738d24dde\"}  \n  \nwork_notes_list  \n•is a list of people who are working on an incident. For example: System Administrator  \n  \nbusiness_service  \n•allows users to select a business service and see the available service offerings. The Service Offering field is dependent on the Business Service that is chosen  \nFor example: {\"display_value\":\"Email\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/cmdb_ci_service/27d32778c0a8000b00db970eeaa60f16\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nbusiness_impact  \n•is part of a business impact analysis (BIA), which is a process that assesses the potential impact of a disruption on a business  \nFor example: Business impact reason to be filled by John Wick  \n  \nsys_domain_path  \n•The sys_domain_path value is unique in the Domain table  \n  \nrfc  \n•stands for Request for Change, which is a formal request to implement a change in  \nServiceNow  \nFor example:  \n{\"display_value\":\"CHG0040007\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/change_request/c83c5e5347c12200e0ef563dbb9a7190\"} -  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \ntime_worked  \n•is a time-tracking field in the Task table that can be used for incidents For example: 1 Hour  \n  \nexpected_start  \n•is populated with the task's created time when a new Catalog Task is created from a workflow. For example: 2024-10-22 00:26:20  \n  \nbusiness_duration  \n•is the time difference between the incident's opened and closed times. For example:1 Day 16 Hours  \n  \ngroup_list  \n•interested groups For example: Analytics Settings Managers  \n  \ncaller_id  \n•is a reference field that identifies the caller of an incident For example: {\"display_value\":\"John Wick\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sys_user/f19d5ff183d15210d81dc590ceaad3d7\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nreopened_time  \n•is a field that indicates the last time the incident was reopened For example: 2024-11-03 22:46:34  \n  \nresolved_at  \n•is the date and time when an incident is resolved For example: 2024-11-03 23:07:58  \n  \napproval_set  \n•is a glide_date_time data type field For example:  2024-10-29 00:24:25  \n  \nsubcategory  \n•is used to provide more specific divisions within broad topics represented by categories For example: Email  \n  \nshort_description  \n•is a field for a short description of the task (with a default character limit of 255), whereas Description [description] field is for a more comprehensive explanation of the issue, often tincluding specific instructions. For example: Short Description by John Wick  \n  \nclose_code  \n•is the Resolution Code field, which is required to be populated when an incident is set to Resolved or Closed. For example: User error  \n  \ncorrelation_display  \n•is used to identify the source of an incident For example: correlation display by John Wick  \n  \ndelivery_task  \n•For example: {\"display_value\":\"Procure PC Hardware\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sc_cat_item_delivery_task/8a3ff7dbc61122780008ffafccebb2a2\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nassignment_group  \n•The \"assignment_group\" field in a ServiceNow incident is a field that can be constrained  \nFor example:  \n{\"display_value\":\"Help Desk\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sys_user_group/679434f053231300e321ddeeff7b12d8\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nadditional_assignee_list  \n•is a tool that allows users to select multiple additional assignees for an incident  \nFor example: System Administrator  \n  \nbusiness_stc  \n•is the data type for the business resolve time of an incident For example:144,000  \n  \ndescription  \n•is a place to provide a detailed explanation of the issue, often including specific instructions. For example: Description from John Wick  \n  \ncalendar_duration  \n•is one of two duration fields that calculate the time difference between an incident's open and closed times For example:6 Days 19 Hours 53 Minutes  \n  \nclose_notes  \n•the Resolution Notes field that must be populated when an incident is set to Resolved or Closed For example: user error  \n  \nnotify  \n•allows users to communicate with customers. Email notifications, SMS notifications, and Push notifications. For example: Do Not Notify  \n  \nservice_offering  \n•is used to define the level of service for a given request. For example: {\"display_value\":\"service2828\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/service_offering/39a1a17d8365d210d81dc590ceaad3ec\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nsys_class_name  \n•also known as the Task Type field, indicates the type of task a record is, such as an incident, change, or problem For example: Incident  \n  \nclosed_by  \n•indicates who closed the incident  \nFor example: {\"display_value\":\"System Administrator\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sys_user/6816f79cc0a8016401c5a33be04be441\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nparent_incident  \n•is used to establish a parent-child relationship between incidents For example: {\"display_value\":\"INC0010031\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/incident/1f46c05183e51210d81dc590ceaad34f\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nreopened_by  \n•is used to track user who has opened the resolved incident  For example: {\"display_value\":\"System Administrator\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/sys_user/6816f79cc0a8016401c5a33be04be441\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nincident_state  \n•is used to track the state of an incident For example:Closed  \n  \nurgency  \n•is a measure of how quickly a resolution is required for the incident For example: 3 – Low  \n  \nproblem_id  \n•In incidents the problem_id field is a reference to the problem table For example: {\"display_value\":\"PRB0001002\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/problem/6632130c730123002728660c4cf6a734\"} -  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \ncompany  \n•is a lookup list that allows users to specify the company associated with an incident For example: {\"display_value\":\"ACME North America\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/core_company/31bea3d53790200044e0bfc8bcbe5dec\"} -  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \nreassignment_count  \n•how many times an incident has been reassigned between groups For example:1  \n  \nactivity_due  \n•is a due date field that indicates when an activity is expected to be completed For example: UNKNOWN  \n  \nseverity  \n•measures the impact an incident has on a business For example:3 – Low  \n  \ncomments  \n•is called the \"Additional Comments\" field. It's where users can add comments to an incident  \n2024-11-03 22:46:34 - System Administrator (Additional comments)  \nFor example:  \nHold by John Wick /n 2024-11-03 22:43:20 - System Administrator (Additional comments) /John Wick wants to reopen the incident  \n  \napproval  \n•is a process that assigns a group, user, or authorized member to either approve or reject a task  \nFor example: Not Yet Requested  \n  \nsla_due  \n•is part of the legacy SLA engine, which is used to associate a single SLA with each Task record  \nFor example: UNKNOWN  \n  \ncomments_and_work_notes  \n•visible entries and IT-team-only entries  \nFor example: contains both customer  \n  \ndue_date  \n•It is essentially a date field that can be used to track and capture follow-up dates or deadlines related to specific records or tasks For example: 2024-10-30 00:26:12  \n  \nsys_mod_count  \n•is a counter that increases each time a record is updated For example: 33  \n  \nreopen_count  \n•tracks the number of times an incident has been reopened For example:2  \n  \nescalation  \n•is a UI option that can be used to escalate an incident to a more experienced resource for help For example: Normal  \n  \nupon_approval  \n•stores work instructions if the incident is approved For example: Proceed to Next Task  \n  \ncorrelation_id  \n•stores the unique identifier for an incoming task or alert from another system For example: Correlation ID goes here  \n  \nlocation  \n•populates information from the location field in the user record  \nFor example: {\"display_value\":\"3260 Street, CA\",\"link\":\"https\\://{domain}.service-now.com/api/now/table/cmn_location/6808184aeb211100420124e05206fe12\"}  \n\\_Note: This output variable is an object which contains two object parameters called `display_value` and link`. To extract `display_value`and`link\\` parameters as variable in flow, it can be either done by using evaluate node or data parser node._  \n  \ncategory  \n•is a choice field that helps define incidents better. Incidents can be categorized based on the nature of the issue, the service or application affected, or the impact on the business  \nFor example: Inquiry / Help  \nresponsePayload",
    "0-2": "onInvalidData  \n•Invalid data  \n  \nonError  \n•Error while invoking the method  \n  \nonInvalidChoice  \n•Invalid choice  \n  \nonTimeout  \n•When the method could not be invoked before the timeout(5 seconds) duration  \nonauthorizationfail  \n  \nonGetIncidentSuccess  \n•If HTTP status received is 200 and X-Total-Count header response = 1.  \n  \nonIncidentNotFound  \n•If HTTP status received is 200 and X-Total-Count header response = 0.  \n  \nonGetIncidentFailure  \n•If HTTP status received is other than 200 and configured error HTTP status codes"
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


<br />

**HTTP Status Codes**

| Status code                          | Description          |
| :----------------------------------- | :------------------- |
| 404                                  | onIncidentNotFound   |
| 200                                  | onGetIncidentSuccess |
| All HTTP Status codes other than 200 | onGetIncidentFailure |

### Method Name- Update Incident

This method is used for updating existing incident ticket in ServiceNow Desk. Below, are the UI parameters that are required to call this method.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8e195ab7c0614f3e1b82fca927eb37a3e1afb3138e13c94510f19e0dae76f610-image.png",
        null,
        "Screenshot of Update Incident method configuration page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Update Incident method configuration page."
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Input Variables",
    "h-1": "Output Variables",
    "h-2": "Node Outcomes",
    "0-0": "Authorization  \n•Need to select valid Authorization configured inside Assets>Integration>Pre-built Integration(Authorization configuration must be the first step before using ServiceNow pre-built integration)  \n  \nInstanceId  \n•The unique identifier for your ServiceNow instance and is used to differentiate between multiple instances of ServiceNow that may exist.  \n  \nSys Id  \n•Please specify the `sys_id`(unique GUID of incident ticket) output variable received from `Create Incident` or `Get Incident`  method.  \n  \nRequest Body  \n•Please specify how you want to pass request body variables. Request body variables can be passed as JSON Object or as a individual key/value pair.\tnumber  ",
    "0-1": "number  \n•incident number  \n  \ntask_effective_number  \n•Incident number.  \n  \nsys_id  \n•unique GUID of the incident  \n.  \nresponsePayload  \n•This will contain all the JSON response object in single variable.",
    "0-2": "onInvalidData  \n•Invalid data  \n  \nonError  \n•Error while invoking the method  \n  \nonInvalidChoice  \n•Invalid choice  \n  \nonIncidentUpdateSuccess  \n•If HTTP status received is 200  \n  \nonBadRequest  \n•If HTTP status received is 400  \n  \nonIncidentNotFound  \n•If HTTP status received is 404  \n  \nonIncidentUpdateFailure  \n•If HTTP status received is other than 200 and configured error HTTP status codes  \n  \nonTimeout  \n•When the method could not be invoked before the timeout(5 seconds) duration"
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


**HTTP Status Codes**

| Status code                                       | Description              |
| :------------------------------------------------ | :----------------------- |
| 400                                               | onBadRequest             |
| 404                                               | onIncidentNotFound       |
| 200                                               | onIncidentUpdateSuccess  |
| All HTTP Status codes other than 400, 404 and 200 | ontIncidentUpdateFailure |