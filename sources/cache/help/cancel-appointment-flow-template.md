# Cancel Appointment Flow Template

Source: https://help.webexconnect.io/docs/cancel-appointment-flow-template
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:44+00:00

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



| Node Type | Purpose | Outcome |
| --- | --- | --- |
| Configure AI Agent Event | Receives the inbound request from the AI Agent and initializes the flow.  <br>  <br>**Input Variables:** `appointmentId`, `patientId`, `cancellationReason`. |  |
| Authenticate | Establishes a secure connection with the EPIC EHR.   | Authentication token required for the cancellation API call. |
| EPIC Cancel Appointment | Executes the subscription-based API call to EPIC to cancel the specified appointment. | Cancellation confirmation status.  <br>  <br>**Behavior:** On success, proceeds to Set Schedule Type; on error/timeout, triggers the Evaluate nodes for retry handling. |
| Set Schedule Type | Updates the schedule type after a successful cancellation. | Success/Failure status for the final response to the AI Agent. |
| Evaluate (Error Handler) | Analyzes the response to determine if the cancellation was successful or if business logic constraints were met (e.g., appointment is too close to start time, or ID is invalid).  <br>  <br>**Logic: **Implements retry loops for transient failures and handles invalid data scenarios. |  |




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