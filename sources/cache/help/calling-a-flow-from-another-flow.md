# Calling a Flow from another Flow

Source: https://help.webexconnect.io/docs/calling-a-flow-from-another-flow
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:42+00:00

Webex Connect users who want to modularise/divide a large flow into sub-flows can use the _Call Workflow_ node on the flow palette. <br>

The _[Call Flow](https://help.webexconnect.io/docs/call-workflow-node)_ node allows flows within a service to invoke other flows within the same service. It’s the suggested approach when calling a flow from another flow when both the flows are within the same service.

## Using Call Flow Node

As shown below, the call workflow node offers a dropdown for you to select the flow (let’s call it flow B) that you want to invoke from the current flow (let’s call it flow A). You can either invoke the flow B from the starting in which case the node type will be start, or invoke flow B from an intermediate node within the flow B.



![Call Flow Node Configuration](https://files.readme.io/136d363-Calling_a_Flow_from_another_Flow.jpg)




> 🚧 Variable Management across Flows when using Call Flow Node
> 
> You will need to use custom variables to pass required variables from calling flow (i.e., parent flow) to called flow (i.e.g, child flow). Visit [Call Flow node docs](https://help.imiconnect.io/docs/call-workflow) to know more.