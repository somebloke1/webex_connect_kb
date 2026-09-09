**For Segment**: 

The following is the error code displayed when the Segment messaging is disabled for your tenant.
[block:code]
{
  "codes": [
    {
      "code": "{\n\n  \"code\": 70,\n\n  \"description\": \"Segment based messaging feature is not available for your tenant\"\n\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "To enable the Segment messaging for your tenant, contact your account manager.",
  "title": "Note"
}
[/block]
[block:callout]
{
  "type": "info",
  "title": "Know Your Endpoint",
  "body": "Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain."
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "If the segment is without criteria and there are existing users in that segment, then the segment cannot be deleted.",
  "title": "Note"
}
[/block]