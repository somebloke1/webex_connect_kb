The _IVR Menu_ node is used to receive and capture the user input on an on-going call and accordingly branch the execution of the flow. The expected user input is a single digit for the _IVR Menu_ node. You can choose to play an audio prompt before asking the user to enter input.<br>

The _IVR Menu_ node can exist only within the [Voice Node Group](doc:voice-node-group).

> 📘 Automatic fallback to an alternate TTS Provider
> 
> The ability for automatic fallback to an alternate TTS Provider is supported for Voice TTS, when the primary TTS service provider is experiencing a higher failure rate.  
> This feature is not enabled by default for all the tenants. Please reach out to your account manager to get this feature enabled for your tenant. The Fallback feature is enabled only for a specific set of languages.  
> Example: If English US is supposed on Azure, and you’re experiencing failures, we will fallback to the same language on the alternate TTS Provider. If the same language is not available on the alternate TTS Provider, we will fallback to English. We do not recommend getting this feature enabled if SSML is being used as part of nodes or APIs. This is because the SSML tags are different for the primary service provider and the secondary service provider.

## Node Configuration

Drag-and-drop the node within the voice node group on to the visual flow builder and double-click it to open the configuration window and configure the IVR options. The input can either be DTMF or speech from the user.

### Configuring Keypress

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7d4d957-IVR.jpg",
        "IVR_Menu_Keypress.jpg",
        "Screenshot of Keypress IVR Menu Node Configuration"
      ],
      "align": "center",
      "border": true,
      "caption": "IVR Menu Node Configuration - Keypress"
    }
  ]
}
[/block]


1. Toggle the **Play Audio** button if you want to play a message to the user during an on-going call before providing a list of IVR options to the user. This is an optional step.  
   See [Node Configuration steps](doc:play-node#section-node-configuration) to know about configuring the play audio message.
2. Click the **Keypress** option.
3. Enter a value for **IVR Time Out** in seconds.
4. Configure the **Branch Name** that you need. The branch name is the name of the IVR option and represents the key for which you have configured it.
5. Repeat the above step for each of the branch names.
6. Click **Save** to complete the configuration.

### Configuring Speech Recognition

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63a177d-IVR1.jpg",
        "IVR_Speech.jpg",
        "Screenshot of Speech IVR Menu Node Configuration"
      ],
      "align": "center",
      "border": true,
      "caption": "IVR Menu Node Configuration - Speech"
    }
  ]
}
[/block]


1. Click the **Speech** option.
2. In the **Language** drop-down menu, select a language.
3. For the **Silence Time Out** option, enter the value in seconds.  
   The silence detection feature of the platform detects silence after the user starts speaking, and once detected, the node exits from the detected keyword. Example, if the configured value is 2 seconds, the the system waits for the user’s speech and looks for continuous silence of 2 seconds. Once detected, it stops speech collection and exits from the appropriate keyword edge.
4. Click **Enable Recording** if you want to record the speech for debug purposes.
5. Enter a value for **IVR Time Out** in seconds.
6. In the **Add Keywords** section, add individual keywords in sequence as indicators in speech recognition.

The speech feature in IVR Menu node will have pricing implications. Please reach out to your account manager to discuss commercials and enable this feature for your tenant.

## Input Variables

You can see a list of all the flow variables available for use within this node under the **Input Variables** pane. You can also search for a variable using the **Search** field.

You can see the list of variables that you explicitly create and configure for this node under the **Custom Variables** pane. You can also add a custom variable to the flow using the **Add New Custom Variable** button. For more information, see [Custom Variables](doc:variable-management#section-custom-variables).

## Output Variables

You can see the data that this node generates as output variables. These [variables](doc:variable-management) are available for use in subsequent nodes. The following are the standard output variables for the _IVR Menu_ node:

- **ivr.input** - stores the user input captured through IVR.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5b08841-IVR2.jpg",
        "IVR Menu Node Output Variables.png",
        "Screenshot of IVR Menu Output Variables"
      ],
      "align": "center",
      "sizing": "300px",
      "border": true,
      "caption": "Output Variables"
    }
  ]
}
[/block]


## Node Outcomes

You can see the list of possible node outcomes for this node under this pane. You can customize the node labels using the **Edit** (pencil) icon. The node exits through one of the node edges corresponding to the outcome of the node.

[block:parameters]
{
  "data": {
    "h-0": "Node Edge",
    "h-1": "Node Event/Outcome",
    "0-0": "Success (green)",
    "0-1": "> - **onSuccess** - the flow exits through this node when the user enters input within the specified duration",
    "1-0": "Timeout (yellow/amber)",
    "1-1": "> - **oninputTimeout** - the flow exits through this node outcome when the user does not provide input within the configured duration",
    "2-0": "Error (red)",
    "2-1": "> _ **onError** - the flow exits through this node outcome when there is an error in playing the configured audio prompts  \n> _ **onwrongInput** - the flow exits through this node outcome when the user input is wrong/invalid"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Transition Actions

Use this tab to configure the transition actions for `On-enter`/`On-leave` events. However, configuring transition actions is optional. For detailed instructions about configuring the transition actions, see [Node Transition Actions](doc:transition-actions).