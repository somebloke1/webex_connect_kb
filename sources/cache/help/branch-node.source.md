The branch node allows you to split your flow based on conditional statements without the need to write any custom code. You can configure multiple branches within a single node with each branch containing a set of logical conditions. 

To name a few, you can use the branch node to execute simple conditions like selecting the correct channel based on the user’s preference, evaluate if the OTP authentication is successful, and decide the next action based on a customer's response to an NPS survey. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9bc1aa1-branch_icon.png",
        "branch_icon.png",
        "Screenshot of Branch Node"
      ],
      "align": "center",
      "sizing": "100rt",
      "border": true,
      "caption": "Branch Node"
    }
  ]
}
[/block]


Define the conditions within a branch using the <code>AND</code> and <code>OR</code> logical operators. The logical operators use the following criteria for evaluation:

- <code>AND</code> - the expression is _True_ only if both the relations are _True_
- <code>OR</code> - the expression is _True_ if either of the relations is _True_.

You can configure the branch names and use them to tag various node outcomes. The conditions configured within different branches are validated sequentially. If none of the branch conditions evaluate to _True_, a default <code>None of the above</code> node outcome is generated. You can rename the default branch.

Double-click the branch node to configure it. The Configuration window has two tabs: **Configuration** and **Transition Actions**.

## Node Configuration

Use this tab to define conditional statements in branches using the <code>AND</code> and <code>OR</code> logical operators. Use only one logical operator to combine two conditions, i.e., you can use either <code>AND</code> or <code>OR</code> to combine one statement with another and form a condition. However, you can use multiple conditions and build a complex logical expression within a branch. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0f0f3aa-Branch_Node_Branch_Node_Configuration.png",
        "Branch Node Branch Node Configuration.png",
        "Screenshot of Branch Node Configuration Page."
      ],
      "align": "center",
      "caption": "Branch Node Configuration"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a374803-branchnode_new_operators1.png",
        "branchnode_new operators1.png",
        "Screenshot of Branch Conditions"
      ],
      "align": "center",
      "caption": "Branch Conditions"
    }
  ]
}
[/block]


Perform the following steps to configure the node:

1. Click the pencil icon to rename the branch if required. **Please note special characters should not be used in the branch name.**
2. Enter the input **Variable** on which you want to apply the condition. For example, <code>$(sms.message)</code> indicates the message of an SMS.
3. Select the **Condition** to apply to the variable. The condition specifies the type of comparison to perform on the variable. The node uses a top-down sequential approach to evaluate the conditions. The supported conditions are:
   - _Equals_
   - _Not equals_
   - _Less than_
   - _Greater than_
   - _Less than or equals_
   - _Greater than or equals_
   - _Regular expression (RegEx)- for validating data quickly such as checking the syntax  of an email address, or searching for a fixed string- pattern in an incoming message, etc. See [Common RegEx Examples](https://help.webexconnect.io/docs/branch-node#common-regex-example) for more information._   
   - _Equals ignore case_
   - _Contains_
   - _Contains ignore case_
   - _In_
   - _Not in_
   - _Starts with_
   - _Ends with_
   - _Between_
4. Enter a **Value** for the input variable. Note: For _In_ and _Not in_, you must press enter after typing each value.  
5. Select the logical **Operator** that you want to use.
6. Click **Save** to save the configuration of the branch.
7. Click **Add Branch** and repeat steps 1 to 6 to add more branches.

## Input Variables

You can see a list of all the flow variables available for this node under this pane. You can also search for a variable using the Search field. For more information, see the [Variable Management](doc:variable-management) section.

## Custom Variables

You can see the list of variables that you explicitly create and configure for this node under the Custom Variables pane. For more information, see the [Variable Management](doc:variable-management) section.

## Output Variables

You can see the data that this node generates as output variables. These [variables](doc:variable-management) are available for use in subsequent nodes. The standard output variables for this node are:

- **branch.output** - the output of the branch, either _True_ or _False_.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3a7f5e5-output_variables.png",
        "output_variables.png",
        "Screenshot of Output Variables."
      ],
      "align": "center",
      "caption": "Output Variables"
    }
  ]
}
[/block]


## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node. Each branch corresponds to a node outcome. 

[block:parameters]
{
  "data": {
    "h-0": "Node Edge",
    "h-1": "Node Event/Outcome",
    "0-0": "Success (green)<br>  \n  \n**Note**: You can see this node edge only when you complete the node configuration.",
    "0-1": "\\* **Branch1** - the flow exits through this node when it is a success. This node is replaced by the branch name for every branch that you configure. For example, if you configure a branch as Request Detailed feedback, the **Branch1** node is replaced by <code>Request Detailed Feedback</code> and likewise for all other branches. For illustration, see the [configuration window](https://files.readme.io/16d9446-branch_node.png).",
    "1-0": "",
    "1-1": "\\* **None of the above** - the flow exits through this node when none of the conditions are met. This is the default branch and node outcome. If you rename the default branch, you see the renamed node outcome.",
    "2-0": "Error (red)",
    "2-1": "\\* **onError** - the flow exits through this node when there is an error. This is the default branch and node outcome. If you rename the default branch, you see the renamed node outcome."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


See the [example](#section-example) for a use case and configuration of different branches.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d4c20a6-node_outcomes.png",
        "node_outcomes.png",
        "Screenshot of Node Outcomes"
      ],
      "align": "center",
      "caption": "Node Outcomes"
    }
  ]
}
[/block]


## Transition Actions

Use this tab to configure the transition actions for <code>On-enter</code>/<code>On-leave</code> events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3d8d241-transition_actions.png",
        "transition_actions.png",
        "Screenshot of Transition Actions"
      ],
      "align": "center",
      "caption": "Define Transition Actions"
    }
  ]
}
[/block]


### Example 1

Use the branch node to process the user's responses (rating), received through SMS, to a [feedback survey](https://www.imiconnect.io/wp-content/uploads/2018/05/imiconnect-cPaaS-Visual-Builder.gif) using the expression builder in the node.<br>  
Define three branches for this use case - **Request Detailed Feedback**, **Update Salesforce**, and **Invalid Input**. See the following configuration to understand the conditions in each branch:

- Request Detailed Feedback (Branch 1 renamed): if the rating is less than or equal to 3, request detailed feedback for further improvement.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6918c9d-branch1.png",
        "branch1.png",
        "Screenshot of Configure the branch to capture user rating."
      ],
      "align": "center",
      "caption": "Configure the branch to capture user rating"
    }
  ]
}
[/block]


- Update Salesforce (Branch 2 renamed): if the rating is 4 or 5, update the case in Salesforce.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3eb7bd9-branch2.png",
        "branch2.png",
        "Screenshot of Configure the branch to capture user rating."
      ],
      "align": "center",
      "caption": "Configure the branch to capture user rating"
    }
  ]
}
[/block]


- Invalid Input (Default branch renamed): if the rating is anything other than 0 to 5, let the user know about it.

## Common RegEx Examples

| Use Case                   | RegEx Pattern                                          | Description                                                                 | Example Matches                                                                           |
| :------------------------- | :----------------------------------------------------- | :-------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| Email Validation           | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`     | Validates standard email formats.                                           | [user@cisco.com](mailto:user@cisco.com) , [user.name@webex.io](mailto:user.name@webex.io) |
| Phone Number (Digits Only) | `^\\d{10,12}$`                                         | Matches a string of 10 to 12 digits (no spaces or dashes).                  | 919045670000, 14155550000                                                                 |
| Keyword Match (OR)         | `._(help\|support\|agent)._`                           | Matches if the message contains any of the specified keywords.              | "I need help", "Connect to support"                                                       |
| Date (DD/MM/YYYY)          | `^(0[1-9]\|[12][0-9]\|3[01])/(0[1-9]\|1[0-2])/\\d{4}$` | Validates a date in DD/MM/YYYY format.                                      | 25/12/2024                                                                                |
| OTP / Numeric Code         | `^\\d{6}$`                                             | Matches exactly 6 digits (useful for verifying OTP inputs).                 | 123456                                                                                    |
| Alphanumeric ID            | `^[a-zA-Z0-9]{8,12}$`                                  | Matches an ID that is 8-12 characters long, containing letters and numbers. | ABC12345678                                                                               |

### Tips for Branch Node RegEx:

- **Case Sensitivity:** By default, RegEx matching in the Branch node is case-sensitive. To make a pattern case-insensitive (e.g., to match "Help" or "help"), use the (?i) flag at the start if supported, or use a range like [hH][eE][lL][pP].
- **Partial vs. Full Match:**
  - Use ^ (start) and $ (end) to ensure the entire input matches your pattern (e.g., for phone numbers).
  - Omit them or use .\* if you only want to check if a pattern exists anywhere in the string (e.g., for keywords).

## Test the Node Configuration

The **Test** option verifies the node outcome for a given input. You can simulate different input variable values and check the outcome while setting up branch conditions. The test mode automatically lists all variables required as input for running the conditions you have configured. For every input, the branch node evaluates each of the conditions and exits the node when a condition is met. <br>  
When you test the node configuration, the branch that evaluates the user input is highlighted.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6469a03-test_node.png",
        "test_node.png",
        "Screenshot of Test the Node Configuration."
      ],
      "align": "center",
      "caption": "Test the Node Configuration"
    }
  ]
}
[/block]