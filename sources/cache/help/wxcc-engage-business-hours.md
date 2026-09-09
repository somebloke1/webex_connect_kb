# Business Hours - WXCC

Source: https://help.webexconnect.io/docs/wxcc-engage-business-hours
Documentation version: 6.20.0
Retrieved: 2026-09-08T23:29:17+00:00

This node calls Webex Engage's '**Business Hours**' API. While configuring flows in Webex Connect, to determine whether the business is currently in working hours, holiday lists or overrides

> 📘 How are Business hours fetched?
> 
> Business Hours on **Webex Engage** are sync'd directly from **Control Hub**

> ❗️ Limitations
> 
> - **Existing** Business hours, Holidays, Overrides that were already configured before this feature was implemented will **not** show up in this node. Please create a new Business Hours, Holidays, Override object on Control Hub to make use of this feature in the interim.
> - Toggling the `status` of an override does NOT sync either as of now. We recommend you to unlink the Overrides entirely from the Business Hours to work-around this limitation while we attempt to fix this in the future.

## Node screenshot - Business Hours



![Business Hours](https://files.readme.io/079fccaca53744bdf7a6d6b2e3c41c55597d5042d74be4cea23fd896394ce051-image.png)




### How to configure this node

- Drag the node from the **'Node Palette'** on the left by searching against the name **'Business Hours'**
- Double-click to **open** the node
- Select the _Method Name _ - **Business Hours**
- Select your configured **Authorization** in the _Node Runtime Authorization_ field. It is recommended that you set this to the _Default Authorization_  screen under WxConnect's Integrations as all your nodes across flows will pick up the updated token once you regenerate one from the **Integrations** screen.
- Under the Schedule Details section, Select the appropriate radio button depending on whether you intend to validate against a Static Business Hour selection (OR) a Dynamic Business Hour Variable (Looked up by `id` as found on Control Hub)
- Depending on the option you choose above, either select a Business Hour from the dropdown (OR) enter a variable containing your Business Hour ID as referenced from Control Hub.

> ❗️ Do not see your Business hours?
> 
> If you still don't see **new** business hours created being reflected after carrying out the above steps, it is likely an error on our side. Please reach out to our support teams.

### Output variables

| Variable                    | Description                                                                                                                                                                                                                                   |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `slot`                      | Determines the current state of business hours. Possible values include: `working_hours`, `holiday`, `override`, `no_match`No match indicates the current time does not meet any of the working hours, holiday lists or overrides configured. |
| `workingHourSlot.shiftName` | Determines the name of the shift as configured on Control Hub. Populated only when the business is currently in working hours                                                                                                                 |
| `workingHourSlot.startTime` | Determines the start time of the shift as configured on Control Hub. Populated only when the business is currently in working hours                                                                                                           |
| `workingHourSlot.endTime`   | Determines the end time of the shift as configured on Control Hub. Populated only when the business is currently in working hours                                                                                                             |
| `holiday.name`              | Determines the name of the holiday as configured on Control Hub. Populated only when the business is currently on a holiday                                                                                                                   |
| `holiday.startDate`         | Determines the start date of the holiday as configured on Control Hub. Populated only when the business is currently on a holiday                                                                                                             |
| `holiday.endDate`           | Determines the end date of the holiday as configured on Control Hub. Populated only when the business is currently on a holiday                                                                                                               |
| `override.name`             | Determines the name of the override as configured on Control Hub. Populated only when the business is currently in override                                                                                                                   |
| `override.startDateTime`    | Determines the start date time of the override as configured on Control Hub. Populated only when the business is currently in override                                                                                                        |
| `override.endDateTime`      | Determines the end date time of the override as configured on Control Hub. Populated only when the business is currently in override                                                                                                          |

### Node outcomes

| Category    | Outcome               | Description                                                                                                                                      |
| :---------- | :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Success** | `inWorkingHours`      | Indicates that the business is currently in Working Hours                                                                                        |
|             | `onHoliday`           | Indicates that the business is currently on Holiday                                                                                              |
|             | `inOverride`          | Indicates that the business is currently in override                                                                                             |
|             | `onNoMatch`           | Indicates that there was no slot that matches the current date and time as per the business hour calendar                                        |
| **Errors**  | `onError`             | Error in WxConnect's middleware services                                                                                                         |
|             | `onTimeout`           | Could not receive an API response from WxEngage within the agreed time-out                                                                       |
|             | `onInvalidData`       | Invalid data configured in the WxConnect node                                                                                                    |
|             | `onInvalidChoice`     | Invalid choice                                                                                                                                   |
|             | `onAuthorizationFail` | Failed to Authorize successfully. Recommend rechecking Auth details in the [Authorize Integration](wxcc-node-palette#node-authorization) section |