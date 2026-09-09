> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

> 🚧 Cautionary Notice
> 
> Once a customer profile is deleted, it cannot be recovered. However, a new customer profile can be created with the same customer id.<br>  
> This process is irreversible.

> 📘 
> 
> For data privacy and security reasons, the REST API is served over encrypted HTTPS. Standard HTTP is not supported.

## **Status Codes**

The following are the response codes this method may return:

| Response Code | Message                         | Description                                                                                |
| :------------ | :------------------------------ | :----------------------------------------------------------------------------------------- |
| 1000          | Queued                          | Returned when the request is queued                                                        |
| 7001          | Authentication failed           | Returned when an invalid service key or profile key is provided in the request             |
| 7002          | Service Key Missing             | Returned when the parameter key is missing in the message request                          |
| 7003          | Mandatory parameters missing    | Returned when the mandatory parameters configured in custom event are missing              |
| 7203          | Customer not found              | Returned when the customer is  not found                                                   |
| 7208          | Source IP is not allowed listed | Returned when a request is sent from an IP that is not in the allowed list in <<prodname>> |