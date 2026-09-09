> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

## **Status Codes**

This API may return the following response codes:

| Response Code | Message                              | Description                                                                                     |
| :------------ | :----------------------------------- | :---------------------------------------------------------------------------------------------- |
| 1000          | Queued                               | Returned when the request is queued.                                                            |
| 7000          | invalid JSON                         | Returned when an invalid JSON request is sent.                                                  |
| 7001          | Authentication failed                | Returned when an invalid service key or profile key is provided in the request.                 |
| 7002          | Service Key Missing                  | Returned when the parameter _key_ is missing in the message request.                            |
| 7003          | Mandatory parameters missing         | [API Response Codes](http://docs.imiconnect.com/docs/response-codes#section-7003)               |
| 7006          | Internal error occurred              | Returned when an internal error occurs in imiconnect.                                           |
| 7010          | Source IP is not in the allowed list | Returned when a request is sent from an IP that is not in the allowed list in <<prodname>>.     |
| 7011          | Invalid Attribute Value              | Returned when an invalid value is provided for the customer or app profile _Attributes_ object. |
| 7012          | Batch size limit(100) exceeded       | Returned when an API request exceeds the limit to create or update or delete using profile API. |
| 7015          | customer already exists              | Returned when a customer or app profile already exists.                                         |