## Overview

This flow receives rescheming and last appointment details, triggers the booking service to book a new appointment, parses the confirmation data, and evaluates the outcome to ensure the appointment and then cancels the last appointment.

## Pre-requisite

- Webex AI Agent Studio
- EPIC Prebuilt Integration

## User Roles

- **Flow Developer: **Configures the Webex Connect flow, EPIC authentication, request/response mappings, and JavaScript logic for data parsing and evaluation.
- **End User: **The patient interacting with the AI Agent to confirm their desired appointment slot.
- **AI Agent:** Captures the final scheduling intent and triggers the booking fulfillment flow.
- **EPIC EHR System: **Processes the booking request and returns a confirmation status.

## Create Flow

To begin building the flow from template, follow these steps:

1. Select or Create a Service: Navigate to the Services dashboard. You may either select an existing service from your list or create a new one to serve as the foundation for your flow.
2. Initiate Flow Creation: Once your service is selected, click the Create Flow.
3. Choose the Template: Within the "Create Flow" window, provide a friendly flow name (Note – the same flow name will have to be selected under AI Agent Studio Action to complete the configuration) and choose the template.
4. The AI Agent Start node configuration is shown in the next screen. You can observe the input received from the AI Agent and click Save.
5. Next, click on make live and publish the flow.

Go to AI Agent Studio, configure this flow under appropriate AI Agent studio Action.

## Node Breakdown

[block:parameters]
{
  "data": {
    "h-0": "Node Type",
    "h-1": "Purpose",
    "h-2": "Outcome",
    "0-0": "AI Agent Event",
    "0-1": "This node receives the inbound request from the AI Agent in JSON format and initializes the flow with the selected appointment parameters (e.g., patient ID, appointment ID, date, time, provider, department, and visit type).  \n•\tAccept input payload from the AI Agent  \n•\tGenerates request variables as output variables for downstream processing  \n  \nInput Received from AI Agent as trigger:  \n  \n•\tpatientId\": \"\",  \n•\tappointmentId\": \"\",  \n•\tappointmentDate\": \"\",  \n•\t\"appointmentTime\": \"\",  \n•\t \"providerId\": \"\",  \n•\t\"departmentId\": \"\",  \n•\t \"visitTypeId\": \"\",  \n•\t\"reschedule\": \" }\\`\\`",
    "0-2": "",
    "1-0": "EPIC Patient OAuth",
    "1-1": "This node performs EPIC authentication using OAuth 2.0 before any scheduling API request is made.  \n  \n•\tRetrieve access token  \n•\t**Method Name: **Specifies the action to be executed, choose Authenticate.  \n•\t**AzureURL:** Determines the target environment endpoint. Setting this to \"Staging\" ensures the flow connects to your staging or production environment.  \n•\t**SubscriptionKey:** Maps the necessary API subscription key for your chosen environment, ensuring that the request is properly authorized by the API Management layer.  \n•\t**EpicTokenURL:** Defines the specific endpoint used to exchange credentials for an access token. It utilizes the $(epicBaseURL) variable to allow for dynamic environment switching. The variable value can be configured in the flow settings under custom variables.  \n•\t**EpicClientId:** Represents the unique identifier for your application, as registered in the Epic App. The variable value can be configured in the flow settings under custom variables.",
    "1-2": "•\tOn success, the flow proceeds to Schedule Appointment  \n•\tOn failure, the flow terminates.",
    "2-0": "Schedule Appointment",
    "2-1": "This node invokes the EPIC scheduling service to schedule the appointment.  \n•\tSubmit the appointment booking request to Epic  \n•\tReceive the appointment details",
    "2-2": "•\tOn success, the flow proceeds to Data Parser  \n•\tOn error, the flow proceeds to Evaluate for retry handling",
    "3-0": "Data Parser",
    "3-1": "This node processes the raw response received from the EPIC booking service.  \nExtract relevant confirmation details (such as the appointment confirmation number or status) from the JSON response.",
    "3-2": "",
    "4-0": "Find Appointment ID",
    "4-1": "This node verifies the validity of the newly created appointment ID within the system to ensure the booking was correctly registered.  \n  \nCheck for EPICAppointmentIdType variable from Schedule appointment node. It should be of type epicNewApptID0, ….., epicNewApptID4.",
    "4-2": "",
    "5-0": "Reschedule Branch Node",
    "5-1": "This node acts as the branching step, it updates the variables in transition actions for new appointment.  \n  \nSet appointment booked and schedule type variables.",
    "5-2": "",
    "6-0": "Cancel Appointment",
    "6-1": "This node calls the EPIC system to cancel the user’s previous/old appointment.  \n  \nCancel the last appointment. The cancellation Comment field is left empty. If you want to customize the template use a variable that contains cancellation comments. Reason for cancellation is configured as Reschedule.",
    "6-2": "•\tOn success, the flow proceeds shares the JSON (Key Value pairs) configured in Flow Outcome to AI Agent.  \n•\tOn failure, the flow retries to cancel appointment.",
    "7-0": "Retry Logic Script",
    "7-1": "The JavaScript in the Evaluate node implements the standard retry pattern used across EPIC fulfillment flows.  \n`apiStatusCode` , `retryCount` and `maxRetryCount` variable values can be updated  in the flow settings under custom variables.  \n  \n•\tConvert retryCount and maxRetryCount to numbers  \n•\tCompare current retries against the maximum allowed retries  \n•\tIf retries remain, increment retryCount and return retry  \n•\tIf retries are exhausted, return fail",
    "7-2": "•\tTemporary failures are retried automatically  \n•\tRepeated failures terminate the flow after the retry threshold is reached"
  },
  "cols": 3,
  "rows": 8,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


<br />

## Payload Description

### Input Payload

- `patientId: `Unique identifier for the patient.
- `appointmentId: `Identifier for the last appointment slot.
- `appointmentDate: `The date of the requested appointment.
- `appointmentTime: `The time of the requested appointment.
- `providerId:` Identifier for the assigned healthcare provider.
- `departmentId:` Identifier for the department where the appointment will be scheduled.
- `visitTypeId:` Code representing the type of visit (e.g., check-up, consultation).
- `reschedule:` Boolean or flag indicating if this is a rescheduling request.

### Output Payload

The following variables from the flow is shared with AI Agent

`{
  "transactionID": "$(transid)",
  "flowname": "$(flowname)",
  "serviceName": "$(serviceName)",
  "statuscode": 1000,
  "patientInstructions": "$(n4.appointmentPatientInstructions)",
  "newAppointmentId": "$(EPICNewApptID)",
  "appointmentBooked": "$(appointmentBooked)",
  "scheduleOutcome": "$(scheduleType)"
}`

## Error Handling

- **API Timeout / Transient Failure:** If the booking request fails due to a temporary issue, the flow routes to an error path to notify the AI Agent.
- **Invalid Data:** If the appointment parameters provided are invalid or if EPIC rejects the booking due to scheduling conflicts, the flow returns a failure status.

## Script Analysis

### Data Parser Script

The JavaScript in the Data Parser node processes the raw response from EPIC.

- **Processing: **Converts the response string to JSON, extracts the confirmation object, and maps specific fields (like appointmentID) to the flow variables.

### Evaluate Script

The JavaScript in the Evaluate node checks the final status of the booking.

- **Processing:** It verifies if the success flag is true and if an appointmentID was returned. If the criteria are met, it returns an "OK" status; otherwise, it marks the flow as failed.