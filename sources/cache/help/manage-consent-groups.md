# Manage Consent Groups

Source: https://help.webexconnect.io/docs/manage-consent-groups
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:38+00:00

Using the Action menu on the Consent Group page, you can manage your groups. This includes viewing consumer records, modifying certain fields, and uploading consumer records. From the Consent Group page, you can also disable or re-enable status reporting. Status can also be changed under Settings.

## View and Modify a Group



![Snapshot of Management Consent Group Page](https://files.readme.io/0e9a569-Manage_Consent_Group.png)




To access, view, and modify a group, or to upload a .csv file, use the directions below.

1. On the Consent Group page, find the group you want to modify. You can use the Search field at the top of the page to find the specific group. The most recently created Consent Groups are listed at the top.
2. Under the Action column, click the down arrow and select **Manage**.  
   The Consent Group page for the selected group appears, listing all the consumer details and when they were last updated. The columns displayed in the Consumer Records tab are
   - Consumer Details
   - Channel
   - Consent
   - Expiry Date
   - Last Updated  
     For WhatsApp consumer records, the **Consumer Details** column displays the customer's WhatsApp address or WAID. If a BSUID is available, it is shown as `alternateAddress` under the consumer details.  
     The `alternateAddress` value stores the customer's Business-Scoped User ID (BSUID), when available. This helps Contact Policy associate a WhatsApp address or WAID with the customer's BSUID.
3. Click Settings, and the Consent Group details appear. The fields listed below can be modified for a consent group.
   - Group Name
   - Description
   - Status
   - Frequency Type
   - Frequency Cap
   - Sender ID
4. Make the appropriate changes.
5. Click **Save**.

## Upload Consumer Records

You can upload a `.csv` file up to 25 MB to a group. The `.csv` file contains the consumer records for the group. The standard CSV format is `date`, `address`, `channel`, `consent`, `expires`, `keyword`, `campaign`, and `source`. For WhatsApp consent records, you can also include `alternateAddress` and `replaceAlternateAddress` to maintain WhatsApp Business-Scoped User ID (BSUID) values. When you upload the CSV file, specify the headers for the mandatory columns.

> 📘 Note
> 
> - `alternateAddress` is applicable only for WhatsApp consent records.
> - If both `address` and `alternateAddress` are provided, Webex Connect uses both values to identify and maintain the consumer record.
> - If `alternateAddress` is already associated with another consumer record, the upload may fail for that record to prevent conflicting consent mappings.

For WhatsApp consent records, the following optional fields are supported:

| Field                     | Description                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alternateAddress`        | The WhatsApp Business-Scoped User ID (BSUID) associated with the consumer. This value is treated as an opaque identifier and is not validated as a phone number or email address. |
| `replaceAlternateAddress` | Indicates whether an existing `alternateAddress` value can be replaced. Supported values are `true` and `false`.                                                                  |

> 📘 Note
> 
> Only 'date', 'address', 'channel', and 'consent' are required and the following is the sample record :
> 
> _The ‘Date’ column includes the timestamp in the UTC format._
> 
> **For Text**
> 
> - 2019-03-30T15:00:00Z,+15558501816,text,TRUE,2025-03-20T15:00:00Z,START,promotion,website
> 
> **For Voice**
> 
> - 2024-12-20T04:00:00Z,+15558501816,voice,TRUE,2025-03-20T15:00:00Z,START,promotion,website
> 
> **For WhatsApp**
> 
> - 2022-01-01T00:00:00Z,+15558501816,whatsapp,TRUE,2025-03-20T15:00:00Z,START,promotion,eventscheduler,US.13491208655302741918,false
> 
> **For email** 
> 
> - 2023-05-01T00:00:00Z,[abc@gmail.com](mailto:abc@gmail.com),email,FALSE,2050-08-01T15:00:00Z,keyword,ConsentGroup,eventscheduler

There are two ways you can upload a file:

- Method 1  – Use the Action menu for a specific group on the Consent Group page.
- Method 2 – Use the Upload Records button on the Manage Consent Group page for the selected group.

> 📘 Note
> 
> It is recommend that the uploaded file includes the most recent consent date and time for each record. The UI will display the latest consent date and time, either from the uploaded file or from any user updates. If the uploaded consent date and time is older than the value already stored in the Contact Policy database, the UI will continue to show the more recent value. Only newer consent date and time values will appear in the UI.

### Method 1

Use the directions below to upload a file from the Action menu.

- On the Consent Group page, find the group to which you want to upload a file. You can use the search field at the top of the page to find the specific group.
- Click the associated Action menu and select Upload. 

1. In the Upload Records window, you can click **Choose File** and navigate to the file location, or you can drag and drop the file to the indicated area.

> 📘 Note
> 
> - You can click**View CSV Sample** to ensure your .csv file is formatted correctly. The mandatory columns in the .csv file are **address**, **channel**, and **consent**. The optional columns in the file are **expires**, **keyword**, **campaign**, **source**, **alternateAddress**, and **replaceAlternateAddress**.
> - The `alternateAddress` and `replaceAlternateAddress` columns are applicable only for WhatsApp consent records.
> - Any entries in the file that are incorrectly formatted will be shown as a failure in the Status column on the Uploaded History page.

2. In the **Reason** field, type the reason for uploading the file.
3. Select the **Update existing policy for documents** checkbox to update any existing records that are already in the group. 

> 📘 
> 
> If you do not select this option, any new information pertaining to existing consumer records will be ignored. For example, if an older file marked the consent for a certain consumer record as “true”, and that of the latest file marked the same consumer record as “false”, and the new file is uploaded, the whole record will be ignored. It is recommended to select this option if a newer version of the same file contains updated consumer information.

4. Click **Upload**. The newly imported file appears in the Management Consent Group page for the specific group under the **Upload History** tab.



![Manage Consent Group - Upload History Tab](https://files.readme.io/66b033710afb9c1e782d733af2396ef4d932f83e908db66c4eafa1958dc030a0-image-20240802-151730.png)




> 📘 Note
> 
> When you use an API to upload the file, the system hides the Uploaded By parameter because it does not display the value.

> 🚧 
> 
> Opening a CSV with some spreadsheet programs (E.g., Excel, Numbers) may alter E.164 phone number formatting.

The records contained in the file appear in the Management Consent Group page for the specific group under the **Consumer Records** tab.

### Method 2

Use the directions below to upload a file from the Manage Consent Group page for the selected group.

1. On the Consent Group page, find the group to which you want to upload a file. You can use the Search field at the top of the page to find the specific group.
2. Click the associated **Action **menu** and select **Manage\*\*.  
3. In the Management Consent Group page for the specific group, click **Upload Records**.

   

![Manage Consent Group - Upload Records Tab](https://files.readme.io/9950bf3ceb96c499530ffccf37928be5f34743d90402ee407e786d532a14519e-c0771694-fd6a-47fa-8e3f-79f07756fb63_1.png)


4. In the Upload Records window, you can click Choose File and navigate to the file location, or you can drag and drop the file to the indicated area.  
   You can click **View CSV Sample** to ensure your .csv file is formatted correctly. For WhatsApp records, the sample CSV can include `alternateAddress` for the customer's BSUID and `replaceAlternateAddress` to indicate whether an existing BSUID mapping should be replaced. Any entries in the file that are incorrectly formatted will be shown as a failure in the Status column on the Uploaded History page.
5. In the Reason field, type the reason for uploading the file.
6. Select the Update existing policy for documents check box to update any existing files that are already in the group. If you do not select this check box, any new information will be ignored. 
7. Click Upload. The newly imported file appears in the Management Consent Group page for the specific group under the Upload History tab.  
   The records contained in the file appear in the Management Consent Group page for the specific group under the Consumer Records tab.

## Upload Status

The status of an uploaded file can be found on a group’s Manage Consent Group page under the Upload History tab.

To view the failed entries, click the file name, and the **Upload Outcome** modal appears. Only the first 50 entries can be viewed. To view details of the entries or to view additional entries and their details, click the **Download Details** (.CSV) button.

In the **Download Details** file, under the **Outcome** column, you can view the reason for the failure. You can also correct the entries in the file, save it, and upload it again.



![Sample of a Downloaded CSV file](https://files.readme.io/d293c621753adbc424a0ba15f07dea9939eb2c330cc2236af0c7cdd305665646-image-20250908-085329.png)




> 🚧 
> 
> Opening a CSV with some spreadsheet programs (eg. Excel, Numbers) may alter E.164 phone number formatting."

Click **OK **to close the** Upload Outcome** modal.

## Reasons for upload failure

The following error messages are displayed on success or failure after uploading the file. For entries that list the “File Upload Status” as “Failure,” you can review the .CSV file for any incorrect information related to these error messages and try uploading the file again for a successful upload.



| Error Message | Description | File Upload Status |
| --- | --- | --- |
| Mandatory field missing | A required field has not been set | Failure |
| Address invalid for channel type | Validation on the address for the specified channel did not pass (E.164 standard for phone number or email) | Failure |
| Invalid format for a field | Different possible errors, mainly if the group does not support the provided channel or invalid date, etc. | Failure |
| Duplicate record ignored | The record already exists for the address, and the 'Update existing policy' option was not selected | Failure |
| Unknown error saving row | Unable to save to the database. Try uploading the file once again after some time. | Failure |
| Row can not be parsed | Unable to read the record from the .csv file. Try uploading the file once again after some time. | Failure |
| Created successfully | Successfully added the record to the group | Success |
| Updated successfully | Successfully updated an existing record for the group | Success |
| Invalid alternate address | The alternate address provided for the WhatsApp record is not valid. | Failure |
| Duplicate alternate address ignored | The alternate address already exists for the record, and the update option was not selected. | Failure |
| Conflicting alternate address | The uploaded record attempts to replace an existing alternate address or BSUID mapping, but `replaceAlternateAddress` is not set to `true`.  <br>Set `replaceAlternateAddress` to `true` to replace the existing BSUID mapping. | Failure |




## Delete a Group

To access and delete a group, use the directions below.

1. On the Consent Group page, find the group you want to delete. You can use the Search field at the top of the page to find the specific group.
2. From the Actions column, click **Delete**.
   > 📘 Note
   > 
   > The 'Delete' option is available for users with full access to the platform. To enable the access permissions for Contact Policy, following are the [Steps](<#Enable Access Permission for Contact Policy>).
3. In the confirmation message, click **Delete**. The group is removed from the Consent Group List.



![A confirmation message displayed with a prompt to click Delete](https://files.readme.io/2d6b07a-Delete_Consent_Group_Confirmation.jpg)




### Enable Access Permission for Contact Policy

Steps to enable the access permissions for Contact Policy:

1. Navigate to **Profile Settings** > **Teammates**
2. **Edit** the user with Full access
3. Select “Full Access” for Contact Policy. Users with the “Full Access” role on the platform will only have the ability to modify the access permission for the Contact Policy and thereafter can see the “Delete” option.
4. Click **Save**

   

![Contact Policy—Full Access](https://files.readme.io/67355fe49da5058ae1ff5f397c714bbda6029cdf2e51e957b450eeed33ded824-Contact_Policy_Picture1.png)



## Deleting a Consumer Consent

To delete a Consumer Consent, follow the below steps:

1. Search for the specified consumer consent using the consumer details such as MSISDN, email address, or BSUID for WhatsApp records.
   > 📘 Note
   > 
   > To retrieve search results for an existing phone number, it is mandatory to include a '+' sign before the number. This requirement does not apply to BSUID values.
2. Select and click the required Consent record from the list.



![Image displaying a list of consumer records](https://files.readme.io/3aaa7c4d351b758815d0e57300c43511b4dd9f44b4ecb2087c2dc1994c604a9e-image-20250609-053832_1.png)




2. Click the **Delete** icon under **Actions**. A pop-up appears.



![A confirmation message displayed with a prompt to click Delete](https://files.readme.io/7b039b6-Delete_User_Consent1.png)




3. Click Delete. A message appears as ”Consent record is deleted successfully.”

> 🚧 Note
> 
> All the deleted consumer consent records are stored within the database for 6 months. To access the record, contact our support team for assistance.