# Event Scheduler

Source: https://help.webexconnect.io/docs/event-scheduler
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:37+00:00

Event Scheduler allows Webex Connect to schedule outbound messages to be sent to your customers as per the configured time schedule. You can send SMS messages or schedule future invocations of Webex Connect rules/live flows simply by uploading a file (on the UI or via an SFTP location) with required information in the relevant format. 

## Configuring a Schedule

On the Event Scheduler page, click 'Add Scheduler'. You can select one of the following two actions to be triggered as per the schedule configured in subsequent steps:

1. [Custom Events](https://help.imiconnect.io/docs/event-scheduler#custom-events) – Allows you to trigger rules or flows associated with the selected Custom Events/Inbound Webhook. The variables required to trigger the Custom Event/Inbound Webhook and for the successful execution of concerned flows/rules should be available in the file.
2. [SMS](https://help.imiconnect.io/docs/event-scheduler#sms) – Allows you to send SMS messages simply by processing the file. One of the columns in the uploaded file must contain the recipients' phone number(s). 

The file types supported by Event Scheduler include .txt, .csv, and .xlsx. The file can be uploaded through the user interface or can be picked from a configured SFTP location. The scheduler can be configured to run either once or in a recurring pattern that can be hourly, daily, weekly, or monthly. 

> 🚧 Limitations
> 
> - Webex Connect Event scheduler can process file sizes of up to 75 MB. Also, the file name of the uploaded file should be less than 75 characters in length. Not subscribing to these limits can lead to schedule failure during execution.
> 
> - Only **one** file can be uploaded per Schedule. 
> 
> - To schedule an event using Event Scheduler, it is mandatory to create a custom event and a rule that is configured with custom event.
> 
> - To invoke an event successfully, it is mandatory to match uploaded files' header parameters with the event parameters.

Follow these steps to create a new schedule:

1. Click **Event Scheduler** in the app tray. The Event Scheduler screen appears as shown below.



![Screenshot of the Event Scheduler page.](https://files.readme.io/4f70116-11.jpeg)




2. To create a new schedule, click **Add Scheduler**. Create a Schedule page appears.



![Create a Schedule](https://files.readme.io/73ab0c9-Event_Scheduler1.jpg)




The configuration varies depending on whether you select 'Custom Event' or 'SMS'. The following are the details:

### Custom Events

To invoke a flow, perform the following steps:

1. Click **Custom Event** under the Select action section. 



![Create Custom Event](https://files.readme.io/c7b25be10da1597222b9b05d10c634e1aac3402340a3442dbf14f415ef22023f-2025-11-18_13-05-49.png)




2. Select a service from the **Select Service** dropdown.
3. Select an event you want to use from **Select Event / Inbound Webhook** dropdown. Make sure to choose an event that is associated with your service. If you select an event that is not linked to the chosen service, the following error message appears: “The selected event is not associated with the chosen Service. Please verify your selection.”
4. Click **Next**.



![Create Custom Event](https://files.readme.io/cf92f47-Event_Scheduler2.jpg)




5. Select one of the following:
   - **Upload File** to upload a file from your system.
   - **SFTP** to pick the file from an SFTP location.
   - **Consent Group** to select the consent groups as per contact policy.

> 📘 Note
> 
> - To maintain the accuracy of your values, always format all columns as Text before saving and uploading your file to the Event Scheduler. This prevents Excel’s default settings from changing your data.
> - The Consent Group option is visible only when the Contact Policy is enabled for your tenant.
> - It is recommended to format all columns as **Text** before saving and uploading your file to the Event Scheduler. This ensures the values remain accurate and are not changed by Excel’s default formatting.

6. **Using Upload File Option**: The Total Rows field displays the total number of rows available in the spreadsheet including the number of Valid Rows, Invalid Rows, and Duplicate Rows. This populates/shows up when a file is uploaded in the "Upload a file" option.

   

![Sample File Format](https://files.readme.io/7e0dd66ebc934b187366c361345dd0aaf78ad344ff37f86543e35395985c5b8f-2025-09-16_18-27-34.png)



   > 📘 Note
   > 
   > Only valid records will be processed further. The total number of rows processed will be displayed in the Total Entries column in the Logs page.
   > 
   > If the transactions fail or if any duplicate or invalid records are found during the processing, they will be captured in the logs csv file.
   > 
   > If you have any emojis in the CSV file, please save the file with the "CSV UTF-8 (Comma-delimited) (.csv)" file format to ensure that the emojis are rendered properly on the customer's device.
7. Select the delimiters of the file and click **OK**.  
   If the file upload is successful, the status is indicated with a tick along with the detail count of values read from the provided file. Such as, the name of the file, name of the person who uploaded the file and the total number of rows (including Valid, Invalid and Duplicate Rows). 



![Screenshot displaying the Upload File option under Target data.](https://files.readme.io/389b53c-ES2.jpg)




The parameters will be matched in **Parameter** and **File Headers**. As without the parameters you would not be able to trigger the errors. 

In case of errors or some values are not readable, you can upload the file again.

8. **Using SFTP Option** To upload a file via SFTP, select **SFTP**.



![Screenshot displaying the Upload SFTP option under Target data.](https://files.readme.io/cd36c82-ES3.jpg)




9. Click **Select Existing SFTP** to upload the file using existing SFTP. The data will be non-editable.  
   Or
10. Click **Create New SFTP** to create a new SFTP.  Refer SFTP section below for more details.  
    Once you have uploaded the file or configured the SFTP details successfully:

> 📘 Note
> 
> The FTP feature is no longer supported for new configurations, because Data sent via FTP is vulnerable to sniffing, spoofing, and brute force attacks, among other basic attack methods.
> 
> The feature will work as is for the existing customers.

11. Click **Next**. Basic Details page appears.



![Create Schedule - Basic Details](https://files.readme.io/3aeda73-Event_Scheduler3.1.jpg)




12. Enter a name for this Schedule, in the **Name** field.
13. Select **Send Trigger Notification Via Email** checkbox (optional) and enter a valid email ID, to receive notifications via Email. You can add multiple email ids separated by commas. A list of notifications through emails for errors that occur in event scheduler is added and gets triggered according to the error type to the entered email ids. The Email contains the summary of the  trigger execution including File Name, Trigger Name, Trigger Id, and so on.  
    Below is the list of events for which error notifications will be sent:
    1. Failure - Folder Path Not Found
    2. Failure - File Header Mismatch
    3. Failure - File Size Too Large
    4. Failure - File Not Found
    5. Failure - No Valid Records Found In The File
    6. Failure - Invalid Zip Password
    7. Failure - Failed To Connect To FTP
    8. Failure - Failed To Connect To SFTP
    9. Failure - End Of File Not Found
    10. Failure - Social Hours

In case the **Send Trigger Notification Via Email** checkbox is unchecked customer can still see the list and progress of the triggered events from the **Logs** option.  

> 📘 Note
> 
> The file name comes as NA if the transaction fails during processing.

14. Click **Next**. The page to configure the execution pattern and the dates of execution for this schedule.

> 📘 Note
> 
> The time and date on which the trigger happens always depends on the time-zone of the tenant. Thus, the start and end date/time need to be defined accordingly.



![Screenshot of selecting the Event Frequency](https://files.readme.io/9dc66c7-Event_Scheduler4.jpg)




15. You can select from one of the following execution patterns for running the schedule:

    1. **Immediate:** the messages or custom event triggers are sent immediately.
    2. **One time:** you can set a future date and time for sending the SMS or invoking custom event.
       1. Enter the start date and start time.
    3. **Hourly:** the hourly allows to set the frequency however many times you want per hour.

       1. Enter the start date and start time.
       2. Enter the Repeat frequency in **After every \_minutes**.
       3. Select one of the from the **End** dropdown:

          1. **No End** trigger will repeat continuously without end.
          2. **After** the trigger stops after entered number of **Occurrences**.
          3. **On** the trigger stops at the entered **End Date** and **End Time**. 

          

![Screenshot of selecting frequency to run the schedule hourly](https://files.readme.io/074a479-Event_Scheduler5.jpg)


       4. **Daily:** the event trigger to be fired daily.
       5. **Weekly:** the event trigger to be fired on weekly basis.
       6. **Expression:** the event trigger can be customized as per the requirement entering expression. 

          1. **No End** trigger will repeat continuously without end.
          2. **After** the trigger stops after entered number of **Occurrences**.
          3. **On** the trigger stops at the entered **End Date** and **End Time**.

             

![Screenshot of selecting the Expression triggers.](https://files.readme.io/17d15d5-2.jpg)


16. You can click the **Social Hours** check box given on the page for all the options to enable the triggers to be delivered only within the set social hours. 

> 📘 Note
> 
> When this option is enabled, triggers that run outside social hours will not process the files found in the SFTP location. Any files not processed will be picked during the next trigger execution that falls within social hours. Any triggers that start execution before social hours will continue to be processed through non-social hours for large files.

17. You need to define the social hour from the **Settings** section of Event Scheduler first to enable the option. See **Social Hours** section for details.<br>
18. From the **Select Execution TPS** dropdown list, select the required TPS. The TPS ranges from 1 to 50. Using this option, you can configure the transactions per second (TPS) limit for various Messaging/Event API invocation schedules configured through the event scheduler. Overall, the TPS is subject to a maximum of the Messaging API and Event API TPS limits of your Webex Connect account. Also, the configured TPS is the max TPS at which platform makes an attempt to execute your Event Schedule. However, it is subjected to the available TPS at any given point in time. When Event Scheduler encounters maximum transaction limit reached i.e., 7020 scenario (this may occur if your Webex Connect tenant is being used for processing other communications while the Event Scheduler is running in parallel), it automatically retries until the TPS becomes available. 



![Select Execution TPS](https://files.readme.io/15386e5-Event_Scheduler6.jpg)




> 📘 Note
> 
> The option to 'Select Execution TPS' may not be enabled by default if your Webex Connect tenant was created before this features was launched. Please reach out to support team if you want to get it enabled.

19. Click **Save**. The Event Scheduler list page appears.
20. **Using Consent Group Option : **Select **Consent Group**.

    

![Screenshot displaying the Consent Group option under Target data](https://files.readme.io/d18d46149d5b5e3849cfa9325453bd72a926802d52f67a4e257449f48ed382ae-image.png)


21. Select one or more consent groups from the dropdown. The dropdown contains only the allowed list from the Contact Policy.
    > 📘 Note
    > 
    > Even if a consumer id is present in more than one selected consent group the message will be sent only once to the consumer id.
22. Map the Consent Group Channel Identifiers with relevant Custom Event Parameters.
    The available identifiers depend on the channels supported by the selected Consent Group. For Text, Voice, and Email consent groups, map the existing identifiers such as `msisdn` and `email`.
    For WhatsApp-enabled consent groups, an additional identifier, `alternateAddress`, is displayed. Use `alternateAddress` to map the Custom Event Parameter that contains the WhatsApp Business-Scoped User ID (BSUID).
    > 📘 Note
    > 
    > - The `alternateAddress` row is displayed only when the selected Consent Group supports WhatsApp.
    > - The `alternateAddress` mapping is optional by default, unless the selected consent flow requires BSUID-based identification.
    > - Each request to be processed may contain `msisdn`,` email`, or `alternateAddress`. Configure the relevant Custom Event Parameter mapping for the identifier or identifiers expected in the request.
    > - If a mapped identifier is not present in the request, an error may be thrown based on execution rules.
    > - If both `msisdn`/address and `alternateAddress` are present, Webex Connect uses the available identifiers to resolve the consumer. If the identifiers conflict, the record is rejected or logged based on the configured error-handling rules.
23. Click **Next**. Basic Details page appears.  
    The list contains information on Trigger ID such as Type, Name - Unique Correlation ID (with details of Creation Time, By Whom), Total Runs, Pattern, and Status of all the schedules. You can manage and update any of these Schedules by clicking the Action dropdown.

> 📘 Event Schedule Correlation ID
> 
> When you configure a schedule using Event Scheduler, Webex Connect generates a unique Correlation ID and uses it as the correlation id for every message sent using this Schedule whether it's a direct outbound SMS schedule, or a custom event trigger based schedule. However, you can use a different Correlation ID in the channel specific Send Node if you want to user a different value.

The list contains information on Trigger ID such as Type, Name (Time, By Who), Total Runs, Pattern, Status and Action of all the triggered events. All the triggers are by default Enabled. 

### SMS

To invoke an SMS schedule type, perform the following steps:

1. Click **SMS** on Select action page. 



![Screenshot of creating a schedule for the SMS channel](https://files.readme.io/ad556da-App_Tray_Event_Scheduler_SMS.png)




2. Select a service type from the **Select Service** dropdown.
3. Select a message type you want to use from **Message Type** dropdown. Available options are- Test, Binary, Flash and Unicode.
4. Select a **Sender ID** from the list.
5. Use 'Extra Parameters' section to pass the DLT Template ID details if you are planning to send these messages to recipients in India. This feature currently supports only this particular use case. 
6. Enter the **Message Validity in Minutes** in the text box.
7. Follow the steps from 5-8 in **Custom Events** section above.
   > 📘 Note
   > 
   > The dropdown for the consent group selection contains the allowed list which has SMS, SMS+Voice, SMS+Voice+Email, SMS+Email, groups.
8. On successful file upload (through either input type) or consent group selection, do the following:

   

![Screenshot displaying the Upload File option under Target data](https://files.readme.io/20cdc9a-2.jpg)



   - (For Upload File and SFTP) Recipient: select a recipient from the dropdown.
   - Message Body: enter a message in the text field. You can enter attributes in the message body by typing $, followed by the variable name in () brackets. The message can contain up to 4000 characters. We recommend that you keep SMS messages below 450 characters for better deliverability and user experience.
   - The character counter shows the number of characters entered in this field only. It does not represent the final SMS message length or segment count.
     > 📘 Note
     > 
     > Messages will be sent only to recipients who have provided consent for SMS and if the consent has not expired.
     > 
     > The valid escape characters like \\n , \\t, \\', \\” ,\\r can be used in the Message Body.
9. Click **Next**.
   > 📘 Note
   > 
   > Any errors occurred during the process, for example, deleted, expired or revoked of consent groups, are captured in the logs.
10. Follow the steps 12 to 15 in **Custom Events** section above. 
11. Click **Save**.  
    The Event Scheduler list page appears with the added SMS Event Schedule.



![Screenshot of the Event Scheduler list page with the added SMS event schedule](https://files.readme.io/6e4078a-Event_Scheduler8.jpg)




> 📘 Note
> 
> If +E.164 format is enabled for your tenant - all the Destination numbers should follow the "+E.164" format.
> 
> This format displays the number with a "+" followed by the country code and the phone number.
> 
> \+E.164 format is not applicable to the numbers in the **Sender** field.

## Configuring SFTP Details for Event Scheduler

The tab displays the current SFTP configuration. 

To upload files using SFTP, perform the following steps:



![Screenshot displaying the list of SFTP configurations](https://files.readme.io/01661be-Event_Scheduler9.jpg)




1. Click **Add SFTP** to create a new SFTP.



![Screenshot of creating an SFTP configuration.](https://files.readme.io/49abc96-2022-03-31_22-35-27.jpg)




2. Select **SFTP Type** from the dropdown. By default the **SFTP** is selected.
3. Enter a **Friendly Name** for the SFTP.
4. Add the **Host Name**.
5. Enter the **Port** number (for ex. SFTP is port 22).
6. Enter a **User Name** and **Password**.
7. Enter the **Folder Path**.
8. Enter the **File Regex**. It limits the file to be uploaded as per the given condition such as you can only upload the file starting from P or Pn etc.

> 📘 Note
> 
> - We support User Name and Password-based authentication for SFTP connections. You can also upload the private key (like example: AWS based Open SSH key files like rsa512.ppk, rsa256.ppk, ecdsa521.ppk, ecdsa384.ppk, ecdsa256.ppk, ed25519.ppk, ECDSAprivate.ppk, EDDSA255private.ppk) for SFTP configuration, when you select the File Destination as SFTP using the **Upload** button.
> - Key-based authentication for both, Linux servers and AWS servers is currently not supported.
> - Regex is applied to filename part alone and not to extensions.

Example:

- [a-z]\*
- [a-zA-Z0-9]\*
- [^xyz]\*

9. Select **Disable end of file** to remove limit of file ending.
10. Select **Enable zip file processing** to enable the processing of even the zipped files.  	  
11. Enter the **Delimiter** value.
12. Click **Upload Key File**, if the upload of SFTP files with key exchange is required.

> 📘 Note
> 
> SFTP now supports uploading a SSH key file which is required to connect to certain SFTP systems.
> 
> - In case of SFTP only .csv and .xlsx are supported and not .txt.

13. Click **Save**.  
    The files will be uploaded and saved.

> 📘 Note
> 
> The server creates different folders for SFTP files based on their status for example - the files still in progress will be saved in **Processing**, the files finished processing successfully in **Done** and unsuccessful file uploads in **Failed** folder respectively.

## Configuring Settings for Social Hour Checks

To configure settings for social hour checks, perform the following steps:

1. Navigate to the **Settings** option to define the **Social Hour**. The social hour will be based on the time-zone of the tenant. By default, for every country social hour is not configured from 9:00 to 18:00. However, you can set exceptions by checking the **Set social hour exception** checkbox. 



![Screenshot of setting Social Hours](https://files.readme.io/abf22b5-Event_Scheduler10.jpg)




2. Enter exception start and end time in **FROM** and **TO** time-pane.
3. Click **Add New** to add another exception in the same day. For each day of the week max two exceptions can be added. The user will not get any messages during the set exception time.  
   You can also add an entire day as **Non-Social Hour** by going to the **Add holiday into list and they are treated as a non-social hour** section on the page. 
4. Click **Add** and select a date from the calendar. 
5. Click **Update**.  
   On success, **Social hour settings saved successfully.** message appears and social hour gets updated.  
   When any trigger happens in non-social hour, it triggers an error email sent to the customer stating the failure as triggers that runs outside social hours will not process the files found in the SFTP location. Similar kind of email will also be sent in case of the successful trigger execution. 



![Screenshot of email notification indicating that scheduled trigger execution has failed](https://files.readme.io/c0c6cd2-error_email.png)




Any files not processed will be picked during the next trigger execution that falls within social hours. Any triggers that start execution before social hours will continue to be processed through non-social hours for large files.

## Event Scheduler Logs

Logs provide a detailed overview of the events that have been triggered.



![Screenshot displaying a list of Event Scheduler Logs](https://files.readme.io/4818448-Event_Scheduler11.jpg)




Table below describes the parameters in the log tab.



| Field | Description |
| --- | --- |
| Search | Enter a keyword to search a log. |
| Schedule Type Filter  | Select the event from the dropdown for which the logs are required to be generated. Options include All Events, SMS or Custom Event. |
| Select Period | Use the dropdown to select the required time period to view the logs.  <br>  <br>You can also select custom date and time.  <br>  <br>Note: Logs are saved only for 6 months. So you cannot select the start date which is more than 6 months ago in the Custom filter. |
| Type | Signifies the event type, for example, SMS. |
| Name | Event scheduler name. |
| Service | Service to which the event being scheduled belongs. |
| Time | Date and time corresponding to the status of the event. |
| Total Entries | Displays the number of but the number of records that will be processed. |
| Processed Entries | DDisplays the number of successfully processed entries. |
| Errors (I/D) | Lists the number of Invalid or Duplicate IDs. |
| Status | Displays the trigger status, for example: Started, Processed or Error. The information icon associated with the Error status displays the error message. |
| Error Report | Downloadable report in csv format, that lists the errors/failed transactions. The report contains the following information:  <br>  <br>·      List of rows that were not processed  <br>  <br>·      Reason of failure and the details along with the transaction id  <br>  <br>Note: The download button is not visible if the errors in the Errors (I/D) column in 0/0. It is available only in case of processing errors. |




### Additional Options

Click the inverted triangle to open the menu of an event to view additional options:

- To rename or make changes to an event, click **Manage**.
- To delete an event, click **Delete**.