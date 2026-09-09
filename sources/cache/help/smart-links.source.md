You can use Smart Links for generating shorter URLs to be sent as part of outbound messages on SMS and other channels to reduce overall message size while leveraging the following intelligent routing capabilities:

- Support device-specific routing by embedding a device OS-agnostic link which when clicked can route recipients to a different URL depending on their mobile operating systems (such as Apple, or Android). This feature can be used to direct users to the right mobile app store for app downloads. 
- Can be configured to expire after a certain duration. If a user clicks the like after the expiry, user will be redirected to a different URL that explains that the campaign/offer is no longer available.

Smart links can be selected through the send node (such as in the SMS send node) or referenced in the [Messaging API](https://developers.imiconnect.io/reference#sms). 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6b6700b-image.png",
        null,
        "Screenshot of Smart links page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Smart links page"
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Description",
    "0-0": "ID",
    "0-1": "Displays the unique identification number for the smart link.",
    "1-0": "Smart Links",
    "1-1": "Displays the name of the smart link.",
    "2-0": "Total Links Sent",
    "2-1": "Displays the count of link sent by various channels.  \n  \n**Note**: The data will be displayed only for the last 30 days.",
    "3-0": "Total Clicks",
    "3-1": "Displays the total number of links clicked.  \n  \n**Note**: The data will be displayed only for the last 30 days. The bot/preview clicks are ignored when identified.",
    "4-0": "Status",
    "4-1": "Displays the status.",
    "5-0": "Device Based Routing",
    "5-1": "Enabled or Disabled is displayed based on the configuration.",
    "6-0": "Actions",
    "6-1": "Manage - You can update the smart links information.  \n  \nDelete - You can delete the smart links."
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 🚧 Status : Active
> 
> Only valid/enabled smartlinks are visible in the drop-down while trying to use it in the _Send_ node.

## Smart Link Support across Channels

The following table describes the supported channels for the Smart Link capability:

| Supported Channels           | Messaging APIs v1 | Messaging APIs v2 | Send Nodes | Rules |
| :--------------------------- | :---------------- | :---------------- | :--------- | :---- |
| SMS                          | Yes               | Yes               | Yes        | Yes   |
| <<AMB>>                      | Yes               | NA                | Yes        | Yes   |
| Facebook Messenger           | Yes               | NA                | Yes        | Yes   |
| WhatsApp                     | Yes               | NA                | Yes        | Yes   |
| Live Chat / In-App Messaging | Yes               | No                | Yes        | Yes   |

## Configuring a Smart Link

To configure a smart link, follow the procedure below:

1. Navigate to **Tools** > **Smart Links**.
2. Click **Add New Smart Link**. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8235f47-image.png",
        null,
        "Screenshot of Configuring the New Smart Link"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Configuring the New Smart Link"
    }
  ]
}
[/block]


3. Configure various details as per below:

[block:parameters]
{
  "data": {
    "h-0": "Options",
    "h-1": "Description",
    "0-0": "Name",
    "0-1": "The name of the Smart Link you want to create. This name appears in the dropdown when you want to use the Smart Link feature.",
    "1-0": "Long URL",
    "1-1": "The long URL that is to be shortened. Along with Http and Https URLs, below URLs are also supported for redirecting users from Smart links to SMS app on Android phones.  \n  \nEg: \\<sms:[webex-connect-cloud@abc.goog](mailto:webex-connect-cloud@abc.goog)  ?body=survey&bot-name=Webex%20Connect%20Cloud>  \n  \nand  \\<sms:+4454XXXXX7435?service_id=[webex-connect-cloud@abc.goog](mailto:webex-connect-cloud@abc.goog)  &body=Hello%20Tom&bot-name=Webex%20Connect%20Cloud>",
    "2-0": "Short Domain",
    "2-1": "The Default available short domain list  will be based on the Environment  \n  \nEg: <https://s-us.imiconnect.io> and <https://s.imiconnect.eu>.  \n  \nCustom domains must be registered with <<prodname>>. To register your domain with <<prodname>>, contact the <<prodname>> support team.",
    "3-0": "Suffix",
    "3-1": "Specifies a text that will be suffixed to the short domain. This will be useful for branding the links. For example, <https://s.imiconnect.co/cisco(Suffix)/Penhgy>",
    "4-0": "Device Routing",
    "4-1": "This capability allows you to intelligently route the user to an OS-specific link.",
    "5-0": "Link Validity",
    "5-1": "This capability allows you to set up the validity of a link on the basis of the purpose and stipulated timeline of an event. For example, users get redirected to a link set up for a commercial offer page until the configured expiry date. After the expiry date of the first link, the user will be redirected to a different URL as per the configuration."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    "left",
    "left"
  ]
}
[/block]


4. Click **Save**. This completes the Smart Link configuration.

Once you're have configured a smart link you can use it while sending SMS messages or other channels using Messaging API or via the SMS Send Node. 

### Steps for configuring branded / short URLs for using 'shortenLinks' capability:

- Work with your IT team to procure the short URL you want to use. 
- Add a CNAME record with relevant redirection based on your <<prodname>> tenant location (table below).
- If you need HTTPS redirection (highly recommended), reach out to <<prodname>> customer support team and provide the domain certificate to add to the Certificate Manager (ACM) for this purpose. This typically requires some lead time hence we recommend you to plan ahead of time for getting this set-up done and leave some time for end-to-end testing.
- Once the backend set-up has been completed by <<prodname>> team, you will be notified over email post which you can start using this.

> 📘 
> 
> Please note that usage of short domains for SMS links can have an impact on deliverability in some cases. Operators and aggregators implement various firewalls and fraud mitigation services in order to protect customers from fraud.  This means URL shortening techniques can sometimes be blocked with no warning, particularly if the words around them seem fraudulent or related to a popular brand or financial entities.

| Webex Connect Region | CNAME                                           |
| :------------------- | :---------------------------------------------- |
| AWS Canada           | star-1176184099.ca-central-1.elb.amazonaws.com  |
| AWS Ireland          | star-1747495833.eu-west-1.elb.amazonaws.com     |
| AWS London           | star-1656037958.eu-west-2.elb.amazonaws.com     |
| AWS Oregon           | star-1571873968.us-west-2.elb.amazonaws.com     |
| Azure (US)           | 52.138.107.55 (A Record)                        |
| AWS Mumbai           | star-64546195.ap-south-1.elb.amazonaws.com      |
| AWS Sydney           | star-131871454.ap-southeast-2.elb.amazonaws.com |
| AWS Singapore        | star-581943434.ap-southeast-1.elb.amazonaws.com |