Data Stream is a data streaming framework and it can be used to receive a copy of message transactions (Incoming Events, Outbound Messages, Delivery Receipts), or [Audit logs](https://help.webexconnect.io/docs/user-audit#log-trail) for a tenant on the configured Kafka destination.

## Understanding the Data Stream Framework

The Data Stream framework is composed of the following :

1. Event
2. Destination
3. Pre-configuration and Enablement
4. Controls (Asset and Payload)

### Event

Events define the data or payloads that will be forwarded to the specified destination.

### Destination

Destinations are nothing but the location where the payloads of events will be sent. Webex Connect only supports Kafka (AWS & Azure) as a destination. Destinations can be pre-configured to enable default streaming of payloads from Webex Connect to the destination, or can be configured by platform users, post-enablement of Data Stream.

### Pre-Configuration and Enablement

Data Streams are pre-configured by the <<prodname>> Support team. Once a Data Stream is enabled for a tenant, it may or may not initiate default streaming of the data to the destination. It depends on how the Data Stream was pre-configured by the <<prodname>> Support team. The <<prodname>> Support team can set up the destination at the client-level. In such cases, data streaming will only commence once the destination is correctly configured within the Data Stream Management section, under the tenant's 'Integrations' area.

> 📘 
> 
> The pairing of Kafka Destination – Kafka Destinations requires VPC(virtual private cloud) pairing.

### Controls (Asset and Payload)

Pre-configured Data Streams are enabled with events for all channels and all assets in your tenant. You can modify the asset configuration in the Data Stream Management section as needed.

A Data Stream payload typically contains three types of parameters:

1. Channel Parameters: Used for channel events, or audit log parameters for audit logs.
2. Pre-configured Parameters: Added by the <<prodname>> Support team during the initial configuration of the Data Stream.
3. User-Defined Parameters: Added by platform users as part of their configuration within the flow. Please refer to the [Sending Flow Variables to Data Stream](https://help.webexconnect.io/docs/data-streams#sending-flow-variables-via-data-stream) section in the lower end of the page for more on how to add parameters in the payload for messages that are exchanged via flows. Adding extra parameters like flows is not possible for the messages sent using Send Message API v1 and Send Message API v2, also if data streaming is enabled at an asset-level. In other words, the ability to add extra parameters is only available for message exchanges via flows.

> 📘 Data Stream feature support
> 
> - Data Stream is supported only on the Start, Send, and Receive nodes of the following channels - SMS, Email, Live Chat or In App, RCS, Messenger, Apple Messages for Business, and WhatsApp.
> - Data Stream is not supported on the Start, Receive, and Send nodes of Voice, MMS channels. Data Stream is also not supported for the Start and Receive node of Push, Webhooks, Custom Events, and Integrations.
> - The Data Stream feature is not supported on the Azure environment.

## Viewing Data Streams

A tenant can have one or more Data streams. You can view the enabled Data streams under 'Integrations'. To view a data stream on the platform:

1. Navigate to **Assets** > **Integrations**.
2. Filter with Data Streams.
3. Enabled Data Streams will be shown in the listing, click Manage associated with the desired stream.
4. The Manage Integration - Data Stream page consists of the following:
   1. Name
   2. Description
   3. Assets
      1. Enable by default for all assets
      2. Choose to enable at an asset-level
   4. Channel Events
   5. Other Events

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5f4a3c1152a96f0eb3bf59bdc0d932e844f6db87fdce396d082bb7a15451b21c-Manage_Integration_-_Data_Stream.png",
        "Data Integration.jpeg",
        "Manage Integration - Data Stream page"
      ],
      "align": "center",
      "border": true,
      "caption": "Manage Integration - Data Stream page"
    }
  ]
}
[/block]


6. Once all the configuration is done, click **Save**.

## Sending Flow Variables via Data Stream

Optionally, Data Streams enabled for your tenants can be selected in the Start, Send, and Receive nodes  to add more context to the Data Stream payloads of Outbound and Incoming Messages. You will have to select a Data Stream in the Start, Send, or Receive nodes in the flow canvas, to be able to add more context (key-value pairs) to the payload. 

To select a Data Stream in a Start, Send, and Receive nodes in a flow:

1. Navigate to the flow for which you want to configure the data stream.
2. Select the channel for which you want to configure the data stream.
3. Navigate to the **Data Stream (Optional)** tab.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d995ee8f985b6d085f001617f52d8bac248da9d6e26e7d89066ce35efcf01d93-Data_Stream_-_Mobile__Web_App_1.png",
        "Data Integration In-app.jpeg",
        "Data Stream tab"
      ],
      "align": "center",
      "border": true,
      "caption": "Data Stream tab"
    }
  ]
}
[/block]


4. Click **Add Data Stream**.
5. Choose the appropriate integration from the list.
6. Click **Add Context**, if you want to build context to the Send or Receive nodes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cc638f1c1a57fdefa826d68916a830403ebb9684994e8694bfbf17d54761e3e1-Data_Stream_-_Mobile__Web_App_2.png",
        "Data Integration 1.jpeg",
        "Add Context option"
      ],
      "align": "center",
      "border": true,
      "caption": "Add Context option"
    }
  ]
}
[/block]


7. For **Parameter Name**, enter the key name and the parameter will be included as data in the notification.
8. For **Value**, enter the flow variables or a static value. This value will be included in the notification against the parameter name. You can add multiple data streams. However, you can choose an integration to be selected only once.
9. Click **Save**.

## Configuration of Data Stream

Data Stream can be enabled either for all assets within a tenant, or for individual assets. The Data Stream configuration gives you the flexibility to enable streaming across all assets, or selectively, at the asset-level.  
By default, Data Stream is enabled for all supported channels. However, you can disable streaming for a specific channel by clearing the selection under the 'Manage Data Stream' section of the platform. This will stop data streaming to the destination for the specified channel.

## Enable Data Streams for Assets

### Configure Data Streams for all Assets at an Integration-Level

1. Log in to <<prodname>> platform.
2. Navigate to **Assets** > **Apps**.
3. Select the desired app or number. The page contains the following details:
   1. **Name**: Contains the name of the Data Stream.
   2. **Description**: Contains the description
   3. **Assets**: Select one of the following:
      1. **Enable by default for all assets**: Select this option to enable the Data Stream for all the assets by default. You must also select the channels for which you want to enable the Data Stream.
      2. **Choose to enable at asset level**: Select this option to enable the Data Stream only for selected assets. To enable the data stream, you must navigate to the selected data stream and toggle the data stream button.
   4. **Channels**: Contains the details about the channels for which you want to enable the Data Stream for.
   5. **Events**: All the events enabled for your tenant will be displayed

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/36350f8c9e315cde5a3013bdc932cd857c79456a4035a173cfe9a4a5394553ce-Manage_Integration_-_Data_Stream.png",
        "",
        "Enabling Data Stream for Assets"
      ],
      "align": "center",
      "border": true,
      "caption": "Enabling Data Stream for Assets"
    }
  ]
}
[/block]


### Configure a Data Stream at Asset-Level

To configure the Data Stream at an asset level, you will have to enable Data Stream for the asset. The configuration to enable Data Stream at an asset-level is found in the ‘Manage Asset’ page. 

To enable Data Stream at an asset-level for RCS channel, you must follow the steps below.

1. Log in to <<prodname>> platform.
2. Navigate to **Assets** > **Apps**.
3. Select the desired app or number.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/edf9751127b92fffa7147a708b799898ed0995ca95fbd8eaeceee053b7c310d4-RCS_-_Configure_New_Application.png",
        "",
        "Configure New Application"
      ],
      "align": "center",
      "border": true,
      "caption": "Configure New Application"
    }
  ]
}
[/block]


4. Toggle the **Data Stream** option to enable it at an asset level to send the messaging APIs (WhatsApp, RCS, Apple Message for Business and In-App Messaging) and receive a copy of the data from Outbound messages and Delivery Receipts for the Integration selected.  
   Select the required integrations from the **Integrations** drop-down. You can select one or more integrations using the checkboxes. Use the **Select All** option to select all the integrations at once.
5. Select the **Receive data streaming for incoming messages on the asset** checkbox if you want to receive a copy of Inbound messages. 
   1. If a flow is not configured with the selected data integration - One copy of inbound message is sent to the data stream.
   2. If a flow is configured with the selected data integration - Two copies of inbound message are sent to the Data Stream, out of which one is from the flow.
   3. If a flow is configured but not with the selected data integration - One copy of inbound message is sent to the Data Stream.
   4. Click **Submit For Approval**.

> 📘 Date Streams - Inbound and Outbound Messages, and Delivery Receipts
> 
> Please refer to the [link](https://developers.imiconnect.io/reference/data-streams) for channel specific information related to Data Streams.

> 📘 Duplicate Payloads
> 
> Possibility of Duplicate Data Stream Payloads – Data Streaming can send duplicate payloads to the same destination if it is configured at different levels. For example, if you have an asset or app, and enable Data Stream for that asset, while also selecting Data Stream in a Flow's Start, Send, or Receive node, there's a chance of receiving two payloads for the same incoming or outgoing message. One payload will be sent based on the asset-level configuration, and the second will include any additional context configured in the Flow's Start, Send, or Receive node.

### Events in Data Stream

The list of events for which the payload is streamed via Data Stream is available for configuration under the Manage Integration - Data Stream section.  
The events preconfigured by <<prodname>> Support are enabled by default for the streaming at the time of Data Stream enablement for your tenant. You are only allowed to clear the selection for an event. Please make sure you understand the impact before you clear the selection of an event, as clicking ‘Save’ will prompt the system to immediately stop the streaming of the payload to the destination for the event.

To view events under Data Stream:

1. Navigate to **Assets** > **Integrations**. 
2. Select **Data Streams** from the Integration Type drop-down.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8026ab30b20b8cb385d1102cb0546d230230b421313e2a8bf62bcd8b61b224a3-Enable_by_Default.png",
        "",
        "Data Streams Integration Type selection"
      ],
      "align": "center",
      "border": true,
      "caption": "Data Streams Integration Type selection"
    }
  ]
}
[/block]


3. Events: All the events enabled for the Data Stream will be pre-selected. The ones that are not allowed for streaming for the Data Stream are in a disabled state.