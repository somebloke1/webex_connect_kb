# Get Available slots

Source: https://help.webexconnect.io/docs/get-available-slots
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:10+00:00

## Overview

This flow accepts slot search criteria, authenticates with EPIC, invokes the slot availability service, applies retry handling for transient failures, trims the result set into a simplified structure, and returns the formatted output payload. This flow is designed to support scheduling use cases where the AI Agent must present available appointment dates and times to the end user.

## Pre-requisite

- Webex AI Agent Studio
- EPIC Prebuilt Integration

## User

- **Flow Developer: **Responsible for configuring, mapping variables, maintaining the flow logic, and publishing the flow.
- **End User (Patient): **The individual providing patient data (e.g., Name, DOB, Phone).
- **AI Agent: **The conversational interface that initiates the verification request and acts upon the validated output.
- **EPIC EHR System: **The backend source of truth for patient records.

## Create flow

To begin building the flow from template, follow these steps:

1. **Select or Create a Service: **Navigate to the Services dashboard. You may either select an existing service from your list or create a new one to serve as the foundation for your flow.
2. **Initiate Flow Creation: **Once your service is selected, click the Create Flow.
3. **Choose the Template**: Within the "Create Flow" window, provide a friendly flow name (Note – the same flow name will have to be selected under AI Agent Studio Action to complete the configuration) and choose the template.
4. The AI Agent Start node configuration is shown in the next screen. You can observe the input received from the AI Agent and click Save.
5. Next, click on make live and publish the flow.
6. Go to AI Agent Studio, configure this flow under appropriate AI Agent studio Action.

## Node Breakdown

### Configure AI Agent

This node receives the inbound request from the AI Agent and payload in JSON format and initializes the flow using the appointment slot search parameters.

**Input Received from AI Agent as trigger**

- `slotStartDate`
- `slotEndDate`
- `providerId`
- `departmentId`
- `visitTypeId`
- `appointmentDate`
- `appointmentTime`
- `patientId`

### Authenticate

This node performs EPIC authentication using OAuth 2.0 before any scheduling API request is made.

#### Purpose

- Retrieve access token
- **Method Name:** Specifies the action to be executed, choose Authenticate.
- **AzureURL:** Determines the target environment endpoint. Setting this to "Staging" ensures the flow connects to your staging or production environment.
- **SubscriptionKey:** Maps the necessary API subscription key for your chosen environment, ensuring that the request is properly authorized by the API Management layer.
- **EPICTokenURL: **Defines the specific endpoint used to exchange credentials for an access token. It utilizes the $(epicBaseURL) variable to allow for dynamic environment switching. The variable value can be configured in the flow settings under custom variables.
- **EPICClientId: **Represents the unique identifier for your application, as registered in the EPIC App. The variable value can be configured in the flow settings under custom variables.

### Outcome

- On success, the flow proceeds to EPIC Get Available slots
- On failure, the flow terminates.

## Get Open Slots Prebuilt Node

This node invokes the EPIC scheduling service to retrieve available appointment slots based on the provided request criteria.

### Purpose

- Submit the slot availability request to EPIC
- Receive the raw slot response
- Store the response for downstream transformation

### Behavior

- On success, the flow proceeds to Trim Result Set
- On error, the flow proceeds to Evaluate for retry handling

## Evaluate

This node implements the retry mechanism used when the Get Open Slots request fails.

### Purpose

- Compare current retry count with maximum retry count
- Decide whether to retry the API request or fail the flow

### Logic

- If retryCount \< maxRetryCount, increment retryCount and return retry. retryCount and maxRetryCount is configured in flow settings under custom variable.
- Otherwise, return fail

### Outcome

- retry loops back to Get Open Slots
- fail exits the flow through the failure path

## Trim Result Set

This Evaluate node parses the raw slot response returned by EPIC and converts it into a simplified array for the AI Agent.

### Purpose

- Parse slot response JSON
- Group available times under each date
- Build the final slotsArray output structure

### Observed Logic

- Parse slotsData
- Iterate through each day object
- Read day.Date
- Iterate through day.Slots
- Extract Time values
- Build result objects in the format:
  - Date
  - Time

## Output

· The transformed array is stored in slotsArray

### Output Payload Description

| Field             | Description                                      |
| :---------------- | :----------------------------------------------- |
| `transactionID`   | Unique transaction identifier for the request    |
| `flowname`        | Name of the executing flow                       |
| `serviceName`     | Name of the invoked service                      |
| `statuscode`      | Flow status code returned on success             |
| `availableSlots`  | Simplified array of available appointment slots  |
| `success`         | Success indicator for the flow                   |
| `visitTypeId`     | Visit type identifier returned in the response   |
| `scheduleOutcome` | Scheduling outcome or type derived from the flow |

## Error Handling

### API Timeout / Transient Failure

If the Get Open Slots request fails due to a temporary API issue, the flow routes to the Evaluate retry node. The retry count is checked and the request is retried until the configured limit is reached.

### Invalid Credentials

If EPIC authentication fails, the flow cannot proceed to slot retrieval and exits through the error path.

### Invalid Data

If the slot response is malformed, empty, or cannot be parsed, the flow follows the configured invalid-data or failure branch.

### No Slots Available

If EPIC returns a valid response with no available slots, the flow can return an empty availableSlots array while still completing the request.

## Script Analysis

### Trim Result Set Script

The JavaScript in the Trim Result Set node parses the raw slot payload and reshapes it into a simplified structure for the AI Agent.

### Observed Processing

- Convert slotsData from string to JSON
- Loop through each date entry in the response
- For each date, loop through all slot entries
- Extract Time values from the nested Slots array
- Create a new object containing:
  - Date
  - Time
- Push each transformed object into the final result array

### Result

The final transformed response is stored in slotsArray

## Retry Logic Script

The JavaScript in the Evaluate node implements the standard retry pattern used across EPIC fulfillment flows.

### Observed Processing

- Convert retryCount and maxRetryCount to numbers
- Compare current retries against the maximum allowed retries
- If retries remain, increment retryCount and return retryIf retries are exhausted, return fail

### Result

- Temporary failures are retried automatically
- Repeated failures terminate the flow after the retry threshold is reached