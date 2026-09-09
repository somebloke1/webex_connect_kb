> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

> 📘 
> 
> Profile details are encapsulated within the Attributes section. Additional key-value pairs may be added as required.

## **Status Codes**

This API may return the following response codes:

| Response Code | Message                                                         | Description                                                                                    |
| :------------ | :-------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| 1000          | Queued                                                          | Returned when the request is queued                                                            |
| 1002          | Partial success                                                 | Returned when at least one app profile could not be created successfully                       |
| 7000          | Invalid JSON                                                    | Returned when an invalid JSON request is sent                                                  |
| 7001          | Authentication failed                                           | Returned when the invalid service key or profile key is provided in the request                |
| 7002          | Service Key Missing                                             | Returned when the parameter _key_ is missing in the message request                            |
| 7003          | Mandatory parameters missing                                    | Returned when the mandatory parameters configured in the custom event are missing              |
| 7006          | Internal error occurred                                         | Returned when an internal error occurs                                                         |
| 7010          | Source IP is not in the allowed list                            | Returned when a request is sent from an IP that is not in the allowed list in <<prodname>>     |
| 7011          | Invalid Attribute Value                                         | Returned when an invalid value is provided for the customer or app profile _Attributes_ object |
| 7018          | invalid app profile or app profile is not linked to this client | Returned when an application master profile does not exists                                    |