# Usage Report Fields

Source: https://help.webexconnect.io/docs/usage-report-fields
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:36+00:00

The following tables contains the field names and descriptions for each spreadsheet when the usage report is downloaded.

Common fields across all sheets in the usage reports. 

| Field Name        | Description                                                                          |
| :---------------- | :----------------------------------------------------------------------------------- |
| subscription_type | License edition of client                                                            |
| subscription_id   | A Unique identification number is assigned when a  tenant is created in the platform |
| Client ID         | Unique id of the client                                                              |
| Client Name       | Name of the client                                                                   |
| cpass_orgid       | Unique id of the CPaaS organisation                                                  |
| cpass_orgname     | Name of the CPaaS organisation                                                       |
| category_tag      | Category to which it belongs                                                         |
| client_domain     | Domain of the client                                                                 |
| Node ID           | Unique id related to teams and groups                                                |
| Group Name        | Name of the group on the Webex Connect  platform                                      |
| TeamName          | Name of the team on the Webex Connect  platform                                       |
| Service Name      | Name of the service on the Webex Connect  platform                                    |
| usage_start_time  | Month start date for usage file                                                      |
| usage_end_time    | Month end date for usage file                                                        |

> 📘 Note
> 
> Service is excluded for Facebook Messenger, In-app Messaging, Push Notifications, RCS, Apple Messages for Business, Automated Interactions, Number of users, Media, Numbers, TPS, 10DLC Brands, 10DLC Campaigns, Apps, Export Logs, Logbook reporting, Logbooks, Add-Ons, Summary.

## SMS Outbound

| Field Name              | Description                                                                                                                   |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| dist_id                 | Refers to distributor ID configured in NGMP. Can be ignored for most cases.                                                   |
| distributor             | Refers to the distributor configured in NGMP. Can be ignored for most cases.                                                  |
| status                  | Status of the request (E.g., submitted).                                                                                      |
| src_address             | Number/Sender Id used to send the message                                                                                     |
| messages_submitted      | Number/Count of messages sent using Webex Connect (Messages submitted to gateways for sending. It’s the multi-part SMS count). |
| destination_country     | Country to which outbound messages were sent to.                                                                              |
| number_type             | Type of asset number.                                                                                                         |
| destination_country_iso | End user number country code.                                                                                                 |
| country_iso             | The ISO code of the country.                                                                                                  |
| asset_country_iso       | Source address country id.                                                                                                    |
| is_10dlc_enabled        | Status of 10DLC enable(Y/N) of asset(Number).                                                                                 |
| carrier_id              | A short internal carrier identifier.                                                                                          |
| carrier_name            | The full name of the carrier that delivered the SMS traffic.                                                                  |
| delivered as RCS basic  | Count of messages that were enabled for RCS basic (branded text) and delivered as RCS basic message.                          |
| rate_type               | Type of rate assosciated with the Number. E.g., Standard or BYO Carrier.                                                      |

## SMS Inbound

| Field Name       | Descriptions                                                                               |
| :--------------- | :----------------------------------------------------------------------------------------- |
| number           | receiver ID.                                                                               |
| number_type      | Type of asset number.                                                                      |
| country_iso      | Source address country code.                                                               |
| message_received | Number of messages received from a end user.                                               |
| is_10dlc_enabled | Status of 10DLC enable(Y/N) of asset(Number).                                              |
| rate_type        | Type of rate assosciated with the Number. E.g., Standard, Free to End User or BYO Carrier. |
| carrier_id       | A short internal carrier identifier.                                                       |
| carrier_name     | The full name of the carrier that delivered the SMS traffic.                               |

## Voice

| Field Name  | Descriptions                                                                |
| :---------- | :-------------------------------------------------------------------------- |
| ServiceName | Name of the Webex Connect service.                                          |
| FlowName    | Name of the Webex Connect flow.                                             |
| Inbound     | Duration of incoming calls handled through the concerned flow (in Seconds). |
| Outbound    | Duration of outbound calls handled through the concerned flow (in Seconds). |

## Voice Pulse

| Field Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :----------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Call Type                                              | Indicates if the call is Outbound, Inbound, Trombone, or Call Transfer.                                                                                                                                                                                                                                                                                                                                                                    |
| Number Type                                            | Indicates the type of the user number - MOBILE and LANDLINE. If the end user type is not found, it indicates the number type as LANDLINE or MOBILE.                                                                                                                                                                                                                                                                                        |
| Country_ISO                                            | Contains the country code of user.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Call count                                             | Indicates the number of calls aggregated in the row. This will be used for calculating the flat rate per call.                                                                                                                                                                                                                                                                                                                             |
| Service number                                         | Contains the details of the Webex Connect asset number from which the outbound calls are made or at which the incoming calls are received.                                                                                                                                                                                                                                                                                                  |
| Asset Country ISO                                      | Contains the ISO country code of the asset/ service number.                                                                                                                                                                                                                                                                                                                                                                                |
| Service number type                                    | Indicates the type of the number - MOBILE, LANDLINE, or TOLLFREE.                                                                                                                                                                                                                                                                                                                                                                          |
| 15 Seconds pulse                                       | Count of 15 seconds pulse. Call duration will be calculated in 15-second increments. This means that if a call lasts, for example, 35 seconds, duration would be calculated three 15-second blocks.                                                                                                                                                                                                                                        |
| 30 Seconds pulse                                       | Count of 30 seconds pulse. Call duration will be calculated in 30-second increments. This means that if a call lasts, for example, 70 seconds, duration would be calculated three 30-second blocks.                                                                                                                                                                                                                                        |
| 45 Seconds pulse                                       | Count of 45 seconds pulse. Call duration will be calculated in 45-second increments. This means that if a call lasts, for example, 100 seconds, duration would be calculated three 45-second blocks.                                                                                                                                                                                                                                       |
| 60 Seconds pulse                                       | Count of 60 seconds pulse. Call duration will be calculated in 60-second increments This means that if a call lasts, for example, 125 seconds, duration would be calculated three 60-second blocks.                                                                                                                                                                                                                                        |
| 30 Seconds (30, 10s pulse), 10 Seconds (30, 10s pulse) | Count of first 30 seconds in call duration as 1 pulse under 30 Seconds (30, 10s pulse) and remaining call duration will be calculated as 10 seconds increments under column 10 Seconds (30, 10s pulse). For example if the call duration 45 seconds then first 30 seconds as one pulse under 30 Seconds (30, 10s pulse) and remaining duration 15 seconds will be calculated as two 10 seconds increments under 10 Seconds (30, 10s pulse) |
| 30 Seconds (30, 6s pulse), 6 Seconds (30, 6s pulse)    | Count of first 30 seconds in call duration as 1 pulse under 30 Seconds (30, 10s pulse) and remaining call duration will be calculated as 6 seconds increments under column 6 Seconds (30, 10s pulse). For example if the call duration 45 seconds then first 30 seconds as one pulse under 30 Seconds (30, 10s pulse) and remaining duration 15 seconds will be calculated as three 6 seconds increments under 6 Seconds (30, 6s pulse)    |

## Voice Ports

| Field Name                  | Description                                                                                       |
| :-------------------------- | :------------------------------------------------------------------------------------------------ |
| ib_ports_provisioned        | Inbound Ports provisioned for the tenant in the platform. It contains the most recent port count. |
| ib_ports_max_provisioned    | Highest Inbound ports provisioned in a current month.                                             |
| ob_ports_provisioned        | Outbound Ports provisioned for the tenant in the platform.                                        |
| ob_ports_max_provisioned    | Highest Outbound ports provisioned in a current month.                                            |
| total_ports_provisioned     | Contains the total count of ports (Inbound and Outbound).                                         |
| total_ports_max_provisioned | Contains the highest ports count for Inbound and Outbound.                                        |

## MMS Outbound

| Field Name              | Descriptions                                                             |
| :---------------------- | :----------------------------------------------------------------------- |
| status                  | Status of the request (e.g., submitted)                                  |
| src_address             | From which number/Sender id message sent                                 |
| messages_sent           | Number of messages sent through MMS channel on the Webex Connect platform |
| destination_country     | End user number's country                                                |
| destination_country_iso | End user number country code                                             |
| asset_country_iso       | Source address country id                                                |
| number_type             | Type of asset number                                                     |

## MMS Inbound

| Field Name       | Description                                  |
| :--------------- | :------------------------------------------- |
| number           | receiver ID                                  |
| number_type      | Type of asset number                         |
| country_iso      | Source address country code                  |
| message_received | Number of messages received from a end user  |
| is_10dlc_enabled | Status of 10DLC enable(Y/N) of asset(Number) |

## In-app Messaging

Please note that this page captured usage details for both In-App Messaging as well as for Live Chat.

| Field Name        | Descriptions                                                                     |
| :---------------- | :------------------------------------------------------------------------------- |
| app_id            | Unique id assigned to a channel app asset in Webex Connect                        |
| active_devices    | Addressable devices for the concerned app                                        |
| messages_sent     | Number of messages sent through the concerned app using in-app messaging channel |
| messages_received | Number of messages received via the concerned app using in-app messaging channel |

## Push Notifications

| Field Name         | Descriptions                                                |
| :----------------- | :---------------------------------------------------------- |
| app_id             | Unique id assigned to a channel app asset in Webex Connect   |
| active_devices     | Addressable devices for the concerned app                   |
| notifications_sent | Number of push notifications sent through the concerned app |

## Facebook Messenger

| Field Name        | Descriptions                                                                  |
| :---------------- | :---------------------------------------------------------------------------- |
| app_id            | Unique id of the concerned Facebook Messenger app asset on the Webex Connect   |
| active_users      | Number of unique users engaged (by sending or receiving a message)            |
| messages_sent     | Number of messages sent through Facebook messenger channel on the platform    |
| messages_received | Number of messages received though Facebook messenger channel on the platform |

## WhatsApp

| Field Name             | Descriptions                                                              |
| :--------------------- | :------------------------------------------------------------------------ |
| app_id                 | Unique id of the concerned WhatsApp app asset on the Webex Connect         |
| attachment             | count of attachments                                                      |
| active_users           | Number of unique users engaged (by sending or receiving a message)        |
| messages_sent          | Number of messages sent through WhatsApp channel                          |
| messages_received      | Number of messages received through WhatsApp channel                      |
| template_messages_sent | Number of template messages sent through WhatsApp channel                 |
| session_messages_sent  | Number of session messages sent through WhatsApp channel                  |
| waba_id                | Unique id of the concerned WhatsApp Business Account on the Webex Connect |

## Email

| Field Name      | Descriptions                                                      |
| :-------------- | :---------------------------------------------------------------- |
| app_id          | Unique id assigned to application on the Webex Connect  platform   |
| emails_sent     | Number of messages sent through email channel on the platform     |
| emails_received | Number of messages received through email channel on the platform |
| type            | template details                                                  |

## Apple Messages for Business

| Field Name        | Descriptions                                                                          |
| :---------------- | :------------------------------------------------------------------------------------ |
| app_id            | Unique id of the concerned Apple Messages for Business  app asset on the Webex Connect |
| active_users      | Number of unique users engaged (by sending or receiving a message)                    |
| messages_sent     | Number of messages sent through AMB channel on the platform                           |
| messages_received | Number of messages received through AMB channel on the platform                       |

## Google Business Messages

| Field Name        | Descriptions                                                                             |
| :---------------- | :--------------------------------------------------------------------------------------- |
| app_id            | Unique id of the concerned Google Business Messages  app asset on the Webex Connect       |
| active_users      | Number of unique users engaged (by sending or receiving a message)                       |
| messages_sent     | Number of messages sent through Google Business Messages channel on the platform         |
| messages_received | Number of messages received through Google Messages Business channel on the Webex Connect |

## RCS



| Field Name | Description |
| --- | --- |
| app_id | Unique id assigned to application on the Webex Connect platform |
| carrier_id | The unique ID assigned to the carrier of the MSISDN/mobile number to which the message is being sent. |
| carrier_name | The name of the carrier of the MSISDN/mobile number to which the message is being sent. |
| country_ISO | The name of the country of the MSISDN/mobile number to which the message is being sent. |
| maap | Maap of the RCS channel |
| messages_sent | Numbers of messages sent through RCS channel on the Webex Connect |
| basic_received | **US:** Incoming text-only messages. Charged per 160-character segment.  <br>**Non-US: **Not Applicable. |
| single_received | **US: **Incoming media or location (any non-text). Flat rate.  <br>**Non-US: **Not Applicable. |
| suggestionclicks_received | **US: **Counted when a user taps a suggested reply.  <br>**Non-US: ** Not Applicable. |
| messages_received | Number of messages received against RCS app on Webex Connect. |
| messages_delivered | Number of messages delivered. |
| capability_requests | Number of requests for capability. |
| basic_sent | **US:** Text, Suggested Reply, or open URL. Charged per 160-character segment.  <br>**Non-US: **Text-only messages 160 characters (UTF-8) |
| single_sent | **US: **Rich media (images/video), Carousel, Advanced Actions (WebView, Location). Flat rate.  <br>**Non-US: ** Text > 160 characters, messages with any Suggestions, or Rich Media. Flat rate. |




## Node Executions

| Field Name           | Descriptions                                  |
| :------------------- | :-------------------------------------------- |
| Node Name            | Name of the flow on the Webex Connectplatform  |
| Flow Name            | Name of the flow on the Webex Connect platform |
| Number of Executions | Count of node executions                      |

## Workflows

| Field Name     | Descriptions                                                                                                                                    |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| workflow       | Name of the flow on the platform                                                                                                                |
| executions     | Number of flow executions                                                                                                                       |
| sumunits       | Chargeable flow execution units. Every 7 days of flow run is counted as one one unit. E.g., A flow that runs for 10 days is counted as 2 units. |
| syncexecutions | Applies to synchronous executions (not a launched feature yet)                                                                                  |

## Numbers

| Field Name             | Descriptions                                                                                                                                                                                                                              |
| :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NUMBER                 | Number (asset)                                                                                                                                                                                                                            |
| type                   | Number type                                                                                                                                                                                                                               |
| bought_on              | Number purchased date                                                                                                                                                                                                                     |
| US 10DLC Brand ID      | Brand ID assigned to the number                                                                                                                                                                                                           |
| US 10DLC Campaign ID   | Campaign ID assigned to the number                                                                                                                                                                                                        |
| US TFN Verified Sender | Is TFN verified yes/no                                                                                                                                                                                                                    |
| country_iso            | Source address country code                                                                                                                                                                                                               |
| features               | The features impacted                                                                                                                                                                                                                     |
| vanity_number          | This field is used to identify the vanity number in the number column. If it contains the value 'Y', then the value in the number column will be the vanity number. If it does not contain the value 'Y', it will be a non-vanity number. |

## Inbound Webhook

| Field Name | Descriptions                                    |
| :--------- | :---------------------------------------------- |
| eventid    | Unique id assigned to the event on the platform |
| executions | Webhooks received count                         |
| type       | type of the webhook                             |

## Outbound Webhook

| Field Name | Descriptions                                      |
| :--------- | :------------------------------------------------ |
| webhook_id | unique id assigned to the webhook on the platform |
| executions | Number of webhook execution count                 |

## Custom Events

| Field Name | Descriptions                                    |
| :--------- | :---------------------------------------------- |
| eventid    | Unique ID assigned to the event on the platform |
| events     | custom events count                             |
| type       | ID of the customEvent type                      |

## Webex Engage

| Field Name    | Descriptions                                  |
| :------------ | :-------------------------------------------- |
| IntegrationId | Unique id assigned to integration in imienage |
| sessions      | No.of imienage sessions                       |
| subchannel    | ID of the sub channel                         |

## Custom Node

| Field Name | Descriptions                            |
| :--------- | :-------------------------------------- |
| Name       | Name of the custom node in the platform |
| methodName | Name of the method in CustomNode        |
| methodtype | Type of method (E.g.,Get/Post/Patch)    |
| execution  | No.of node executions                   |

## PrebuiltIntegration

| Field Name       | Descriptions                                      |
| :--------------- | :------------------------------------------------ |
| node_name        | Contains the node name on the platform            |
| methodName       | Name of the method on the platform                |
| methodtype       | Type of the method (E.g.,Get/Post/Delete/Put)     |
| methodID         | Unique ID assigned to the method in the platform  |
| node_id          | Unique ID assigned to node on the platform.       |
| execution        | Prebuilt node execution count                     |
| integration_name | Contains the integration name                     |
| integration_id   | Unique ID assigned to integration on the platform |

## Speech recognition, TTS and Recording

| Field Name               | Descriptions                                                                                                                                                                                                           |
| :----------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| flowname                 | Name of the flow on the Webex Connect platform                                                                                                                                                                          |
| Recording duration       | duration of the recording in secs                                                                                                                                                                                      |
| Recording size           | size of the recording in MB                                                                                                                                                                                            |
| TTS Characters processed | Number of characters processed                                                                                                                                                                                         |
| TTS Type                 | Type of TTS (Standard/Neural)                                                                                                                                                                                          |
| Speech to text (mins)    | Duration of the speech recognition in minutes                                                                                                                                                                          |
| TTS Billables            | Webex Connect stores the content generated for 24 hours. If the TTS request with same content is made within 24 hours, then it considered as cached content. Characters from such requests are excluded in this column. |

## Answering machine

| Field Name | Descriptions                                  |
| :--------- | :-------------------------------------------- |
| flowname   | Name of the flow on the Webex Connect platform |
| calls      | No.of calls answered                          |
| flowid     | Unique ID assigned to the flow                |

## Logbooks

| Field Name      | Descriptions                                                        |
| :-------------- | :------------------------------------------------------------------ |
| LogbookID       | Unique id assigned to logbook created on the Webex Connect  platform |
| Logbook_name    | Name of the logbook created on the Webex Connect platform            |
| BI_enabled      | logbook reporting enabled status(Yes/No)                            |
| Files_generated | Number of logbook files generated on the platform                   |
| Total_size_KB   | Total size of generated logbooks on the platform                    |
| Total_records   | Total record count of generated logbooks on the platform            |

## Logbook Reporting

| Field Name | Descriptions                       |
| :--------- | :--------------------------------- |
| item       | access details of users(Edit/View) |
| Users      | Number of users                    |

## Export Logs

| Field Name                    | Descriptions                                       |
| :---------------------------- | :------------------------------------------------- |
| Type                          | type of export                                     |
| Date                          | date of the export                                 |
| Number of files processed     | Total number of files processed                    |
| Total size of files processed | Total size of the files processed                  |
| Number of schedules           | Number of export schedules configured and executed |

## Debug-Archive search

| Field Name       | Descriptions                           |
| :--------------- | :------------------------------------- |
| type             | type of search                         |
| datetime         | date and time of the search            |
| query_count      | total count of queries                 |
| datascan_size_KB | Total size of datascan on the platform |

## Add-Ons

| Field Name | Descriptions                            |
| :--------- | :-------------------------------------- |
| Add Ons    | Name of the add-on                      |
| Access     | status of the add-on (enable / disable) |

## Automated Interactions

| Field Name                   | Description                                               |
| :--------------------------- | :-------------------------------------------------------- |
| direction                    | Direction of the interaction(Inbound/Outbound)            |
| channel                      | Name of the channel on which the interaction has happened |
| automated_interactions_count | Total count of number of interactions                     |
| total_count                  | Count of interactions with and without agent              |

## TPS

| Field Name    | Description                                           |
| :------------ | :---------------------------------------------------- |
| event_api_tps | TPS value configured for event api for the tenant     |
| msg_api_tps   | TPS value configured for messaging api for the tenant |

## Number of Users

| Field Name | Descriptions                   |
| :--------- | :----------------------------- |
| count      | total count of number of users |

> 📘 Exclusion of specified users in count
> 
> The ‘Users’ count available within Webex Connect Usage section and exported XLS usage reports will exclude Cisco helpdesk users from the calculations.

## 10DLC Brands

| Field Name         | Description                                      |
| :----------------- | :----------------------------------------------- |
| brands_registered  | Count of brands registered                       |
| brands_resubmitted | Number of times clicked on brand resubmit button |

## 10DLC Campaigns

| Field Name          | Description                   |
| :------------------ | :---------------------------- |
| campaign_usecase    | Name of the campaign use case |
| campaigns_activated | Count of campaigns created    |

## Apps

| Field Name    | Description                                                                                                                                           |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| app_id        | A unique identification number that is assigned when an app is created                                                                                |
| app_name      | Name of the app in the Webex Connect flow                                                                                                             |
| created_on    | Date on which the app is created in the usage file                                                                                                    |
| channel       | Contains the name of the channel                                                                                                                      |
| timezone      | Displays the timezone of the app                                                                                                                      |
| app_type      | This field is only applicable for WhatsApp apps. Contains On-premise and Cloud. This contains the API settings of the WhatsApp app                    |
| migrated_date | Contains the date on which the app is migrated from On-prem to Cloud. If not applicable, it will display as 'NA' (displays NA for all other channels) |

## Summary

| Field Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :----------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Billing Region                                         | The country code of the location where the bill was generated.                                                                                                                                                                                                                                                                                                                                                                             |
| SMS Outbound (messages)                                | Contains total count of the SMS channel messages sent                                                                                                                                                                                                                                                                                                                                                                                      |
| Voice (secs)                                           | Contains total duration of the Voice Inbound and Outbound                                                                                                                                                                                                                                                                                                                                                                                  |
| MMS Outbound (messages)                                | Contains total count of messages sent through MMS channel                                                                                                                                                                                                                                                                                                                                                                                  |
| In-app (MADs)                                          | In-app channel Monthly Addressable Device count                                                                                                                                                                                                                                                                                                                                                                                            |
| Push Notifications (MADs)                              | Contains total count of the Push Notifications monthly addressable device count                                                                                                                                                                                                                                                                                                                                                            |
| Facebook Messenger (MAUs)                              | Contains Facebook Messenger total count of monthly active users                                                                                                                                                                                                                                                                                                                                                                            |
| WhatsApp (messages)                                    | Contains total count of the WhatsApp Outbound and Inbound messages                                                                                                                                                                                                                                                                                                                                                                         |
| Email (messages)                                       | Contains total count of Emails sent and received                                                                                                                                                                                                                                                                                                                                                                                           |
| Email Submits                                          | Contains total count of Emails sent                                                                                                                                                                                                                                                                                                                                                                                                        |
| RCS (messages)                                         | Contains total count of messages sent and received through RCS channel                                                                                                                                                                                                                                                                                                                                                                     |
| RCS Submits                                            | Contains total count of messages sent through RCS channel                                                                                                                                                                                                                                                                                                                                                                                  |
| Apple Messages for Business (MAUs)                     | Contains AMB total count of Monthly Active Users                                                                                                                                                                                                                                                                                                                                                                                           |
| Node Executions                                        | Contains total count of node executions                                                                                                                                                                                                                                                                                                                                                                                                    |
| Workflow Execution Units                               | Contains total count flow executions                                                                                                                                                                                                                                                                                                                                                                                                       |
| Numbers                                                | Contains total count of numbers provisioned.                                                                                                                                                                                                                                                                                                                                                                                               |
| Media (size)                                           | Contains total size of media                                                                                                                                                                                                                                                                                                                                                                                                               |
| InboundWebhook                                         | Contains total count of inbound webhooks                                                                                                                                                                                                                                                                                                                                                                                                   |
| OutboundWebhook                                        | Contains total count of outbound webhooks                                                                                                                                                                                                                                                                                                                                                                                                  |
| CustomEvents                                           | Contains total count of messages received and sent via custom events                                                                                                                                                                                                                                                                                                                                                                       |
| imiconnect Bot                                         | Contains total count of messages sent via native Bot Builder nodes (QnA, Task native nodes)                                                                                                                                                                                                                                                                                                                                                |
| Third-Party Bot                                        | Contains total count of execution of Third-Party Bot integration.                                                                                                                                                                                                                                                                                                                                                                          |
| CustomNode                                             | Contains total count of custom node executions                                                                                                                                                                                                                                                                                                                                                                                             |
| PrebuiltIntegration                                    | Contains total count of prebuilt integration executions                                                                                                                                                                                                                                                                                                                                                                                    |
| Recordings (Duration)                                  | Contains total duration of recordings                                                                                                                                                                                                                                                                                                                                                                                                      |
| TTS Standard (Characters)                              | Contains total count of processed characters with TTS type TTS Standard                                                                                                                                                                                                                                                                                                                                                                    |
| TTS Neural (Characters)                                | Contains total count of processed characters with TTS type TTS Neural                                                                                                                                                                                                                                                                                                                                                                      |
| Answering machine (Calls Proccessed)                   | Contains total count of calls processed                                                                                                                                                                                                                                                                                                                                                                                                    |
| Logbooks (Total_size_KB)                               | Contains total size of logbooks processed                                                                                                                                                                                                                                                                                                                                                                                                  |
| BILogbook-ViewOnlyUsers                                | Contains total count of users with view  permissions                                                                                                                                                                                                                                                                                                                                                                                       |
| BILogBook-EditUsers                                    | Contains total count of users with edit  permissions                                                                                                                                                                                                                                                                                                                                                                                       |
| Export Logs (Total_size_KB)                            | Contains total size of export logs processed                                                                                                                                                                                                                                                                                                                                                                                               |
| Debug-Archive search (Total_size_KB)                   | Contains total size of data scan of debug-archive search                                                                                                                                                                                                                                                                                                                                                                                   |
| Prebuilt Async                                         | Contains total count of Prebuilt Async Events invoked                                                                                                                                                                                                                                                                                                                                                                                      |
| 15 Seconds pulse                                       | Count of 15 seconds pulse. Call duration will be calculated in 15-second increments. This means that if a call lasts, for example, 35 seconds, duration would be calculated three 15-second blocks.                                                                                                                                                                                                                                        |
| 30 Seconds pulse                                       | Count of 30 seconds pulse. Call duration will be calculated in 30-second increments. This means that if a call lasts, for example, 70 seconds, duration would be calculated three 30-second blocks.                                                                                                                                                                                                                                        |
| 45 Seconds pulse                                       | Count of 45 seconds pulse. Call duration will be calculated in 45-second increments. This means that if a call lasts, for example, 100 seconds, duration would be calculated three 45-second blocks.                                                                                                                                                                                                                                       |
| 60 Seconds pulse                                       | Count of 60 seconds pulse. Call duration will be calculated in 60-second increments This means that if a call lasts, for example, 125 seconds, duration would be calculated three 60-second blocks.                                                                                                                                                                                                                                        |
| 30 Seconds (30, 10s pulse), 10 Seconds (30, 10s pulse) | Count of first 30 seconds in call duration as 1 pulse under 30 Seconds (30, 10s pulse) and remaining call duration will be calculated as 10 seconds increments under column 10 Seconds (30, 10s pulse). For example if the call duration 45 seconds then first 30 seconds as one pulse under 30 Seconds (30, 10s pulse) and remaining duration 15 seconds will be calculated as two 10 seconds increments under 10 Seconds (30, 10s pulse) |
| 30 Seconds (30, 6s pulse), 6 Seconds (30, 6s pulse)    | Count of first 30 seconds in call duration as 1 pulse under 30 Seconds (30, 10s pulse) and remaining call duration will be calculated as 6 seconds increments under column 6 Seconds (30, 10s pulse). For example if the call duration 45 seconds then first 30 seconds as one pulse under 30 Seconds (30, 10s pulse) and remaining duration 15 seconds will be calculated as three 6 seconds increments under 6 Seconds (30, 6s pulse)    |

Please note that the following fields are not listed above as those features have already been deprecated: Enghouse, InContact, Cisco ECE, Salesforce (old version of Salesforce integration), imiengage, and SkypeforBusiness (messages).