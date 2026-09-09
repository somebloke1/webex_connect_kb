# Using Branch Node to build a flow with conditional branching

Source: https://help.webexconnect.io/docs/branch-node-to-build-flow-with-conditional-branch
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:41+00:00

The Branch node can be used in the start (after the first node that's used to trigger the flow) or anywhere in the middle of a flow. 

## Step 1 – Add the Branch Node

Drag and drop the Branch node from the Nodes palette to the left on to the flow canvas.

## Step 2 – Configure the branch flow

Drag-drop the Branch node into the flow builder. Double-click the Branch node to configure.

1. Name the branch node in **Branch1** field. For example, _Positive Feedback_.
2. Enter the conditional variable name in the input variable field. The value of the conditional variable will decide which path is to be executed.
3. Select the **Condition** as **Equals** from the drop-down.
4. Enter the required number in the **VALUE** field. For example, 10.



![Setting up a branch node with conditions in a flow builder.](https://files.readme.io/ef075e9-Branch.jpg)




5. Click **ADD BRANCH** to add a new branch and repeat the steps from 1-4 with a different match condition for the new branch.  
   You can add multiple branches this way with a business logic. Rename the default flow if needed. 

> 📘 Note
> 
> The default branch is named as "none of the above" which can be updated to the needed value