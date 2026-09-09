# Integrations

Source: https://help.webexconnect.io/docs/integrations
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:59+00:00

On the Integrations tab, you can monitor the performance of the different types of integrations. You can also see and analyse the reasons of integration failures.



![Integration Dashboard](https://files.readme.io/68625531b12a46bc1232f9e00dd20a683d1beea601eee0362bfb9a7da7481a6c-WatchTowere_1.jpg)




### Integration Overview

This section displays the overview of all the errors or failed transactions for different integrations types such as Outbound Webhooks, Pre-built Integration, Custom Node, Custom Event, and Inbound Webhooks.  The donut chart displays the number of failures or errors for each type of integration. You can click the integration type to show or hide the failure or errors of that integration type in the chart.



![Integrations Overview](https://files.readme.io/8c16b906184ee5c56b1ee43d532c41488df39fe29b1be10b75f32e70da0095ea-Watchtower2.jpg)




## Total Count and Percentage Change

The numbers next to integration and the arrows next to integration counts display the number of failed or successful transactions along with their percentage changes for the integration. The percentage change denotes the increase or decrease in the number of failed or successful transactions with respect to the previous period. For example, if you select to show the data for 1 day, the percentage change is calculated by comparing the data with the previous day.

<CustomTimePeriodDataRetention />

<br />



![Percentage Change for Integrations](https://files.readme.io/f26ef8215964560a4e14136739e09e341851c0a9696e9a4d458efa3cb70f7bf0-2025-03-27_13-26-53.jpg)




## Counts of Integration Executions and Failures

This section shows the total and failed integration executions for each integration type, along with a comparison to the previous period. For example, the Outbound Webhook was executed 7.58k times in the selected period, with 7.20k failures. Execution of the Outbound Webhook decreased by 9% compared to the previous period, and failures decreased by 11%. For more details on the types of failures, description, and service wise counts please refer to the 'Failures in Integration' section.

The default time frame for viewing the dashboard is the last day, or "Yesterday." You can choose a different period, with a maximum limit of the past 30 days.



![Counts of Integration Executions and Failures](https://files.readme.io/4f89dfe96540eeced86cbb1974c0ddc1cd70505540cf9f87a6249017b71e4c27-2025-03-27_13-38-59.jpg)




## Trends

This section shows the error trends for each integration type for the selected period. By default, the graph is shown for all the integration types with the period as yesterday. You can select individual integration types from the dropdown to see the graph for that integration type or you can click the integration type (Inbound Webhooks, Outbound Webhooks, etc) to show or hide the failure or errors of that integration type in the graph.



![Trends for the Integrations](https://files.readme.io/5d4f050b81dd24ec63797ab80a9090cf94283ebf7cf5ed1511fe21e1b5cf4587-2025-03-27_13-42-16.jpg)




## Failures in Integrations

This section shows the details of the errors that occurred in the integrations at flow and service levels.



![Failures in Integrations](https://files.readme.io/0d282f05deae1f9f4475a30fd133c03cdc290f3c3f0453cc78376d604f38eb21-2025-03-27_13-44-28.jpg)




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



![Failure Details for the Integration type](https://files.readme.io/85455e6fa44969c7106df9f9405dd5421708c57aea033e9ff75d03075bf09fc0-2025-03-27_13-50-36.jpg)




### Common Errors for Various Integrations

The following table explains the different scenarios when errors for various integrations occur. 



| Error | Description | Inbound Webhooks | Outbound Webhooks | Custom Nodes | Pre-built Integrations | Custom Events |
| --- | --- | --- | --- | --- | --- | --- |
| 308 | Permanent Redirect | Not applicable | This is a Webex Connect related issue. Please reach out to your account manager or the operations team to resolve the issue. | The resolution of the issue depends on the API provider. Please contact the API providers for assistance. | The resolution of the issue depends on the API / Prebuilt integration provider. Please contact the API  / Prebuilt integration for assistance. | Not applicable. |
| 400 | Bad Request | Kindly review your Inbound Webhook request to confirm that the request header, body, and API endpoint are correct. For detailed guidance on making a proper request, please refer to the Inbound Webhook [doc](https://help.webexconnect.io/docs/inbound-webhooks). | This is a Webex Connect related issue. Please reach out to the account manager or operations team to resolve the issue. | Kindly review your custom node configuration to verify that the API endpoint, request header, and body are correct. The resolution will depend on the API provider. | Kindly review your Prebuilt node configuration to verify that the API endpoint, request header, and body are correct or reach out to the integration provider for resolution of the issue. | Kindly review your Inbound Webhook request to confirm that the request header, body, and API endpoint are correct. For detailed guidance on making a proper request, please refer to the Inbound Webhook [doc](https://help.webexconnect.io/docs/custom-events). |
| 401 | Unauthorized | This issue generally occurs when the Service key or JWT is empty or not attached correctly in the Inbound webhook request. For detailed guidance on making a proper request, please refer to the Inbound Webhook [doc](https://help.webexconnect.io/docs/inbound-webhooks) . | The issue occurs If the selected authorization in the Outbound Webhooks is incorrect or expired, you can fix this error by going to the Authorization tab under Assets > Integrations. Choose the appropriate authorization, verify the credentials, and re-authorize it. | This issue occurs when the selected Authorization in the Custom Node is incorrect or expired, you can resolve this error by navigating to the Custom Node in Assets > Integrations. Select the required authorization in the custom node, check the credentials, and re-authorize it. | If the selected Authorization in the Pre-built Integration is incorrect or expired, it displays as Auth Pending or re-authorize in the status. You can resolve this error by navigating to the Pre-built Integrations in Assets > Integrations. Check the credentials and re-authorize it. | If the Service key or JWT auth is empty or not attached, you will see the error. To resolve this error, you must add the authentication as a request body. |
| 403 | Forbidden | Not applicable. | Please reach out to the account manager or operations team to resolve the issue. | The error is dependent on the API provider. Generally, this happens if the scope or access is not provided for the API request. | The error is dependent on the API provider when the API request's scope or access is not provided. | Not applicable. |
| 404 | Not Found | If the Inbound webhook is deleted. | If the endpoint URL in the Outbound webhook is deleted or does not exist. | The error is dependent on the API provider. When a user attempts to access a webpage that does not exist, has been moved, or has a dead or broken link, the response from the API provider can vary. | The error is dependent on the API provider. when a user attempts to access a webpage that does not exist, has been moved, or has a dead or broken link, the response from the API provider can vary. | If the custom event is deleted. |
| 405 | Method Not Allowed | The HTTP request protocol is incorrect. Please use HTTP\:[POST] protocol. | Reach out to account manager or operations team to resolve the issue. | The error is dependent on whatever endpoint you configured with  respective HTTP method is not allowed by the API provider, please follow the API provider documentation for the proper method (GET/POST/..) and check if the URL configured is correct. | The error is dependent on whatever endpoint you configured with respective HTTP method is not allowed by the API provider, please follow the API provider documentation for the proper method (GET/POST/..) and check if the URL configured is correct. | The HTTP request protocol is incorrect. Please use HTTP\:[POST] protocol. |
| 406 | Not Acceptable | Not applicable | Not applicable | The error is dependent on the API provider. This generally happens when the API server is not able to fulfill the request. | The error is dependent on API provider. This generally happens when API server is not able to fulfill the request. If your integration is offered by Partner, please reach out to Partner. | Not applicable |
| 408 | Request Timeout | Try increasing the request timeout of the HTTP request. It is configured in the header. Then, try again. | Generally, this happens when the endpoint configured is not responding within X seconds. | Try increasing the request timeout of the HTTP request. It is configured in the header. Then, try again. | The error is dependent on API provider. This generally happens when the API server is not able to fulfill the request. If your integration is offered by Partner, please reach out to Partner. | Try increasing the request timeout of the HTTP request. It is configured in the header. Then, try again. |
| 409 | Conflict | Not applicable | Not applicable | The error is dependent on API provider,  we recommend you retry the request if you receive the error. | The resolution of the output depends on API provider. We recommend retrying the request if you receive the error. | Not applicable |
| 413 | Content Too Large | The error is received when the Payload size is bigger than the payload size that is allowed for your tenant.  | Please reach out to your account manager or operations team to resolve the issue. | The error "Content too large" occurs when the payload size exceeds the allowed limit of the API provider. We recommend you check the API provider documentation for maximum payload size and take appropriate action to reduce the payload. | The error is received when the Payload size is bigger than the payload size that is allowed for your tenant. | The error is received when the Payload size is bigger than the payload size that is allowed for your tenant. |
| 429 | Too Many Requests | The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the TPS limit or reduce the number of request per second. | Reach out to account manager or operations team to resolve the issue. | The number of requests that you are sending to the API provider is getting rejected because, the API provider is allowing only limited number of requests per second. To check the exact number of requests refer to the API provider documentation. | The number of requests that you are sending to the API provider is getting rejected because, the API provider is allowing only limited number of requests per second. To check the exact number of requests refer to the API provider documentation. | The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the limit or reduce the number of request per second. |
| 500 | Internal Server Error | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | The API provider servers is not able to fullfill your request. | The error is dependent on API provider. This generally happens when API server is not able to fulfill the request. If your integration is offered by Partner, please reach out to Partner. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. |
| 502 | Bad Gateway | Server is not responding. Please retry after some time.  <br>Reach out to operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | The API end point server is not able to fulfill the request, please check with the API provider. | The API end point server is not able to fulfill the request, please check with the API provider. If your integration is offered by Partner, please reach out to Partner | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. |
| 503 | Service Unavailable | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please reach out to API provider. | Internal server errors can occur due to server issues. We recommend you to retry. Please reach out to Partner. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. |
| 504 | Gateway Timeout | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please reach out to API provider. | Internal server errors can occur due to server issues. We recommend you to retry. Please reach out to Partner. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. |
| 521 | Web server is down | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | It is a connection time-out error that indicates the website is experiencing a server-side problem. It is a common error that affects Cloudflare-enabled websites. This error occurs when the origin server rejects Cloudflare's connection request. It will not occur for all connection timeout cases. It depends on the provider whether they are giving this status or simply rejecting the request. |  | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. |
| 523 | Origin is unreachable | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server is possible because of the server errors. We recommend you to retry.  Please reach out to operations team. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. | Internal server errors can occur due to server issues. We recommend that you retry. Please contact the operations team for assistance. |
| 804 | Problem while processing action | For the incoming event, the application is unable to process it. | Not applicable. | Dependent on API provider. | Dependent on API provider. | For the incoming event, the application is unable to process it. |
| 811 | Action submission failed | For the incoming event, the application is unable to process it. | Not applicable. | Dependent on API provider | Dependent on API provider | For the incoming event, the application is unable to process it. |
| 816 | User profile not found | For an incoming event, the corresponding action is not executed because the user profile cannot be found. | Not applicable. | Dependent on API provider. | Dependent on API provider. | For an incoming event, the corresponding action is not executed because the user profile cannot be found. |
| 844 | User has not verified his profile | For an incoming event, the corresponding action is not executed because the user profile cannot be found. | Not applicable. | Dependent on API provider. | Dependent on API provider. | For an incoming event, the corresponding action is not executed because the user profile cannot be found. |
| 852 | Not able to resolve action params to fulfill action | For the incoming event, the application is unable to process it. | Not applicable. | Dependent on API provider. | Dependent on API provider. | For the incoming event, the application is unable to process it. |
| 882 | TPS rate exceeded | The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the TPS limit or reduce the number of request per second. | Not applicable. | Dependent on API provider. | Dependent on API provider. | The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the TPS limit or reduce the number of request per second. |
| 883 | TPS quota exceeded | The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the quota or reduce the number of requests. | Not applicable. | Dependent on API provider. | Dependent on API provider. | The TPS request is greater than TPS allocated for your tenant. To resolve this error, either reach out to account manager to increase the quota or reduce the number of requests. |
| 884 | Contact policy not enabled | Please reach out to your account manager to enable the Contact Policy feature. | Not applicable. | Dependent on API provider. | Dependent on API provider. | Please reach out to your account manager to enable the Contact Policy feature. |

