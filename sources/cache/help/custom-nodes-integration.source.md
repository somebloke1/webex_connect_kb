Custom Node Integration feature allows you to configure reusable integrations with your existing business system or with third-party applications using REST/SOAP APIs. Once a custom node is configured, it becomes available for use across various flows within your Team/Group/Across Platform. For more information on accessibility of Custom Node within your Team/Group, please refer to [Groups and Teams](https://help.webexconnect.io/docs/sub-accounts).

It can also be used over HTTP Request Node, when you want to configure a reusable integration node, or when you need to integrate with an API that supports advanced authentication mechanisms that are not supported within HTTP Request node.

You must have the following resources for building a custom node integration:

- REST API: a resource URL that points to the location of the third-party APIs.
- SOAP API: a WSDL file or its location. A WSDL file contains a set of web services, their methods, and functionality.

> 📘 Note:
> 
> Custom Node integration is an add-on feature available as part of some select <<prodname>> tiers. Please get in touch with your account manager if you would like to enable it for your tenant.

Callback URLs for all your pre-built integrations, custom integration configurations, that use OAuth 2.0 authorization with ‘Auth Code’ Grant Type will be updated with <<prodname>>  branded URLs. This doesn’t impact functioning of any of your existing integration configurations until the Refresh Token for that integration expires or until you decide to reauthorize. In either of these two cases, you would need to start using the new Callback URL provided on <<prodname>> UI in the third-party application you have integrated with. Another example of this is OAuth 2.0 based authentication for Gmail when using SMTP for Outbound Email channel configuration which is currently available only for <<prodname>>  tenants used for Webex Contact Center Integration. 

Please make sure your applications, firewalls, etc. do not restrict access to these new Callback URLs in case you have an internal policy/practice to add these URLs to the allow/accept/allowed list. 

## Create a Custom Node

To create a custom node:

1. Click Assets > Integrations > Add Integration > Custom Node on the services dashboard.
2. Enter the following details in the Create New Custom Node dialog box:  
   a. Node Name – the name of the custom node.  
   b. Description – meaningful description of the custom node. This is optional.  
   c. API Integration Type – the API type you want to use for the custom node integration.  
   d. Node Category – the category under which you want to classify the custom node. You can either choose an existing category or create a new category.  
   e. Creation Type – choose to create a blank integration and configure it or copy the configuration from an existing integration.  
   f. Node Icon – select an SVG file that you want to use as an icon for the custom node. This is optional.
3. Click OK to create a custom node with the provided details.

## Configure a REST API Node

Specify the resource URL for the RESTful API, create methods, and configure the methods.

1. Configure the request details of the method.
2. Configure the interface of the node.  
   After you configure this node, you can use it in the flows like any other node.

### Configure Request Details

On the Settings tab, you can add methods and configure the method settings. 

To add a method:

1. Provide the Request Details.  
   a.	Request Name – the name of the request or the method.  
   b.	Request Timeout (ms) – duration (in milliseconds) after which the request times out.  
   c.	Connection Timeout (ms) – duration (in milliseconds) after which the connection times out.  
   d.	Type – method type of the request. Any REST API supports the POST, PUT, GET, DELETE, and PATCH method types.  
   e.	Resource URL – the location where the third-party service provider hosts the REST API. Use the notation of $() if you want to pass variables in the URL. For example, $(param1).  
   f.	Parse Variables – button to parse the variables in the URL and extract them. 

| Field           | Description                                                               |
| :-------------- | :------------------------------------------------------------------------ |
| Parameter       | Variable parsed from the URL                                              |
| Parameter Type  | Specify If the parameter is Static or Dynamic                             |
| Parameter Value | This is applicable if the parameter is static. Provide value.             |
| Field Name      | This is applicable if the parameter is dynamic. Provide value at runtime. |

> 📘 Restriction on number of methods
> 
> From v5.6.0 release onwards, you can add only up to 25 methods in a Custom Node. Existing custom nodes will not be affected by this change; however, you will not be able to add additional new methods to a custom node already using 25 or more methods.

> 📘 Note:
> 
> With the v6.18.0 release, you will see two options: API Requests and Authorization Requests (OAuth 2.0). For certificates uploaded prior to v6.18.0, the system will by default, enable the certificates for API Requests. This behavior applies to both the Key Store and Trust Store.

4. Select an Authorization type and configure the details. This is optional.

> 👍 Authorization Types Supported by Custom Integration Node
> 
> - Basic Auth 
> - Digest Auth
> - AWS Signature 
> - OAuth 2.0

You must configure the following parameters based on the authorization type:

a.	No Auth – select this type when you do not need an authorization  
b.	Basic Auth – select this type when you need to do an authorization using username and password

| Field                | Description                                                               |
| :------------------- | :------------------------------------------------------------------------ |
| Username/Password    | Login credentials that you want to use for authentication                 |
| Parameter Value Type | Specify If the parameter is Static or Dynamic                             |
| Parameter value      | This is applicable if the parameter is static. Provide value.             |
| Field Name           | This is applicable if the parameter is dynamic. Provide value at runtime. |

c.	Digest Auth - select this option when you need to validate the user identity before sending any sensitive information like online banking transactional details. In this type of authorization, a network server receives the request from a user and then sends it to a domain controller. The domain controller responds with a special session key.

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Username",
    "0-1": "Username to authenticate the request",
    "1-0": "Realm",
    "1-1": "String from the server within the www-Authenticate response header",
    "2-0": "Password",
    "2-1": "The password to authenticate the request",
    "3-0": "Nonce",
    "3-1": "Unique string from the server within the www-Authenticate response header",
    "4-0": "Algorithm",
    "4-1": "String that indicates a pair of algorithms used to produce the digest and a checksum",
    "5-0": "QOP",
    "5-1": "The quality of protection applied to the message. The value must be one of the alternatives specified by the server in the www-Authenticate response header.",
    "6-0": "Nonce Count",
    "6-1": "The hexadecimal count of the number of requests (including the current request) that the client has sent with the nonce value in this request.  \nYou must specify the count only if a QOP directive is sent in the www-Authenticate response header.",
    "7-0": "Client Nonce",
    "7-1": "An opaque quoted string value provided by the client. This value is used by both client and server to avoid chosen plaintext attacks, provide mutual authentication, and message integrity protection.  \nYou must specify the count only if a QOP directive is sent in the www-Authenticate response header.",
    "8-0": "Opaque",
    "8-1": "A string specified by the server in the www-Authenticate response header. Use this string as is with URLs in the same protection space. <<prodname>> recommends that this string be base64 encoded data."
  },
  "cols": 2,
  "rows": 9,
  "align": [
    "left",
    "left"
  ]
}
[/block]


d.	AWS Signature - select this option when you want to use the Amazon Work Services workflow for authorization. You must use a custom HTTP scheme based on a keyed-HMAC (Hash Message Authentication Code) for authentication.

| Field        | Description                                                   |
| :----------- | :------------------------------------------------------------ |
| Access_Key   | Unique access key for an account used to send the request     |
| Secret_Key   | The unique secret key for an account used to send the request |
| Region       | The region that receives the request                          |
| Service_Name | Service that receives the request                             |

e.	OAuth 2.0 –  is a well-adopted delegated authorization framework. <<prodname>> custom node supports two different grant types for OAuth 2.0

1. Authorization code - server issues the token in the context of a user.
2. Client credentials - grant type is used to obtain an access token outside of the context of a user.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/34b04022c89f3ac8c1292806183e54d94c7264ca267c049290ccf7915778b22a-image.png",
        null,
        "Screenshot of OAuth 2.0 Authorization"
      ],
      "align": "center",
      "caption": "Screenshot of OAuth 2.0 Authorization"
    }
  ]
}
[/block]


[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Consumer ID",
    "0-1": "Unique identifier of the consumer obtained during the registration process",
    "1-0": "Grant Type",
    "1-1": "Type of authentication - Authorization Code or Client Credentials. Its selection depends on the grant type offered by the API.",
    "2-0": "Client ID (Client Credentials only)",
    "2-1": "Unique identifier of the client obtained from the platform through which the authorization is done",
    "3-0": "Client Secret (Client Credentials only)",
    "3-1": "The unique secret of the client obtained from the platform through which the authorization is done",
    "4-0": "Consumer ID (Authorization Code only)",
    "4-1": "Unique identifier of the consumer obtained during the registration process",
    "5-0": "Consumer Secret (Authorization Code only)",
    "5-1": "The unique secret of the consumer obtained during the registration process",
    "6-0": "Call Back URL (Authorization Code only)",
    "6-1": "<<prodname>> callback URL will be used during the registration process at the authorization provider’s end.  \n**Note**: The [callback URL](#section-callback-url) is not accessible from a web browser. You need to test it using the custom node only.",
    "7-0": "Authorization URL (Authorization Code only)",
    "7-1": "Endpoint for authorization server, which retrieves the authorization code must be provided by the authorization provider.",
    "8-0": "Scope",
    "8-1": "Scope of the access request (multiple space-separated values). This is optional.",
    "9-0": "Access Token URL",
    "9-1": "Endpoint for the resource server, which exchanges the authorization code for an access token",
    "10-0": "Access token has a limited validity",
    "10-1": "Specifies if the token has a limited validity and must be provided by the authorization provider.",
    "11-0": "Validity",
    "11-1": "Validity of the token",
    "12-0": "Refresh URL Token",
    "12-1": "It should be provided by the authorization provider.  \n  \nIt ensures smooth functioning of authorization in the case provided access token has limited validity.",
    "13-0": "Advance Settings",
    "13-1": "Toggle button that allows you to enable or disable advanced settings",
    "14-0": "Access Token URL Method",
    "14-1": "An additional method for the access token",
    "15-0": "Access Token URL Parameter type",
    "15-1": "Type of access token URL parameter – Body or URL",
    "16-0": "Access Token URL Headers",
    "16-1": "Additional URL header parameters for the access token",
    "17-0": "Get Access Token",
    "17-1": "Button to retrieve the access token",
    "18-0": "Access Token",
    "18-1": "Displays the refresh token",
    "19-0": "Refresh Token",
    "19-1": "Displays the refresh token",
    "20-0": "Client Authentication",
    "20-1": "Value of Client Authentication is defined by the authorization provider’s API.  \n  \nSend client credentials in body is selected by default.",
    "21-0": "Validity",
    "21-1": "The validity of the token"
  },
  "cols": 2,
  "rows": 22,
  "align": [
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> To enable mTLS certificates for OAuth 2.0 token requests, navigate to the Security Configuration section. Within the Key Store and Trust Store settings, enable **Authorization Requests (OAuth 2.0)**.

3. Enable Security Configuration, if required. This is optional. When you enable it, you can configure the security certificate(s).  
   a.	**Configure Key Store Certificates.**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/37951de0ce2fbd40c4f997076ed644cad4126ef5b245579bea324868bb10180c-image.png",
        null,
        "Screenshot of Security Configuration - Key Store Certificates"
      ],
      "align": "center",
      "caption": "Screenshot of Security Configuration - Key Store Certificates"
    }
  ]
}
[/block]


1. Click Add New and configure the following fields:

| Field              | Description                                                                                                                                                       |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Browse Certificate | Browse and upload the key store certificate                                                                                                                       |
| Select File Format | Select the key store file format – JKS or PKCS12                                                                                                                  |
| Store Password     | The password to access the store                                                                                                                                  |
| Key Password       | The password to access the key                                                                                                                                    |
| Name               | Enter a name for the certificate                                                                                                                                  |
| Validate           | Click the button to extract the validity information from the certificate                                                                                         |
| Valid From         | The date from which the certificate is valid. This field is greyed out and automatically populated when the certificate is validated. This is a read-only field.  |
| Valid Till         | The date until which the certificate is valid. This field is greyed out and automatically populated when the certificate is validated. This is a read-only field. |
| Identifier         | Unique identifier of the certificate. This field is greyed out and automatically populated when the certificate is validated. This is a read-only field.          |

2. Based on the expiry date (Valid Till date), an email is sent to the owner, full-access, and limited-access users of the tenant to remind you 30, 15, 7, 3, 2, and 1 day(s) before expiry. If you do not upload a valid certificate after the expiry date, another email is sent 1 and 7 days after expiry.
3. Under "Apply this certificate to", select where the certificate should be used. At least one option must be selected.
   - **API Requests: **Certificate applies when the Custom Node sends API Requests from a flow.
   - **Authorization Requests (OAuth 2.0): **Certificate applies when the Custom Node sends OAuth 2.0 token requests from a flow, including access token and refresh token requests.

b.	**Configure Trust Store Certificates.**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/509cb2693654739e75fb6c1bda1b6408c8ee91a626b66c987b2717d0b35bf24c-image.png",
        null,
        "Screenshot of Security Configuration - Trust Store Certificates"
      ],
      "align": "center",
      "caption": "Screenshot of Security Configuration - Trust Store Certificates"
    }
  ]
}
[/block]


1. Click Add New and configure the following fields:

| Field               | Description                                                                                                                                                       |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Browser Certificate | Browse and upload the key store certificate                                                                                                                       |
| Select File Format  | Select the key store file format – JKS or PKCS12                                                                                                                  |
| Store Password      | The password to access the store                                                                                                                                  |
| Name                | Enter a name for the certificate                                                                                                                                  |
| Validate            | Click the button to extract the validity information from the certificate                                                                                         |
| Valid From          | The date from which the certificate is valid. This field is greyed out and automatically populated when the certificate is validated. This is a read-only field.  |
| Valid Till          | The date until which the certificate is valid. This field is greyed out and automatically populated when the certificate is validated. This is a read-only field. |
| Identifier          | Unique identifier of the certificate. This field is greyed out and automatically populated when the certificate is validated. This is a read-only field.          |

2. Based on the expiry date (Valid Till date), an email is sent to the owner, full-access, and limited-access users of the tenant to remind you 30, 15, 7, 3, 2, and 1 day(s) before expiry. If you do not upload a valid certificate after the expiry date, another email is sent 1 and 7 days after expiry.
3. Under "Apply this certificate to", select where the certificate should be used. At least one option must be selected.
   - **API Requests: **Certificate applies when the Custom Node sends API Requests from a flow.
   - **Authorization Requests (OAuth 2.0): **Certificate applies when the Custom Node sends OAuth 2.0 token requests from a flow, including access token and refresh token requests.

c.	Configure Security Protocols.

Choose the security protocol that applies to the security certificate. You can choose multiple protocols for a single certificate. <<prodname>> supports the following protocol categories:

- SSL (Secure Sockets Layer) - standard security protocol that establishes a secured and encrypted connection between a web server and a browser.
- TSL (Transport Layer Security) - security protocol that provides privacy and data integration between two communicating applications.

| Protocol             | Description                                                                                                                               |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| SSL 2.0 (Deprecated) | Initiates a basic SSL handshake to establish a secure connection.                                                                         |
| SSL 3.0 (Deprecated) | Initiates a secure handshake with support for certificate-based authentication.                                                           |
| TLS 1.0              | Provides secure communication using HMAC for message integrity and supports DSS/DH key exchange algorithms.                               |
| TLS 1.1              | Enhances TLS 1.0 by introducing an explicit initialisation vector (IV) to improve protection against cipher block chaining (CBC) attacks. |
| TLS 1.2              | Provides secure communication using modern cryptographic algorithms, authenticated key exchange, and strong cipher suites.                |
| TLS 1.3              | Provides faster and more secure communication with a simplified handshake, modern cipher suites, and improved forward secrecy.            |

> 📘 Note
> 
> Custom Nodes now support TLS 1.3 for secure connections to downstream REST and SOAP services. New configurations can use TLS 1.2 or TLS 1.3. 
> 
> TLS 1.0 and TLS 1.1 are unavailable for new configurations, while existing custom nodes using these protocols continue to operate.

> 🚧 Important
> 
> As a security recommendation, customers using TLS 1.0 or TLS 1.1 are strongly encouraged to migrate to TLS 1.3. 
> 
> TLS 1.0 and TLS 1.1 will be deprecated in an upcoming sprint, so customers should update their configurations in advance.

4. Specify Header parameters. This is optional.  
   Click Add New and add the parameters that you want to send in the header of the request.  
   Define the following fields:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Parameter",
    "0-1": "Name of the parameter or variable",
    "1-0": "Parameter Value Type",
    "1-1": "Type of parameter – Static or Dynamic",
    "2-0": "Parameter Value",
    "2-1": "Value of the parameter/variable  \nThis is applicable only for a static parameter.",
    "3-0": "Field Name",
    "3-1": "Name of the field to which you can pass a value  \nThis is applicable only for a dynamic parameter."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


5. Define URL Parameters. This is optional.  
   Click Add New to add parameters that you want to send in the URL of the request. Provide details for the following fields:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Parameter",
    "0-1": "Name of the parameter or variable",
    "1-0": "Parameter Value Type",
    "1-1": "Type of parameter – Static or Dynamic",
    "2-0": "Parameter Value",
    "2-1": "Value of the parameter/variable  \nThis is applicable only for a static parameter.",
    "3-0": "Field Name",
    "3-1": "Name of the field to which you can pass a value  \nThis is applicable only for a dynamic parameter."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


6. Configure Body of the request.  
   The request body can be in any of the following formats:
   - Text (text/plain)
   - JSON (application/json)
   - XML (application/xml)
   - form-data  
     Select a suitable format and enter or paste the body. You can directly add parameters to the body using the Add Parameters button. The Parse button allows you to extract the parameters from the body of the request.  
     Specify the following details and configure the parameters:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Parameter",
    "0-1": "Name of the parameter or variable",
    "1-0": "Parameter Value Type",
    "1-1": "Type of parameter – Static or Dynamic",
    "2-0": "Parameter Value",
    "2-1": "Value of the parameter/variable  \nThis is applicable only for a static parameter.",
    "3-0": "Field Name",
    "3-1": "Name of the field to which you can pass a value  \nThis is applicable only for a dynamic parameter."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


7. Configure the Response of the request.  
   Import response paths from a sample response to create a node event. A node event signifies the outcome of a node. Specify the status code/response path to create a node event and map it. You can map multiple responses to a node event.  
   You can save the response path and use it as a variable within the node.
   1. Select a suitable format for the response. The response can be in Text (text/plain), JSON (application/json), or XML (application/xml) formats. You can import a sample response for JSON or XML.
   2. Click Parse when you import the response from a sample to populate both node events and node variables with the response path. Select the required parameters and click Import to complete importing the response.
   3. Fill in the required details and Configure Node Events.
   4. Set data to be returned in a flow session.  
      The parameters you add here appear as output variables in the node. You can map these parameters to session variables in the node.  
      Click Add New and provide the following details for the parameters and repeat the steps for all parameters you want to add.
      - Parameter Name
      - Body – Body, HTTP Status, or HTTP Header
      - Response Path – specify a response path for Body and HTTP Header. HTTP Status does not require a response path.
        > 📘 Workaround for 'Text/Plain' response type.
        > 
        > When you configure 'Text/plain' as the Response, the following aspects are to be additionally configured. Under 'Set data to be returned in a flow session', you configure 'Parameter Name' as 'Param', select 'Body' as the response data location, and use '$.' under 'Response Path'.
        > 
        > In the Flow, you might expect to access the 'Param' variable using the format $(NodeID.Param), but this returns a null value for the variable. Instead of using $(NodeID.Param), the variable can be accessed via $(Param).
        > 
        > Please note that this workaround is only applicable for the 'Text/Plain' response type."
8. Click Save to save the details of the request.
9. Use the Test button to launch the Node Configuration dialog where you can preview the configuration settings of the node.

## Callback URL

The callback URL is not accessible through a web browser. You need to test it using the custom node only.

### Configure the Node UI

The Node UI tab allows you to configure all the dynamic parameters in the method. You can group the parameters, make the parameters mandatory, perform regex validation, and add a tooltip to the parameter.

1. Specify the Information Text. This is optional.  
   This is the description of the node and it appears on the Node Configuration dialog.
2. Add New Field Group. This is optional.  
   All parameters appear under the Ungrouped category by default. Create field groups and move the parameters around to group them.
3. Select the Field Type for each parameter – Text box, Selection box, or Date and time. Text box is the default type.

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Text box",
    "0-1": "•\tRegex Validation – add a regex validation string  \n•\tTest Regex- check if the regex validation string is valid",
    "1-0": "Selection box",
    "1-1": "•\tAdd New – use to add values to the selection box  \n•\tDisplay Name – the name of the option in the selection box  \n•\tValue – value of the option in the selection box",
    "2-0": "Date and time",
    "2-1": "•\tDate format – format of the date  \n•\tDate-Time Separator – separator between date and time  \n•\tTime format – format of time"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


4. Mark the parameter as Mandatory Parameter if it is a required parameter. It is the default selection.
5. Provide text that you want as Tooltip.
6. Click Save to save the node configuration.
7. Use the Test button to launch the Node Configuration dialog where you can preview the configuration settings of the node. You need to pass values for the dynamic parameters.

## Configure a SOAP API Node

Specify a WSDL file and the methods within that file to use for the SOAP API node integration.

1. Enter the WSDL Location or browse for a WSDL file on your local machine and click Parse.  
   When you browse your local machine, you must select a zip file that contains the WSDL file. Select the required WSDL file within the zip file. 
2. Select the required methods within the WSDL file and click Import to import those methods into the custom node.
3. Configure the request details of the method.
4. Configure the interface of the node.  
   After you configure this node, you can use it in the flows like any other node.

### Throttling for Custom Node Integration

The custom node integration now provides you with the ability to configure the following throttling limits:

- **Rate Limit** – Limit the total number of requests per second. Beyond this limit, the node returns 429 response code.
- **Concurrency Limit** - Limit the maximum number of parallel custom node executions. Beyond this limit, the node returns 430 response code.
- **Volume Limit** - Limit the maximum number of custom node executions within a time period. Beyond this limit, the node returns 430 response code.

These limits can be used to control the rate at which the requests will be made to an API that’s being called from the respective custom node. Once enabled, these limits apply at a platform level to all the flows that use the concerned custom node and may impact the flow execution rate depending on the configurations.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/584273a-throttling.png",
        "throttling.png",
        "Screenshot of Throttling for Custom Node Integration."
      ],
      "align": "center",
      "caption": "Screenshot of Throttling for Custom Node Integration."
    }
  ]
}
[/block]


## Response Codes

The following are the response codes when the custom node throttle limits have reached:

- 429 - Throttle rate limit reached - Too Many requests,
- 430  - Throttleconcurrencylimit reached - Too Many requests,
- 431   -  Throttlevolume limit reached - Too Many requests.

You can find the logged codes in `sfe_trans_logs`.

> 📘 Note
> 
> This integration is available only in the cloud version of <<prodname>>.

## Setting up mTLS in Custom Node

### Prerequisites

- You must have a Key Store Certificate. (Provided by the API Provider)
- You must have a Trust Store Certificate. (Provided by the API Provider)

### Procedure

To set up mTLS in the Custom Node, follow the steps below:

- Log in to the <<prodname>> platform and navigate to the Manage Custom Node page.
- Turn on the **Security Configuration** button.
- In the Security Configuration section, perform the following:
  - Upload the key store certificate in the **Configure Key store certificates** section.  
    Refer to step 3(a) in this section [Configure Request Details](https://help.webexconnect.io/docs/custom-nodes#configure-request-details) on the current page.
  - Upload the trust store certificate in the **Configure Trust store certificates** section.  
    Refer to step 3(b) in this section [Configure Request Details](https://help.webexconnect.io/docs/custom-nodes#configure-request-details) on the current page.
- Click **Save**.

> 📘 Acceptance of Certificate
> 
> Please ensure that the Integration Provider is notified of a potential API call and the certificates are accepted by the Integration Provider when an API request is sent.
> 
> Please refer to the following section ([FAQs for mTLS configuration](https://help.webexconnect.io/docs/custom-nodes#faqs-for-the-mtls-configuration)) for more details on mTLS configuration.

## FAQ

### FAQs for mTLS configuration

1. What is mTLS and its benefits?  
   mTLS (Mutual Transport Layer Security) is an extension of TLS (Transport Layer Security) where both the client and server authenticate each other using digital certificates.  
   mTls is stronger than just authorisations (cannot be phished or intercepted easily). It prevents impersonation and man-in-the-middle (MitM) attacks.

2. What are the prerequisites for establishing mTLS?  
   mTLS requires two types of certificates – The Key Store is required to authenticate the request in mTLS. The Trust Store is required to authenticate the server. You don’t always need to set a Trust Store if the server’s certificate is already trusted in the key store certificate.  
   The Custom node UI does not mandate a Trust Store certificate; the UI will allow establishing mTLS using the Key Store certificate. However, we recommend using a Trust Store certificate to establish mTLS unless you are using Public CA certificates for Key Store. Only public CA certificates do not require a Trust Store certificate, all others do require trust store certificate. However, we advise you to verify this with the API provider.

3. Does support for mTLS means Connect provides Key Store and Trust Store certificates? Or from where do I get Key store and Trust store certificates?  
   <<prodname>> doesn't provide any certificates for mTLS, <<prodname>> uses the certificates uploaded in the Custom node (Key store and Trust store certificates) to establish mutual TLS.  
   The Key store and Trust store certificates are provided by the API provider. These two certificates can be uploaded in the Custom node for mTLS. During Custom node execution in the flows, <<prodname>> will use these certificates to establish a Connection with the API provider. The API providers in turn should validate and accept these certificates as they are shared by them. 

4. Is it mandatory for me to configure mTLS? Am I exposed to security issues if I don’t configure mTLS?  
   mTLS is determined by the API provider. <<prodname>> doesn’t mandate configuring mTLS for establishing API integration. We recommend using mTLS if the client's identity must be strongly verified, or you’re working in regulated industries, or handling sensitive data. Please check with the API provider to understand the security risk if you don’t use mTLS.

### I want to use an Integration (Prebuilt/Custom/HTTP) node immediately after a Social Hour node. However, I'm experiencing failures such as HTTP 429 Status Code ("Too Many Requests") and my flow execution stops. What should I do?

The HTTP 429 "Too Many Requests" status code means that the downstream system configured in integration (Custom/HTTP/Prebuilt) node is receiving requests faster than it can process them. This often happens when a large number of requests are released simultaneously from a Delay Node, Social Hour Node, or Event Scheduler and sent to integration node.

To resolve this, we recommend to implement a retry mechanism in your flow. Introduce a loop around the Integration or HTTP node that retries the failed request three times before stopping. This approach helps smooth out request bursts and increases the chances of successful processing, even if the target system is temporarily overloaded. Note that this does not guarantee all requests will be accepted by the downstream system. 

**How to implement a retry:**

1. Add a loop around the Integration(Custom/HTTP/Prebuilt) node.
2. Set the loop to attempt the request up to three times before failing the transaction.
3. Include a delay between retries to avoid overwhelming the endpoint (for example: 60 seconds, 120 seconds, and 180 seconds).
4. Optionally, log failed transactions using Logbook or Flow Outcome for monitoring and troubleshooting.