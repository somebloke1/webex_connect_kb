> 📘 Know Your Endpoint
> 
> Based on the domain you use to log in to imiconnect, the endpoint for your API varies. See the [endpoint](https://developers.imiconnect.io/reference/endpoints) section to understand which endpoint to use for your domain.

## **Status Codes**

This API may return the following response codes:

[block:parameters]
{
  "data": {
    "h-0": "Response Code",
    "h-1": "Message",
    "h-2": "Description",
    "0-0": "1000",
    "0-1": "Success",
    "0-2": "Returned when the request is completed successfully",
    "1-0": "7600",
    "1-1": "No result found",
    "1-2": "Returned when an invalid transaction is sent.  \n  \nNote: Request  may be in queue, try once again after some time.",
    "2-0": "7001",
    "2-1": "Authentication failed",
    "2-2": "Returned when the invalid service key or profile key is provided in the request"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]