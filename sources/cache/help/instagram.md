# Instagram (Deprecated)

Source: https://help.webexconnect.io/docs/instagram
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:03+00:00

Instagram has over 1 billion active users and is one of the most viable social platforms available for businesses to reach customers and increase their revenue today.

Users can easily connect their Instagram pages with their Facebook accounts and build rich messaging experiences using messaging API and/or flow builder. We support various rich messaging features offered by Instagram such as text, image and sticker, audio, video, quick replies, and generic templates.

## Prerequisites for Configuring the Instagram App

1. Create an Instagram account.
2. Change the account type from **Personal **to **Professional **account.
3. Login to the mobile app with the same account credentials.
4. Navigate to **Settings **> **Privacy** > **Messages** > and enable **Allow access to messages**.



![Message Controls](https://files.readme.io/012a350-Step_4.png)




5. Create a Facebook Professional account or keep the login details ready for an existing Facebook Professional account.
6. Create a Facebook Page for the newly created Facebook account or existing Facebook account.Facebook User should be able to perform Tasks with at least 'Moderate' level access on that Page.
7. In your Instagram account, navigate to the newly created Facebook account or existing Facebook account by clicking **Settings **> **Instagram** > Webex Connect account. You will be routed to the **Instagram Login** page.
8. Log in to your Instagram account and you will be navigated to the connected Facebook page.



![Screenshot of Connected Facebook page.](https://files.readme.io/07736f3-Step8_1.png)






![Screenshot of Connect to Instagram page.](https://files.readme.io/241a0ec-Creating_Insta5.png)




9. Look for text with Instagram account is connected (Or) if there is an alert message for review connection, then click on **Review Connect** and enter Instagram login details.



![Screenshot of Connected Instagram page.](https://files.readme.io/5f24abe-Creating_Insta4.png)




## Configuring your Instagram App on Webex Connect

You can register you’re an Instagram with Webex Connect from 'Assets -> Apps' section. Here are the steps for registering:

1. Select Instagram from **Configure New App** dropdown.
2. Provide a name for your Instagram app asset and click **Add Instagram Account**. You must be the admin of the Facebook page to integrate an Instagram with Webex Connect.



![Screenshot of Configuring New Instagram App.](https://files.readme.io/36086a9-Instagram.jpg)




3. Click on Add Instagram account. You will be navigated to the Facebook Login page and it will display all the available Facebook pages. You must skip this step if you're already logged in.



![Facebook login popup.](https://files.readme.io/87178ef-Configuring_Insta2.png)




4. Select the Facebook page that was linked with the Instagram app in the procedure above.
5. Provide the requested access permissions and click **Done**.
6. At this stage, you'll be redirected to Webex Connect. If you selected multiple pages in the previous step, you will be asked to choose the page that you want to use for the asset you are configuring. Select the required page.



![Screenshot Displaying to Select the Required Page.](https://files.readme.io/ad2fbc4-Configuring_Insta3.png)




The screen below is displayed if the configuration is successful.



![Screenshot of Managing Instagram App.](https://files.readme.io/e01f455-1.jpg)




5. Click **Save**.
6. Optionally, you can add Ice Breakers in the Ice Breakers section.

## Ice-Breakers

Ice Breaker questions are a way for users to interact with a business with a list of frequently asked questions. A maximum of 4 questions can be set via the Ice Breakers API. There are two set of questions in the Ice Breakers section:

- Default questions: If the mobile application is not able to identify the location of the customer, these questions are displayed.

- Region-specific questions: You can set a unique set of questions for customers in different regions. The questions displayed on their screen will depend on the questionnaire that you create for that region. You can set questionnaires for multiple locations.



![Screenshot of Ice Breakers.](https://files.readme.io/a76374f-2.jpg)




## Authorization Expiry

The following is a list of scenarios in which the authorization of your Instagram app will expire:

- When you change your Instagram login password.
- If the user who requested the token no longer has a role on the page.
- If you deselect any of the integrated pages when adding a new page in the Webex Connect platform. Make sure to include all the integrated pages.

## Edit/Manage/Delete the Instagram App Asset

1. Go to **Assets** > **Apps**.
2. Search for the Instagram that you want to edit and click **Manage** in the drop-down list box at the right to manage the settings of this app.



![Manage Instagram App asset](https://files.readme.io/739f518a09c382b29053949734217f6f2ecde263efa8a7f79d35e7cfe6fff72c-Instagram_-_Manage_app.png)




You see the **Manage – Instagram** page, where you can manage the settings of the app. <br>

### Delete Instagram App Asset

1. Go to Assets > Apps.
2. Search for the Instagram app asset that you want to edit and click **Delete** in the drop-down list box at the right to delete the app.



![Deleting Instagram app asset](https://files.readme.io/ccc9c1459c4e71a0b1708dba0edbbcea4b2b95fe5ca8b396d73def06943c1b78-Instagram_app_asset.png)




## Using the Channel

### User Identity

To message users on Instagram, you need the IGS ID of the users. You receive this when a user messages the business for the first time.

## API

Here is a Postman collection to test our APIs. Make sure you change the key in the header to your service key.

Latest Collection: [![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/cisco/webex-connect/collection/pyjw227/webex-connect-apis)

Archived Collection: Refer [Postman Collection](https://www.postman.com/cisco/webex-connect/folder/68yfedu/archived-collections)

[Download](https://www.getpostman.com/) Postman from official site.

## Webhooks

Once a Instagram app is configured, you can configure Outbound Webhooks by choosing the Instagram  app from the entity dropdown to receive incoming messages and events from your customers. Formats supported are Text, Media - Image and Sticker (Like_Heart), Audio, Video, Gif, Postback, and Message Deleted.  
To receive delivery receipts of the messages you sent out, configure Outbound Webhooks on the service from which you sent the message. For information on examples, refer to [Outbound Webhooks](https://help.imiconnect.io/docs/outbound-webhooks).

## Message Types

Instagram Direct Message supports the following message types:

1. Text
2. Attachment (Image)
3. Generic Template
4. Sticker

## Rules

When you select Instagram as the channel, the following events and actions are available for configuration:



| Channel Events | Actions |
| --- | --- |
| _ Incoming message  <br>_ Postback  <br>\* Message Deleted | \* Notify URL |




## Flows

In flow, you can configure the Start Node to invoke a flow and Receive node to receive messages from an Instagram page. Currently, interaction with the end-user is facilitated through Send Message v2 APIs.

## FAQs

You can refer to the [Instagram channel FAQs](https://developers.imiconnect.io/reference/instagram) for contextual information.