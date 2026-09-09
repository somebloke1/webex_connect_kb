# Inbound Webhooks

Source: https://help.webexconnect.io/docs/inbound-webhooks
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:06+00:00

Inbound Webhooks generate a unique endpoint that can be embedded into your applications to notify Webex Connect of events occurring on business systems.

In essence, they work the same way as custom events but are flexible with the input JSON/XML body that will be parsed as JPath/Xpath and the variables will be made available in flows/rules.

We have additional support for signatures within headers of inbound webhooks that trigger flows. This is in addition to the already existing authentication using a service key or JWT tokens in the header and will remain optional while setting up your inbound webhooks. It will add an additional layer of security to your inbound webhook requests and help prevent man-in-the-middle type attacks.

> 📘 Authentication
> 
> It is not mandatory to use authentication when using inbound webhooks, however, we recommend you to select the authentication option as a security best practice. We support two types of authentication for inbound webhooks: 
> 
> a. Service Key based
> 
> b. JWT based authentication. When authentication is enabled you need to use one of service key or JWT credentials associated with the relevant Webex Connect service which contains the rule/flow you've associated the inbound webhook with.

## Trigger Conditions for Inbound Webhook

Different conditions on variables can be set using the AND/OR operators. When AND is part of the condition, that part of the condition must be true to qualify the condition. When OR is used, the statement is executed if any one of the conditions qualifies.



![Inbound Webhook with a trigger condition to invoke the flow](https://files.readme.io/bdc8fba23a7b2007ec2008277bca8190472035f0af9c782440624de71d313b76-05_31_19.jpg)




One of the several conditional operators that can be used to set conditions are listed below:

- Equals
- Not equals
- In
- Contains
- Not in
- Equals ignore-case
- Starts with
- Ends with
- Regex
- Contains ignore-case

More information on Inbound Webhooks is available in our [API documentation](https://developers.imiconnect.io/reference#external-event)

> 📘 Note
> 
> Starting from the v6.3.0 release, there is a limit for the payload size for the inbound webhooks. Whenever the inbound webhook requests contain payloads of size higher than the limit configured at the tenant level, the request is rejected with an error code - 430. The default size limit configured for the tenant is 256 KB. Reach out to your system administrator to increase the limit.