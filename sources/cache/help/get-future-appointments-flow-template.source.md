## Overview

This flow acts as a prerequisite for downstream workflows such as appointment confirmation, cancellation, or rescheduling.

## Pre-requisites

- Webex AI Agent Studio
- EPIC Prebuilt Integration

## User Roles

- **Flow Developer: **Configures the Webex Connect flow, EPIC authentication, and JavaScript logic for result trimming.
- **End User: **The patient requesting information about their upcoming schedule.
- **AI Agent: **Triggers the flow when a patient asks, "What are my upcoming appointments?"
- **EPIC EHR System:** Processes the request and returns the list of future appointment records.

## Node Breakdown

[block:parameters]
{
  "data": {
    "h-0": "Node Type",
    "h-1": "Purpose",
    "h-2": "Outcome",
    "0-0": "Configure AI Agent Event",
    "0-1": " Receives the inbound request from the AI Agent and initializes the flow.  \n  \n**Input Variable: **`patientId`",
    "0-2": "",
    "1-0": "Authenticate",
    "1-1": "Establishes a secure connection with the EPIC EHR.",
    "1-2": "Authentication token required for subsequent API calls.",
    "2-0": "Get Future Appointments",
    "2-1": "Executes a subscription-based API call to EPIC to fetch future records.",
    "2-2": "Raw JSON list of appointments.  \n  \n**Behavior:** On success, proceeds to Trim Result Set; on error/timeout, triggers the Evaluate nodes for retry handling.",
    "3-0": "Trim Result Set",
    "3-1": "Uses JavaScript to filter and format the raw JSON response.",
    "3-2": "A clean, simplified appointment list (Date, Time, Provider) ready for the AI Agent to present to the user.",
    "4-0": "Evaluate (Error Handler)",
    "4-1": "Manages scenarios where no future appointments exist or where transient API timeouts occur.  \n  \n**Logic:** Implements retry loops for temporary failures and handles empty result sets gracefully.",
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

`patientId:` The unique identifier for the patient whose appointments are being retrieved.

### Output Variables

The flow processes the raw data into a structured format (e.g., appointmentList) that contains the date, time, and provider details for each upcoming visit.

## Error Handling

- **API Timeout: **If the request to EPIC fails due to a network or service issue, the flow routes to the Evaluate node to attempt a retry.
- **No Appointments Found: **If the API returns a successful response but the list is empty, the flow exits through the failure path to inform the AI Agent that no upcoming appointments were found.

## Script Analysis

### Trim Result Set Script

- **Processing:** The JavaScript logic iterates through the raw JSON response from EPIC. It extracts specific fields—Date, Time, and Provider—and maps them into a simplified array structure.
- **Result:** A clean, human-readable list that the AI Agent can easily relay to the patient.

### Evaluate Script

- **Processing:** Checks the status of the API call. If a retry is required, it increments the retry counter and loops back to the "Get Future Appointments" node. If the maximum number of retries is reached, it terminates the flow.