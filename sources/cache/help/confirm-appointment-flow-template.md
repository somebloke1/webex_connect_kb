# Confirm Appointment Flow Template

Source: https://help.webexconnect.io/docs/confirm-appointment-flow-template
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:28:43+00:00

## Overview

This flow handles the authentication, confirms the patient attendance on EPIC manages potential retries for transient errors, and notifies the confirmation status to AI Agent.

## Pre-requisites

- Webex AI Agent Studio
- EPIC Prebuilt Integration

## User Roles

- **Flow Developer: **Configures EPIC authentication, handles the confirmation API logic, and manages the retry/evaluation scripts.
- **End User: **The patient receiving confirmation that their appointment is officially booked.
- **AI Agent: **Triggers the confirmation flow once the appointment details have been selected.
- **EPIC EHR System: **Receives the confirmation signal and updates the appointment status.

## Node Breakdown



| Node Type | Purpose | Outcome |
| --- | --- | --- |
| Configure AI Agent Event | Initializes the flow with the specific identifiers needed to confirm the booking.  <br>**Input Variables:** `appointmentId`, `patientId` |  |
| Authenticate | •	Retrieve access token  <br>•	**Method Name: **Specifies the action to be executed, choose Authenticate.  <br>•	**AzureURL: **Determines the target environment endpoint. Setting this to "Staging" ensures the flow connects to your staging or production environment.  <br>•	**SubscriptionKey:** Maps the necessary API subscription key for your chosen environment, ensuring that the request is properly authorized by the API Management layer.  <br>•	**EPICTokenURL: **Defines the specific endpoint used to exchange credentials for an access token. It utilizes the $(epicBaseURL) variable to allow for dynamic environment switching. The variable value can be configured in the flow settings under custom variables.  <br>•	**EPICClientId:** Represents the unique identifier for your application, as registered in the Epic App. The variable value can be configured in the flow settings under custom variables. | •	On success, the flow proceeds to **Confirm Appointment **  <br>•	On failure, the flow terminates. |
| Confirm Appointment | Sends the patient final confirmation to the EPIC.  <br>  <br>**Behavior:** On success, moves to Update Schedule Type. On timeout or invalid choice, triggers the Evaluate nodes for retry logic. |  |
| Update Schedule Type | Performs a final data update to ensure the appointment is correctly categorized in the EHR. | Finalizes the flow upon successful execution. |
| Evaluate (Retry Logic) | Manages transient errors (like timeouts or invalid choices).  <br>  <br>**Logic: **Compares current retry counts against thresholds. If retries remain, it loops back to the Confirm Appointment node; otherwise, it terminates the flow. |  |




## Input & Output Variables

### Input Variables (Configure AI Agent Event)

- `appointmentId: `The unique ID of the appointment to be confirmed.
- `patientId: `The unique ID of the patient associated with the appointment.

### Output Variables

The flow maintains these identifiers throughout the process to ensure the correct record is updated in the EPIC EHR system.

## Error Handling

- **Authentication Failure: **If the flow fails to authenticate, it exits immediately to prevent unauthorized API calls.
- **API Timeout:** If the EPIC system does not respond, the flow routes to the Evaluate node to attempt a retry.
- **Invalid Choice: **If the confirmation request is rejected due to invalid parameters, the flow triggers the retry/failure logic to allow for correction or graceful termination.

## Script Analysis

### Evaluate Script

- **Processing: **The script in the Evaluate node monitors the retryCount. It increments the count after each failed attempt and compares it against the maxRetryCount.
- **Result: **Automates the recovery process for temporary network or service issues, ensuring a robust user experience.