## Introduction

The Resolve Conversation node invokes a middleware micro-service between Webex Contact Center and Webex Engage, managing conversations and tasks across these integrated platforms. Its primary function is to evaluate incoming messages using sender, recipient, and channel details to determine whether to initiate a new conversation or append the message to an existing one. By consolidating logic that was previously distributed across multiple nodes—such as searching for a conversation, appending to an existing one, or creating a new task—the Resolve Conversation node simplifies flow configuration, although it may make the underlying process less transparent to users.

## Authorization

Refer to section [Node Authorizations](https://help.imiconnect.io/docs/wxcc-node-palette#section-node-authorization) for more information.

## Context

### How does this work internally?

The Resolve Conversation node automatically checks for existing conversations across various channels-such as chat, email, or social by evaluating sender, recipient, and channel information. If a matching conversation is found, it routes the message; accordingly, otherwise, it initiates a new conversation.

### Chat

A step-by-step procedure for how the Resolve Conversation node handles chat:

1. **Identify conversation context: **  
   The node extracts key attributes from the incoming chat:
   - Customer Address → Livechat Browser Fingerprint
   - Business Address → Livechat App ID
   - Livechat Thread ID → UUID
2. **Search for a unique conversation: **  
   Using the combination of these attributes (Customer Address + Business Address + Thread ID), the node searches for an existing conversation in the system.
3. **Invoke next steps based on conversation status: **

   - If an Active or Queued conversation exists:
     - Append the incoming message to the ongoing conversation.
   - If only a Closed conversation exists, or if no conversation is found:

     - Create a new conversation.
     - Generate a new task and link it to the new conversation.

       [block:image]{"images":[{"image":["https://files.readme.io/265ba1f600529371b634a883d78edf842624477fe050b74eee32314db956600e-Resolve_conversation_node_-_Chat.png",null,"Chat Resolve Conversation"],"align":"center","sizing":"2000px","caption":"Chat Resolve Conversation"}]}[/block]

> 📘 Note:
> 
> We currently do not support reopening a conversation on Livechat channel.

Email

A step-by-step procedure for how the Resolve Conversation node handles email:

1. **Extract Attributes from Incoming Email: **
   - Check if the "In-Reply-To" header is present.
   - If not, resort to subject-recipient based search using the following parameters by capturing them from the incoming email :
     - Customer Address (Email ID)
     - Business Address (Mailbox)
     - Email Subject
2. **Search for an Existing Conversation: **
   - First, use the "In-Reply-To" header to try to find a matching conversation.
   - If "In-Reply-To" is not available, use the combination of Customer Address, Business Address, and Email Subject.
3. **Evaluate Conversation Status: **

   - If an Active or Queued conversation is found:
     - Append the incoming message to the existing conversation.
   - If a Closed conversation is found:
     - Re-open the closed conversation to preserve customer history.
     - Append the new message to the re-opened conversation.
     - Create a new task and update the conversation with this new task ID.
   - If no conversation exists (new customer):

     - Create a new conversation.
     - Create a new task and update the conversation with the task ID.

       [block:image]{"images":[{"image":["https://files.readme.io/328a171f3fa7aa083500d655d4e9c70dd16752ce5082413ab86b993b49d9d803-Resolve_conversation_node_-_Email.png",null,"Email Resolve Conversation"],"align":"center","caption":"Email Resolve Conversation"}]}[/block]

### Social (SMS / Facebook / Apple Messages for Business/ Whatsapp)

A step-by-step procedure for how the Resolve Conversation node handles channels like SMS, Facebook, Apple Messages for Business, and Whatsapp:

1. **Extract Key Attributes from the Incoming Message: **
   - Customer Address (e.g., Customer Mobile Number, Page Scoped ID (PSID), AMB Opaque ID, Whatsapp Number)
   - Business Address (e.g., SMS Longcode, Facebook Page ID, Apple Messages for Business Account ID, Whatsapp Business Longcode)
2. **Search for an Existing Conversation: **  
   - Use the combination of customer and business address to identify a unique conversation ID.
3. ** Evaluate and Route Based on Conversation Status: **

- If an Active or Queued conversation exists:
  - Append the incoming message to the ongoing conversation.
- If a Closed conversation exists:
  - Re-open the closed conversation to preserve customer history.
  - Append the new message to the re-opened conversation.
  - Create a new task and update the conversation with this new task ID.
- If no conversation exists (new customer):

  - Create a new conversation.
  - Create a new task and update the conversation with the task ID.

    [block:image]{"images":[{"image":["https://files.readme.io/c51acab59bd7ce274905705d09bada56ddf26047a99f21d3252fc3096db5a489-Resolve_conversation_node_-_Social.png",null,"Social Resolve Conversation"],"align":"center","caption":"Social Resolve Conversation"}]}[/block]

## JSON payloads

> 🚧 Note
> 
> As Webex Connect variables deal with strings alone, these JSON payloads are constructed in an Evaluate node generally (already implemented in the template flows from GitHub) and passed on as stringified JSON to the Resolve conversation node. 
> 
> Below is a JSON representation of the same for better readability

### Chat

### Sample payload - `detailsJson`

```json Chat - Text - Details JSON
{
    "messageDetails": {
        "appId": "LI07154615",
        "domain": "transcendent-starburst.netlify.app",
        "threadId": "e5f0ccab-c350-4d2a-ad74-3c71993506de",
        "threadTitle": "1765454452383_0.688648135896382",
        "threadStatus": "",
        "userId": "ba30f8e0-b6a3-4a10-90b6-d1467abd5b8a",
        "message": "Hi this is a sample message",
        "attachmentCount": 0,
        "attachment": "",
        "extras": "",
        "version": "v2",
        "tid": "709c153e-e865-4dc1-8cef-4dcbae6f7b11",
        "serviceKey": "b373dc37-73a5-11f0-840f-027f9a8873c5",
        "customerName": "Customer",
        "customerEmail": "ba30f8e0-b6a3-4a10-90b6-d1467abd5b8a",
        "timestamp": "2025-12-11T12:01:33.495Z",
        "proactiveRuleId": ""
    },
    "pciDetails": {
        "isPCICompliant": true,
        "isPCIValidationDone": "true",
        "nonPCIComplianceReason": "",
        "isAttachmentEnabled": true,
        "droppedAttachmentCount": 0
    }
}
```
```json Chat - Attachment - Details JSON
{
    "messageDetails": {
        "appId": "LI07154615",
        "domain": "transcendent-starburst-5fc84f.netlify.app",
        "threadId": "e5f0ccab-c350-4d2a-ad74-3c71993506de",
        "threadTitle": "1765454452383_0.688648135896382",
        "threadStatus": "",
        "userId": "ba30f8e0-b6a3-4a10-90b6-d1467abd5b8a",
        "message": "",
        "attachmentCount": 1,
        "attachment": "[{\"file\":\"https://oregon-webex-encryption.s3.us-west-2.amazonaws.com/589517eb-5a89-490f-bf7f-c0ea9e059c19dee3f14e-4d0c-4b36-8b6f-1c51b6ca482e.png?keyUri=kms%3A%2F%2Fkms-us.wbx2.com%2Fkeys%2Fd71a43c8-947f-48ef-897e-f80849c33f95&JWE=eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..gMF9nnWXnPRA5utz.z9qRXaAStEFF1VqUoI7OMeFZOn55hqwIDwTyjfhsnpexMUpVRLBoqDfKi5fCrMsRVeM3rXTMHs2BnK9paDCgHGq8QHBpnmnIIapKOg88ENrUjZYUs3HRMXdvpc449XEMdzkQCRLE95CaBabkzW8OME0CxcKWpEGX03IU4Zrx41Sojf6idoLwsKDvwISC0WSmsMqYTHAhNOjnRxlsn1jVl2hbCzOlFBYRlz3dT0KRFktnIlRvRyOuxdnUWIO2LxjKV7IHN76OJbO8oIWsNUYv68qNPiFf-36pkXl18E2u8sP6Uj16l-vCzalO-ntmgFxgsy4wcsVACMRW2rxArCuAJy4sW20CWyOG732SmYpHoYDnchsX3z0Ve2ZRVA97XPbP2tWxDvF6HVM3pkNWig.tEdzE1RO2dlGh40EzKezYQ\",\"contentType\":\"image\"}]",
        "extras": "",
        "version": "v2",
        "tid": "709c153e-e865-4dc1-8cef-4dcbae6f7b11",
        "serviceKey": "b373dc37-73a5-11f0-840f-027f9a8873c5",
        "customerName": "Customer",
        "customerEmail": "ba30f8e0-b6a3-4a10-90b6-d1467abd5b8a",
        "timestamp": "2025-12-11T12:01:33.495Z",
        "proactiveRuleId": ""
    },
    "pciDetails": {
        "isPCICompliant": true,
        "isPCIValidationDone": "true",
        "nonPCIComplianceReason": "",
        "isAttachmentEnabled": true,
        "droppedAttachmentCount": 0
    }
}
```
```json Parameterised JSON
var messageDetails = {
    "appId": appId,
    "domain": liveChatDomain,
    "threadId": threadId,
    "threadTitle": threadTitle,
    "threadStatus": threadStatus,
    "userId": userId,
    "message": resolveConversationMessage,
    "attachmentCount": parseInt(attachmentCount),
    "attachment": attachment,
    "extras": JSON.stringify(messageExtras),
    "version": version,
    "tid": transId,
    "serviceKey": serviceKey,
    "customerName": customerName,
    "customerEmail": customerEmail,
    "timestamp": timestamp
};

var pci = {
    "isPCICompliant": JSON.parse(isPCICompliance.replace("NA", "true")),
    "isPCIValidationDone": resolveConversationIsPCIValidationDone,
    "nonPCIComplianceReason": resolveConversationNonPCIComplianceReasonObject,
    "isAttachmentEnabled": JSON.parse(isAttachmentEnabled.replace("NA", "true")),
    "droppedAttachmentCount": JSON.parse(droppedAttachmentCount.replace("NA", "0"))
};

var details = {
    "messageDetails": messageDetails,
    "pciDetails": pci
};

var detailsJson = JSON.stringify(details);
```

### Field Descriptions

| Field Key       | Field Description                                                              | Mandatory |
| :-------------- | :----------------------------------------------------------------------------- | :-------- |
| appId           | Created when the app/asset is created; used for Connect and Engage integration | Yes       |
| domain          | Domain of the website where the Livechat widget is hosted                      | Yes       |
| threadId        | The ID of the thread created at Webex Connect                                  | Yes       |
| threadTitle     | Fetched from thread at Webex Connect                                           | Yes       |
| threadStatus    | Refers to the status of the thread like open or closed                         | Yes       |
| userId          | Fetched from the conversation details                                          | Yes       |
| messagetext     | The actual message from the customer                                           | Yes       |
| attachmentCount | The number of attachments per message received                                 | Yes       |
| attachment      | Attachment information (URL                                                    | Yes       |
| extras          | Additional optional information                                                | No        |
| version         | Version information                                                            | No        |
| tid             | Holds the Transaction ID of the conversation                                   | Yes       |
| serviceKey      | Comes from Connect service                                                     | No        |
| customerName    | Customer Name either configured in the field or from pre-chat form             | Yes       |
| customerEmail   | Customer email address configured in the field or from pre-chat                | Yes       |
| timestamp       | Refers to timestamp of region                                                  | Yes       |

### Email

### Sample payload - `detailsJson`

```json Email - Details JSON
        "messageDetails": {
        "appId": "a_638296118145560000",
        "assetType": "AWS SES",
        "senderName": "Rajesh imI",
        "recipient": "wxccengage@gmail.com",
        "businessEmailId": "wxccengage@gmail.com",
        "customerEmailId": "rajeshimi21@gmail.com",
        "customerName": "Rajesh imI",
        "toAddresses": "[\"wxccengage@gmail.com\"]",
        "ccRecipients": "[]",
        "bccRecipients": "[]",
        "subject": "inbound chat 1205",
        "inReplyTo": "",
        "headers": "  ",
        "htmlMessage": "<div dir=\"ltr\"><div>hello there </div><br>",
        "strippedText": "hello there\r\n",
        "strippedHtml": "<div dir=\"ltr\"><div>hello there </div><br>",
        "attachments": "[]",
        "serviceKey": "79d7035b-d435-11f0-b1a0-02e9c3f1ccb1",
        "timestamp": "2026-05-12T12:13:20.743Z"
      },
      "pciDetails": {
        "isPCICompliant": true,
        "isPCIValidationDone": "true",
        "nonPCIComplianceReason": "[]",
        "droppedAttachmentCount": 0
      },
      "malwareScanDetails": {
        "isMalwareCompliant": true,
        "isMalwareValidationDone": "true",
        "malwareFailedReason": "[]",
        "droppedAttachmentCount": 0
      },
      "securityScanDetails": {
        "isSecurityCompliant": true,
        "isSecurityValidationDone": "true",
        "securityFailedReason": "[]",
        "droppedAttachmentCount": 0
      }
```
```javascript Parameterized  Sample
 var messageDetails = "{" +
"\"appId\": \""+ appId + "\"," +
"\"assetType\": \""+ assetType + "\"," +
"\"senderName\": \""+ senderName + "\"," +
"\"recipient\": \""+ bizemailid + "\"," +
"\"businessEmailId\": \""+ bizemailid + "\"," +
"\"customerEmailId\": \""+ customerEmailId + "\"," +
"\"customerName\": \""+ senderName + "\"," +
"\"toAddresses\": "+ JSON.stringify(toAddresses) + "," +
"\"ccRecipients\": "+ JSON.stringify(ccRecipients) + "," +
"\"bccRecipients\": "+ JSON.stringify(bccRecipients) + "," +
"\"subject\": "+ JSON.stringify(subject) + "," +
"\"inReplyTo\": \""+ inReplyTo + "\"," +
"\"headers\": "+ JSON.stringify(headers) + "," +
"\"message\": \""+ messagetext + "\"," +
"\"htmlMessage\": \""+ messageHTML + "\"," +
"\"strippedText\": \""+ strippedText + "\"," +
"\"strippedHtml\": \""+ strippedHtml + "\"," +
"\"attachments\": "+ attachmentEmptyName + "," +
"\"serviceKey\": \""+ serviceKey + "\"," +
"\"timestamp\": \""+ timestamp + "\"" +
"}";

resolveConversationNonPCIComplianceReasonObject =
resolveConversationNonPCIComplianceReasonObject.replace("name\":\"\"", "name\":\"no_filename\"");

var pci = JSON.stringify({
"isPCICompliant": JSON.parse(isPCICompliance.replace("NA", "true")),
"isPCIValidationDone": resolveConversationIsPCIValidationDone,
"nonPCIComplianceReason": resolveConversationNonPCIComplianceReasonObject,
"droppedAttachmentCount": JSON.parse(droppedAttachmentCount.replace("NA", "0"))
});

var malwareScanDetails = JSON.stringify({
"isMalwareCompliant": JSON.parse(isMalwareCompliance.replace("NA", "true")),
"isMalwareValidationDone": isMalwareValidationDone,
"malwareFailedReason": malwareNonComplianceReasonObject,
"droppedAttachmentCount": JSON.parse(malwareScanDroppedAttachmentCount.replace("NA", "0"))
});


var securityScanDetails = JSON.stringify({
"isSecurityCompliant": JSON.parse(isSecurityCompliance.replace("NA", "true")),
"isSecurityValidationDone": isSecurityValidationDone,
"securityFailedReason": securityNonComplianceReasonObject,
"droppedAttachmentCount": JSON.parse(securityScanDroppedAttachmentCount.replace("NA", "0"))
});

var details = "{\"messageDetails\":" + messageDetails +
" , \"pciDetails\": " + pci +
" , \"malwareScanDetails\": " + malwareScanDetails +
" , \"securityScanDetails\": " + securityScanDetails +
"}";

var detailsJson = details;
```

### Field Descriptions

| Field Key       | Field Description                                                              | Mandatory |
| :-------------- | :----------------------------------------------------------------------------- | :-------- |
| appID           | Created when the app/asset is created; used for Connect and Engage integration | Yes       |
| assetType       | Type of assets, e.g., email, chat, or social                                   | Yes       |
| senderName      | Customer’s name in the form of email or name                                   | Yes       |
| bizemailid      | Business email Id which is configured for the organization                     | Yes       |
| customerEmailId | Represents customer’s email address                                            | Yes       |
| senderName      | Customer’s name in the form of email or name                                   | Yes       |
| toAddress       | Customer's email address where email is sent                                   | Yes       |
| ccRecipients    | Represents CC recipients                                                       | Yes       |
| bccRecipients   | Represents BCC recipients                                                      | Yes       |
| subject         | Represents subject of the email                                                | Yes       |
| headers         | Contains all header content from the email gateway                             | Yes       |
| messagetext     | Contains email message body                                                    | Yes       |
| messagehtml     | Contains HTML message content                                                  | Yes       |
| strippedText    | Contains stripped/cleaned version of text from email gateway                   | Yes       |
| strippedHtml    | Contains stripped version of HTML from email gateway                           | Yes       |
| attachments     | Contains all incoming attachments                                              | Yes       |
| serviceKey      | Comes from Connect service                                                     | No        |
| timestamp       | Refers to timestamp of region                                                  | Yes       |

### Social

### Sample payload - `detailsJson`

```json Social - AMB - Details JSON
messageDetails = {
    "appId": appId,
    "abcUserId": abcUserId,
    "accountId": accountId,
    "customerName": customerName,
    "message": resolveConversationmessagetext,
    "attachments": attachments,
    "attachmentUrl": attachmentUrl,
    "serviceKey": serviceKey,
    "timestamp": timestamp,
    "deviceCapabilityList": deviceCapabilityList
};
```
```json AMB parameterised sample
 var tid = transId.split('_')[0];
var messageDetails = {
    "appId": appId,
    "abcUserId": abcUserId,
    "accountId": accountId,
    "customerName": customerName,
    "message": resolveConversationmessagetext,
    "attachments": attachments,
    "attachmentUrl": attachmentUrl,
    "serviceKey": serviceKey,
    "timestamp": timestamp
};

var pci = {
    "isPCICompliant": JSON.parse(isPCICompliance.replace("NA", "true")),
    "isPCIValidationDone": resolveConversationIsPCIValidationDone,
    "nonPCIComplianceReason": resolveConversationNonPCIComplianceReasonObject,
    "isAttachmentEnabled": JSON.parse(isAttachmentEnabled.replace("NA", "true")),
    "droppedAttachmentCount": JSON.parse(droppedAttachmentCount.replace("NA", "0"))
};

var details = {
    "messageDetails": messageDetails,
    "pciDetails": pci
}


var detailsJson = JSON.stringify(details);

1;
```
```json Social - WAB - Details JSON
{
  "details": {
    "messageDetails": {
      "appId": "a_173200067561504200",
      "waId": "916303330251",
      "customerWhatsappId": "919618413605",
      "customerUsername": "Rajeshh",
      "message": "hey there",
      "attachments": "[]",
      "caption": "",
      "serviceKey": "79d7035b-d435-11f0-b1a0-02e9c3f1ccb1",
      "timestamp": "2026-05-12T10:40:54.000Z"
    },
    "pciDetails": {
      "isPCICompliant": true,
      "isPCIValidationDone": "true",
      "nonPCIComplianceReason": "{\"text\":\"\"}",
      "isAttachmentEnabled": true,
      "droppedAttachmentCount": 0
    },
    "malwareScanDetails": {
      "isMalwareCompliant": true,
      "isMalwareValidationDone": "NA",
      "malwareFailedReason": "NA",
      "droppedAttachmentCount": 0
    },
    "securityScanDetails": {
      "isSecurityCompliant": true,
      "isSecurityValidationDone": "true",
      "securityFailedReason": "{\"text\":\"\"}",
      "droppedAttachmentCount": 0
    }
  }
}
```
```json WAB parameterised JSON
 var messageDetails = {
"appId": appId,
"waId": WANumber,
"customerWhatsappId": customerWhatsappId,
"customerUsername": customerUsername,
"message": message,
"attachments": attachments,
"caption": caption,
"serviceKey": serviceKey,
"timestamp": isoTimeStamp
};

var pci = {
"isPCICompliant": JSON.parse(isPCICompliance.replace("NA", "true")),
"isPCIValidationDone": resolveConversationIsPCIValidationDone,
"nonPCIComplianceReason": resolveConversationNonPCIComplianceReasonObject,
"isAttachmentEnabled": JSON.parse(isAttachmentEnabled.replace("NA", "true")),
"droppedAttachmentCount": JSON.parse(pciScanDroppedAttachmentCount.replace("NA", "0"))
};

var malwareScanDetails = {
"isMalwareCompliant": JSON.parse(isMalwareCompliance.replace("NA", "true")),
"isMalwareValidationDone": isMalwareValidationDone,
"malwareFailedReason": malwareNonComplianceReasonObject,
"droppedAttachmentCount": JSON.parse(malwareScanDroppedAttachmentCount.replace("NA", "0"))
};

var securityScanDetails = {
"isSecurityCompliant": JSON.parse(isSecurityCompliance.replace("NA", "true")),
"isSecurityValidationDone": isSecurityValidationDone,
"securityFailedReason": securityNonComplianceReasonObject,
"droppedAttachmentCount": JSON.parse(securityScanDroppedAttachmentCount.replace("NA", "0"))
};

var details = {
"messageDetails": messageDetails,
"pciDetails": pci,
"malwareScanDetails": malwareScanDetails,
"securityScanDetails": securityScanDetails
};

var detailsJson = JSON.stringify(details);
 
```
```Text Social - SMS - Details JSON
{
  "details": {
    "messageDetails": {
      "serviceNumber": "447418369300",
      "senderNumber": "447966197542",
      "message": "hey",
      "serviceKey": "79d7035b-d435-11f0-b1a0-02e9c3f1ccb1",
      "timestamp": "2026-04-27T06:42:11.262Z"
    },
    "pciDetails": {
      "isPCICompliant": true,
      "isPCIValidationDone": "true",
      "nonPCIComplianceReason": "{\"text\":\"\"}",
      "droppedAttachmentCount": 0
    },
    "malwareScanDetails": {
      "isMalwareCompliant": true,
      "isMalwareValidationDone": "NA",
      "malwareFailedReason": "NA",
      "droppedAttachmentCount": 0
    },
    "securityScanDetails": {
      "isSecurityCompliant": true,
      "isSecurityValidationDone": "true",
      "securityFailedReason": "{\"text\":\"\"}",
      "droppedAttachmentCount": 0
    }
  }
}
  
```
```json SMS parameterised JSON
 var messageDetails = {
    "serviceNumber": serviceNumber,
    "senderNumber": senderNumber,
    "message": message,
    "serviceKey": serviceKey,
    "timestamp": timestamp
}

var pci = {
    "isPCICompliant": JSON.parse(isPCICompliance.replace("NA", "true")),
    "isPCIValidationDone": isPCIValidationDone,
    "nonPCIComplianceReason": nonPCIComplianceReasonObject,
    "droppedAttachmentCount": JSON.parse(droppedAttachmentCount.replace("NA", "0"))
};

var malwareScanDetails = {
    "isMalwareCompliant": JSON.parse(isMalwareCompliance.replace("NA", "true")),
    "isMalwareValidationDone": isMalwareValidationDone,
    "malwareFailedReason": malwareNonComplianceReasonObject,
    "droppedAttachmentCount": JSON.parse(malwareScanDroppedAttachmentCount.replace("NA", "0"))
};

var securityScanDetails = {
    "isSecurityCompliant": JSON.parse(isSecurityCompliance.replace("NA", "true")),
    "isSecurityValidationDone": isSecurityValidationDone,
    "securityFailedReason": securityNonComplianceReasonObject,
    "droppedAttachmentCount": JSON.parse(securityScanDroppedAttachmentCount.replace("NA", "0"))
};

var details = {
    "messageDetails": messageDetails,
    "pciDetails": pci,
    "malwareScanDetails": malwareScanDetails,
    "securityScanDetails": securityScanDetails
};

var detailsJson = JSON.stringify(details);

1;
```
```Text Social - FB - Details JSON
{
  "details": {
    "messageDetails": {
      "appId": "a_638838409917150000",
      "facebookPageId": "391273087404701",
      "psId": "24371667315851482",
      "customerName": "User",
      "message": "test",
      "attachments": "",
      "attachmentUrl": "",
      "serviceKey": "79d7035b-d435-11f0-b1a0-02e9c3f1ccb1",
      "timestamp": "2026-05-12T06:46:13.243Z"
    },
    "pciDetails": {
      "isPCICompliant": true,
      "isPCIValidationDone": "true",
      "nonPCIComplianceReason": "{\"text\":\"\"}",
      "droppedAttachmentCount": 0
    },
    "malwareScanDetails": {
      "isMalwareCompliant": true,
      "isMalwareValidationDone": "NA",
      "malwareFailedReason": "NA",
      "droppedAttachmentCount": 0
    },
    "securityScanDetails": {
      "isSecurityCompliant": true,
      "isSecurityValidationDone": "true",
      "securityFailedReason": "{\"text\":\"\"}",
      "droppedAttachmentCount": 0
    }
  }
}  
 
```
```json FB parameterised JSON
 var messageDetails = {
    "appId": appId,
    "facebookPageId": FBpageid,
    "psId": psId,
    "customerName": customerName,
    "message": resolveConversationmessagetext,
    "attachments": resolveConversationMessengerPayloadObject,
    "attachmentUrl": attachmentURL,
    "serviceKey": serviceKey,
    "timestamp": timestamp
};

var pci = {
    "isPCICompliant": JSON.parse(isPCICompliance.replace("NA", "true")),
    "isPCIValidationDone": resolveConversationIsPCIValidationDone,
    "nonPCIComplianceReason": resolveConversationNonPCIComplianceReasonObject,
    "droppedAttachmentCount": JSON.parse(droppedAttachmentCount.replace("NA", "0"))
};

var malwareScanDetails = {
    "isMalwareCompliant": JSON.parse(isMalwareCompliance.replace("NA", "true")),
    "isMalwareValidationDone": isMalwareValidationDone,
    "malwareFailedReason": malwareNonComplianceReasonObject,
    "droppedAttachmentCount": JSON.parse(malwareScanDroppedAttachmentCount.replace("NA", "0"))
};

var securityScanDetails = {
    "isSecurityCompliant": JSON.parse(isSecurityCompliance.replace("NA", "true")),
    "isSecurityValidationDone": isSecurityValidationDone,
    "securityFailedReason": securityNonComplianceReasonObject,
    "droppedAttachmentCount": JSON.parse(securityScanDroppedAttachmentCount.replace("NA", "0"))
};

var details = {
    "messageDetails": messageDetails,
    "pciDetails": pci,
    "malwareScanDetails": malwareScanDetails,
    "securityScanDetails": securityScanDetails
};

var detailsJson = JSON.stringify(details);

1;

```

### Field Descriptions

| Field Key            | Field Description                                                                | Mandatory |
| :------------------- | :------------------------------------------------------------------------------- | :-------- |
| appId                | Created when app/asset is created, referred to in Connect and Engage integration | Yes       |
| abcUserId            | Apple user ID                                                                    | Yes       |
| accountId            | Apple account ID                                                                 | Yes       |
| customerName         | Customer's name                                                                  | Yes       |
| message              | Message received from customer                                                   | Yes       |
| attachments          | Customer attachments                                                             | Yes       |
| attachmentUrl        | URL of the attachment                                                            | Yes       |
| serviceKey           | Comes from Connect service                                                       | No        |
| Timestamp            | Refers to the timestamp of the region                                            | Yes       |
| deviceCapabilityList | List of device capabilities received from the gateway                            | Yes       |

### Field Descriptions

| Field Key          | Field Description                                                                | Mandatory |
| :----------------- | :------------------------------------------------------------------------------- | :-------- |
| appId              | Created when app/asset is created, referred to in Connect and Engage integration | Yes       |
| waId               | Refers to the Whatsapp Business number                                           | Yes       |
| customerWhatsappId | Customer's Whatsapp number                                                       | Yes       |
| customerUsername   | Customer's Whatsapp username                                                     | Yes       |
| message            | Whatsapp message received from the customer                                      | Yes       |
| attachments        | Attachments sent by the Whatsapp customer                                        | Yes       |
| caption            | Caption along with attachments, considered as text only                          | No        |
| serviceKey         | Comes from Connect service                                                       | No        |
| timestamp          | Refers to the timestamp of the region                                            | Yes       |

### Field Descriptions

| Field Key     | Field Description             | Mandatory |
| :------------ | :---------------------------- | :-------- |
| serviceNumber | Incoming service number       | Yes       |
| senderNumber  | Customer's number             | Yes       |
| message       | Customer message              | Yes       |
| serviceKey    | Comes from Connect service    | No        |
| timestamp     | Refers to timestamp of region | Yes       |

### Field Descriptions

| Field Key      | Field Description                                                              | Mandatory |
| :------------- | :----------------------------------------------------------------------------- | :-------- |
| appId          | Created when the app/asset is created; used for Connect and Engage integration | Yes       |
| facebookPageId | Refers to the Facebook Page ID created with Connect Engage integration         | Yes       |
| psId           | Page-specific ID for users who interact using the Facebook page                | Yes       |
| customerName   | Refers to the Facebook customer's name                                         | Yes       |
| messagetext    | Contains the customer's message text                                           | Yes       |
| attachments    | Attachments sent from the customer                                             | Yes       |
| messagetext    | Contains the customer's message text                                           | Yes       |
| attachments    | Attachments sent from the customer                                             | Yes       |
| attachmentURL  | URL of the attachments                                                         | Yes       |
| serviceKey     | Comes from Connect service                                                     | No        |
| timestamp      | Refers to the timestamp of the region                                          | Yes       |

## How to configure this node

| Field Key                                     | Field Description                                                                                                                                                             |
| :-------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method Name                                   | Specifies the action to be performed. In this case, it is set to "Resolve Conversation," which indicates this node is responsible for ending an active interaction.           |
| Node Runtime Authorization                    | Required for the node to execute with the necessary permissions.                                                                                                              |
| Flow Id                                       | A field to input the specific identifier for the workflow or flow instance that this node belongs to.                                                                         |
| Trans Id (Transaction ID)                     | A variable field (currently set to $(tid)) that identifies the specific customer transaction or interaction being resolved.                                                   |
| Media Type                                    | Select the type of communication being handled, such as "Chat."                                                                                                               |
| Media Channel                                 | Specify the particular channel used for the interaction, such as "Web, Mobile."                                                                                               |
| Details                                       | A text field to provide additional context or metadata about the resolution, such as "Live Chat/ In-App Messaging."                                                           |
| Override Default Contact Close Event Handling | A checkbox that, when selected, allows the user to bypass the standard system-level logic for closing a contact, providing more granular control over the resolution process. |

## Node outcomes

### Success outcomes

| Node Outcome | When does this occur?                                                                                                                         | Suggested next steps                                |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| `accepted`   | Request has been acknowledged by the service and is awaiting async events                                                                     | Wait for subsequent events                          |
| `created`    | A Webex CC task and a Webex Engage conversation has been created and have been linked. The message has already been added to the conversation | Proceed to next steps (e.g. AI agent or Queue Task) |
| `reopened`   | An existing closed conversation was re-opened on Webex Engage, a task has been created for this and both have been linked                     | Proceed to next steps (e.g. AI agent or Queue Task) |
| `appended`   | An existing active / queued interaction was found on Webex Engage and the message was appended to the conversation                            | End the flow successfully                           |

### Error outcomes

[block:parameters]
{
  "data": {
    "h-0": "Node Outcome",
    "h-1": "When does this occur?",
    "h-2": "Suggested next steps",
    "0-0": "`onInvalidData`",
    "0-1": "This error occurs when any of the mandatory fields on the node's UI did not have a value passed during flow run time",
    "0-2": "Debug your flow offline",
    "1-0": "`onError`",
    "1-1": "This error occurs when the underlying API calls to the microservice fails (responds with a non 2XX series code)",
    "1-2": "Implement exponential retry logic in your flow",
    "2-0": "`onInvalidChoice`",
    "2-1": "This error occurs when the API responds with an unknown code that has not been implemented in the code  \n  \nThis is an internal error outcome exposed by default from the pre-built integration framework and should not occur ideally in a live scenario with this node in general",
    "2-2": "Contact Cisco Support",
    "3-0": "`onauthorizationfail`",
    "3-1": "This error occurs when we've failed to authenticate your request",
    "3-2": "Recheck your Integration's Auth credentials",
    "4-0": "`tooManyRequests`",
    "4-1": "This error occurs when you've hit the rate limits of this service",
    "4-2": "Implement exponential retry logic in your flow",
    "5-0": "`serviceUnavailable`",
    "5-1": "This error occurs when the middleware service is down and responds with a 5XX series response code specifically",
    "5-2": "Implement expotential retry logic in your flow (in the order of a few minutes preferably)",
    "6-0": "`error`",
    "6-1": "This occur occurs when the pre-built integration framework on Webex Connect's side is down",
    "6-2": "Contact Cisco Support",
    "7-0": "`taskFailed`",
    "7-1": "This error occurs when the task creation failed on Webex CC's side (OR) conversation creation failed on Webex Engage's side",
    "7-2": "Implement exponential retry logic in your flow  \n  \nIf you still notice errors consistently, contact Cisco Support",
    "8-0": "`appendFailed`",
    "8-1": "This error occurs when the message was attempted to be appended to an existing conversation but it failed",
    "8-2": "Implement exponential retry logic in your flow  \n  \nIf you still notice errors consistently, contact Cisco Support",
    "9-0": "`onTimeout`",
    "9-1": "This error occurs when the node timed-out waiting for a synchronous (OR) asynchronous response back from this service",
    "9-2": "Contact Cisco Support"
  },
  "cols": 3,
  "rows": 10,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Best practices

- Implement exponential retry logic for error outcomes listed above
- Contact Cisco Support if you notice errors consistently on this node across all your flows using this node