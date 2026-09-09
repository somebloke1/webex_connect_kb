You can invoke/trigger a flow in any one of the following ways in <<prodname>>:
 
  * Channel Events e.g., an incoming message on any of the channels
  * Business System Events e.g., an incoming event trigger from Webex Contact Center 
  * Custom event API or Inbound Webhook

 The above these events are typically configured within the Start Node for any given flow.

Once a flow has been configured, it can be used/triggered in following ways additionally:

  * Event Scheduler (which invokes the flow via Custom Event API or Inbound Webhook)
  * Rules
  * Another flow (using Call Workflow node)