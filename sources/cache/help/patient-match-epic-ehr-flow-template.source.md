## Overview

This flow template begins by authenticating the session, sanitizing user-provided name data, and executing a multi-stage validation loop. The flow utilizes decision nodes to handle API response statuses and retry logic, ultimately parsing the EPIC FHIR resource to extract a verified unique patient identifier for the AI Agent.

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

1. Select or Create a Service: Navigate to the Services dashboard. You may either select an existing service from your list or create a new one to serve as the foundation for your flow.
2. Initiate Flow Creation: Once your service is selected, click the Create Flow.
3. Choose the Template: Within the "Create Flow" window, provide a friendly flow name (Note – the same flow name will have to be selected under AI Agent Studio Action to complete the configuration) and choose the template.
4. The AI Agent Start node configuration is shown in the next screen. You can observe the input received from the AI Agent and click Save.
5. Next, click on make live and publish the flow.
6. Go to AI Agent Studio, configure this flow under appropriate Ai Agent studio Action.

## Flow Logic & Node Breakdown

[block:parameters]
{
  "data": {
    "h-0": "Order",
    "h-1": "Node Type",
    "h-2": "Purpose",
    "h-3": "Outcome",
    "0-0": "1",
    "0-1": "AI Agent Event",
    "0-2": "This component receives a JSON payload from the AI Agent containing trigger information in the following format:  \n`{  \n    \"patientLastname\": \"Lawson\",  \n    \"patientFirstname\": \"Dave\",  \n    \"patientDOB\": \"1921-01-01\",  \n    \"patientPhonenumber\": \"234-123-4567\",  \n    \"patientAddress\": \"123 Main St\",  \n    \"patientCity\": \"Madison\",  \n    \"patientState\": \"WI\",  \n    \"patientZipcode\": \"53703\"  \n}`  \nTo add a new input parameter to the flow, include the parameter in the JSON payload and click parse. The newly added parameter will then appear as a new variable in the output variables.",
    "0-3": "JSON input  \n parameters from AI Agent",
    "1-0": "2",
    "1-1": "EPIC Authenticate (OAuth)",
    "1-2": "This node is critical for establishing a secure, authorized session with the EPIC EHR system before any patient data can be queried.  \n•\t**Method Name: **Specifies the action to be executed, choose Authenticate.  \n•\t**AzureURL**: Determines the target environment endpoint. Setting this to \"Staging\" ensures the flow connects to your staging or production environment.  \n•\t**SubscriptionKey:** Maps the necessary API subscription key for your chosen environment, ensuring that the request is properly authorized by the API Management layer.  \n•\t**EPICTokenURL:** Defines the specific endpoint used to exchange credentials for an access token. It utilizes the $(EPICBaseURL) variable to allow for dynamic environment switching. The variable value can be configured in the flow settings under custom variables.  \n•\t**EPICClientId:** Represents the unique identifier for your application, as registered in the EPIC App. The variable value can be configured in the flow settings under custom variables.",
    "1-3": "EPIC Patient Auth Token",
    "2-0": "3",
    "2-1": "Generate Array Evaluate",
    "2-2": "The node prepares name components for consistent formatting and processing. The function splits a given name string by spaces or hyphens into parts, capitalizes the first letter of each part, and converts the rest to lowercase, returning an array of these formatted name parts. Additionally, the code removes spaces or hyphens from a surname string by replacing them with an empty string.",
    "2-3": "Sanitized Name Array",
    "3-0": "4",
    "3-1": "EPIC Patient Match",
    "3-2": "Queries `PatientMatch` endpoint using parameters.",
    "3-3": "Match Status/Patient ID",
    "4-0": "5",
    "4-1": "Evaluate",
    "4-2": "The script evaluates the `apiStatusCode` to determine the next action in a retry process:  \n•\tWhen the status code is 200, it resets `retryCount` to zero and proceeds with \"continue\".  \n•\tIf the status code is 400, it resets `retryCount` to zero and triggers a \"fail\" response.  \n•\tFor any other status code, it increases `retryCount` by one if it is below `maxRetryCount` and signals \"retry\"; if the retry limit is reached, it signals \"fail\".  \n•\tThis mechanism governs whether to continue, fail immediately, or retry based on the API response and retry attempts.  \n  \n`apiStatusCode`, `retryCount `and `maxRetryCount `variable values can be updated  in the flow settings under custom variables.",
    "4-3": "Boolean/Status Code",
    "5-0": "6",
    "5-1": "Data Parser",
    "5-2": "Transforms raw JSON response into usable variables.",
    "5-3": "Parsed Patient Object",
    "6-0": "7",
    "6-1": "Record Found?",
    "6-2": "Logic branch to check if a valid record exists.",
    "6-3": "Found/None",
    "7-0": "8",
    "7-1": "Evaluate",
    "7-2": "Extracts specific 'EPIC' identifier from the resource. The script performs the following steps:  \n•\tIt parses a JSON string stored in the variable patientDetails into a JavaScript object called patientData.  \n•\tIt accesses the identifier array located within the first entry of patientData at patientData.entry[0].resource.identifier.  \n•\tIt then iterates through each element in the identifiers array to find an object where the type.text property equals \"EPIC\".  \n•\tOnce found, it assigns the corresponding value of that identifier to the variable patientId and exits the loop.",
    "7-3": "Verified Patient ID"
  },
  "cols": 4,
  "rows": 8,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


<br />

<br />

## Variables & Data Mapping

### Input JSON from AI Agent

`{  “patientLastname": "Lawson",
    "patientFirstname": "Dave",
    "patientDOB": "1921-01-01",
    "patientPhonenumber": "234-123-4567",
    "patientAddress": "123 Main St",
    "patientCity": "Madison",
    "patientState": "WI",
    "patientZipcode": "53703" }`

### Output Variables sent to AI Agent

Configured in flow settings under flow settings: `patientID, matchStatus, verificationTimestamp`

`{ "transactionID": "$(transid)",
  "flowname": "$(flowname)",
"serviceName": "$(serviceName)",
 "statuscode": 1000,
"patientId": "$(n17.patientFHIRId)",
 "patientFound": "$(patientFound)"}`

## Error Handling & Fallbacks

- **No Match Found: **If the API returns a "None" status, the flow triggers a "Retry" prompt or requests secondary verification (e.g., last 4 digits of SSN).
- **API Timeout/Failure: **Errors are logged in the Webex Connect console. The flow initiates a graceful fallback to a human agent if the retryCount exceeds maxRetryCount.
- **Invalid Credentials:** Attempts are logged as security events; the administrator is notified, and the AI Agent informs the user that verification cannot be completed.

## FAQs

### Script Analysis & Logic

**Question: **What does the first Evaluate node script do? 

**Answer: **This script ensures the patient's name is in a standardized format before being sent to the EPIC API. It splits the input string into an array, capitalizes the first letter of each part, and removes special characters (spaces/hyphens) from the surname to ensure the API query is clean and compliant with EPIC's data requirements.

**Question**: How does the second Evaluate node handle API responses? 

**Answer**: This node manages flow control based on HTTP status codes.  
•	200 (Success): Resets the retryCount and proceeds to data parsing.  
•	400 (Bad Request): Stops the flow immediately as the input is invalid.  
•	Other (e.g., 500, Timeout): Checks if the retryCount is less than the maxRetryCount. If so, it increments the count and triggers a "retry" loop; otherwise, it marks the flow as a "fail."

**Question**: What is the purpose of the final Evaluate node script? 

**Answer**: This script parses the JSON response from the EPIC EHR. It navigates the nested FHIR-based structure to find the specific identifier where the type.text is "EPIC." Once found, it extracts the value (the patient ID) and assigns it to the patientID variable for downstream use by the AI Agent.

## General Implementation

**Question**: How do I handle multiple patients returned for one search? 

**Answer:** You should add an additional "Evaluate" node after the Data Parser. If the entry array length is > 1, the AI Agent should be configured to ask the user for clarifying information (e.g., "I found two records, could you please confirm your date of birth?").

**Question**: Is the EPIC Auth token cached? 

**Answer:** Yes, the EPIC Prebuilt node handles token caching automatically.