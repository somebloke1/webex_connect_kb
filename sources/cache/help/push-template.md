# Push

Source: https://help.webexconnect.io/docs/push-template
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:33+00:00

## Configuring Push Templates



![Screenshot of Push Template Configuration](https://files.readme.io/7f73ec1-Push_Template1.png)




To configure a new RCS template:

1. Go to **Tools** > **Templates**.
2. Click **Add New Template**.
3. Enter a **Name** for the template. Only lower case letters and underscores are allowed in this field. Do not use spaces in the template name.
4. Select the **Channel** as **Push**.
5. Enter the details for:
   1. **Title**
   2. **Expiry In Seconds**
6. Click one of the options below based on the type of device or OS configuration:
   1. **[Android](https://help.imiconnect.io/docs/push#:~:text=each%20of%20these.-,Android,-These%20are%20Android)**
   2. **[iOS](https://help.imiconnect.io/docs/push#:~:text=to%20each%20notification.-,iOS,-These%20are%20iOS)**
   3. **[Webpush](https://help.imiconnect.io/docs/push#:~:text=Time%20to%20live-,WebPush,-These%20are%20Web)**
   4. **[Interactions](https://help.imiconnect.io/docs/push#:~:text=On%2Dclick%20URL-,Interactions,-OS%20%2D%20the%20operating)**
7. Select **Lock this template to prevent other users to make changes**.
8. Click **Save**.

> 📘 Note
> 
> Only the configured data from the earlier steps will be considered when a template ID is passed in the messaging API. The messaging API will not take into consideration any extra parameters that are sent in separately.