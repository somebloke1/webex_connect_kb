The _HTTP Request_ node enables you to perform requests to external API services. The HTTP Request node makes an HTTP request to the specified server and processes the response.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/81eeaef-HTTP.jpg",
        "HTTP.jpg",
        "Screenshot of HTTP Request Node"
      ],
      "align": "center",
      "caption": "HTTP Request Node"
    }
  ]
}
[/block]


## Node Configuration

Drag-and-drop the HTTP Request node onto the visual flow builder and double-click it to open the configuration window. Perform the following steps to complete the configuration:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4381cb7-HTTP.jpg",
        "",
        "Screenshot of HTTP Node Configuration Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of HTTP Node Configuration Page."
    }
  ]
}
[/block]


1. Select the relevant **Method**:
   - _GET_ - use this method when you need to retrieve data from a server at the specified resource.
   - _POST_ - use this method to send data to the API server to create or update a resource.
   - _PUT_ - use this method to pass data from a server at the specified resource.
   - _PATCH_ - use this method when you need to update partial resources. For example, you can use it when you need to update only one field of the resource.
   - _DELETE_ - use this method to delete the resource at the specified URL.
2. Enter the **Endpoint URL** to which you will send the HTTP request.
   > 📘 Note
   > 
   > Query parameters in the endpoint URLs are automatically encoded following the standard HTTP URL encoding process.
   > 
   > - Example1: 
   > 
   > If the given endpoint URL is:
   > 
   > Endpoint URL: `https://api.example.com/search?Report=Sales report 2024&tag=ab&moreinfor=x y`
   > 
   > The Resulting final URL sent to the server will be:  `https://api.example.com/search?Report=Sales+report+2024&tag=ab&moreifor=x+y`
   > 
   > - Example-2
   > 
   > If the given endpoint URL is:
   > 
   > Endpoint URL: `https://api.example.com/search?name=John Doe&Address=USA%20&page=1&filter=a/b`
   > 
   > The Resulting final URL sent to the server will be:`https://api.example.com/search?name=John+Doe&Address=USA%2520&page=1&filter=a%2Fb`
   > 
   > However, URL encoding may not function correctly in certain cases. Please refer to the [Percent-encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encodingarticle) for details on which parameters are excluded from encoding if not provided in the correct format.
   > 
   > Example:  
   > If the given enpoint URL is:
   > 
   > Endpoint URL: `https://api.example.com/search?q=Sales report 2024&tag=a&b&more=x y`
   > 
   > The expected URL is: `https://api.example.com/search?q=Sales+report+2024&tag=a%26b&space=x+y`
   > 
   > But this will not be encoded as expected, "&b" from query parameter tag will be removed the resulting URL will be: `https://api.example.com/search?q=Sales+report+2024&tag=a&b&space=x+y`
3. Enter the request **Header** and its **Value**. You can add multiple headers by clicking the **Add Another Header** button.
4. Specify the request **Body**. The request body is required only for _POST_, _PUT_ and \_PATCH \_methods.
5. Provide a value for Connection Timeout in milliseconds. Starting release v5.6.3 onwards, the max. timeout configuration is 20,000 milliseconds. This is the time after which the connection to the endpoint times out. If a connection is not established within the specified time, the node proceeds to the error edge.
6. Provide a value for Request Timeout in milliseconds. Starting release v5.6.3 onwards, the max. timeout configuration is 20,000 milliseconds. This is the time after which the HTTP request timeout. If a response is not received within the specified time, the node proceeds to the onTimeout edge.
7. Enter a **Proxy Address**. The proxy address is the additional IP address to access the HTTP URL. This is optional.
8. In Output Variables, select **JSON or XML**.
9. Click **Import from Sample**. 
10. In the **Data Parser** dialog box, paste your sample and click **Parse**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6335438-HTTP3.jpg",
        "Data Parser Dialog Box 2.png",
        "Screenshot of JSON Data Parser."
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Screenshot of JSON Data Parser"
    }
  ]
}
[/block]


11. Click **Parse**.  All the values will be extracted as shown below.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a936cfe-HTTP4.jpg",
        "Data Parser Dialog Box 3.png",
        "Screenshot of Select key paths to be extracted."
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Screenshot of Select key paths to be extracted"
    }
  ]
}
[/block]


12. Select the required parameters under the **Select key paths to be extracted**. 
13. Click **Import**. All the selected parameters will populate as shown below in the selected output variables.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c40e435-HTTP5.jpg",
        "",
        "Screenshot of Output Variables"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Output Variables"
    }
  ]
}
[/block]


12. Click **Test** to test the HTTP request configuration. See the [Test the HTTP Request](#section-test-the-http-request) section.
13. Click **Save** to complete the configuration.

> 📘 Note
> 
> You can only use alphabets, numbers, underscores, hyphens, and spaces in the variable names.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0e100cb-HTTP.jpeg",
        "HTTP Node 2.png",
        "Screenshot of HTTP Request Configuration Page"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of HTTP Request Configuration Page"
    }
  ]
}
[/block]


14. Click **Save**.

15. Click **Test ** to test the HTTP request configuration. See **Test the HTTP Request** section.

16. Click **Save ** to complete the configuration.

> 👍 Looking to integrate with an API that supports OAuth 2.0 based authentication?
> 
> If you're looking for invoking an API that supports OAuth 2.0 based authentication mechanism, you can use [Custom Integration Node capability](https://help.imiconnect.io/docs/custom-nodes). Please refer this page for more info.

## Input Variables

You can see a list of all the flow variables available for this node under this pane. You can also search for a variable using the **Search** field. For more information, see the [Variable Management](https://help.imiconnect.io/docs/variable-management) section.

## Custom Variables

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. For more information, see the [Variable Management](https://help.imiconnect.io/docs/variable-management) section.

## Output Variables

You can see the data that this node generates as output variables. These [variables](https://help.imiconnect.io/docs/variable-management) are available for use in subsequent nodes. The standard output variables for this node are:

- **https.statusCode** - contains the status code of the HTTP request
- **https.statusText** - contains the status message of the request sent
- **https.responseBody** - contains the response body of the request sent
- **https.responseHeaders** - contains the response headers of the request sent.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2bdb999-HTTP2.jpg",
        "HTTP Request Node Output Variables.png",
        "Screenshot of Output Variables"
      ],
      "align": "center",
      "sizing": "250px",
      "border": true,
      "caption": "Output Variables"
    }
  ]
}
[/block]


## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.

| Node Edge       | Node Event/Outcome                                                                                                                                                       |
| :-------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success (green) | \* **onSuccess** -  the flow exits through this node when the HTTP request is successfully executed                                                                      |
| Error (red)     | \* **onError** - the flow exits through this node when the HTTP request cannot be processed due to invalid input                                                         |
|                 | **outcome onTimeout** - this is the duration after which the HTTP request times out. If no response is received within this period, the node follows the onTimeout path. |

## Test the HTTP Request

After you provide all the required parameters for configuring the HTTP Request node, test it to make sure that the configuration works.

1. Click **Test**. The Test window appears.
2. Specify the **Request Parameter** and the **Response Type**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f572a9b-HTTP1.jpg",
        "HTTP Request Node Test Window.png",
        "Screenshot of Test Window"
      ],
      "align": "center",
      "border": true,
      "caption": "Test Window"
    }
  ]
}
[/block]


3. Click the **Test** button to test the HTTP request.

## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).

## FAQ

## I want to use an Integration (Prebuilt/Custom/HTTP) node immediately after a Social Hour node. However, I'm experiencing failures such as HTTP 429 Status Code ("Too Many Requests") and my flow execution stops. What should I do?

The HTTP 429 "Too Many Requests" status code means that the downstream system configured in integration (Custom/HTTP/Prebuilt) node is receiving requests faster than it can process them. This often happens when a large number of requests are released simultaneously from a Delay Node, Social Hour Node, or Event Scheduler and sent to integration node.

To resolve this, we recommend to implement a retry mechanism in your flow. Introduce a loop around the Integration or HTTP node that retries the failed request three times before stopping. This approach helps smooth out request bursts and increases the chances of successful processing, even if the target system is temporarily overloaded. Note that this does not guarantee all requests will be accepted by the downstream system. 

**How to implement a retry:**

1. Add a loop around the Integration(Custom/HTTP/Prebuilt) node.
2. Set the loop to attempt the request up to three times before failing the transaction.
3. Include a delay between retries to avoid overwhelming the endpoint (for example: 60 seconds, 120 seconds, and 180 seconds).
4. Optionally, log failed transactions using Logbook or Flow Outcome for monitoring and troubleshooting.