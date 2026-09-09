To make or receive calls, send or receive SMS, or use certain apps available within <<prodname>>, you must associate the services with the right type of phone number. Phone numbers can be either purchased or rented from <<prodname>> for a monthly rental.

Phone numbers are of three types:

- Landline
- Toll free
- Mobile

Each type of phone number has the following features associated to it:

- SMS
- MMS
- Voice

> 📘 Note
> 
> Due to limitations in auto-provisioning MMS for 10DLC numbers in the U.S., the MMS option is hidden for United States landline numbers.

> 📘 Number Availability
> 
> Below are the existing number types migrated to new number types:
> 
> - All the countries with the “Phone Numbers" which have “SMS” feature have migrated to number type “Mobile” .
> - For the US all “Phone Numbers” which have “SMS” feature have migrated to number type “Landline”.
> - “Tollfree and Landline” numbers have remained the same.

## Numbers List

The Numbers page under Assets lists all the phone numbers added in the current tenant. You can search for or filter the numbers list by Number Type. The different number types available to filter are:

- All Numbers
- Short Code
- Phone Number
- Sender ID
- Keyword 

> 📘 Note
> 
> From 5.6.2 onwards, the numbers ordered with SMS capability will be enabled as Sender ID by default.

> 📘 Note
> 
> - In order to comply with the US market requirements, we send SMS to US and Canada using only pre-approved, pre-registered products: 10 Digit Long Codes, Toll Free Numbers, and Short Codes. International long numbers cannot send SMS to US or Canada.
> - Delivery with a country's long number to another country is best effort, but we cannot guarantee it. If it's against the regulations (such as using other countries' long numbers to deliver to the US) the traffic will be actively blocked.

## Get a Number

1. Select **Numbers** from the **Assets** menu and choose the **Phone Number** option from the **Get Numbers** drop-down list box.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8362149-328e62e-Phone_Number_Get_Number.png",
        "Phone Number Get Number.png",
        "Screenshot of Accessing a Phone Number from Numbers"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot Displaying to Select the Phone Number."
    }
  ]
}
[/block]


2. Select the **Country**, **Number Type**, and click **Find Numbers**.

> 📘 Unavailability
> 
> In case you cannot find the country you are looking for, please reach out to the Support Team using the details mentioned in the ‘Contact Support’ section within your <<prodname>> account.
> 
> Voice Numbers purchased in the certain countries have a limitation on the "From Number" displayed on the handset. We are working with our Voice providers to resolve this.

## Search Numbers

1. Select Numbers from the Assets menu and choose the Phone Number option from the Get Numbers drop-down list box.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c3bdd44-Get_Numbers2.png",
        "Phone Number Search Number.png",
        "Screenshot of Searching for a Phone Number"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Search Numbers Page."
    }
  ]
}
[/block]


2. Select the Country, Type, and Features, and click Find Numbers.  
   If you selected United States or Canada as the Country, you can also search by Area Code or Location.

3. Click Find Numbers.

## Number Availability

The type of phone numbers available in different countries may vary depending on the local government regulations and restrictions. If you cannot find a phone number for a certain country, reach out to your regional support team.

## Unavailability

In case you cannot find the country you are looking for, please reach out to the Support Team using the details mentioned in the ‘Contact Support’ section within your <<prodname>> account.

## Order Numbers

When you search for numbers, all the available numbers based on the search criteria are displayed.

1. Click **Buy** associated with the desired number.
2. Click **Confirm Purchase** on the confirmation dialog box to confirm the order. If the number is available, you will see the message "Number purchased and added to your account" and the number will be added to the Numbers list. If the order is pending, you will see a **Pending** badge against the number. Click the badge to view the order status.

## Release Number

You can stop using a number without deleting it.

To release a number:

1. Navigate to **Assets** → **Numbers**.
2. Click **Action** → **Manage** associated with the number you want to release.
3. On the Manage Phone Number page, click **Release Number**.
4. On the confirmation dialog, click **Release Number** to confirm the release.

## Modify Voice Capacity

Depending on the type of tenancy (shared or dedicated) you can modify the voice capacity for your tenant on a whole or for an individual number respectively.

Before you modify the voice capacity, you must ensure that the contract is changed to increase the voice capacity.

To modify the voice capacity at the tenant level (for shared tenancy):

1. Go to Assets > Numbers.
2. Click Modify Voice Capacity.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/98175eb-Voice1.png",
        null,
        "Screenshot of Numbers Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Numbers Page."
    }
  ]
}
[/block]


3. On the Modify Voice Capacity pop-up, enter/update the values for the following for inbound and outbound calls:
   - Concurrency Limit
   - CPS/TPS
   - Usage Cap
4. Click Update.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ab16205-Voice2.png",
        null,
        "Screenshot of Modify Voice Capacity."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Modify Voice Capacity."
    }
  ]
}
[/block]


To modify the voice capacity at a number level (for dedicated tenancy):

1. Go to Assets > Numbers.
2. Click Actions > Modify Voice Capacity associated with the number for which you want to modify the voice capacity.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/872bff0-Voice3.png",
        null,
        "Screenshot of Numbers Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Numbers Page."
    }
  ]
}
[/block]


3. On the Modify Voice Capacity pop-up, enter/update the values for the following for inbound and outbound calls:
   - Concurrency Limit
   - CPS/TPS
   - Usage Cap
4. Click Update.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/87f652c-Voice2.png",
        null,
        "Screenshot of Modify Voice Capacity."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Modify Voice Capacity."
    }
  ]
}
[/block]


## 10 Digit LongCode (10DLC) Numbers

A 10DLC long code is a phone number with the same length as standard mobile or landline numbers (typically a 10-digit number in many countries). In the past, business messaging traffic over long codes was sent over the carriers’ P2P networks, which limited them to very low throughput and restrictions on use from the carriers. With the introduction of 10DLC A2P messaging, carriers in the U.S. have rolled out a verified method of sending A2P traffic which has removed these constraints on business messaging making 10DLC enabled numbers more suitable for lower volume business messaging.

With release v5.6.2, you can buy phone numbers and toll-free numbers by selecting the country as the United States and then the area code or location. These numbers can be provisioned for Voice, SMS, and MMS.

### Buy Numbers for the United States

1. Select the Country as the United States, and the Type as Landline. 
2. Select the Features as SMS.
3. Search for numbers using either the **Area Code** or **Location** and click **Buy Number** next to the required number.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e610f92-Buy_NUmbers.jpg",
        "Buy NUmbers.jpg",
        "Screenshot of Buy Phone Number Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Buy Phone Number Page."
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ee2d51b-10DLC.jpg",
        "10DLC.jpg",
        "Screenshot of Numbers Listing Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Numbers Listing Page."
    }
  ]
}
[/block]


> 📘 Note
> 
> For 10 Digit Long Code (10DLC) numbers in the US, you can now see the details of brand ID and campaign ID associated with the numbers when you hover over the 10DLC badge in the number listing page.

You can see the number that you have purchased on the Numbers page with a yellow color pending badge. In the **Actions** drop-down list box against that phone number with the SMS capability, click **Request 10DLC**. In the pop-up screen, select the **Request 10DLC** checkbox and then select the required brand ID and campaign ID. The brand ID and campaign IDs in the drop-down list are the list of brand and campaign IDs shared by the client with the [operations teams](mailto:operations@imimobile.com) and added in the Admin Console.

A badge saying **10DLC Requested** appears next to the number. Once this number is enabled for 10DLC and the Sender ID, a badge **10DLC** appears next to the number and it can be used in Flows and Rules.

## Provisioning the Numbers for MMS, Custom, Bulk, Porting or Vanity TFN (Tollfree)

Click the **For MMS, Custom, Bulk, Porting or Vanity TFN Number Requests** link. A form appears. In this form, enter the message for requesting the number to provision for MMS and Tollfree number and click **Send**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0b50f39-10dlc_provisioning_form.png",
        "10dlc_provisioning_form.png",
        "Screenshot of Provisioning the Numbers for MMS, Custom, Bulk, Porting or Vanity TFN."
      ],
      "align": "center",
      "border": true,
      "caption": "Provisioning the Numbers for MMS, Custom, Bulk, Porting or Vanity TFN"
    }
  ]
}
[/block]


## Process for supporting number procurement requests

The new number management system provides an option to request existing numbers to be text-enabled by attaching the Letter of Authority (LOA) documents. LOAs provide the necessary authorization needed for <<prodname>> to register a number owned by another service provider for messaging on its network. The <<prodname>> staff will authenticate the LOA before text enabling or porting the number.

Additionally, the newly enhanced number management system includes the following updates:

- Custom requests for MMS Numbers, bulk number purchasing, porting, and searches for vanity TFNs from your tenant.
- Adds the capabilities to buy Phone Numbers with ‘Voice’ and ‘Voice, SMS’ and Toll-free ‘Voice’ and ‘Voice, SMS’ in the United States and Canada
- Usage Reports: In the Numbers section we’ve added ‘US 10DLC Brand ID’, ‘US 10DLC Campaign ID’, and the ‘US TFN Verified Sender’. 

## Enabling an Existing Number for sending Text Messages

Click the **For Text Enabling an Existing Number** link. A form appears where you need to enter a request message for enabling the existing number for sending text messages.

The new number management system provides an option to request existing numbers to be text-enabled by attaching the Letter of Authority (LOA) documents. LOAs provide the necessary authorization needed for <<prodname>> to register a number owned by another service provider for messaging on its network. The <<prodname>> staff will authenticate the LOA before text enabling or porting the number. 

Click **Attach LOA** and attach the letter of authority. Click **Attach List** and attach the list of numbers, in case of multiple numbers.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ae79388-10dlc_attach_loa.png",
        "10dlc_attach_loa.png",
        "Screenshot of Enabling an Existing Number for sending Text Messages."
      ],
      "align": "center",
      "border": true,
      "caption": "Enabling an Existing Number for sending Text Messages."
    }
  ]
}
[/block]


## Send SMS from 10DLC and TFN numbers

With this release, you can send SMS from TFN and 10DLC enabled phone numbers in <<prodname>>:

- All phone numbers added as a Sender ID with 10DLC enabled label confirmation can be used to send SMS via Messaging API v1, v2, and v3.
- All numbers are available to be used in the rules and flows to send and receive SMS in the tenant.
- TFN numbers can also be authorized as a verified sender ID by going through a similar registration process like 10DLC. Verified sender ID for TFNs permits high messaging and prevents carrier blocks. 

> 📘 TFN and VSF
> 
> The time taken for number provisioning may vary by region based on the operator requirements.  
> For example, in the US, TFNs may take 2 weeks, and long codes take about 2 days, based on review and registration requirements.  
> The current processing time for a verified sender form for TFN to be vetted and approved is estimated at 15 business days.  
> The Cisco code management communicates the approval via email and updates all the labels indicating that your Toll-Free Numbers (TFNs) are cleared to send messages.

## DLT Registered Numbers

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e6ec87c7086e27bbae5744750b62a70691a298d57f21166a4c6dba4a7ea2b8fa-DLT_Template_Registration.png",
        "",
        "Entity ID for number registered on the DLT portal"
      ],
      "align": "center",
      "border": true,
      "caption": "Entity ID for number registered on the DLT portal"
    }
  ]
}
[/block]


Only numbers registered against your DLT primary entity can be used for SMS communications within India.  
In the **Short Code** page > **Registered on the DLT portal** section >, select your **Entity ID** from the **Entity ID** drop-down menu.

## Reserved Keywords

You can reserve and associate particular keywords to a specific number. Up to a maximum of 50 keywords is allowed per number.

To reserve a keyword:

1. Go to **Assets** -> **Numbers**.
2. Click **Manage** next to the number to which you want to associate the keywords.
3. In the Keywords List section, enter a keyword of 3-30 characters with no spaces and special characters and click **Add Keyword**. If the specified keyword is available, the platform adds it to your **Reserved Keywords** list.

Once you add a keyword as a _reserve keyword,_ you can no longer use that keyword as the trigger for a Rule or a Flow within <<prodname>>.

> 📘 
> 
> When a reserved keyword is received as an SMS, even if you are having a conversation with a customer using a flow, only the URL configured against the reserved keyword will be called, and the flow won’t receive this message. For more information refer to the [Start Node](https://help.imiconnect.io/docs/start-node) chapter.

## Delete Number

You can delete a phone number using the Delete option under the Actions menu.

To delete a phone number:

1. Go to Assets -> Numbers.
2. Click Action -> Delete associated with the number you want to delete.
3. On the confirmation dialog, click Delete to confirm the deletion.

When you delete a number, it is deactivated from all the related services and marked as inactive. The inactive status will be shown to all the other users in tenant.

## Handle incoming calls via callback URL

Enable this to configure the callback URL that needs to be notified when an incoming call comes to this number. Once configured, this number cannot be used as a trigger for Incoming calls in Rules or Flows. To use it as part of flow you must disable it. 

Detailed description of[ Handling Incoming Calls](https://developers.imiconnect.io/reference/answer-incoming-calls-to-a-connect-asset-handle-via-events-and-actions)