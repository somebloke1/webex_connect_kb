# Link Shortener

Source: https://help.webexconnect.io/docs/link-shortener
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:10+00:00

## Introduction

The Link Shortener Prebuilt Node allows you to pass a long URL and convert it into a short URL. The short URL can then be embedded in the message content when sending messages to customers through channels supported by Webex Connect Flow Builder.

This node can be utilized alongside all Send Nodes. The domain you want to use for creating shortened links should be mapped to your Webex Connect tenant by following certain configurations, which will be added to our documentation alongside this release. 

These configurations can be done by a 'Tenant Owner' or 'Full Access User' with requisite permissions. In addition to the creation of short links, you will be able to add up to two reporting tags along with your link shortening requests. This configuration will allow you to view the counts of links created and clicked at the individual reporting tag level. These will be accessible under the 'Reports' section.

Further, you will have the ability to configure details such as Callback Data, Correlation ID, and Notify URLs to get notified each time this link is clicked by a recipient.

In the Access version, the capability can be utilized through Messaging APIs. In the Early Access phase, the prebuilt node must be activated via the Admin Console for the selected tenants and synchronized with the designated regions.

This node is currently in Early Access mode and will not be available by default. Please get in touch with your account manager to enable the Link Shortener nodes on your tenant.



![Link Shortener](https://files.readme.io/c29f29800f3f01b15f3d77b4f37cccef0a10ad426d55572776313b47bd4a7e88-image-20250515-121830.png)




## Version Supported

> 📘 
> 
> This integration is based on Link Shortener Node API  is v1.0.0.

## Pre-requisites

1. Activate the Link Shortener Prebuilt Node. Note that this feature isn't enabled by default and requires activation for your account. Please get in touch with your account manager in case you wish to enable it for your account.
2. Additionally, a CNAME record must be added at the domain level with the appropriate redirection. Please get in touch with Webex Customer Support for guidance.

   - **Client Custom Domains**: Add a Record Name with relevant redirection based on your Webex Connect tenant location (table below). Reach out to the Webex Connect customer support team and provide the domain certificate to add to the Certificate Manager (ACM) for this purpose. This typically requires some lead time; hence, we recommend you plan ahead of time for getting this setup done and leave some time for end-to-end testing.
   - **Default Webex Connect Branded Domain**: The region-specific Record Names can also be used directly as the default domain of the tenant.

   | Webex Connect Region | Record Name |
   | :------------------ | :---------- |
   | AWS Canada          | ca.wbxc.io  |
   | AWS Ireland         | eu.wbxc.io  |
   | AWS London          | uk.wbxc.io  |
   | AWS Mumbai          | in.wbxc.io  |
   | AWS Oregon          | us.wbxc.io  |
   | AWS Singapore       | sg.wbxc.io  |
   | AWS Sydney          | au.wbxc.io  |
3. [Generate client credentials](#generate-client-credentials) for your tenant. Enter up to 50 branded subdomains owned by the customer that they wish to use for Link Shortening via Webex Connect Messaging APIs and/or Flow Builder. 
4. Once the credentials are generated, ensure they are securely saved, as they will be required to add prebuilt authorization under **Assets → Integrations → Prebuilt Integration → Link Shortener → Authorization**. 
5. Add a valid prebuilt authorization. For more information, refer to the [Add a Valid Authorization](https://help.webexconnect.io/docs/shortened-urls#add-a-valid-authorization) section.

## Generate Client Credentials

1. Navigate to **Tenant Settings**. (Only users with the Tenant Owner or Full Access User roles have the ability to modify this setting.)
2. Within the ‘Custom Domain Setup for Link Shortening’ section, complete the following actions:
   1. In the input field, enter the custom domain you want to use for the Link shortener.
      > 📘 Note
      > 
      > The domain registered on the Tenant Settings page will be shown in the Link Shortener Prebuilt Node under the Short Domain drop-down. (link to the Prebuilt node.)
   2. Click **Generate Credentials**.
3. Copy the **Client ID ** and **Client Secret ** generated.  
   These credentials will be used for authorizing the prebuilt node and are configured at the tenant level and can be shared across all groups and teams within the tenant.

   

![Tenant Settings—Custom Domain Setup for Link Shortening](https://files.readme.io/c524c56a5f6dff1fcd70dd292945c8dd340728370c010b68bc39311e9464cb59-image-20250515-124112.png)



## Add a Valid Authorization

1. Navigate to **Assets > Integrations**.
2. Choose "Prebuilt Integrations" from the drop-down menu.
3. Select the Link Shortener node that has been created, then proceed to add the necessary authorization.
4. Enter a **name** along with the **Client Credentials ** and **Client Secret ** obtained from the Tenant Settings page.  
   To create a new Authorization, navigate to the Authorization section and generate a new entry. Ensure that you securely save the ID, as it will be needed in the flow builder.

## Node Configuration

This Link Shortener node can be used with all the send nodes except (Instagram, AMB).

Drag-and-drop the node onto the visual flow builder and double-click the node to configure it.

1. Choose **Method Name** “Create Shortlink“ from the drop-down.
2. Select the **Authorization Name** you created for this prebuilt node, located under Assets>Integrations.
3. Provide the **Long URL** that you want to shorten.
4. Select the **Short domain **that is configured for Link Shortening on the Tenant Settings page.
5. Provide the **Reporting Tags** which are alphanumeric character set used for collating link-shortening statistics e.g., name used for a messaging program. Each reporting tag can be up to 50 characters long and may include special characters such as underscores (\_) and hyphens (-). Tags are optional; however, if provided, they will enable reporting on link clicks and creation based on the selected reporting tag. For more information, refer to the Reports > URL Shortener section. 
6. Provide the **Notify URL** to receive click notification for the respective shortened link at this URL.
7. Select **Notify Authorization ID** from the drop-down.
8. Enter **Callback Data **to include any additional data that needs to be sent to the notify URL as a part of click notification.
9. Enter a unique **Correlation ID **to identify link click events. These will be sent to the Notify URL as part of click notifications.

   

![Link Shortener](https://files.readme.io/f6b1f28b1d3c4bf02b282a0c2b3446fc3cf555aa95f204fa16fee8e9874551a6-image-20250526-181806.png)



## Methods and Outcomes

Here’s a brief description of various methods and corresponding output variables and node outcomes associated with each of the methods.

### Method Name - Create Shortlink

The following are the UI parameters that are required to call this method.



![Link Shortener](https://files.readme.io/fd031a30b8d492ddcb63c3b86bb0e43199c90f677c6060bb5aca534de0ee4149-image-20250526-181549.png)






| Input Variables | Output Variables | Node Outcomes |
| --- | --- | --- |
| Long URL  <br>• Please provide the long URL that you would like to shorten.  <br>  <br>Short domain  <br>• Review the custom domain(s) configured for Link Shortening on the Tenant Settings page and select one.  <br>  <br>Reporting Tags  <br>• Tags are keywords or combinations of words and numbers used to classify or describe your link.  <br>  <br>Webhook URL  <br>•Notify URL  <br>  <br>Webhook URL Authorization ID  <br>•Notify URL Authorization ID  <br>  <br>Callback data  <br>•Include any additional data that needs to be sent to the notify URL.  <br>  <br>Correlation ID  <br>•Enter your unique reference ID that will be passed back to you in click notification via notify URL. | Shortlink  <br>• This is the shortened link that has been created.  <br>  <br>ID  <br>• This is the unique identifier created for the shortened link.  <br>  <br>Response Code  <br>  <br>Response Message | onInvalidData  <br>•Invalid data  <br>  <br>onError  <br>• Error while invoking the method  <br>  <br>onInvalidChoice  <br>• Invalid choice  <br>  <br>onAuthorizationfail  <br>  <br>Error  <br>• Indicates one of the following:  <br>onInvalidData : Invalid data  <br>onError: Error while invoking the method  <br>onInvalidChoice: Invalid choice  <br>onAuthorizationfail: When an authorization fails  <br>  <br>Success  <br>  <br>• indicates:  <br>onSuccess - The shortened link is generated successfully.  <br>  <br>onTimeout  <br>• When the method could not be invoked before the timeout (10 seconds) duration |




## Limitation

- The Link Shortener feature is not compatible with Email and WhatsApp templates in this release.
- Reporting Tag fields lack validation when dynamic data is provided.