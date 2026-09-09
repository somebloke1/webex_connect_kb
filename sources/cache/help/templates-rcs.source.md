> 📘 
> 
> Please note that RCS message templates can be used only with Messaging API v2 at the moment.

## Configuring RCS Templates

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c71fc73-RCS_Templates.png",
        "",
        "Screenshot of Configuring New RCS Template"
      ],
      "align": "center",
      "sizing": "600px",
      "border": true,
      "caption": "Screenshot of Configuring New RCS Template"
    }
  ]
}
[/block]


To configure a new RCS template:

1. Go to **Tools** > **Templates**.
2. Click **Add New Template**.
3. Enter a **Name** for the template. Only lower case letters and underscores are allowed in this field. Do not use spaces in the template name.
4. Select the **Channel** as **RCS**.
5. Select the required **Notification Type** for the RCS template. The available message types are as stated below. Refer to the procedures for each of the individual message options and return to continue with the current procedure.

   1. **[Text](https://help.imiconnect.io/docs/rcs-1#configuring-the-text-option)**
   2. **[File](https://help.imiconnect.io/docs/rcs-1#configuring-the-file-option)**
   3. **[Rich Card](https://help.imiconnect.io/docs/rcs-1#configuring-the-rich-card-option)**
   4. **[Carousal Card](https://help.imiconnect.io/docs/rcs-1#configuring-the-carousal-card-option)**
6. (Optional) Click **Add Suggestions** and add one of the following:
   1. **Simple Reply**
   2. **View Location**
   3. **Dial Phone**
   4. **Share Location**
   5. **Open URL**
   6. **Calendar Event**
7. Select **Lock this template to prevent other users to make changes** if you want the template to remain inaccessible for other users to make changes.
8. Click **Save**. The template is created.

## Configuring the Text Option

1. In the **Notification Type** drop-down menu, select **Text**.
2. (Optional) Enter the carrier code in the **Carrier** field, if you are aware of the carrier that the customer is subscribed to.
3. Enter the message that you want to send to the users in the **Message** field.You can add parameters ($name, $designation) to the message to send customized and personalized messages to users. 
4. Return to the Step 7 in the main procedure **[Configuring RCS Templates](https://help.imiconnect.io/docs/rcs-1#configuring-rcs-templates)** to complete the remaining steps.

   [block:image]{"images":[{"image":["https://files.readme.io/7ce8372812c9f0c1f905d2102f8ac5653923ff1d26b4d9621980c83759fab7c4-image-20250104-134909.png","","Manage Template"],"align":"center","border":true,"caption":" Manage Template"}]}[/block]

## Configuring the File Option

1. In the **Notification Type** drop-down menu, select **File**.  
   (Optional) Enter the carrier code in the Carrier field, if you are aware of the carrier that the customer is subscribed to.
2. In the **Thumbnail URL** field, enter the URL of the thumbnail that you want to display on the user’s screen, also specifying the **Size**.
3. In the field below the **Thumbnail URL** field, enter the example URL of the thumbnail that you want to display on the user’s screen, also specifying the **Size**.
4. Return to the Step 7 in the main procedure **[Configuring RCS Templates](https://help.imiconnect.io/docs/rcs-1#configuring-rcs-templates)** to complete the remaining steps.

## Configuring the Rich Card Option

1. In the **Notification Type** drop-down menu, select **Rich Card**.
2. (Optional) Enter the carrier code in the **Carrier** field, if you are aware of the carrier that the customer is subscribed to.
3. For **Card Orientation**, select one of the following:
   1. **Vertical**
   2. **Horizontal**
4. For **Media**, select one of the following:
   1. **Short**
   2. **Medium**
   3. **Tall**
5. In the **Media URL** field, enter the URL of the media image that you want to display on the user’s screen, also specifying the **Size**.
6. For **Thumbnail URL**, enter the URL of the thumbnail image that you want to display on the user’s screen, also specifying the **Size**.
7. In the Title, enter the template title to be displayed on the user’s screen. You can add parameters ($name) to the title to send customized and personalized messages to users.
8. In the **Description** field, enter the message to be displayed in the user’s screen.You can add parameters ($designation) to the description to send customized and personalized messages to users.  
   (Optional) Click **Add Suggestions** and add one of the following:
   1. **Simple Reply**
   2. **View Location**
   3. **Dial Phone**
   4. **Share Location**
   5. **Open URL**
   6. **Calendar Event**
9. Return to the Step 7 in the main procedure **[Configuring RCS Templates](https://help.imiconnect.io/docs/rcs-1#configuring-rcs-templates)** to complete the remaining steps.

   [block:image]{"images":[{"image":["https://files.readme.io/8ca140ddfa67656ad9c2dc7078462d4d886e9e4b8ddcbcc139623e0d8e676660-image-20250104-134254.png","","Manage Template for Rich Card"],"align":"center","border":true,"caption":"Manage Template for Rich Card"}]}[/block]

## Configuring the Carousel Card Option

1. In the **Notification Type** drop-down menu, select **Carousal Card**.
2. (Optional) Enter the carrier code in the **Carrier** field, if you are aware of the carrier that the customer is subscribed to.
3. For **Card Orientation**, select one of the following:
   1. **Vertical**
   2. **Horizontal**
4. For **Media**, select one of the following:
   1. **Short**
   2. **Medium**
   3. **Tall**
5. In the **Media URL** field, enter the URL of the media image that you want to display on the user’s screen, also specifying the **Size**.
6. For **Thumbnail URL**, enter the URL of the thumbnail image that you want to display on the user’s screen, also specifying the **Size**.
7. In the Title, enter the template title to be displayed on the user’s screen. You can add parameters ($name) to the title to send customized and personalized messages to users.
8. In the **Description** field, enter the message to be displayed in the user’s screen.You can add parameters ($designation) to the description to send customized and personalized messages to users.  
   (Optional) Click **Add Suggestions** and add one of the following:
   1. **Simple Reply**
   2. **View Location**
   3. **Dial Phone**
   4. **Share Location**
   5. **Open URL**
   6. **Calendar Event**
9. Return to Step 7 in the main procedure **[Configuring RCS Templates](https://help.imiconnect.io/docs/rcs-1#configuring-rcs-templates)** to complete the remaining steps.

Refer to the [Limits and Best Practices](https://help.webexconnect.io/docs/rcs-message-node#limits-and-best-practices) section for more information on Field/Element and their best practices.

Refer to the [Supported File Type for RCS Channel](https://help.webexconnect.io/docs/supported-file-types-for-channels#rcs)  section for more information on RCS file formats.