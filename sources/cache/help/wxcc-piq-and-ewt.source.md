This node provides the caller's current Position in Queue (PIQ) and the Estimated Wait Time (EWT)

The flow developer can use these variables with flow logic to fetch the PIQ - Position in queue and WT - Wait time and route elsewhere when needed.

> 📘 Note:
> 
> - PIQ/EWT node can currently be used only after the Queue Task Node and only while the interaction is actively queued. 
> - Do not use the PIQ/EWT node for post-queue or post-completion logic, such as after a delay that allows the interaction to leave the queue.

## General Settings

**QUEUE ID**: the queue to get the estimated wait time and the contact's current position  
LOOKBACK MINUTES: Specify the Lookback Time for which the Estimated Wait Time (EWT) is calculated after the node is triggered.  The Estimated Wait Time (EWT) parameter is reported in milliseconds (ms).

> 📘 Note:
> 
> Specify the duration in minutes only. Ensure that your input has numeric values only.  
> The accepted value range is 5–240 minutes.

The node has three types of output flow branches. These branches get triggered based on return status and values of EWT and PIQ.

- Success: This branch is triggered when both EWT and PIQ APIs succeed and return nonnegative values. In this flow, you can retrieve and access valid EWT, and PIQ variable values.
- Insufficient Information Flow: This branch is triggered when the PIQ API returns a valid variable value, and EWT has the value as -1. In this flow, you can retrieve and access the PIQ value, but the EWT API fails due to insufficient data to calculate the EWT value.
- Failure: This branch is triggered when PIQ API or EWT API fail and/or return invalid values. The EWT API fails due to reasons other than insufficient data to calculate the EWT value.

## Output Variables

- Position in the Queue (PIQ) provides the contact's current position in the selected queue. Use PIQ/EWT only while the interaction is actively queued. If the interaction is not queued when the PIQ/EWT node runs, PIQ does not return a null, empty, or historical queue position. Instead, PIQ returns the position the contact would receive if it were queued at that time. For example, if no contacts are waiting in the selected queue, PIQ returns 1.
- Estimated Wait Time (EWT) provides an estimated waiting time or the average wait time for the contact before talking to an agent.

## Calculating Estimated Wait Time

The EWT in a queue for the next XX minutes is equal to the average of the Average Queue Times (AQT) for that queue in the past XX minutes. AQT is computed and stored every minute for each queue, based on the interactions that connected to an agent in that one-minute period. AQT is the average duration a caller spent in queue before connecting to an agent.

AQT is calculated by dividing the total duration that all callers together spent in queue, by the total number of callers in that one-minute period. AQT value is not considered valid if the standard deviation of queue times is more than 15 percent of the AQT.

An EWT request returns a value only if valid AQT values are available for at least 80 percent of the specified duration. 

For example, EWT for 10 minutes can be calculated only if valid AQT values are available for at least eight one-minute periods in the past 10 minutes. If the EWT is not returned, the script will proceed with the defined flow.