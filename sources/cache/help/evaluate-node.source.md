The Evaluate node allows you to run JavaScript code as part of a flow execution to handle complex flows that require advanced computations or data transformations. 

The **Configuration** tab provides a script input box where you can add your own JavaScript code. The script output section allows you to conditionally branch the flow based on your script output. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/98b8111-Evaluate.png",
        "Evaluate.png",
        "Screenshot of Evaluate Node."
      ],
      "align": "center",
      "sizing": "smart",
      "border": true,
      "caption": "Evaluate Node"
    }
  ]
}
[/block]


## Using Evaluate Node

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0824cb7-23.png",
        "Evaluate Click the image to view it larger.png",
        "Screenshot of Evaluate Node Configuration Page."
      ],
      "align": "center",
      "border": true,
      "caption": "Evaluate Node"
    }
  ]
}
[/block]


> 📘 Accessing Flow Variables in Evaluate Node
> 
> - Custom Variables can be accessed by their names in the Evaluate node script. For example, a custom variable ‘Phone’ can be accessed as $(Phone). 
> - Auto-generated (or Node Output variables) can be accessed as $(nodeid.variablename). For example, sms.timestamp is a variable in the SMS Start node and the Node ID for the Start node is always 2 (Node ID is available at the bottom left corner of the Node pop-up). Hence, sms.timestamp can be accessed in the script as $(n2.sms.timestamp). Note that you do not need to know the Node ID and variable format. Custom variables or Node Output variables can be accessed in the script by directly clicking the list of variables available on the right side of the Node pop-up. Click the variable name from the list to automatically populate the node variable with the correct formatting in the script.
> - The variables are case-sensitive.
> - The Evaluate node script returns the result as a decimal value. If you want the output without the decimal portion, add '' + to the expression to convert the final result to a string.
>   Example: var abc = '' + (parseInt($(a), 10) - parseInt($(b), 10));
>   In this example, parseInt($(a), 10) and parseInt($(b), 10) convert the input values to integers before the subtraction is performed. However, using parseInt() alone does not change how the Evaluate node returns the final output. The '' + converts the final result to a string, so the value is returned without the decimal portion.

Description of Interface elements:

[block:parameters]
{
  "data": {
    "h-0": "S. No",
    "h-1": "Element",
    "h-2": "Description",
    "0-0": "1",
    "0-1": "Configuration tab",
    "0-2": "Use this tab to evaluate javascript.  \n  \nField descriptions:  \n  \n**Configure Script output**  \nSpecify a **name** for the **script output** in this field.  \n  \nIt appears in the Output Variables panel.  \n  \n**Branch Name**  \nOnce the script output is configured, then specify the **branch name** in this field.",
    "1-0": "2",
    "1-1": "Transition Actions tab",
    "1-2": "Use this tab to configure node **on-enter/on-leave** operations.",
    "2-0": "3",
    "2-1": "Test button",
    "2-2": "Both the Configuration tab and the Transition Actions tab contain a **Test** button. Click the **Test** button on the **Configuration** tab to test the script output. Similarly, click the **Test** button on the **Transition Actions **tab to test the  **on-enter /on-leave** operations that are configured.",
    "3-0": "4",
    "3-1": "Input Variable",
    "3-2": "Click this collapsible panel to view the list of all the available flow variables. You can search for a variable using the **Search** field. You can also add a variable to the flow variables list by clicking the **Add new flow** variable link at the bottom of the list.",
    "4-0": "5",
    "4-1": "Output Variables",
    "4-2": "Click this collapsible panel to view the output variables.",
    "5-0": "6",
    "5-1": "Node Outcomes",
    "5-2": "Click this collapsible panel to view the list of possible node outcomes. You can also customize the node labels by clicking the **Edit** icon.",
    "6-0": "7",
    "6-1": "Generate Code using AI",
    "6-2": "Enable the toggle button to generate code using AI.  \nIt is important to note that Bot builder application is mandatory for enabling the toggle to generate code using AI. ",
    "7-0": "8",
    "7-1": "Prompt textbox",
    "7-2": "Enter the message which will be sent to the AI.  \nExample - Write a JavaScript for generating a 25-digit random string to use it as a Correlation ID.",
    "8-0": "9",
    "8-1": "Script generated as output textbox",
    "8-2": "This is the script generated as output when the message added in the above Prompt textbox is sent to AI.",
    "9-0": "10",
    "9-1": "Script editor",
    "9-2": "Enter your script here. The script in the editor is executed during flow execution."
  },
  "cols": 3,
  "rows": 10,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


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

Generate sample JavaScript code tailored to your specific use case or requirements by providing a prompt. The resulting code is designed to be compatible with the JavaScript Engine utilized by <<prodname>>.

**Prerequisite**: Code generation using AI requires Bot Builder App Tray. If Bot Builder is not enabled for your tenant,  reach out to your account manager to get it enabled. For more information on Bot Builder, see [Bot Builder](https://help.imiconnect.io/docs/getting-started-with-bot-builder) documentation.

To generate code with AI:

1. Double-click the Evaluate Node. The Evaluate screen appears.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8cdd427-18.png",
        "",
        "Screenshot of Enabling Generate Code using AI"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Enabling Generate Code using AI"
    }
  ]
}
[/block]


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

<<prodname>> platform provides libraries that you can include in the **Evaluate** node. The libraries contain pre-defined functions that can be directly called instead of writing code for them. Use the following syntax at the beginning of the JavaScipt code to include libraries:

- For single library - `includeJs(LibraryName1)`
- For multiple libraries - `includeJs(LibraryName1,LibraryName2,LibraryName3)`

### **imi_general Library**

The following table provides a list of functions available in this library:

[block:parameters]
{
  "data": {
    "h-0": "Function Name",
    "h-1": "No. of Parameters",
    "h-2": "Parameter Type",
    "h-3": "Output/Example",
    "0-0": "typeof",
    "0-1": "1",
    "0-2": "ANY",
    "0-3": "Returns the type of the variable  \n  \n`IMI_GENERAL.typeof(<<variable_to_be_evaluated>>);`",
    "1-0": "length",
    "1-1": "1",
    "1-2": "ANY",
    "1-3": "Returns the length of the given object  \n  \n`IMI_GENERAL.length(<<variable_to_be_evaluated>>);`",
    "2-0": "unicodeToString",
    "2-1": "1",
    "2-2": "Array or Object",
    "2-3": "Returns the String from charCode  \n  \n`IMI_GENERAL.unicodeToString(<<variable_to_be_evaluated>>);`",
    "3-0": "urlEncode",
    "3-1": "1",
    "3-2": "String",
    "3-3": "Returns the encoded URL  \n  \n`IMI_GENERAL.urlEncode(<<variable_to_be_evaluated>>);`",
    "4-0": "urlDecode",
    "4-1": "1",
    "4-2": "String",
    "4-3": "Returns the decoded URL  \n  \n`IMI_GENERAL.urlDecode(<<variable_to_be_evaluated>>);`",
    "5-0": "encodeURIComponent",
    "5-1": "1",
    "5-2": "String",
    "5-3": "Returns the complete encoded URL including the protocol  \n  \n`IMI_GENERAL.encodeURIComponent(<<variable_to_be_evaluated>>)`",
    "6-0": "decodeURIComponent",
    "6-1": "1",
    "6-2": "String",
    "6-3": "Returns the complete decoded URL component  \n  \n`IMI_GENERAL.decodeURIComponent(<<variable_to_be_evaluated>>);`",
    "7-0": "stringToUnicode",
    "7-1": "2",
    "7-2": "string, output_type ( output_type variable can accept 'string', 'array' and 'object')",
    "7-3": "Returns the unicode of the provided string  \n  \n`IMI_GENERAL.stringToUnicode(<<variable_to_be_evaluated>>, '<<output_type>>');`"
  },
  "cols": 4,
  "rows": 8,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Function Name",
    "h-1": "No. of Parameters",
    "h-2": "Parameter Type",
    "h-3": "Output/Example",
    "0-0": "encodeBase64",
    "0-1": "1",
    "0-2": "String",
    "0-3": "Returns the encoded base64 string  \n  \n`var messageencode = base64encode(<<variable_to_be_evaluated>>);`  \n  \nTo encode any special characters or unicode character please refer to the note below.",
    "1-0": "decodeBase64",
    "1-1": "1",
    "1-2": "String",
    "1-3": "Returns the decoded base64 string  \n  \n`var messagedecode = base64decode(<<variable_to_be_evaluated>>);`  \n  \nTo decode any special characters or unicode character please refer to the note below."
  },
  "cols": 4,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


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

[block:parameters]
{
  "data": {
    "h-0": "Function Name",
    "h-1": "No. of Parameters",
    "h-2": "Parameter Type",
    "h-3": "Output/Example",
    "0-0": "length",
    "0-1": "1",
    "0-2": "ANY",
    "0-3": "Returns the length of the variable  \n  \n`IMI_STRINGS.length(<<variable_to_be_evaluated>>);`",
    "1-0": "concat",
    "1-1": "2",
    "1-2": "String and String  \nor  \nString and Number",
    "1-3": "Adds the provided input to the string  \n  \n`IMI_STRINGSs.concat(<<variable1_to_be_evaluated>>, <<variable2_to_be_evaluated>>);`",
    "2-0": "lastIndexOf  \n  \nThe method name is case-sensitive",
    "2-1": "3",
    "2-2": "  _ search_text (mandatory) - String  \n  _ text (mandatory) - String  \n  \\* start_pos (optional) - String; the start position from where the search should start within the string ",
    "2-3": "Returns the position of the last occurrence of a specified value in a string. This method returns -1 if the value to search for never occurs.  \n  \n**Note**: The string is searched from the end to the beginning, but returns the index starting at the beginning, at position 0.  \n  \n`IMI_STRINGS.lastIndexOf(<<search_text>>, <<text>>, <<start_pos>>);`",
    "3-0": "indexOf",
    "3-1": "3",
    "3-2": "search_text (mandatory) - String  \n  \ntext (mandatory) - String  \n  \nstart_pos (optional) - String; the start position from where the search should start within the string",
    "3-3": "Returns the first occurrence position of the search_text within the actual text or returns -1 if not found  \n  \n`IMI_STRINGS.indexOf(<<search_text>>, <<text>>, <<start_pos>>);`",
    "4-0": "search",
    "4-1": "2",
    "4-2": "  _ search_text (mandatory) - String or regular expression  \n  _ text (mandatory) - String ",
    "4-3": "Returns a number, representing the position of the first occurrence of the specified search value, or -1 if no match is found  \n  \n`IMI_STRINGS.search(<<search_text_or_regular_expression>>, <<text>>);`",
    "5-0": "replace",
    "5-1": "3",
    "5-2": "  _ search_text (mandatory) - the value, or regular expression that needs to be replaced by the new value  \n  _ newvalue (mandatory) - the value to replace the search value with  \n  \\* text (mandatory) - String ",
    "5-3": "Returns a new string, where the specified value(s) has been replaced by the new value.  \nIf a normal string is provided, it will replace the first occurrence. For global use, use a regular expression instead.  \n  \n`IMI_STRINGS.replace(<<search_text_or_regular_expression>>, <<newvalue>>, <<text>>);`",
    "6-0": "toUpperCase",
    "6-1": "1",
    "6-2": "String",
    "6-3": "Returns the upperCase format of the provided string  \n  \n`IMI_STRINGS.toUpperCase(<<variable_to_be_evaluated>>);`",
    "7-0": "toLowerCase",
    "7-1": "1",
    "7-2": "String",
    "7-3": "Returns the lowerCase format of the provided string  \n  \n`IMI_STRINGS.toLowerCase(<<variable_to_be_evaluated>>);`",
    "8-0": "trim",
    "8-1": "1",
    "8-2": "String",
    "8-3": "Removes whitespace from both sides of a string  \n  \n`IMI_STRINGS.trim(<<variable_to_be_evaluated>>);`",
    "9-0": "split",
    "9-1": "2",
    "9-2": "  _ text (mandatory) - String  \n  _ separator (mandatory) - String ",
    "9-3": "Converts the provided string to an array based on the provided separator  \n  \n`IMI_STRINGS.split(<<variable_to_be_evaluated>>, <<separator>>);`",
    "10-0": "slice",
    "10-1": "3",
    "10-2": "  _ start (mandatory)- the position where to begin the extraction. The first character is at position 0  \n  _ end(optional) - the position (up to, but not including) at which to end the extraction. If omitted, slice() selects all characters from the start position to the end of the string  \n  \\* text (mandatory) - the actual text ",
    "10-3": "Returns a string, representing the extracted part  \n  \n`IMI_STRINGS.slice(<<start>>, <<end>>, <<the_actual_text>>);`",
    "11-0": "substring",
    "11-1": "3",
    "11-2": "  _ start (mandatory) - the position where to start the extraction. The first character is at index 0  \n  _ text (mandatory) - the actual text  \n  \\* end (optional) - the position (up to, but not including) at which to end the extraction. If omitted, it extracts the rest of the string ",
    "11-3": "Returns a string containing the extracted characters  \n  \n`IMI_STRINGS.substring(<<text>>, <<start>>, <<end>>);`",
    "12-0": "substr",
    "12-1": "3",
    "12-2": "  _ start (mandatory) - the position where to start the extraction. The first character is at index 0. If start is positive and greater than, or equal, to the length of the string, substr() returns an empty string. If start is negative, substr() uses it as a character index from the end of the string. If start is negative or larger than the length of the string, start is set to 0.  \n  _ length (optional) - the number of characters to extract. If omitted, it extracts the rest of the string  \n  \\* text (mandatory) - the actual text ",
    "12-3": "Returns a string, containing the extracted part of the text. If length is 0 or negative, an empty string is returned  \n  \n`IMI_STRINGS.substr(<<start>>, <<length>>, <<text>>);`"
  },
  "cols": 4,
  "rows": 13,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


### **imi_array Library**

The following table provides a list of functions available in this library:

[block:parameters]
{
  "data": {
    "h-0": "Function Name",
    "h-1": "No. of Parameters",
    "h-2": "Parameter Type",
    "h-3": "Output/Example",
    "0-0": "concat",
    "0-1": "1",
    "0-2": "args (mandatory) - an array of elements",
    "0-3": "Returns an array object, representing the joined ar  \n  \n`IMI_ARRAY.concat(<<Array_of_Elements>>);`",
    "1-0": "indexOf",
    "1-1": "3",
    "1-2": "  _ array (mandatory) - the original array  \n  _ item (mandatory) - the item to search for  \n  \\* start (optional) -  the position from where to start the search. Negative values will start at the given position counting from the end, and search to the end ",
    "1-3": "Returns a number, representing the position of the specified item, otherwise -1  \n  \n`IMI_ARRAY.indexOf(<<Original_Array>>, <<Item_to_Search>>, <<optional_start_position>> );`",
    "2-0": "isArray",
    "2-1": "1",
    "2-2": "object (mandatory)",
    "2-3": "Returns true if the object is an array, otherwise it returns false  \n  \n`IMI_ARRAY.isArray(<<variable_that_need_to_tested>>);`",
    "3-0": "join",
    "3-1": "2",
    "3-2": "  _ array (mandatory) - the original array  \n  _ separator (optional) -   the string value which is used as a separator between the array elements ",
    "3-3": "Returns a string, representing the array values, separated by the specified separator  \n  \n`IMI_ARRAY.join(<<Array>>, <<Optional_Separator>>);`",
    "4-0": "lastIndexOf",
    "4-1": "3",
    "4-2": "  _ array (mandatory) - the original array  \n  _ item (mandatory) - the item to search for  \n  \\* start (mandatory) - the position from which to start the search. Negative values will start at the given position counting from the end, and search to the beginning ",
    "4-3": "Returns a number, representing the position of the specified item, otherwise -1  \n  \n`IMI_ARRAY.lastIndexOf(<<Original_Array>>, <<Item_to_Search>>, <<optional_start_position>> );`",
    "5-0": "push",
    "5-1": "2",
    "5-2": "  _ array (mandatory) - the original array  \n  _ items (mandatory) -  an array of Items ",
    "5-3": "Returns a number, representing the new length of the array. Note\\*: Add item at the end of the array  \n  \n`IMI_ARRAY.push(<<Original_Array>>, <<Array_of_Items>> );`",
    "6-0": "unshift",
    "6-1": "2",
    "6-2": "  _ array (mandatory) - the original array  \n  _ items (mandatory) -  an array of items ",
    "6-3": "Returns a number, representing the new length of the array. Note\\*: Add item at the beginning of the array  \n  \n`IMI_ARRAY.unshift(<<Original_Array>>, <<Array_of_Items>> );`",
    "7-0": "reverse",
    "7-1": "1",
    "7-2": "array (mandatory) - the original array",
    "7-3": "Returns an array, representing the array after it has been reversed  \n  \n`IMI_ARRAY.reverse(<<Original_Array>> );`",
    "8-0": "splice",
    "8-1": "4",
    "8-2": "  _ array (mandatory) - the original array  \n  _ index (mandatory) - an integer that specifies at what position to add/remove items. Use negative values to specify the position from the end of the array  \n  _ howmany (optional) - the number of items to be removed. If set to 0, no items will be removed  \n  _ items (mandatory) - an array of elements to be added to the original array ",
    "8-3": "Adds/removes items to/from an array, and returns the removed item(s)  \n  \n`IMI_ARRAY.splice(<<Original_Array>>, <<Index>>, <<Optional_howmany>>, <<Array_of_elements>> );`",
    "9-0": "fill",
    "9-1": "4",
    "9-2": "  _ originalarray (mandatory) - array  \n  _ value (mandatory) - the value to be filled in array  \n  _ start (optional) -  the position from where to start filling the value in the array  \n  _ end (optional) - the position to stop filling the value in the provided originalarray ",
    "9-3": "Returns the changed array  \n  \n`IMI_ARRAY.fill(<<Original_Array>>, <<value>>, <<Start>>, <<end>> );`"
  },
  "cols": 4,
  "rows": 10,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


## **Testing the Script**

After configuring the script output, you need to test it to evaluate its function.

1. Click **Test** button at the bottom.  
   The Test Evaluate Script window appears. 
2. On the **Test** window:
   - In the **Variable Name** field, enter the **variable**. For example, age.
   - In the **Value** field, enter the **value** corresponding to the variable.
   - Click the **Test** button at the bottom to test it.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/73a3606-Evaluate.png",
        "Evaluate Test Window.png",
        "Screenshot of Test Window."
      ],
      "align": "center",
      "border": true,
      "caption": "Test Window"
    }
  ]
}
[/block]


- Finally, click the **Save** button at the bottom.  
  The script is evaluated.

## Configuring Transition Actions

The Transition Actions tab in a node enables you to configure the On-enter and On-leave actions to capture logs when the flow is executed. 

For information, see [Transition Action](https://help.imiconnect.io/docs/transition-actions).

## FAQs

1. **Is the script generated by AI always secure?**  
   It is advisable to verify and test the script using the 'Test' option in the node before incorporating it into the flow. The script generated by AI is designed to be compatible with the JavaScript Engine employed by <<prodname>>. However, it's important to acknowledge that a third-party tool is utilized for script generation.
2. I** have written a prompt to AI, but when I click on generate code, I receive TPS reached error? I have not exhausted my 1000 request per month quota.**  
   Access to TPS for code generation using AI is limited for each tenant. Please attempt the operation again. If the issue persists, kindly raise an operational ticket or contact your account manager for further assistance.