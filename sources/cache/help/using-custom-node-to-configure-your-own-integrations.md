# Using Custom Node to configure your own integrations

Source: https://help.webexconnect.io/docs/using-custom-node-to-configure-your-own-integrations
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:49+00:00

## Step 1: Go to Integrations

1. Hover over **Assets** and click **Integrations **from the menu bar on the left to navigate to the Integrations screen.



![Navigate to the Integrations screen by selecting Integrations from the Assets menu.](https://files.readme.io/5e030ed-20.jpg)




## Step 2: Add a custom node

2. Click **ADD INTEGRATION** button and select **CUSTOM NODE** from the drop-down.



![Adding a custom node by selecting it from the ADD INTEGRATION drop-down menu.](https://files.readme.io/cdf7c8e-21.jpg)




Once you click the Custom Node option, a 'Create new custom node' pop-up appears as shown below. As you would notice, Webex Connect enables you to integrate with both Rest API and Soap API compliant systems. 



![Pop-up window for creating a new custom node after selecting the Custom Node option.](https://files.readme.io/f0027fc-Custom_Node1.jpg)




Provide a user friendly node name and description. Upload a relevant **SVG** image for your integration.

In this example, we are going to show how you can integrate the REST API integration option to configure a reusable integration with IBM Watson Tone Analyzer API.

> 📘 Note:
> 
> The following integration follows the IBM Watson Tone Analyzer API reference.

## Step 1: Configure the Watson REST API under the SETTINGS tab

1. Enter a name in the Request Name field on the Request Details window.
2. Choose **POST** as the **TYPE** from the drop-down.
3. Enter the API Resource URL: <https://cloud.ibm.com/apidocs/tone-analyzer> in the Resource URL field as available on IBM Watson API reference.
4. Configure the request parameter version as follows:
   - Enter “version” in the Parameter field 
   - Choose DYNAMIC from the Parameter value type drop-down.
   - Enter “version” in the Field Value field. 



![ Configuration screen for setting up Request Details in custom node.](https://files.readme.io/986f86e-1.jpg)




## Step 1.1: Configure the Authorization

1. Choose **BASIC AUTH** as the Authorization Type.
2. Configure the User Name
   - Enter **username** in the Username field.
   - Choose **DYNAMIC** as the Parameter value type from the drop-down.
   - Enter Username in the Field name field.
3. Assign a Password
   - Enter the password in the Password field.
   - Choose **DYNAMIC** as the Parameter value type from the drop-down.
   - Enter Password in the Field name field.



![Configuration screen for setting up Authorization in custom node.](https://files.readme.io/c306014-2.jpg)




## Step 1.2: Configure the Headers

1. Enter **Content-Type** as the Parameter.
2. Choose **Static** from the Parameter value type drop-down.
3. Enter **application/json** under the Parameter value field.



![Configuration screen for setting up Headers in custom node.](https://files.readme.io/b31da9b-3.jpg)




## Step 1.3: Configure the Body

1. Choose **JSON(application/json)** from the drop-down.
2. Enter the code as shown below:



![Configuration screen for setting up request Body.](https://files.readme.io/3861bcc-4.jpg)




```text
{
"text":"$(text)"
}
```

3. Enter text under the Parameter field.
4. Choose **DYNAMIC** as the Parameter value type from the drop-down. 
5. Enter **text ** under the Field Value field.

## Step 1.4 : Configure the Response

1. Configure a node event for the success response :
   - Enter success under the Node Event field.
   - Choose HTTP Status from the drop-down.
   - Choose equals from the drop-down.
   - Enter the value 200 in the Value field.
   - Choose Success from the Node Edge drop-down.
2. Click Add New and configure another node event for an error response
   - Enter error under the Node Event field.
   - Choose HTTP Status from the drop-down.
   - Choose not equals from the drop-down. 
   - Enter the value 200 in the Value field.
   - Choose Error from the Node Edge drop-down.



![Configuring the node events in the Response section.](https://files.readme.io/d761040-5.jpg)




3.Map the response object to a node variable

- Enter ToneId in the Parameter Name field.
- Choose Body from the drop-down.
- Enter $.document_tone.tones[0].tone_id under Response Path field.
- Click Add New from the bottom.
- Enter ToneName in the Parameter Name field.
- Choose Body from the drop-down.
- Enter $.document_tone.tones[0].tone_name in the Response Path field.
- Click Add New from the bottom.
- Enter ToneScore in the Parameter Name field.
- Choose Body from the drop-down.
- Enter $.document_tone.tones[0].score in the Response Path field.



![Configure Response Path](https://files.readme.io/0d95c83-6.jpg)




## Step 2: Configure the NODE UI Tab

1. Enter a name in the INFORMATION TEXT field (e.g., Authentication).
2. Choose Text box from the Field Type drop-down under Username.
3. Check the Mandatory parameter checkbox.



![Node UI](https://files.readme.io/8a7fc34-7.jpg)




4. Choose Text box from the Field Type drop-down under Password.
5. Check the Mandatory parameter checkbox.
6. Choose Text box from the Field Type drop-down under version.
7. Check the Mandatory parameter checkbox.
8. Choose Text box from the Field Type drop-down under user input.
9. Check the Mandatory parameter checkbox.
10. Click **SAVE** at the bottom of the screen.