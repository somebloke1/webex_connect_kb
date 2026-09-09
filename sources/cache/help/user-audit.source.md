This feature is accessible only to the tenant owner of the clients who have subscribed for this feature. It allows the tenant owner to view the actions performed by all the users across groups and teams within the last 30 days. You can specify the date/time range, user role, and user actions filters to view audit logs as per your requirements.

Navigate to your **Account Settings** and select **User Audit **from the submenu:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4e5ed272c22df8e05b3c01f9bbbb07f5f702d45495ce256158b60e94aa5590e8-2025-03-19_11-31-58.jpg",
        "Monitoring1.jpg",
        "Sceenshot of User Audit"
      ],
      "align": "center",
      "border": true,
      "caption": "User Audit"
    }
  ]
}
[/block]


Select the required **Role**, **User ID**, and **Period** and click **Apply**. The audit trail will appear based on the selection.

Selecting all the fields is not mandatory, you can select any one of the fields to view the audit trail. 

## Top Actions

This section lists the top 5 actions in the descending order of counts or the number of times that an action has been performed by various users. It also specifies the number of actions performed by users. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4d10b5e-Monitoring-Custom_Date.jpg",
        "Monitoring-Custom Date.jpg",
        "Screenshot of Custom Date popup"
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Screenshot of Custom Date popup"
    }
  ]
}
[/block]


Here you can enter a start date and end date to get data for a required time-period. However, the number of days for retrieval of data is maximum of 30 days which means only the actions performed within the last 30 days can be viewed. The data will appear in descending order based on ‘No. of Actions’.    

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0e50f8b-Monitoring1.png",
        "audit trail3.png",
        "Screenshot displaying the list of Actions"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot displaying the list of Actions"
    }
  ]
}
[/block]


## Log Trail

Log trail provides the audit trail for the selected **Role**, **User ID**, and **Time Period** at a User ID level.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/beaffa2-Monitoring2.png",
        "audit trail4.png",
        "Screenshot of Log Trail"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of Log Trail"
    }
  ]
}
[/block]


You can expand the rows further to see the **User IP** address, **Description**, **Status** of action performed, and the **Time Stamp** of the action.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d52f1e0-Monitoring3.png",
        "audit trail5.png",
        "Screenshot of the Log Trail Details"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of the Log Trail Details"
    }
  ]
}
[/block]


If the count of the number of user ids is more than 100 then pagination will be enabled. To view further user details, you must move to the next page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/abad55f-Monitoring4.png",
        "audit trail6.png",
        "Screenshot of the Log Trail Details"
      ],
      "align": "center",
      "border": true,
      "caption": "Screenshot of the Log Trail Details"
    }
  ]
}
[/block]


> 📘 Note
> 
> Audit logs can be streamed to Data Stream via Kafka. The configuration can be accessed on [Data Streams](https://help.webexconnect.io/docs/data-streams), and the payload can be viewed on the [API page](https://developers.webexconnect.io/reference/data-streams-audit-logs).