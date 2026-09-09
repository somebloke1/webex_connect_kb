## Sample flow

<https://imiprodus1org.us.webexconnect.io/flowdesigner/view/public/de56af4a-db1c-4e62-b011-3b67395e35c3> (pass: 123)

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7b369b6-Complete_flow.png",
        "Complete flow.png",
        "Screenshot of 'bot loop' part of the flow for using rich responses."
      ],
      "align": "center",
      "border": true,
      "caption": "The 'bot loop' part of the flow for using rich responses. The numbers above each box correspond to steps in this documentation."
    }
  ]
}
[/block]


## Steps to use rich responses in a <<prodname>> flow

1. Define rich responses (quick replies, carousels, etc.) in your bot responses. Refer for more [information](https://help.imiconnect.io/docs/response-designer)
2. In the bot node, select Set Variable from Action and define 'botresponse' as a Variable and set the Value as 'full_response' output variable.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ca63a0f-Task1.png",
        "Task bot var set.png",
        "Screenshot of setting the 'botresponse' variable in bot node."
      ],
      "align": "center",
      "border": true,
      "caption": "Setting the 'botresponse' variable in bot node."
    }
  ]
}
[/block]


3. Use an evaluate node for 'Success' node outcome of the bot node to parse the bot output and transform it into the format required by the inApp node.
   1. Use the code provided in the document in the evaluate node.
   2. Set script outputs for the three possible outcomes
      1. Text response
      2. Quick replies with text
      3. Generic template

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e145129-Eval_branches.png",
        "Eval branches.png",
        "Screenshot of setting script outputs in evaluate node."
      ],
      "align": "center",
      "border": true,
      "caption": "Setting script outputs in evaluate node."
    }
  ]
}
[/block]


4. For each of the three node outcomes, use a different In-app Messaging channel node and select the message type based on the appropriate branch.
   1. Text response 
      1. Message type = Message
      2. Message = `$(text)`
   2. Quick replies with text 
      1. Message type = Message with Quick Replies
      2. Message = `$(text)`
      3. Content type = Dynamic
      4. Quick replies = `$(quick_replies)`
   3. Generic template 
      1. Message type = Generic template
      2. Message = `$(text)`
      3. Content type = Dynamic
      4. Template Elements = `$(generic_template)`

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8077a04-in_app_carousel.png",
        "in app carousel.png",
        "Screenshot of delivering a generic template/carousel to the user."
      ],
      "align": "center",
      "border": true,
      "caption": "Delivering a generic template/carousel to the user."
    }
  ]
}
[/block]


5. Select the appropriate 'Message Type' in subsequent Append Conversation nodes and provide the values from the preceding channel nodes. Set the Timestamp field as `$(timestamp)`.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cf2b90b-Append.png",
        "evaluate carousel.png",
        "Screenshot of appending the conversation with generic template."
      ],
      "align": "center",
      "border": true,
      "caption": "Appending the conversation with generic template."
    }
  ]
}
[/block]


6. Connect receive nodes to Append conversation nodes in each of the three branches. Add 'Incoming message' and 'Postback' event names. Update the value of the variable that is being used as an input message to the bot node when exiting these receive nodes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a8ad2c4-Receive_events.png",
        "Receive events.png",
        "Screenshot of event names in the receive nodes."
      ],
      "align": "center",
      "border": true,
      "caption": "Event names in the receive nodes."
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7b95262-Receive_var_set.png",
        "Receive var set.png",
        "Screenshot of updating the variable that is used as the input message to bot node."
      ],
      "align": "center",
      "border": true,
      "caption": "Updating the variable that is used as the input message to bot node."
    }
  ]
}
[/block]


7. For the app.mo node outcome of the receive nodes in step 6, connect them to the evaluate node for checking PCI compliance and parsing any attachments. This should already be present in your livechat flow. If now, you can use the code and transition actions from the evaluate node in linked sample flow.

8. For each of the 3 branches, use the Append conversation node for incoming user messages. Select the appropriate message type and response object based on the branch.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6ceb303-Append1.png",
        "Append last.png",
        "Screenshot of appending conversation with generic template response received from the user."
      ],
      "align": "center",
      "border": true,
      "caption": "Appending conversation with generic template response received from the user."
    }
  ]
}
[/block]


9. For the branches with app.postback node outcome of the receive nodes in step 6, use a data parser node extract the payload of the button clicked by the user if you wish to send the payload back to the bot as user message. Update the value of the variable that is being used as an input message to the bot node when exiting these data parser nodes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3d907bd-Data_parser_0.png",
        "Data parser_0.png",
        "Screenshot of extracting the payload value from the button clicked by user."
      ],
      "align": "center",
      "border": true,
      "caption": "Extracting the payload value from the button clicked by user."
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/264c6a6-Data_parse.png",
        "Data parse.png",
        "Screenshot of updating the variable that is used as the input message to bot node."
      ],
      "align": "center",
      "border": true,
      "caption": "Updating the variable that is used as the input message to bot node."
    }
  ]
}
[/block]


10. Connect the success outcomes of data parser or append conversation nodes back to the bot node in all branches.

### Evaluate node code for data transformation

Use the below code for the evaluate node in step 3.

```javascript Evaluate
var response = [];
response = JSON.parse(botresponse);
var text = '';
var quick_replies = {};
var generic_template = {};
var response_types = [];
var timern = new Date();
var timestamp = timern.toISOString();

// Array of response types
for (var x = 0; x < response.length; x++) {
    response_types.push(Object.keys(response[x]));
}
response_types = [].concat.apply([], response_types); //Flattens array

if (response.length === 0) {
    0;
} else if (response[0].hasOwnProperty('text') && response.length === 1) {
    text = response[0].text;
    1;
} else if (response_types.indexOf('quick_reply') >= 0) {
    var pos = response_types.indexOf('quick_reply');
    var options = [];
    for (var i = 0; i < response[pos].quick_reply.quick_replies.length; i++) {
        options[i] = {};
        options[i].payload = {};
        options[i].title = response[pos].quick_reply.quick_replies[i].title;
        options[i].identifier = response[pos].quick_reply.quick_replies[i].title;
        options[i].imageUrl = "";
        options[i].payload.payload = response[pos].quick_reply.quick_replies[i].payload;
        options[i].type = "quickReplyPostback";
    }
    quick_replies.options = options;
    quick_replies.reference = "bot reference";
    quick_replies = JSON.stringify(quick_replies);
    text = response[pos].quick_reply.text;
    2;
} else if (response_types.indexOf('media') >= 0) {
    var pos = response_types.indexOf('media');
    var elements = [];
    for (var i = 0; i < response[pos].media.length; i++) {
        elements[i] = {};
        elements[i].imageUrls = [];
        elements[i].title = response[pos].media[i].title;
        elements[i].subtitle = response[pos].media[i].description;
        elements[i].imageUrls[0] = response[pos].media[i].url;
        elements[i].buttons = [];
        for (var j = 0; j < response[pos].media[i].buttons.length; j++) {
            elements[i].buttons[j] = {};
            elements[i].buttons[j].title = response[pos].media[i].buttons[j].title;
            elements[i].buttons[j].identifier = response[pos].media[i].buttons[j].title;
            elements[i].buttons[j].payload = {};
            if (response[pos].media[i].buttons[j].type === "postback") {
                elements[i].buttons[j].type = "templatePostback";
                elements[i].buttons[j].payload.payload = response[pos].media[i].buttons[j].payload;
                elements[i].buttons[j].url = "";
            } else {
                elements[i].buttons[j].type = "webUrl";
                elements[i].buttons[j].url = response[pos].media[i].buttons[j].url;
            }
        }
    }
    for (var k = 0; k < response.length; k++) {
        if (response[k].hasOwnProperty('text')) {
            text = response[k].text;
        }
    }
    generic_template.elements = elements;
    generic_template.reference = "bot reference";
    generic_template = JSON.stringify(generic_template);
    3;
}
```