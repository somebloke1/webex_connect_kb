# Evaluate Node

Source: https://help.webexconnect.io/docs/evaluate-node
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:53+00:00

The Evaluate node allows you to run JavaScript code as part of a flow execution to handle complex flows that require advanced computations or data transformations. 

The **Configuration** tab provides a script input box where you can add your own JavaScript code. The script output section allows you to conditionally branch the flow based on your script output. 



![Evaluate Node](https://files.readme.io/98b8111-Evaluate.png)




## Using Evaluate Node



![Evaluate Node](https://files.readme.io/0824cb7-23.png)




> 📘 Accessing Flow Variables in Evaluate Node
> 
> - Custom Variables can be accessed by their names in the Evaluate node script. For example, a custom variable ‘Phone’ can be accessed as $(Phone). 
> - Auto-generated (or Node Output variables) can be accessed as $(nodeid.variablename). For example, sms.timestamp is a variable in the SMS Start node and the Node ID for the Start node is always 2 (Node ID is available at the bottom left corner of the Node pop-up). Hence, sms.timestamp can be accessed in the script as $(n2.sms.timestamp). Note that you do not need to know the Node ID and variable format. Custom variables or Node Output variables can be accessed in the script by directly clicking the list of variables available on the right side of the Node pop-up. Click the variable name from the list to automatically populate the node variable with the correct formatting in the script.
> - The variables are case-sensitive.
> - The Evaluate node script returns the result as a decimal value. If you want the output without the decimal portion, add '' + to the expression to convert the final result to a string.
>   Example: var abc = '' + (parseInt($(a), 10) - parseInt($(b), 10));
>   In this example, parseInt($(a), 10) and parseInt($(b), 10) convert the input values to integers before the subtraction is performed. However, using parseInt() alone does not change how the Evaluate node returns the final output. The '' + converts the final result to a string, so the value is returned without the decimal portion.

Description of Interface elements:



| S. No | Element | Description |
| --- | --- | --- |
| 1 | Configuration tab | Use this tab to evaluate javascript.  <br>  <br>Field descriptions:  <br>  <br>**Configure Script output**  <br>Specify a **name** for the **script output** in this field.  <br>  <br>It appears in the Output Variables panel.  <br>  <br>**Branch Name**  <br>Once the script output is configured, then specify the **branch name** in this field. |
| 2 | Transition Actions tab | Use this tab to configure node **on-enter/on-leave** operations. |
| 3 | Test button | Both the Configuration tab and the Transition Actions tab contain a **Test** button. Click the **Test** button on the **Configuration** tab to test the script output. Similarly, click the **Test** button on the **Transition Actions **tab to test the  **on-enter /on-leave** operations that are configured. |
| 4 | Input Variable | Click this collapsible panel to view the list of all the available flow variables. You can search for a variable using the **Search** field. You can also add a variable to the flow variables list by clicking the **Add new flow** variable link at the bottom of the list. |
| 5 | Output Variables | Click this collapsible panel to view the output variables. |
| 6 | Node Outcomes | Click this collapsible panel to view the list of possible node outcomes. You can also customize the node labels by clicking the **Edit** icon. |
| 7 | Generate Code using AI | Enable the toggle button to generate code using AI.  <br>It is important to note that Bot builder application is mandatory for enabling the toggle to generate code using AI.  |
| 8 | Prompt textbox | Enter the message which will be sent to the AI.  <br>Example - Write a JavaScript for generating a 25-digit random string to use it as a Correlation ID. |
| 9 | Script generated as output textbox | This is the script generated as output when the message added in the above Prompt textbox is sent to AI. |
| 10 | Script editor | Enter your script here. The script in the editor is executed during flow execution. |




## Evaluating a Script Output

You can evaluate the JavaScript in two steps: Configuring Script and Transition Actions.

## **Configuring the Script**

As part of configuring the script, you need to first configure and then test it. 

Here are the steps:

1. Double click the **Evaluate Node**.  
   The Evaluate screen appears. See the above image.
2. Do the following on the **Configuration** tab:
   1. In the **Input** box, specify the **Javascript**, enter the Javascript, which you want to evaluate or generate code using AI.
   2. In the **Script Output** field, enter a **name** for the script output. It appears in the Output Variables in the panel.
   3. In the **Branch Name** field, enter a **name** for the branch.  
      ** Note:** Click the **+ Add New **, if you want to configure more javascript. 

### Generate Code using AI

Generate sample JavaScript code tailored to your specific use case or requirements by providing a prompt. The resulting code is designed to be compatible with the JavaScript Engine utilized by Webex Connect.

**Prerequisite**: Code generation using AI requires Bot Builder App Tray. If Bot Builder is not enabled for your tenant,  reach out to your account manager to get it enabled. For more information on Bot Builder, see [Bot Builder](https://help.imiconnect.io/docs/getting-started-with-bot-builder) documentation.

To generate code with AI:

1. Double-click the Evaluate Node. The Evaluate screen appears.



![Screenshot of Enabling Generate Code using AI](https://files.readme.io/8cdd427-18.png)




2. Enable the **Generate Code using AI** toggle button (field 7 in the above table)..
3. Enter a prompt for the AI in the Prompt textbox (field 8 in the above table). Tip: To get the anticipated output from the Bot, the prompt message must be as descriptive as possible. Example - Write a JavaScript for generating a 25-digit random string to use it as a Correlation ID.
4. Click **Generate Code**. Based on the prompt entered, the script is generated in the Output textbox (field 9 in the above table).
5. Click **Transfer Code** to move the AI-generated script to your script editor (field 10 in the above table). The script will be transferred to the editor in a new line.  
   Note: If the script output generated by the AI poses a security risk, you can report it.

> 📘 Note
> 
> If the script output generated by the AI poses a security risk, you can report it.

6. Click **Test**. Make sure to test your script and verify that it is generating the desired output.

> 📘 Note
> 
> The Generate Code button is disabled after generating the code. It is enabled only when a new change is added to your previous prompt.

> 📘 Note
> 
> Each Bot Builder-enabled tenant is permitted a maximum of 1000 requests per month for generating scripts using AI. Once this quota is exhausted, it will automatically reset at the beginning of the next month. The quota of 1000 requests per month is applied across tenants and includes all groups and teams.

#### Report Output

To report the generated output:

1. Click Report Output. A pop-up appears.
2. Enter the feedback message and select the required checkbox under Report AI’s Output.  
   Note: It is mandatory to enter one character and select one checkbox.
3. Click Submit.

## Pre-defined Functions

Webex Connect platform provides libraries that you can include in the **Evaluate** node. The libraries contain pre-defined functions that can be directly called instead of writing code for them. Use the following syntax at the beginning of the JavaScipt code to include libraries:

- For single library - `includeJs(LibraryName1)`
- For multiple libraries - `includeJs(LibraryName1,LibraryName2,LibraryName3)`

### **imi_general Library**

The following table provides a list of functions available in this library:



| Function Name | No. of Parameters | Parameter Type | Output/Example |
| --- | --- | --- | --- |
| typeof | 1 | ANY | Returns the type of the variable  <br>  <br>`IMI_GENERAL.typeof(<<variable_to_be_evaluated>>);` |
| length | 1 | ANY | Returns the length of the given object  <br>  <br>`IMI_GENERAL.length(<<variable_to_be_evaluated>>);` |
| unicodeToString | 1 | Array or Object | Returns the String from charCode  <br>  <br>`IMI_GENERAL.unicodeToString(<<variable_to_be_evaluated>>);` |
| urlEncode | 1 | String | Returns the encoded URL  <br>  <br>`IMI_GENERAL.urlEncode(<<variable_to_be_evaluated>>);` |
| urlDecode | 1 | String | Returns the decoded URL  <br>  <br>`IMI_GENERAL.urlDecode(<<variable_to_be_evaluated>>);` |
| encodeURIComponent | 1 | String | Returns the complete encoded URL including the protocol  <br>  <br>`IMI_GENERAL.encodeURIComponent(<<variable_to_be_evaluated>>)` |
| decodeURIComponent | 1 | String | Returns the complete decoded URL component  <br>  <br>`IMI_GENERAL.decodeURIComponent(<<variable_to_be_evaluated>>);` |
| stringToUnicode | 2 | string, output_type ( output_type variable can accept 'string', 'array' and 'object') | Returns the unicode of the provided string  <br>  <br>`IMI_GENERAL.stringToUnicode(<<variable_to_be_evaluated>>, '<<output_type>>');` |




> 📘 Response Outputs supported by `typeof` Method.
> 
> Following the response for `typeof` method when a variable type to be evaluated.
> 
> - object- Object
> - array- Array
> - string- string
> - number- number
> - NaN -number
> - function- Object
> - undefined- undefined
> - null - “”(Empty String)

### **imi_base64 Library**



| Function Name | No. of Parameters | Parameter Type | Output/Example |
| --- | --- | --- | --- |
| encodeBase64 | 1 | String | Returns the encoded base64 string  <br>  <br>`var messageencode = base64encode(<<variable_to_be_evaluated>>);`  <br>  <br>To encode any special characters or unicode character please refer to the note below. |
| decodeBase64 | 1 | String | Returns the decoded base64 string  <br>  <br>`var messagedecode = base64decode(<<variable_to_be_evaluated>>);`  <br>  <br>To decode any special characters or unicode character please refer to the note below. |




> 📘 Note
> 
> For example -
> 
> To encode or decode Japanese text which contains unicode character,follow the below syntax: 
> 
> `var japaneseText = '注文開始'`
> 
> `var encodeJapaneseText = base64encode(unescape(encodeURIComponent(japaneseText)));`
> 
> `var decodeJapaneseText = decodeURIComponent(escape(base64decode(encodeJapaneseText)));`

### **imi_strings Library**

The following table provides a list of functions available in this library:



| Function Name | No. of Parameters | Parameter Type | Output/Example |
| --- | --- | --- | --- |
| length | 1 | ANY | Returns the length of the variable  <br>  <br>`IMI_STRINGS.length(<<variable_to_be_evaluated>>);` |
| concat | 2 | String and String  <br>or  <br>String and Number | Adds the provided input to the string  <br>  <br>`IMI_STRINGSs.concat(<<variable1_to_be_evaluated>>, <<variable2_to_be_evaluated>>);` |
| lastIndexOf  <br>  <br>The method name is case-sensitive | 3 |   _ search_text (mandatory) - String  <br>  _ text (mandatory) - String  <br>  \* start_pos (optional) - String; the start position from where the search should start within the string  | Returns the position of the last occurrence of a specified value in a string. This method returns -1 if the value to search for never occurs.  <br>  <br>**Note**: The string is searched from the end to the beginning, but returns the index starting at the beginning, at position 0.  <br>  <br>`IMI_STRINGS.lastIndexOf(<<search_text>>, <<text>>, <<start_pos>>);` |
| indexOf | 3 | search_text (mandatory) - String  <br>  <br>text (mandatory) - String  <br>  <br>start_pos (optional) - String; the start position from where the search should start within the string | Returns the first occurrence position of the search_text within the actual text or returns -1 if not found  <br>  <br>`IMI_STRINGS.indexOf(<<search_text>>, <<text>>, <<start_pos>>);` |
| search | 2 |   _ search_text (mandatory) - String or regular expression  <br>  _ text (mandatory) - String  | Returns a number, representing the position of the first occurrence of the specified search value, or -1 if no match is found  <br>  <br>`IMI_STRINGS.search(<<search_text_or_regular_expression>>, <<text>>);` |
| replace | 3 |   _ search_text (mandatory) - the value, or regular expression that needs to be replaced by the new value  <br>  _ newvalue (mandatory) - the value to replace the search value with  <br>  \* text (mandatory) - String  | Returns a new string, where the specified value(s) has been replaced by the new value.  <br>If a normal string is provided, it will replace the first occurrence. For global use, use a regular expression instead.  <br>  <br>`IMI_STRINGS.replace(<<search_text_or_regular_expression>>, <<newvalue>>, <<text>>);` |
| toUpperCase | 1 | String | Returns the upperCase format of the provided string  <br>  <br>`IMI_STRINGS.toUpperCase(<<variable_to_be_evaluated>>);` |
| toLowerCase | 1 | String | Returns the lowerCase format of the provided string  <br>  <br>`IMI_STRINGS.toLowerCase(<<variable_to_be_evaluated>>);` |
| trim | 1 | String | Removes whitespace from both sides of a string  <br>  <br>`IMI_STRINGS.trim(<<variable_to_be_evaluated>>);` |
| split | 2 |   _ text (mandatory) - String  <br>  _ separator (mandatory) - String  | Converts the provided string to an array based on the provided separator  <br>  <br>`IMI_STRINGS.split(<<variable_to_be_evaluated>>, <<separator>>);` |
| slice | 3 |   _ start (mandatory)- the position where to begin the extraction. The first character is at position 0  <br>  _ end(optional) - the position (up to, but not including) at which to end the extraction. If omitted, slice() selects all characters from the start position to the end of the string  <br>  \* text (mandatory) - the actual text  | Returns a string, representing the extracted part  <br>  <br>`IMI_STRINGS.slice(<<start>>, <<end>>, <<the_actual_text>>);` |
| substring | 3 |   _ start (mandatory) - the position where to start the extraction. The first character is at index 0  <br>  _ text (mandatory) - the actual text  <br>  \* end (optional) - the position (up to, but not including) at which to end the extraction. If omitted, it extracts the rest of the string  | Returns a string containing the extracted characters  <br>  <br>`IMI_STRINGS.substring(<<text>>, <<start>>, <<end>>);` |
| substr | 3 |   _ start (mandatory) - the position where to start the extraction. The first character is at index 0. If start is positive and greater than, or equal, to the length of the string, substr() returns an empty string. If start is negative, substr() uses it as a character index from the end of the string. If start is negative or larger than the length of the string, start is set to 0.  <br>  _ length (optional) - the number of characters to extract. If omitted, it extracts the rest of the string  <br>  \* text (mandatory) - the actual text  | Returns a string, containing the extracted part of the text. If length is 0 or negative, an empty string is returned  <br>  <br>`IMI_STRINGS.substr(<<start>>, <<length>>, <<text>>);` |




### **imi_array Library**

The following table provides a list of functions available in this library:



| Function Name | No. of Parameters | Parameter Type | Output/Example |
| --- | --- | --- | --- |
| concat | 1 | args (mandatory) - an array of elements | Returns an array object, representing the joined ar  <br>  <br>`IMI_ARRAY.concat(<<Array_of_Elements>>);` |
| indexOf | 3 |   _ array (mandatory) - the original array  <br>  _ item (mandatory) - the item to search for  <br>  \* start (optional) -  the position from where to start the search. Negative values will start at the given position counting from the end, and search to the end  | Returns a number, representing the position of the specified item, otherwise -1  <br>  <br>`IMI_ARRAY.indexOf(<<Original_Array>>, <<Item_to_Search>>, <<optional_start_position>> );` |
| isArray | 1 | object (mandatory) | Returns true if the object is an array, otherwise it returns false  <br>  <br>`IMI_ARRAY.isArray(<<variable_that_need_to_tested>>);` |
| join | 2 |   _ array (mandatory) - the original array  <br>  _ separator (optional) -   the string value which is used as a separator between the array elements  | Returns a string, representing the array values, separated by the specified separator  <br>  <br>`IMI_ARRAY.join(<<Array>>, <<Optional_Separator>>);` |
| lastIndexOf | 3 |   _ array (mandatory) - the original array  <br>  _ item (mandatory) - the item to search for  <br>  \* start (mandatory) - the position from which to start the search. Negative values will start at the given position counting from the end, and search to the beginning  | Returns a number, representing the position of the specified item, otherwise -1  <br>  <br>`IMI_ARRAY.lastIndexOf(<<Original_Array>>, <<Item_to_Search>>, <<optional_start_position>> );` |
| push | 2 |   _ array (mandatory) - the original array  <br>  _ items (mandatory) -  an array of Items  | Returns a number, representing the new length of the array. Note\*: Add item at the end of the array  <br>  <br>`IMI_ARRAY.push(<<Original_Array>>, <<Array_of_Items>> );` |
| unshift | 2 |   _ array (mandatory) - the original array  <br>  _ items (mandatory) -  an array of items  | Returns a number, representing the new length of the array. Note\*: Add item at the beginning of the array  <br>  <br>`IMI_ARRAY.unshift(<<Original_Array>>, <<Array_of_Items>> );` |
| reverse | 1 | array (mandatory) - the original array | Returns an array, representing the array after it has been reversed  <br>  <br>`IMI_ARRAY.reverse(<<Original_Array>> );` |
| splice | 4 |   _ array (mandatory) - the original array  <br>  _ index (mandatory) - an integer that specifies at what position to add/remove items. Use negative values to specify the position from the end of the array  <br>  _ howmany (optional) - the number of items to be removed. If set to 0, no items will be removed  <br>  _ items (mandatory) - an array of elements to be added to the original array  | Adds/removes items to/from an array, and returns the removed item(s)  <br>  <br>`IMI_ARRAY.splice(<<Original_Array>>, <<Index>>, <<Optional_howmany>>, <<Array_of_elements>> );` |
| fill | 4 |   _ originalarray (mandatory) - array  <br>  _ value (mandatory) - the value to be filled in array  <br>  _ start (optional) -  the position from where to start filling the value in the array  <br>  _ end (optional) - the position to stop filling the value in the provided originalarray  | Returns the changed array  <br>  <br>`IMI_ARRAY.fill(<<Original_Array>>, <<value>>, <<Start>>, <<end>> );` |




## **Testing the Script**

After configuring the script output, you need to test it to evaluate its function.

1. Click **Test** button at the bottom.  
   The Test Evaluate Script window appears. 
2. On the **Test** window:
   - In the **Variable Name** field, enter the **variable**. For example, age.
   - In the **Value** field, enter the **value** corresponding to the variable.
   - Click the **Test** button at the bottom to test it.



![Test Window](https://files.readme.io/73a3606-Evaluate.png)




- Finally, click the **Save** button at the bottom.  
  The script is evaluated.

## Configuring Transition Actions

The Transition Actions tab in a node enables you to configure the On-enter and On-leave actions to capture logs when the flow is executed. 

For information, see [Transition Action](https://help.imiconnect.io/docs/transition-actions).

## FAQs

1. **Is the script generated by AI always secure?**  
   It is advisable to verify and test the script using the 'Test' option in the node before incorporating it into the flow. The script generated by AI is designed to be compatible with the JavaScript Engine employed by Webex Connect. However, it's important to acknowledge that a third-party tool is utilized for script generation.
2. I** have written a prompt to AI, but when I click on generate code, I receive TPS reached error? I have not exhausted my 1000 request per month quota.**  
   Access to TPS for code generation using AI is limited for each tenant. Please attempt the operation again. If the issue persists, kindly raise an operational ticket or contact your account manager for further assistance.