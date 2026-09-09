# Reports

Source: https://help.webexconnect.io/docs/service-reports
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:58+00:00

The Reports section helps you view and analyze your messaging and flow traffic across various services. Webex Connect provides reporting at three levels - platform level summary, channel asset level summary, and service level summary. 

Here's a brief description of the reports available at each level.

## Platform Summary

The platform summary report provides the aggregated count of the total number of messages sent and received across various channels within the specified time period.

Select Platform > Summary option under the Entity dropdown and mention the time period as shown below. 

The apps at channel level are categorized in the Entity dropdown.

> 📘 Timezone Settings
> 
> Please note that the data shown in the report is based on the tenant timezone settings.



![Screenshot of Reports Page.](https://files.readme.io/36c51f5-10.jpg)




The details of messages sent (i.e., messages submitted and processed for delivery) and messages received across various channels will be available as shown below. You can simply hover over the line graph to get the details for any specific day within the selected time period. The data for each channel is represented by a color as shown in the graph. The channels for which data is displayed are as follows:

- SMS
- Voice
- Live Chat / In-app Messaging
- Messenger
- Email
- Apple Messages for Business
- RCS
- WhatsApp
- Instagram
- MMS
- Push



![Navigating to the Summary option in the Entity dropdown menu on the Platform with specified time period](https://files.readme.io/25245b3-24.jpg)




When you select a single day or partial day (Today/Yesterday/Custom) in the Period filter, the hour-wise data is shown on the graph.

> 📘 Custom Time Period
> 
> When you select **Custom **in the **Time Period **field, the **Custom Date** pop-up allows you to choose a date range within the past 13 months. You can select time value in hours (hh) only; minutes (mm) are not supported. For example, if today’s date is 1st January, 2025, you can set the **End Date** to January 1, 2025, but the **Start Date** cannot be older than 1st December, 2023 in the report.



![Custom Date](https://files.readme.io/125b7fc650720b86a147a5c14c017968bcecf929b53bbfd21be754e806078915-image.png)






![Service Level Report for WhatsApp Channel.](https://files.readme.io/d9824aa-13.png)




If needed, you can download the reports in PNG, JPEG, PDF, SVG, CSV, and XLS format by clicking the hamburger menu icon towards the top-right side of the chart, as shown below.



![Screenshot displaying to download the reports.](https://files.readme.io/f294396-14.jpg)




### Reports for Outbound Emails

Sample report for Email channel usage at a service level.



![Sample report for Email channel usage at a service level.](https://files.readme.io/83da0899d028210127432decab12eb85c66ae8f62daf26d874cc1c1a9bcec3d7-ob_email_dr.png)




The above screenshot shows details for Email channel usage at a service level with the following data points:

- Total number of requests
- Number of email messages sent
- Number of email messages submitted for processing
- Number of email messages scheduled (email messages waiting to be submitted)
- Number of email messages rejected (email messages rejected by the platform due to various reasons)
- Number and percentage of email messages delivered (email messages with confirmed delivery receipt)
- Number and percentage of email messages failed
- Total links clicked
- Number of email messages hard bounced (not delivered because of invalid email address, etc.)
- Number of email messages soft bounced (not delivered because of insufficient space in the inbox, etc.)
- Number of complaints (phishing, abuse, spam, etc.)

Since it’s not possible to display all the sub-categories at the high-level report, a sub-report for bounced emails and complaints is displayed, called Messages Bounced and Email Complaints.



![Messages Bounced and Email Complaints](https://files.readme.io/c318258eb11678a7173cea196ca0976245182cc28bcabcf34868967d287a9b0f-Bounce1.jpg)




> 📘 Note
> 
> The default retention period for email bounce list is **Seven** days for email via AWS SES. To change the retention period, reach out to your account manager.

| Field Name   | Description                                                                                         |
| :----------- | :-------------------------------------------------------------------------------------------------- |
| Status Name  | Indicates if it is a bounced message or an email complaint.                                         |
| Sub-Category | Indicated the category to which the event belongs.                                                  |
| Details      | Captures granular information about the reason for email bounce. It’s not applicable to Complaints. |
| Count        | Displays the number of times the event occurred.                                                    |

### Reports for Voice

Sample report for voice channel usage at a service level.



![Sample Report for Voice Channel usage at service level](https://files.readme.io/2051f11e6bfae283061699090715efa4f007e714e9aa5344271b8b33eb26df30-2025-07-25_10-49-03.png)




The above screenshot shows details for Voice channel usage at a service level with the following data points:

- Total Requests
- Total Calls Submitted
- Total Calls Scheduled
- Total Calls Rejected
- Total Calls Answered by User
- Total Calls Answered by Machine
- Total Calls Failed
- Average Call Duration

### Reports for SMS



![SMS Reports](https://files.readme.io/182857aaa4aa06955ccb4b40838f4980a76a62ec68281b85fed367f4183b5d5f-image-20250225-152232.png)




Following is the information that’s displayed as part of the reports:

- Total Requests  - Number of requests submitted by the user to the Webex Connect platform.
- Requests Submitted - Number of requests submitted by the Webex Connect platform to the messaging gateways.
- Requests Scheduled - Number of requests waiting to be submitted by the Webex Connect platform to the messaging gateways.
- Requests Rejected - Number of requests rejected by the Webex Connect platform.
- Total Messages Submitted - Total count of messages delivered and messages failed to be delivered to the end user.
- Messages Delivered as RCS Basic - Total count of messages delivered to the end user as RCS basic.
- Message Delivered as SMS- Total count of messages delivered to the end user.
- Message Enabled for RCS Basic- Total number of messages activated for RCS Basic.
- Messages Failed - Total count of messages failed to be delivered to the end user.
- Messages Clicked - Number of messages clicked.

> 📘 Custom Time Period
> 
> When you select **Custom **in the **Time Period **field, the **Custom Date** pop-up allows you to choose a date range within the past 13 months. You can select time value in hours (hh) only; minutes (mm) are not supported. For example, if today’s date is 1st January, 2025, you can set the **End Date** to January 1, 2025, but the **Start Date** cannot be older than 1st December, 2023 in the report.



![Custom Date](https://files.readme.io/125b7fc650720b86a147a5c14c017968bcecf929b53bbfd21be754e806078915-image.png)




#### Using Sender ID

1. Select the Sender ID for which you want to generate the report.
2. Select the required time. Click Get reports.



![Asset Level Report for SMS Channel.](https://files.readme.io/9b2d0a6-10.png)




Following is the information that’s displayed as part of the reports:

- Total Messages Submitted (Estimated Segments) - Total count of messages delivered and messages failed to be delivered to the end user.
- Messages Delivered (Actual Segments) - Total count of messages delivered to the end user.
- Messages Failed (Actual Segments) - Total count of messages failed to be delivered to the end user.

## Channel Asset Level Reports

Alternatively, the reports can be viewed at a channel asset level by selecting the channel asset for example a Number (in case of SMS and Voice), or an App (for OTT channels such as Apple Messages for Business and WhatsApp). 

Select your desired number or the app name from the Entity dropdown and mention the time period as shown below. 



![Asset Level Report for SMS or Voice Channel.](https://files.readme.io/aa8c85c-3.jpg)




The details of messages received on the selected channel asset (i.e. a number or an app) will be available as shown below. This is the aggregated count of messages received on the select asset across various services within Webex Connect where the selected asset is being used. Hover over the line graph to get the details of the number of messages received on any given day within the selected time period.



![Asset Level Report for SMS or Voice Channel.](https://files.readme.io/9cda302-4.jpeg)




## Service Level Reports

While the high-level stats of messaging, flow execution, and API invocation details for each service are visible as soon as you enter the service-specific dashboard (sample below), more granular information about channel usage and flow executions are present within the Reports section. 



![Service Specific Dashboard](https://files.readme.io/bccb285-6.jpg)




To view and analyze detailed reports for any of your services visit the 'Reports' section and select your desired service from the Entity dropdown. Further, select the channel or the flow name and specify the time period you would like to see the reports for. Click Get Reports. 

**Sample report for SMS channel usage at a service level.** 



![Service Level Report for SMS Channel.](https://files.readme.io/62aeb339a95cd230122b88ab56fc2f9bdbbc82ef5962f4c5fa38bf5961fefae0-image-20250225-090556.png)




Following is the information that’s displayed as part of the reports:

- Total Requests  - Number of requests submitted by the user to the connect platform.
- Requests Submitted - Number of requests submitted by the connect platform to the messaging gateways.
- Requests Scheduled - Number of requests waiting to be submitted by the connect platform to the messaging gateways.
- Requests Rejected - Number of requests rejected by the connect platform.
- Total Messages Submitted - Total count of messages delivered and messages failed to be delivered to the end user.
- Message Delivered as RCS Basic- Total count of messages delivered to the end user as RCS Basic.
- Message Delivered as SMS- Total count of messages delivered to the end user.
- Message Enabled for RCS Basic- Total number of messages activated for RCS Basic.
- Messages Failed - Total count of messages failed to be delivered to the end user.
- Messages Clicked - Number of messages clicked.

Details for other channels are also available in a similar reporting format with some variations keeping in view channel-specific capabilities. 

> 📘 What's multi-part SMS message count
> 
> The standard character limit for a single SMS is 160 characters. If you send an SMS message that contains more than 160 characters, the message is split into smaller chunks at the operator end and is concatenated at the device end to form a single message for the recipient. If you send a message that contains 200 characters, the multi-part message count would be 2.

**Sample report for a flow within a service.** 



![Sample Report for a Flow within a Service](https://files.readme.io/5ef7681ce7d07b4e6ad17f9f14ff844229f87281151ccbc32b5b62a310fe55ab-Reports.jpg)




> ❗️ 'No of Messages'
> 
> The platform UI incorrectly represents the Y axis of Flow Reports as 'No of Messages'. It is actually the number of times that the flow is invoked, excluding sub-flow executions.

The above screenshot shows details for a flow with the following data points:

- Number of times the flow was invoked from external systems or as part of execution of main flow. 
  > 📘 Sub-flow execution count
  > 
  > If the graph isn't plotted and you see counts invoked, it is likely that the flow executions were part of the main flow execution, meaning they occurred as sub-flows execution. Sub-flow execution counts are not included in the plotting of graph.
- Number of flow executions - completed, incomplete, and errors 
- Count of flows that were successful vs failed as per user configuration on exit nodes 
- Report of custom exit reasons using user defined tags  

Flow specific reports can are available in two formats:

- **Regular View** - flow execution stats as shown in the above image.
- **Sankey View** - flow usage stats in a Sankey chart.

The following image displays a sample Sankey chart report for a workflow.



![A Sample Sankey Chart Report](https://files.readme.io/2ce6b2c-sankey_view_reports.png)




In this view, a list of saved Sankey charts for each version of the selected workflow appears in the **Sankey View** pane. Select an entity, a workflow, and the **Report Type** as _Sankey View_. Now select the version of the flow for which you want to see the Sankey chart and click **View Charts**.

> ❗️ Interactive Reports and Insights
> 
> As part of the reporting and analytics enhancements to the platform, we introduced a new interactive reports and insights capability in Beta mode earlier this year. This feature provides a richer reporting experience allowing you to analyze your customer interactions better. Some of the key capabilities include:
> 
> - Rich data visualisations
> - Drill through reports
> - Cross highlighting and filtering between report visuals
> - Customizable views
> - Export report pages as PDF files
> - Export summarized data from individual visuals into CSV, XLS files.
> 
> This is a controlled beta release. Please reach out to your account manager if you would like to know more about this feature.

**Sample Report for Link Shortener**



![Sample report for Link Shortener engagement.](https://files.readme.io/3ec4fd9553f971e8f52f7e92ab8f71a81dc83d5724dd78fd0171dae023ac475d-webex-connect-reports-link-shortener.png)




The above screenshot shows details for Link Shortener with the following data points:

- Total Creates: The number of shortened links created using the selected tag.
- Total Clicks: The total number of clicks recorded for the selected tag.
- Link Shortener Engagement - This provides a comprehensive overview of the Link Shortener report, displaying the number of links created and the total clicks associated with a selected tag, irrespective of the channels.
- CTR: To calculate the click-through rate (CTR): Divide the number of clicks by the number of links sent (or impressions), then multiply by 100 to express it as a percentage.