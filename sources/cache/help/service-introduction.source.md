A service is a named workspace for managing all necessary configurations and components required to automate a specific customer interaction use case/customer journey. 

As a best practice, we recommend you to use a separate service for each customer interaction use case. Doing so allows you to segregate flows, rules and API credentials associated with each use case and view statistics for that use case.

Every service has a unique service key and JWT tokens that can be used to authenticate and authorize external triggers for invoking [Messaging APIs](https://developers.imiconnect.io/reference#external-event), [Custom Event API](https://developers.imiconnect.io/reference#messagesv2), and [Inbound Webhooks](doc:inbound-webhooks).

Within a service, you can:

- [Create and manage flows](doc:flows)
- [Create and manage rules](doc:rules) 
- [View, copy or regenerate Service Key and/or JWT tokens needed for invoking various APIs](doc:api-settings)	

The following stats are available on the Services screen for each live service:

- Total Requests
- Flows Executed
- Delivery Rate

There is no upper limit on the number of services you can create within an <<prodname>> account.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/11ce165-2.jpg",
        "services_dashboard.png",
        "Services Dashboard"
      ],
      "align": "center",
      "border": true,
      "caption": "Services Dashboard"
    }
  ]
}
[/block]


## NGMP Services

NGMP services added through the Admin console appear as services in the dashboard. These services are not editable/clickable. 

> 📘 NGMP Service
> 
> An NGMP service can only be created by the admin from the Admin Console and the data is accessible only through reports.