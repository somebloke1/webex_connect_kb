## Overview

This flow ensures secure authentication, processes the cancellation via the EPIC API, and evaluates the outcome to provide feedback to the patient.

## Pre-requisites

- Webex AI Agent Studio
- EPIC Prebuilt Integration

## User Roles

- **Flow Developer: **Configures the Webex Connect flow, EPIC authentication, and JavaScript logic for error handling and result formatting.
- **End User: **The patient requesting to cancel their upcoming appointment.
- **AI Agent: **Triggers the flow upon receiving a cancellation request for a specific appointment.
- **EPIC EHR System: **Processes the cancellation request and returns the status of the operation.

## Node Breakdown

[block:parameters]
{
  "data": {
    "h-0": "Node Type",
    "h-1": "Purpose",
    "h-2": "Outcome",
    "0-0": "Configure AI Agent Event",
    "0-1": "Receives the inbound request from the AI Agent and initializes the flow.  \n  \n**Input Variables:** `appointmentId`, `patientId`, `cancellationReason`.",
    "0-2": "",
    "1-0": "Authenticate",
    "1-1": "Establishes a secure connection with the EPIC EHR.  ",
    "1-2": "Authentication token required for the cancellation API call.",
    "2-0": "EPIC Cancel Appointment",
    "2-1": "Executes the subscription-based API call to EPIC to cancel the specified appointment.",
    "2-2": "Cancellation confirmation status.  \n  \n**Behavior:** On success, proceeds to Set Schedule Type; on error/timeout, triggers the Evaluate nodes for retry handling.",
    "3-0": "Set Schedule Type",
    "3-1": "Updates the schedule type after a successful cancellation.",
    "3-2": "Success/Failure status for the final response to the AI Agent.",
    "4-0": "Evaluate (Error Handler)",
    "4-1": "Analyzes the response to determine if the cancellation was successful or if business logic constraints were met (e.g., appointment is too close to start time, or ID is invalid).  \n  \n**Logic: **Implements retry loops for transient failures and handles invalid data scenarios.",
    "4-2": ""
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Input & Output Variables

### Input Variables (Configure AI Agent Event)

- `appointmentId: `The unique identifier of the appointment to be cancelled.
- `patientId:` The unique identifier for the patient.
- `cancellationReason: `The reason provided by the patient for the cancellation.

### Output Variables

The flow processes the result into a status object that informs the AI Agent whether the cancellation was successfully processed or if an error occurred.

# Error Handling

- **API Timeout: **If the cancellation request fails due to network issues, the flow routes to the Evaluate node to attempt a retry.
- **Invalid Data/Business Logic: **If the appointment cannot be cancelled (e.g., it is too close to the start time), the Evaluate node captures this and routes the flow to a failure path to notify the patient.

## Script Analysis

### Evaluate Script

- **Processing:** The JavaScript logic in the Evaluate nodes checks the response from EPIC. It handles retry logic by incrementing a counter and checking it against the maximum allowed retries.
- **Result:** Ensures that transient failures are resolved automatically, while permanent failures (like invalid IDs) terminate the flow with a clear status.