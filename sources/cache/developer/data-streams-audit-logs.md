# Data Streams - Audit Logs

Source: https://developers.webexconnect.io/reference/data-streams-audit-logs
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:31:49+00:00

## Audit Logs Payload Sample

Following is the inbound message payload:

```json Payload Sample
{
  "user_action": "updateApp",
  "description": "Jim failed to update Facebook Messenger app",
  "dataIntegration": {
    "context": {},
    "appContext": {}
  },
  "alert_type": "ERROR",
  "service_id": "",
  "webexOrgId": "211e0b7c-3b5e-XXXX-a616-346ee668xxxx",
  "client_ip": "72.xxx.220.xx",
  "status_of_action": "ERROR",
  "transid": "062dxxxx-58d7-431e-XXXX-f79fe4b3xxxx",
  "cpassOrgId": "ed4cxxxx-f14c-46f2-XXXX-af0e6615xxxx",
  "role_name": "Owner",
  "clientUUID": "66cexxxx-26a9-405e-XXXX-02be1af8xxxx",
  "x-wx-gtrid": "",
  "created_on": "20xx-09-25T08:11:02.xxxx",
  "user_id": "JimRohn@@xyz.com",
  "group_id": "50xx"
}
```

## Message Descriptions

The following table contains the parameter descriptions of Audit Logs Message.



| Field Name | Description | Example |
| --- | --- | --- |
| user_action | List of all the user actions. There are around 100+ user actions in the Audit Log. The list of these actions will be available  under Profile > User Audit > Select Action. There are about 270 actions in the Audit Logs. Please note that the Webex Connect platform adds new user actions from time to time. For the complete list of User Actions, please refer to the [User Actions](https://developers.webexconnect.io/reference/data-streams-audit-logs#user-actions) section after this table. | "updateMobileWebAppType" |
| description | The description of the user action. | "Jack updated MultiprofileAWSUK app" |
| dataIntegration | The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object. | "dataIntegration": {    "context":  <br> {       <br>"key1": "value1",  <br>"key2": "value2",  <br>"key3": "value3"     <br>},  <br>“appContext”: {  <br>}  <br>} |
| context | The object contains key-value pairs which are added by platform users in the flow. | "context": {   <br>"key1": "value1",  <br>"key2": "value2",  <br>"key3": "value3"     <br>} |
| appcontext | The object is added as key-value pair by Data Stream admin. | “appContext“: {  <br>“key1”: “value1“,  <br>“key2”: “value2“  <br>} |
| alert_type | The type of alert. It can be success, error etc. Example if update app action failed the alert type will be Error. | "SUCCESS" |
| service_id | Unique identifier of the service that the action was part of. If the action doesn’t involve service, then the value is empty. | "89195" |
| WebexOrgid | Unique identifier of the Webex Organization that is mapped to Connect tenant. | "211e0b7c-3b5e-49e0-a616-346ee668xxxx" |
| client_ip | The IP address of the user. | "20.7.156.890" |
| status_of_action | The execution status of the action. | "SUCCESS" |
| transid | Unique identifier of the transaction. | "062dxxxx-58d7-431e-9e5b-f79fe4b3xxxx" |
| cpaasOrgid | Unique identifier of the CPaas Organization that is mapped to Connect tenant. | "ed4cxxxx-f14c-46f2-96b8-af0e6615xxxx" |
| role_name | The role name assigned to the user. | "Owner" |
| clientUUID | Unique identifier of the tenant in which the action has occurred. | "66cexxxx-26a9-405e-b3a9-02be1af8xxxx" |
| x-wx-gtrid | Unique identifier parameter added by Webex Connect. It is always empty for Audit Logs. | "66cexxxx-26a9-405e-b3a9-02be1af8xxxx" |
| created_on | The timestamp when the action occurred on the platform. | "20xx-07-30T67:05:xx.605Z" |
| user_id | Unique identifier of the user. The email address of the user. | [xyzuser@abc.com](mailto:xyzuser@abc.com) |
| group_id | Unique identifier of the Group that the user is part of. | "4675" |




## User Actions (User Audit - Event Categories)

The following table contains the complete list of User Actions on the Webex Connect platform.

| User Actions                                    |
| ----------------------------------------------- |
| ArchiveDecryptLogs                              |
| ArchiveIntegrationDebugLogs                     |
| ArchiveNodeData                                 |
| ArchiveNodeHistory                              |
| ArchiveQueryByDestinationId                     |
| ArchiveQueryByTransactionId                     |
| ArchiveVoiceDebug                               |
| Copied Profile Key                              |
| Copied Service ID                               |
| Copied Service Key                              |
| Copied Service Secret                           |
| DecryptLogs                                     |
| DeleteMMSAttachment                             |
| HttpNodeLogsInFlowTrans                         |
| InboudEventLogs                                 |
| LockedLogBook                                   |
| MMSFilesListing                                 |
| QueryByTransactionId                            |
| TemplateLocked                                  |
| TemplateUnLocked                                |
| ViewFlow                                        |
| Viewed Profile Key                              |
| Viewed Service ID                               |
| Viewed Service Key                              |
| Viewed Service Secret                           |
| addOptOutKeyword                                |
| addOrUpdateSAMLSettings                         |
| addPrebuiltAuthentication                       |
| addSystemUserToWabaId                           |
| attacheCreditLineToWaba                         |
| automationusageReport                           |
| campaignMMUpload                                |
| cancelInviteUser                                |
| changePassword                                  |
| createApp                                       |
| createBrandId                                   |
| createCampaignId                                |
| createCustomEvent                               |
| createCustomNode                                |
| createFlow                                      |
| createFolder                                    |
| createFolderWithDefaultId                       |
| createGroup                                     |
| createInviteUser                                |
| createLangFolder                                |
| createLogBook                                   |
| createMediaFile                                 |
| createMobileWebTypeApp                          |
| createNodeMethod                                |
| createRule                                      |
| createService                                   |
| createServiceCredential                         |
| createShortLink                                 |
| createTeam                                      |
| createTemplate                                  |
| deleteApp                                       |
| deleteAuthorizationIntegration                  |
| deleteCredential                                |
| deleteCustomEvent                               |
| deleteCustomNode                                |
| deleteFlow                                      |
| deleteFolder                                    |
| deleteKwd                                       |
| deleteLangFolder                                |
| deleteLogBook                                   |
| deleteMedia                                     |
| deleteOutBoundWebHook                           |
| deletePrebuiltAuthentication                    |
| deleteRule                                      |
| deleteSenderId                                  |
| deleteService                                   |
| deleteShortCode                                 |
| deleteShortLink                                 |
| deleteTemplate                                  |
| deleteUserByUUID                                |
| deprovisioningNumber                            |
| discardCredential                               |
| dkimVerificationStatus                          |
| downloadExportLogFile                           |
| downloadExportTransactionLogs                   |
| downloadMultiSelectExportTransactionLogs        |
| downloadMultiSelectExportTransactionLogsViaFile |
| exportFlow                                      |
| fetchMobileNumbersInWaba                        |
| fetchSharedWabaId                               |
| fetchVoiceTTSResourceDetails                    |
| fetchVoiceTTSResourceURL                        |
| generateFlowConcurrencyReport                   |
| generateSmartLinksClickReport                   |
| getASRProviderDetails                           |
| getAllNumbers                                   |
| getAllSenderIds                                 |
| getAllWhatsappTemplates                         |
| getApprovedTemplates                            |
| getApprovedVoiceLimits                          |
| getAppsReport                                   |
| getAuthorizationIntegrationDetails              |
| getAuthorizationIntegrationsList                |
| getAutomationUsage                              |
| getAvailableKeywords                            |
| getBrandDetailsByTenant                         |
| getBrandDetailsByUUID                           |
| getBrandFeedBack                                |
| getCPXStockExchange                             |
| getCampaignDetailsById                          |
| getCampaignDetailsList                          |
| getCampaignSupportingDocsList                   |
| getCampaignUsecases                             |
| getCampaignVerticals                            |
| getChannelHistory                               |
| getChartFlowsAnalytics                          |
| getConsentGroups                                |
| getCountries                                    |
| getCustomNodeJSONPathParams                     |
| getCustomNodeLogs                               |
| getDedicatedIps                                 |
| getDescriptiveLogs                              |
| getDmarcPolicy                                  |
| getDomainStatus                                 |
| getEmailReport                                  |
| getEvent                                        |
| getFacebookReport                               |
| getFlowAnalytics                                |
| getFlowExecutions                               |
| getFlowExecutionsWithMessageSent                |
| getFlowList                                     |
| getFlowsByServiceIds                            |
| getFolders                                      |
| getFoldersMenuList                              |
| getInstgaramReport                              |
| getIntegrationDetails                           |
| getIntegrationErrorDetails                      |
| getIntegrationGraphDetails                      |
| getIntegrationGroups                            |
| getIntegrationSyncChangeLogs                    |
| getLangFiles                                    |
| getLangFolders                                  |
| getLanguagePromptDetailsByFolderId              |
| getLogBookById                                  |
| getLogBooksFlowInfo                             |
| getLogBooksLogs                                 |
| getMappedRules                                  |
| getMessageFailuresByReason                      |
| getMessagingAPIRequests                         |
| getNodeIntegrationList                          |
| getNodeMethod                                   |
| getNodeMethodList                               |
| getNumberReport                                 |
| getNumbersReport                                |
| getOptOutKeyword                                |
| getOptOutKeywords                               |
| getOutBoundWebHook                              |
| getOutboundWebhookList                          |
| getPrebuiltAuthenticationDetails                |
| getPrebuiltDataIntegrationDetails               |
| getPrebuiltIntegrationDetails                   |
| getRcsReports                                   |
| getRecordingListing                             |
| getRecordingsSearch                             |
| getReports                                      |
| getResource                                     |
| getRuleExecutions                               |
| getRuleInfo                                     |
| getSMPPBindDetails                              |
| getServicelanding                               |
| getServicesByTeamAndGroupId                     |
| getServicetraffic                               |
| getShortLinkInfo                                |
| getShortLinkList                                |
| getSocialApp                                    |
| getSpfSettings                                  |
| getSummaryData                                  |
| getTPSLimitReachedErrorReports                  |
| getTPSSummaryAPIReports                         |
| getTPSSummaryReports                            |
| getTemplateCategories                           |
| getTemplateInfo                                 |
| getTemplateLanguages                            |
| getTemplates                                    |
| getTenantSettings                               |
| getUsageHistory                                 |
| getUsageHistoryXLFile                           |
| getUsers                                        |
| getVoiceDebug                                   |
| getVoiceProviderDetails                         |
| getVoiceProviderDetailsNewApi                   |
| getWAAccountStatus                              |
| getWFNodeHistory                                |
| getWabaId                                       |
| getWabaTemplatesAndSave                         |
| getWebexIntegrationDetails                      |
| getWfNodeVariables                              |
| getWhatsAppReport                               |
| getWhatsappBusinessCategories                   |
| insertKeyword                                   |
| insertOutBoundWebHook                           |
| insertVoicePin                                  |
| integrationSyncUserUpdate                       |
| login                                           |
| logout                                          |
| makeDefaultPrebuiltAuthentication               |
| notifyOnThrottleVoiceSettingUpdate              |
| numberAssignment                                |
| orderStatus                                     |
| parseSSOSamlResponse                            |
| prebuiltActivateInboundAuth                     |
| purchaseNumber                                  |
| qualifyBrandByUsecase                           |
| qualifyBrandForAllUsecases                      |
| reactivateCredential                            |
| regenerateProfileKey                            |
| reinviteUser                                    |
| releaseNumber                                   |
| requestResource                                 |
| resubmitBrandId                                 |
| saveAuthorizationIntegration                    |
| saveSenderId                                    |
| searchPhoneNumbers                              |
| shareApp                                        |
| subscribeWebhookEvents                          |
| switchLevel                                     |
| syncCPXWebhookEvent                             |
| tenantHelpDeskCallback                          |
| unLockLogBook                                   |
| updateApp                                       |
| updateBounceListRetentionPeriodSettings         |
| updateBrandId                                   |
| updateCustomEvent                               |
| updateCustomNode                                |
| updateDescriptiveLogs                           |
| updateEmailDomainSettings                       |
| updateFolder                                    |
| updateGroup                                     |
| updateHelpDeskSettings                          |
| updateInviteUser                                |
| updateLogBook                                   |
| updateLogBookStatus                             |
| updateMobileWebAppType                          |
| updateMultiSelectSchedulerDetails               |
| updateNodeMethod                                |
| updateNodeStatus                                |
| updateOutBoundWebHook                           |
| updatePrebuiltAuthentication                    |
| updatePrebuiltDynamicData                       |
| updateResourceNotificationSettings              |
| updateRule                                      |
| updateRuleStatus                                |
| updateSchedulerStatusDetails                    |
| updateServiceLockStatus                         |
| updateShortLink                                 |
| updateTemplate                                  |
| updateTenantSecuredMediaSettings                |
| updateTenantSettings                            |
| updateUser                                      |
| updateWfStatusOnCreateRule                      |
| updateWfStatusOnUpdateRule                      |
| uploadCampaignSupportingDocs                    |
| uploadMediaFile                                 |
| uploadMediaURL                                  |
| uploadMediaUtil                                 |
| uploadSFTPCertificate                           |
| uploadVoiceTTSMediaFile                         |
| waFetchNumberByAppId                            |
| waLinkPhoneNumber                               |
| waRequestOTP                                    |
| waValidateOTP                                   |
| waWabaReviewStatus                              |
| webexCICpassCallback                            |

## API reference metadata

These are source metadata and examples. `api.auth` is ReadMe metadata; verify authentication in the documented headers/security scheme.

```json
{
  "method": "get",
  "url": "",
  "auth": "required",
  "results": {
    "codes": [
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 200
      },
      {
        "name": "",
        "code": "{}",
        "language": "json",
        "status": 400
      }
    ]
  },
  "params": [],
  "examples": {
    "codes": []
  }
}
```
