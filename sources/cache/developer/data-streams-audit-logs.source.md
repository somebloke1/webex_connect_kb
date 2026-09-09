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

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "user_action",
    "0-1": "List of all the user actions. There are around 100+ user actions in the Audit Log. The list of these actions will be available  under Profile > User Audit > Select Action. There are about 270 actions in the Audit Logs. Please note that the <<prodname>> platform adds new user actions from time to time. For the complete list of User Actions, please refer to the [User Actions](https://developers.webexconnect.io/reference/data-streams-audit-logs#user-actions) section after this table.",
    "0-2": "\"updateMobileWebAppType\"",
    "1-0": "description",
    "1-1": "The description of the user action.",
    "1-2": "\"Jack updated MultiprofileAWSUK app\"",
    "2-0": "dataIntegration",
    "2-1": "The object contains   key-value pairs which are added either by Data Stream admin or in flow and also app context object.",
    "2-2": "\"dataIntegration\": {    \"context\":  \n {       \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n},  \n“appContext”: {  \n}  \n}",
    "3-0": "context",
    "3-1": "The object contains key-value pairs which are added by platform users in the flow.",
    "3-2": "\"context\": {   \n\"key1\": \"value1\",  \n\"key2\": \"value2\",  \n\"key3\": \"value3\"     \n}",
    "4-0": "appcontext",
    "4-1": "The object is added as key-value pair by Data Stream admin.",
    "4-2": "“appContext“: {  \n“key1”: “value1“,  \n“key2”: “value2“  \n}",
    "5-0": "alert_type",
    "5-1": "The type of alert. It can be success, error etc. Example if update app action failed the alert type will be Error.",
    "5-2": "\"SUCCESS\"",
    "6-0": "service_id",
    "6-1": "Unique identifier of the service that the action was part of. If the action doesn’t involve service, then the value is empty.",
    "6-2": "\"89195\"",
    "7-0": "WebexOrgid",
    "7-1": "Unique identifier of the Webex Organization that is mapped to Connect tenant.",
    "7-2": "\"211e0b7c-3b5e-49e0-a616-346ee668xxxx\"",
    "8-0": "client_ip",
    "8-1": "The IP address of the user.",
    "8-2": "\"20.7.156.890\"",
    "9-0": "status_of_action",
    "9-1": "The execution status of the action.",
    "9-2": "\"SUCCESS\"",
    "10-0": "transid",
    "10-1": "Unique identifier of the transaction.",
    "10-2": "\"062dxxxx-58d7-431e-9e5b-f79fe4b3xxxx\"",
    "11-0": "cpaasOrgid",
    "11-1": "Unique identifier of the CPaas Organization that is mapped to Connect tenant.",
    "11-2": "\"ed4cxxxx-f14c-46f2-96b8-af0e6615xxxx\"",
    "12-0": "role_name",
    "12-1": "The role name assigned to the user.",
    "12-2": "\"Owner\"",
    "13-0": "clientUUID",
    "13-1": "Unique identifier of the tenant in which the action has occurred.",
    "13-2": "\"66cexxxx-26a9-405e-b3a9-02be1af8xxxx\"",
    "14-0": "x-wx-gtrid",
    "14-1": "Unique identifier parameter added by <<prodname>>. It is always empty for Audit Logs.",
    "14-2": "\"66cexxxx-26a9-405e-b3a9-02be1af8xxxx\"",
    "15-0": "created_on",
    "15-1": "The timestamp when the action occurred on the platform.",
    "15-2": "\"20xx-07-30T67:05:xx.605Z\"",
    "16-0": "user_id",
    "16-1": "Unique identifier of the user. The email address of the user.",
    "16-2": "[xyzuser@abc.com](mailto:xyzuser@abc.com)",
    "17-0": "group_id",
    "17-1": "Unique identifier of the Group that the user is part of.",
    "17-2": "\"4675\""
  },
  "cols": 3,
  "rows": 18,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## User Actions (User Audit - Event Categories)

The following table contains the complete list of User Actions on the <<prodname>> platform.

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