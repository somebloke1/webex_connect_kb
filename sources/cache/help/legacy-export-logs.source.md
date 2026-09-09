> 📘 
> 
> The below documentation applies only for tenants that have the legacy export logs interface enabled. We now offer a richer and advanced Export Logs experience and encourage you to reach out to the support team if you would like to get it enabled for your tenant.

The Export Logs feature allows you to export transaction logs for inbound and outbound messages sent using various channels, supported by the platform in .zip file format. The logs are available for the past 30 days, by default. However, you can download the logs for any time range within the last 30 days period.

The downloaded Outbound and Inbound Logs are segregated at channel-level and channel event-level respectively.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bc2b1ed-Export_Logs_Default.jpeg",
        "",
        "Screenshot of Export Logs"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Export Logs"
    }
  ]
}
[/block]


The access to download the logs depends on your decryption access. If you have decryption access, you can download the decrypted log files. If you do not have decryption access, you can download only encrypted files.

> 📘 Download Limits
> 
> You can currently download up to 100,000 messages at once. If you select a time period with more than 100,000 messages, only the first 100,000 will be downloaded. Please contact your account manager to increase the limit of messages beyond the 100,000 downloaded messages.

## Fields in the Export Logs

The following are the common and default Outbound log fields across all channels in the Export Logs. 

| Outbound Logs     |
| :---------------- |
| Transaction ID    |
| Correlation ID    |
| Template ID       |
| CRN Number        |
| Source            |
| Channel           |
| Asset             |
| Event Description |
| Current Status    |
| Time              |
| Timezone          |
| MSISDN            |
| Message           |

The following are the common and default Inbound log fields across all channels in the Export Logs.

| Inbound Logs      |
| :---------------- |
| Transaction ID    |
| CRN Number        |
| Channel           |
| Asset             |
| Event Description |
| Current Status    |
| Time              |
| Timezone          |
| MSISDN            |
| Message           |

## Channel-specific Fields in the Export Logs

The channel-specific outbound logs and inbound logs contain the following fields channel-wise:

[block:parameters]
{
  "data": {
    "h-0": "Channel",
    "h-1": "Outbound Logs",
    "h-2": "Inbound Logs",
    "0-0": "SMS",
    "0-1": "Segments [Segment counts for outbound SMS transactions for which delivery receipts have not been received by the time of exporting the logs will be logged as zero (value ‘0’)].",
    "0-2": "Segments",
    "1-0": "Voice",
    "1-1": "Duration",
    "1-2": "Duration",
    "2-0": "In-app",
    "2-1": "User ID",
    "2-2": "Source  \nThread ID  \nDate  \nUser ID",
    "3-0": "Push",
    "3-1": "Type  \nTotal Sent  \nTotal Submitted  \nOS  \nDestination Type  \nDestination",
    "3-2": "N/A",
    "4-0": "Facebook Messenger",
    "4-1": "Type  \nPS ID",
    "4-2": "Date  \nPS ID",
    "5-0": "RCS",
    "5-1": "Payload",
    "5-2": "Date  \nMedia",
    "6-0": "WhatsApp",
    "6-1": "WAID  \nBSUID                                                                                                                         BSUID_DR                                                                                                                              Media  \nHSM  \nSent Time  \nDelivered Time  \nRead Time",
    "6-2": "Date  \nWAID                 BSUID",
    "7-0": "Apple Business Chat",
    "7-1": "ABC ID  \nPayload",
    "7-2": "Date  \nABC ID",
    "8-0": "Email",
    "8-1": "From  \nEmail ID  \nSubject",
    "8-2": "Date  \nTo  \nEmail ID  \nSubject"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]