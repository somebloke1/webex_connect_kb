# What's a Service

Source: https://help.webexconnect.io/docs/service-introduction
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:50+00:00

A service is a named workspace for managing all necessary configurations and components required to automate a specific customer interaction use case/customer journey. 

As a best practice, we recommend you to use a separate service for each customer interaction use case. Doing so allows you to segregate flows, rules and API credentials associated with each use case and view statistics for that use case.

Every service has a unique service key and JWT tokens that can be used to authenticate and authorize external triggers for invoking [Messaging APIs](https://developers.imiconnect.io/reference#external-event), [Custom Event API](https://developers.imiconnect.io/reference#messagesv2), and [Inbound Webhooks](https://help.webexconnect.io/docs/inbound-webhooks).

Within a service, you can:

- [Create and manage flows](https://help.webexconnect.io/docs/flows-introduction)
- [Create and manage rules](https://help.webexconnect.io/docs/rules) 
- [View, copy or regenerate Service Key and/or JWT tokens needed for invoking various APIs](https://help.webexconnect.io/docs/service-key-and-jwt-authentication-tokens)	

The following stats are available on the Services screen for each live service:

- Total Requests
- Flows Executed
- Delivery Rate

There is no upper limit on the number of services you can create within an Webex Connect account.



![Services Dashboard](https://files.readme.io/11ce165-2.jpg)




## NGMP Services

NGMP services added through the Admin console appear as services in the dashboard. These services are not editable/clickable. 

> 📘 NGMP Service
> 
> An NGMP service can only be created by the admin from the Admin Console and the data is accessible only through reports.