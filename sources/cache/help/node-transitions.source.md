You can configure node transitions when using <<prodname>> flow builder by dragging the edges emerging from the circular dot available on the right edge of one node and connecting it with the subsequent node. 

If you want to end the flow execution for a given edge you can do so by dragging the edge and releasing it in the free space (as shown below).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2e2f32f-Screenshot_2021-09-27_at_2.33.09_PM.png",
        "Screenshot 2021-09-27 at 2.33.09 PM.png",
        "Screenshot of Node Transitions."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Node Transitions."
    }
  ]
}
[/block]


You'll see the following screen when you release the edge in the free space to configure flow termination points.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d0e3859-Node_Transitions.jpg",
        "Node Transactions  End Termination point.png",
        "Screenshot of End Node Event Configuration Window."
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of End Node Event Configuration Window."
    }
  ]
}
[/block]


Sometime there may be multiple node events associated with the same node (e.g., onSuccess, onError, onPolicyFailure, etc.). You will need to complete this step for all such events separately by selecting the Node Event and the Corresponding Flow Result, and clicking 'Save'.

> ❗️ Note
> 
> You'll also notice a Checkbox (refer: above screen) to indicate whether this is an intermediate break point in the flow or the final flow termination. This field is applicable only when you are configuring the edges for some specific pre-built integration nodes which offer the ability to execute a flow branch for an intermediate event and then resume flow processing at the same node until a final event is received. In general, you must skip this checkbox.