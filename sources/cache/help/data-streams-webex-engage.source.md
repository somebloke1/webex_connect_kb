> 📘 Note:
> 
> Data stream support in Webex Engage is exclusively available for the Apple Messages for Business (AMB) channel, specifically for the Typing Indicator event.

## Enabling Data Streams for Apple Business for Messages (AMB) assets

To enable Data streams for AMB assets, follow these steps:

1. Provision your Apple Messages for Business asset.
2. Login to Webex Connect and navigate to **Assets** > **Integrations**.
3. Search for the Integration: **Webex Engage Streaming**.
4. Choose **Manage** from the Actions drop-down list.

This integration is enabled by default for all channels on the Webex Engage Streaming screen.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9218240bddaa01dfe7ec214c43952a5f2807b0b02cce84f8eb0cfc0a05b8a5bc-image.png",
        null,
        "Interface showing options to enable Data Streams for Apple Business for Messages (AMB) assets"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the enabling of Data Streams for Apple Business for Messages (AMB) assets."
    }
  ]
}
[/block]


5. Uncheck all channels except the AMB channel from the Channels drop-down list, as we only support that one.
6. Click **Save**.

> 📘 Note:
> 
> Even though the Integration lists events as Incoming Events and Messages, Webex Engage does not process incoming messages on channels through this method. You can only stream customer Typing Indicator events alone to the Live Agent.

## Enabling Data Streams for select assets

To turn ON the Webex Engage Stream for select AMB assets, follow these steps:

1. Login to Webex Connect and navigate to **Assets** > **Integrations**.
2. Search for the Integration: **Webex Engage Streaming**.
3. Choose **Manage** from the Actions drop-down list.

This integration is enabled by default for all channels on the Webex Engage Streaming screen.

4. Change the setting to **Choose to enable at an asset level**.
5. Click **Save**.
6. Navigate to **Assets** > **Apps**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2ace47a9f1a716847c853b66b95ea145f9f518f30b04c9d8969d5e01b408214d-image.png",
        null,
        "Screenshot displaying the enabling of Data Streams for Apple Business for Messages (AMB) assets"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the enabling of Data Streams for Apple Business for Messages (AMB) assets"
    }
  ]
}
[/block]


7. Find your Apple Messages Asset that you would like to turn ON the data streams and Choose **Manage** from the Actions drop-down list.
8. Tun ON the Data Stream toggle.
9. Choose **Webex Engage Streaming** from the Integration drop-down list.
10. Click **Save**.