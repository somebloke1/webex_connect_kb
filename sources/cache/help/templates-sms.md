# SMS

Source: https://help.webexconnect.io/docs/templates-sms
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:32+00:00

## Configuring SMS Templates



![Configuring a new SMS template](https://files.readme.io/5a5b915556be2c471ce149ca041fd1352d052a0c843bbf7d51c6923d5a3cac07-Configure_NEw_Template.png)




To configure a new SMS template:

1. Go to **Tools** > **Templates**.
2. Click **Add New Template**.
3. Enter a **Name** for the template. Only lower case letters and underscores are allowed in this field. Do not use spaces in the template name.
4. Select the **Channel** as _SMS_.
5. Select the required **Message Type** for the SMS template. The available message types are:
   - _Text_
   - _Flash_
   - _Binary_
   - _Unicode_.
6. Enter the message that you want to send to the users in the **Message** field. The message can contain up to 4000 characters. We recommend that you keep SMS messages below 450 characters for better deliverability and user experience.
7. Click  '**+ Add Variable**' option for adding variables for passing dynamic values. The same variable name that's generated automatically is to be used under params within the message block in the Messaging API v1
8. By default **Template Type** is set to 'Regular' but provides an additional option named **DLT**. The **DLT** option is to be used for passing the DLT Template ID in case you want to send messages to customers based in India. Else, for all other geographies, you can use the Regular option.  
   The **Template Type** drop-down option is set to **Regular** by default, but provides an additional option named **Approved DLT Template**. When this option is selected, you have to enter your DLT registered template ID in the ‘Template ID’ field. The DLT option is used when you want to send messages to customers based in India. Else, for all other geographies, you can use the **Regular** option.
   > 📘 Note
   > 
   > When you select the **Approved DLT Template** option from the **Template Type** drop-down field, then ensure that the Sender IDs are also configured on the **DLT **section on the **Numbers** page for the India region.
9. Click **Save**. The template is created.

### Sample Payload for SMS

```json Messaging API v1 - SMS Template Sample Payload
{
    "deliverychannel":"sms",
    "message":{
        "template":"H1ENXXXMR",
        "parameters":{
            "parameter1":"<value>",
            "parameter2":"<value>",
            "parameter3":"<value>"
        }
    },
    "destination":[
        {
            "msisdn":[
                "4477xxxxxxxx"
            ]
        }
    ]
}
```