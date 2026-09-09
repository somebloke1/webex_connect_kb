[block:callout]
{
  "type": "info",
  "title": "Know Your Endpoint",
  "body": "Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "For data privacy and security reasons, the REST API is served over encrypted HTTPS. The standard HTTP is not supported."
}
[/block]

[block:textarea]
{
  "text": "\n### **Response Parameters**",
  "sidebar": true
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Status",
    "0-1": "Number",
    "0-2": "Zero indicates success response",
    "1-0": "Description",
    "1-1": "String",
    "1-2": "Describes the status of API call",
    "2-0": "Records",
    "2-1": "Array",
    "2-2": "An array of Outward links and Inward links",
    "3-0": "Record[].Attributes",
    "3-1": "Array",
    "3-2": "Outward links and Inward links",
    "4-0": "Attributes[].Name",
    "4-1": "String",
    "4-2": "Name of the column. For example, CustomerId -Column Name",
    "5-0": "Attributes[].Value",
    "5-1": "String",
    "5-2": "Value Contained with in the column Eg: CustomerId- 1234",
    "6-0": "Attributes[].ID",
    "6-1": "Number",
    "6-2": "System generated unique Id for the column",
    "7-0": "InwardLinks",
    "7-1": "Array",
    "7-2": "Shows app profiles mapped  to the Customer Id",
    "8-0": "OutwardLinks",
    "8-1": "Array",
    "8-2": "Displays customer profile information on Get app profile call",
    "9-0": "OutwardLinks[].ProfileId",
    "9-1": "Number",
    "9-2": "Unique system Generated ID  on profile store creation",
    "10-0": "OutwardLinks[].ProfileName",
    "10-1": "String",
    "10-2": "Profile store Name",
    "11-0": "OutwardLinks[].Records",
    "11-1": "Array",
    "11-2": "List of columns mapped to the profile store Eg: Customer Id,Name,Mobile No etc.",
    "12-0": "OutwardLinks[].Records[].Value",
    "12-1": "String",
    "12-2": "Value Contained with in the column Eg: CustomerId- 1234",
    "13-0": "OutwardLinks[].Records[].ID",
    "13-1": "Number",
    "13-2": "System generated unique Id for the column",
    "14-0": "OutwardLinks[].Records[].Name",
    "14-1": "String",
    "14-2": "Name of the column Eg : CustomerId -Column Name",
    "15-0": "code",
    "15-1": "String",
    "15-2": "Internal code handling by imiconnect",
    "16-0": "transid",
    "16-1": "String",
    "16-2": "Unique system generated id for API call"
  },
  "cols": 3,
  "rows": 17,
  "sidebar": true
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Response Code",
    "h-1": "Message",
    "h-2": "Description",
    "0-0": "1000",
    "0-1": "Success",
    "1-0": "7000",
    "1-1": "Invalid JSON",
    "2-0": "7001",
    "2-1": "Authentication failed",
    "3-0": "7003",
    "3-1": "Mandatory parameters missing",
    "0-2": "Returned when the request is completed successfully.",
    "1-2": "Returned when an invalid JSON request is sent.",
    "2-2": "Returned when the invalid service key or profile key is provided in the request.",
    "3-2": "Returned when the mandatory parameters configured in custom event are missing"
  },
  "cols": 3,
  "rows": 4
}
[/block]