> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

[block:textarea]
{
  "text": "### **Response Parameters**",
  "sidebar": true
}
[/block]


| Parameter            | Type   | Description                                                   |
| :------------------- | :----- | :------------------------------------------------------------ |
| Status               | Number | Zero indicates success response                               |
| Description          | String | Describes the status of the API call                          |
| Records              | Array  | An array of Outward links and Inward links                    |
| Record\[].Attributes | Array  | Outward links and Inward links                                |
| Attributes\[].Name   | String | Name of the column. For example, CustomerId -Column Name      |
| Attributes\[].Value  | String | Value Contained with in the column Eg: CustomerId- 1234       |
| Attributes\[].ID     | Number | System generated unique Id for the column                     |
| InwardLinks          | Array  | Shows app profiles mapped  to the Customer Id                 |
| OutwardLinks         | Array  | Displays customer profile information on Get app profile call |
| code                 | String | Internal code handling by imiconnect                          |
| transid              | String | Unique system generated id for API call                       |

## **Status Codes**

This API may return the following response codes:

| Response Code | Message                      | Description                                                                     |
| :------------ | :--------------------------- | :------------------------------------------------------------------------------ |
| 1000          | Success                      | Returned when the request is completed successfully                             |
| 7000          | Invalid JSON                 | Returned when an invalid JSON request is sent                                   |
| 7001          | Authentication failed        | Returned when the invalid service key or profile key is provided in the request |
| 7003          | Mandatory parameters missing | Returned when the mandatory parameters configured in custom event are missing   |