The  Event API is a single API that allows third-party/external applications to make event requests using a RESTful API over HTTPS to the <<prodname>> platform.

The external application can raise one or more events in a single request. Each event can be attached to a set of parameters representing event-specific information. These parameters will be passed along as context parameters to the actions defined in the rules on these events. 

Clients can create custom events and configure rules that are executed when the event API request is received on the <<prodname>> platform.  Events are defined in the services section by defining parameter blocks that consist of variable names and types. These will then be passed when the event is invoked.
[block:callout]
{
  "type": "info",
  "body": "A **Service Key** must be passed with every API request."
}
[/block]
**Prerequisites:**

  * A [Service Key](https://help.imiconnect.io/docs/api-settings). The Service Key is obtained by [creating a service](https://help.imiconnect.io/docs/creating-a-service).
  * An event associated with the Service.
  * At least one Rule associated with the Event.
  * Properly defined actions for the Rule in order to complete the expected flow.
[block:api-header]
{
  "type": "basic",
  "title": "API Parameters"
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "For data privacy and security reasons, the REST API is served over encrypted HTTPS. Standard HTTP is not supported.",
  "title": ""
}
[/block]

[block:parameters]
{
  "data": {
    "0-0": "key",
    "h-0": "Parameter",
    "h-1": "Mandatory",
    "h-2": "Use",
    "0-1": "Yes",
    "0-2": "Passed in the header.",
    "1-1": "Yes",
    "2-1": "No",
    "1-0": "events",
    "1-2": "Passed in the request body.",
    "2-0": "notifyurl",
    "3-0": "expiry",
    "3-2": "Passed in the request body.",
    "3-1": "No",
    "2-2": "Passed in the request body.",
    "h-3": "Description",
    "0-3": "The service key authenticates event API requests and must be passed with every request.",
    "1-3": "An array containing a list of events.",
    "2-3": "A notification is sent to the specified notifyurl after an event is executed.",
    "3-3": "Expiry time of event in UTC format."
  },
  "cols": 4,
  "rows": 4
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Response / Error Codes"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Code",
    "h-1": "Message",
    "h-2": "Description",
    "0-0": "1002",
    "1-0": "7000",
    "2-0": "7001",
    "3-0": "7003",
    "4-0": "7004",
    "5-0": "7005",
    "6-0": "7025",
    "0-1": "Queued",
    "1-1": "Invalid JSON",
    "2-1": "Authentication failed",
    "3-1": "Mandatory parameters missing",
    "4-1": "Invalid parameters/values",
    "5-1": "Internal error occurred",
    "6-1": "Mandatory custom parameters missing",
    "0-2": "Returned when the request is accepted by <<prodname>>.",
    "1-2": "Returned when an invalid JSON request is sent.",
    "2-2": "Returned when an invalid service key or profile key is provided in the request.",
    "3-2": "Returns when any mandatory parameter is missing in request body.",
    "5-2": "Returned when an internal error occurs.",
    "4-2": "Returns when any invalid value is given for any parameter in request body.",
    "6-2": "Returns when any mandatory custom event parameter is missing,  where these custom parameters are created in custom event creation screen."
  },
  "cols": 3,
  "rows": 7
}
[/block]