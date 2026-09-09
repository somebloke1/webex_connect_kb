# Exception handling at the node level

Source: https://help.webexconnect.io/docs/exception-handling-at-the-node-level
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:49+00:00

The below examples assume that the outcome at the occurrence of any of these exceptions is to stop the execution. However, there are cases when you may want to branch the flow i.e. transition to some other node in case of onError or other such events. E.g. if you send an SMS to a customer and that time outs, you may want to fall back to some other channel rather than ending the flow execution at the instant.

Here's how you configure the events when ending the execution at the occurrence of their events.

## 1. Configure "onError" event for a node

The '**onError**' event is configured to record the instance when the flow fails due to any internal error.  
To configure the **onError **event response: See the image below. Let us take the example of an SMS Node.

1. Click & Drag the red dot next to **Send SMS** Node edge.
2. You will see a dotted line appearing as in the below image. Release to end & open up the end configuration screen.



![Configuration of the 'onError' event for a node](https://files.readme.io/cf142a4-Error_Configs.png)




3. Choose the onError from the Node event drop-down on the **END FLOW - SETTINGS** tab. 
4. Choose **102 – Flow completed with an error [Error]** from the Custom flow result drop-down and click on **OK**. 



![Selecting the 'onError' event from the Node event drop-down on the END FLOW - SETTINGS tab.](https://files.readme.io/72f92e3-Exception_Handling.jpg)




## 2. Configure "onPolicyFail" event for a node

1. Drag the red dot next to Call User Node edge similar to 1.1 & 1.2 mentioned in the **onError** configuration screen.
2. Choose the **onPolicyFail **from the Node event drop-down on the **END FLOW - SETTINGS** tab. 
3. Choose 103 – Flow ended due to an interruption [ Incomplete ] from the Custom flow result drop-down and click on **OK** to save this setting.



![Selecting the 'onPolicyFail' event from the Node event drop-down on the END FLOW - SETTINGS tab.](https://files.readme.io/302870b-Exception_Handling1.jpg)




## 3. Configure "onTimeOut" event for a node

The '**ontimeout**' event occurs when the time (in seconds) mentioned in the Timeout field has been exceeded.  
To configure the **ontimeout **event response:

1. Drag and drop the orange dot on a node with timeout configuration ( for illustration receive node is shown in the below image )



![Configuration of the 'onTimeout' event for a node.](https://files.readme.io/76a9529-onTimeOutConfigs.png)




2. Choose **ontimeout **from the Node event drop-down on the **[END FLOW - SETTINGS]** tab. 
3. Choose **103 – Flow ended due to an interruption [Incomplete] **from the Custom flow result drop-down. 
4. Click **OK **.



![Selecting the 'onTimeout' event from the Node event drop-down on the END FLOW - SETTINGS tab.](https://files.readme.io/df28c6d-Exception_Handling2.jpg)

