On the Integrations tab, you can monitor the performance of the different types of integrations. You can also see and analyse the reasons of integration failures.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/68625531b12a46bc1232f9e00dd20a683d1beea601eee0362bfb9a7da7481a6c-WatchTowere_1.jpg",
        "",
        "Screenahot of Integrations Dashboard"
      ],
      "align": "center",
      "border": true,
      "caption": "Integration Dashboard"
    }
  ]
}
[/block]


### Integration Overview

This section displays the overview of all the errors or failed transactions for different integrations types such as Outbound Webhooks, Pre-built Integration, Custom Node, Custom Event, and Inbound Webhooks.  The donut chart displays the number of failures or errors for each type of integration. You can click the integration type to show or hide the failure or errors of that integration type in the chart.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8c16b906184ee5c56b1ee43d532c41488df39fe29b1be10b75f32e70da0095ea-Watchtower2.jpg",
        "",
        "Screenshot of Integrations Overview"
      ],
      "align": "center",
      "sizing": "80% ",
      "border": true,
      "caption": "Integrations Overview"
    }
  ]
}
[/block]


## Total Count and Percentage Change

The numbers next to integration and the arrows next to integration counts display the number of failed or successful transactions along with their percentage changes for the integration. The percentage change denotes the increase or decrease in the number of failed or successful transactions with respect to the previous period. For example, if you select to show the data for 1 day, the percentage change is calculated by comparing the data with the previous day.

<CustomTimePeriodDataRetention />

<br />

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f26ef8215964560a4e14136739e09e341851c0a9696e9a4d458efa3cb70f7bf0-2025-03-27_13-26-53.jpg",
        "",
        "Screenshot of Percentage Change for Integrations"
      ],
      "align": "center",
      "sizing": "500px",
      "border": true,
      "caption": "Percentage Change for Integrations"
    }
  ]
}
[/block]


## Counts of Integration Executions and Failures

This section shows the total and failed integration executions for each integration type, along with a comparison to the previous period. For example, the Outbound Webhook was executed 7.58k times in the selected period, with 7.20k failures. Execution of the Outbound Webhook decreased by 9% compared to the previous period, and failures decreased by 11%. For more details on the types of failures, description, and service wise counts please refer to the 'Failures in Integration' section.

The default time frame for viewing the dashboard is the last day, or "Yesterday." You can choose a different period, with a maximum limit of the past 30 days.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4f89dfe96540eeced86cbb1974c0ddc1cd70505540cf9f87a6249017b71e4c27-2025-03-27_13-38-59.jpg",
        "",
        "Screenshot showing Counts of Integration Executions and Failur"
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Counts of Integration Executions and Failures"
    }
  ]
}
[/block]


## Trends

This section shows the error trends for each integration type for the selected period. By default, the graph is shown for all the integration types with the period as yesterday. You can select individual integration types from the dropdown to see the graph for that integration type or you can click the integration type (Inbound Webhooks, Outbound Webhooks, etc) to show or hide the failure or errors of that integration type in the graph.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5d4f050b81dd24ec63797ab80a9090cf94283ebf7cf5ed1511fe21e1b5cf4587-2025-03-27_13-42-16.jpg",
        "",
        "Screenshot of Trends for the Integrations"
      ],
      "align": "center",
      "border": true,
      "caption": "Trends for the Integrations"
    }
  ]
}
[/block]


## Failures in Integrations

This section shows the details of the errors that occurred in the integrations at flow and service levels.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0d282f05deae1f9f4475a30fd133c03cdc290f3c3f0453cc78376d604f38eb21-2025-03-27_13-44-28.jpg",
        "",
        "Screenshot of Failures in Integrations"
      ],
      "align": "center",
      "border": true,
      "caption": "Failures in Integrations"
    }
  ]
}
[/block]


Following information is displayed in this section:

| Name                | Description                                        |
| :------------------ | :------------------------------------------------- |
| Integration Type    | Type of the integration.                           |
| Integration Name    | Name of the integration.                           |
| Failure description | Reason with which the failure has occurred.        |
| Services            | Name of the service in which the failure occurred. |
| Flows               | Name of the flow in which the service is present.  |
| Total errors        | Total number of errors occurred.                   |
| Actions             | Click the icon to view the failure details.        |

When you click the icon under Actions for a failure, the Failure Details screen is displayed with the same information as above. The Failure Details screen lets you directly go to the integration and service in which the failure occurred.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/85455e6fa44969c7106df9f9405dd5421708c57aea033e9ff75d03075bf09fc0-2025-03-27_13-50-36.jpg",
        "",
        "Screenshot of Failure Details for the Integration type"
      ],
      "align": "center",
      "sizing": "500px",
      "border": true,
      "caption": "Failure Details for the Integration type"
    }
  ]
}
[/block]


### Common Errors for Various Integrations

The following table explains the different scenarios when errors for various integrations occur. 

[block:parameters]
{
  "data": {
    "h-0": "Error",
    "h-1": "Description",
    "h-2": "Inbound Webhooks",
    "h-3": "Outbound Webhooks",
    "h-4": "Custom Nodes",
    "h-5": "Pre-built Integrations",
    "h-6": "Custom Events",
    "0-0": "308",
    "0-1": "Permanent Redirect",
    "0-2": "Not applicable",
    "0-3": "This is a <<prodname>> related issue. Please reach out to your account manager or the operations team to resolve the issue.",
    "0-4": "The resolution of the issue depends on the API provider. Please contact the API providers for assistance.",
    "0-5": "The resolution of the issue depends on the API / Prebuilt integration provider. Please contact the API  / Prebuilt integration for assistance.",
    "0-6": "Not applicable.",
    "1-0": "400",
    "1-1": "Bad Request",
    "1-2": "Kindly review your Inbound Webhook request to confirm that the request header, body, and API endpoint are correct. For detailed guidance on making a proper request, please refer to the Inbound Webhook [doc](https://help.webexconnect.io/docs/inbound-webhooks).",
    "1-3": "This is a <<prodname>> related issue. Please reach out to the account manager or operations team to resolve the issue.",
    "1-4": "Kindly review your custom node configuration to verify that the API endpoint, request header, and body are correct. The resolution will depend on the API provider.",
    "1-5": "Kindly review your Prebuilt node configuration to verify that the API endpoint, request header, and body are correct or reach out to the integration provider for resolution of the issue.",
    "1-6": "Kindly review your Inbound Webhook request to confirm that the request header, body, and API endpoint are correct. For detailed guidance on making a proper request, please refer to the Inbound Webhook [doc](https://help.webexconnect.io/docs/custom-events).",
    "2-0": "401",
    "2-1": "Unauthorized",
    "2-2": "This issue generally occurs when the Service key or JWT is empty or not attached correctly in the Inbound webhook request. For detailed guidance on making a proper request, please refer to the Inbound Webhook [doc](https://help.webexconnect.io/docs/inbound-webhooks) .",
    "2-3": "The issue occurs If the selected authorization in the Outbound Webhooks is incorrect or expired, you can fix this error by going to the Authorization tab under Assets > Integrations. Choose the appropriate authorization, verify the credentials, and re-authorize it.",
    "2-4": "This issue occurs when the selected Authorization in the Custom Node is incorrect or expired, you can resolve this error by navigating to the Custom Node in Assets > Integrations. Select the required authorization in the custom node, check the credentials, and re-authorize it.",
    "2-5": "If the selected Authorization in the Pre-built Integration is incorrect or expired, it displays as Auth Pending or re-authorize in the status. You can resolve this error by navigating to the Pre-built Integrations in Assets > Integrations. Check the credentials and re-authorize it.",
    "2-6": "If the Service key or JWT auth is empty or not attached, you will see the error. To resolve this error, you must add the authentication as a request body.",
    "3-0": "403",
    "3-1": "Forbidden",
    "3-2": "Not applicable.",
    "3-3": "Please reach out to the account manager or operations team to resolve the issue.",
    "3-4": "The error is dependent on the API provider. Generally, this happens if the scope or access is not provided for the API request.",
    "3-5": "The error is dependent on the API provider when the API request's scope or access is not provided.",
    "3-6": "Not applicable.",
    "4-0": "404",
    "4-1": "Not Found",
    "4-2": "If the Inbound webhook is deleted.",
    "4-3": "If the endpoint URL in the Outbound webhook is deleted or does not exist.",
    "4-4": "The error is dependent on the API provider. When a user attempts to access a webpage that does not exist, has been moved, or has a dead or broken link, the response from the API provider can vary.",
    "4-5": "The error is dependent on the API provider. when a user attempts to access a webpage that does not exist, has been moved, or has a dead or broken link, the response from the API provider can vary.",
    "4-6": "If the custom event is deleted.",
    "5-0": "405",
    "5-1": "Method Not Allowed",
    "5-2": "The HTTP request protocol is incorrect. Please use HTTP\\:[POST] protocol.",
    "5-3": "Reach out to account manager or operations team to resolve the issue.",
    "5-4": "The error is dependent on whatever endpoint you configured with  respective HTTP method is not allowed by the API provider, please follow the API provider documentation for the proper method (GET/POST/..) and check if the URL configured is correct.",
    "5-5": "The error is dependent on whatever endpoint you configured with respective HTTP method is not allowed by the API provider, please follow the API provider documentation for the proper method (GET/POST/..) and check if the URL configured is correct.",
    "5-6": "The HTTP request protocol is incorrect. Please use HTTP\\:[POST] protocol.",
    "6-0": "406",
    "6-1": "Not Acceptable",
    "6-2": "Not applicable",
    "6-3": "Not applicable",
    "6-4": "The error is dependent on the API provider. This generally happens when the API server is not able to fulfill the request.",
    "6-5": "The error is dependent on API provider. This generally happens when API server is not able to fulfill the request. If your integration is offered by Partner, please reach out to Partner.",
    "6-6": "Not applicable",
    "7-0": "408",
    "7-1": "Request Timeout",
    "7-2": "Try increasing the request timeout of the HTTP request. It is configured in the header. Then, try again.",
    "7-3": "Generally, this happens when the endpoint configured is not responding within X seconds.",
    "7-4": "Try increasing the request timeout of the HTTP request. It is configured in the header. Then, try again.",
    "7-5": "The error is dependent on API provider. This generally happens when the API server is not able to fulfill the request. If your integration is offered by Partner, please reach out to Partner.",
    "7-6": "Try increasing the request timeout of the HTTP request. It is configured in the header. Then, try again.",
    "8-0": "409",
    "8-1": "Conflict",
    "8-2": "Not applicable",
    "8-3": "Not applicable",
    "8-4": "The error is dependent on API provider,  we recommend you retry the request if you receive the error.",
    "8-5": "The resolution of the output depends on API provider. We recommend retrying the request if you receive the error.",
    "8-6": "Not applicable",
    "9-0": "413",
    "9-1": "Content Too Large",
    "9-2": "The error is received when the Payload size is bigger than the payload size that is allowed for your tenant. ",
    "9-3": "Please reach out to your account manager or operations team to resolve the issue.",
    "9-4": "The error \"Content too large\" occurs when the payload size exceeds the allowed limit of the API provider. We recommend you check the API provider documentation for maximum payload size and take appropriate action to reduce the payload.",
    "9-5": "The error is received when the Payload size is bigger than the payload size that is allowed for your tenant.",
    "9-6": "The error is received when the Payload size is bigger than the payload size that is allowed for your tenant.",
    "10-0": "429",
    "10-1": "Too Many Requests",
    "10-2": "The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the TPS limit or reduce the number of request per second.",
    "10-3": "Reach out to account manager or operations team to resolve the issue.",
    "10-4": "The number of requests that you are sending to the API provider is getting rejected because, the API provider is allowing only limited number of requests per second. To check the exact number of requests refer to the API provider documentation.",
    "10-5": "The number of requests that you are sending to the API provider is getting rejected because, the API provider is allowing only limited number of requests per second. To check the exact number of requests refer to the API provider documentation.",
    "10-6": "The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the limit or reduce the number of request per second.",
    "11-0": "500",
    "11-1": "Internal Server Error",
    "11-2": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "11-3": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "11-4": "The API provider servers is not able to fullfill your request.",
    "11-5": "The error is dependent on API provider. This generally happens when API server is not able to fulfill the request. If your integration is offered by Partner, please reach out to Partner.",
    "11-6": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "12-0": "502",
    "12-1": "Bad Gateway",
    "12-2": "Server is not responding. Please retry after some time.  \nReach out to operations team for assistance.",
    "12-3": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "12-4": "The API end point server is not able to fulfill the request, please check with the API provider.",
    "12-5": "The API end point server is not able to fulfill the request, please check with the API provider. If your integration is offered by Partner, please reach out to Partner",
    "12-6": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "13-0": "503",
    "13-1": "Service Unavailable",
    "13-2": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "13-3": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "13-4": "Internal server errors can occur due to server issues. We recommend that you retry. Please reach out to API provider.",
    "13-5": "Internal server errors can occur due to server issues. We recommend you to retry. Please reach out to Partner.",
    "13-6": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "14-0": "504",
    "14-1": "Gateway Timeout",
    "14-2": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "14-3": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "14-4": "Internal server errors can occur due to server issues. We recommend that you retry. Please reach out to API provider.",
    "14-5": "Internal server errors can occur due to server issues. We recommend you to retry. Please reach out to Partner.",
    "14-6": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "15-0": "521",
    "15-1": "Web server is down",
    "15-2": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "15-3": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "15-4": "It is a connection time-out error that indicates the website is experiencing a server-side problem. It is a common error that affects Cloudflare-enabled websites. This error occurs when the origin server rejects Cloudflare's connection request. It will not occur for all connection timeout cases. It depends on the provider whether they are giving this status or simply rejecting the request.",
    "15-5": "",
    "15-6": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "16-0": "523",
    "16-1": "Origin is unreachable",
    "16-2": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "16-3": "Internal server is possible because of the server errors. We recommend you to retry.  Please reach out to operations team.",
    "16-4": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "16-5": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "16-6": "Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance.",
    "17-0": "804",
    "17-1": "Problem while processing action",
    "17-2": "For the incoming event, the application is unable to process it.",
    "17-3": "Not applicable.",
    "17-4": "Dependent on API provider.",
    "17-5": "Dependent on API provider.",
    "17-6": "For the incoming event, the application is unable to process it.",
    "18-0": "811",
    "18-1": "Action submission failed",
    "18-2": "For the incoming event, the application is unable to process it.",
    "18-3": "Not applicable.",
    "18-4": "Dependent on API provider",
    "18-5": "Dependent on API provider",
    "18-6": "For the incoming event, the application is unable to process it.",
    "19-0": "816",
    "19-1": "User profile not found",
    "19-2": "For an incoming event, the corresponding action is not executed because the user profile cannot be found.",
    "19-3": "Not applicable.",
    "19-4": "Dependent on API provider.",
    "19-5": "Dependent on API provider.",
    "19-6": "For an incoming event, the corresponding action is not executed because the user profile cannot be found.",
    "20-0": "844",
    "20-1": "User has not verified his profile",
    "20-2": "For an incoming event, the corresponding action is not executed because the user profile cannot be found.",
    "20-3": "Not applicable.",
    "20-4": "Dependent on API provider.",
    "20-5": "Dependent on API provider.",
    "20-6": "For an incoming event, the corresponding action is not executed because the user profile cannot be found.",
    "21-0": "852",
    "21-1": "Not able to resolve action params to fulfill action",
    "21-2": "For the incoming event, the application is unable to process it.",
    "21-3": "Not applicable.",
    "21-4": "Dependent on API provider.",
    "21-5": "Dependent on API provider.",
    "21-6": "For the incoming event, the application is unable to process it.",
    "22-0": "882",
    "22-1": "TPS rate exceeded",
    "22-2": "The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the TPS limit or reduce the number of request per second.",
    "22-3": "Not applicable.",
    "22-4": "Dependent on API provider.",
    "22-5": "Dependent on API provider.",
    "22-6": "The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the TPS limit or reduce the number of request per second.",
    "23-0": "883",
    "23-1": "TPS quota exceeded",
    "23-2": "The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the quota or reduce the number of requests.",
    "23-3": "Not applicable.",
    "23-4": "Dependent on API provider.",
    "23-5": "Dependent on API provider.",
    "23-6": "The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the quota or reduce the number of requests.",
    "24-0": "884",
    "24-1": "Contact policy not enabled",
    "24-2": "Please reach out to your account manager to enable the Contact Policy feature.",
    "24-3": "Not applicable.",
    "24-4": "Dependent on API provider.",
    "24-5": "Dependent on API provider.",
    "24-6": "Please reach out to your account manager to enable the Contact Policy feature."
  },
  "cols": 7,
  "rows": 25,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]